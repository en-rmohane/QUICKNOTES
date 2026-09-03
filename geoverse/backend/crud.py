import datetime
import json
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from backend import models, schemas, auth

# User operations
def get_user_by_username(db: Session, username: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    hashed_pwd = auth.get_password_hash(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pwd,
        is_admin=False,
        streak=1,
        xp=0,
        last_login=datetime.datetime.utcnow()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_streak(db: Session, user: models.User):
    now = datetime.datetime.utcnow()
    delta = now - user.last_login
    if delta.days == 1:
        user.streak += 1
    elif delta.days > 1:
        user.streak = 1
    user.last_login = now
    db.commit()

# Country operations
def get_countries(
    db: Session, 
    continent: Optional[str] = None, 
    koppen: Optional[str] = None,
    limit: int = 250
) -> List[models.Country]:
    query = db.query(models.Country)
    if continent:
        query = query.filter(models.Country.continent == continent)
    if koppen:
        query = query.filter(models.Country.koppen_classification.contains(koppen))
    return query.limit(limit).all()

def get_country_by_id(db: Session, country_id: int) -> Optional[models.Country]:
    return db.query(models.Country).filter(models.Country.id == country_id).first()

def get_country_by_name(db: Session, name: str) -> Optional[models.Country]:
    return db.query(models.Country).filter(models.Country.name.ilike(name)).first()

def get_country_by_code(db: Session, code: str) -> Optional[models.Country]:
    return db.query(models.Country).filter(models.Country.code.ilike(code)).first()

# India State operations
def get_india_states(db: Session) -> List[models.IndiaState]:
    return db.query(models.IndiaState).all()

def get_india_state_by_id(db: Session, state_id: int) -> Optional[models.IndiaState]:
    return db.query(models.IndiaState).filter(models.IndiaState.id == state_id).first()

# Quiz operations
def get_quizzes(
    db: Session, 
    topic: Optional[str] = None, 
    difficulty: Optional[str] = None, 
    limit: int = 10
) -> List[models.Quiz]:
    query = db.query(models.Quiz)
    if topic:
        query = query.filter(models.Quiz.topic == topic)
    if difficulty:
        query = query.filter(models.Quiz.difficulty == difficulty)
    return query.order_by(func.random()).limit(limit).all()

def get_quiz_by_id(db: Session, quiz_id: int) -> Optional[models.Quiz]:
    return db.query(models.Quiz).filter(models.Quiz.id == quiz_id).first()

def record_quiz_attempt(
    db: Session, 
    user_id: int, 
    quiz_id: int, 
    is_correct: bool, 
    time_taken: int
) -> models.UserQuizStat:
    stat = models.UserQuizStat(
        user_id=user_id,
        quiz_id=quiz_id,
        is_correct=is_correct,
        time_taken=time_taken,
        answered_at=datetime.datetime.utcnow()
    )
    db.add(stat)
    # Award XP
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.xp += 15 if is_correct else 5
    db.commit()
    db.refresh(stat)
    return stat

def get_user_quiz_stats(db: Session, user_id: int):
    # Total count, correct count, topic stats
    stats = db.query(models.UserQuizStat).filter(models.UserQuizStat.user_id == user_id).all()
    total = len(stats)
    correct = sum(1 for s in stats if s.is_correct)
    return {
        "total_attempts": total,
        "correct_attempts": correct,
        "accuracy": (correct / total * 100) if total > 0 else 0
    }

# Progress operations
def update_user_progress(db: Session, user_id: int, country_id: int, section: str) -> models.UserProgress:
    progress = db.query(models.UserProgress).filter(
        models.UserProgress.user_id == user_id,
        models.UserProgress.country_id == country_id
    ).first()

    if not progress:
        progress = models.UserProgress(
            user_id=user_id,
            country_id=country_id,
            topics_completed_json=json.dumps([section]),
            last_studied=datetime.datetime.utcnow()
        )
        db.add(progress)
    else:
        completed = json.loads(progress.topics_completed_json)
        if section not in completed:
            completed.append(section)
            progress.topics_completed_json = json.dumps(completed)
        progress.last_studied = datetime.datetime.utcnow()
    
    # Award XP
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.xp += 10
        
    db.commit()
    db.refresh(progress)
    return progress

def get_user_progress(db: Session, user_id: int) -> List[models.UserProgress]:
    return db.query(models.UserProgress).filter(models.UserProgress.user_id == user_id).all()

# Bookmark operations
def add_bookmark(db: Session, user_id: int, b: schemas.BookmarkCreate) -> models.UserBookmark:
    bookmark = models.UserBookmark(
        user_id=user_id,
        country_id=b.country_id,
        section=b.section,
        fact_key=b.fact_key,
        fact_value=b.fact_value
    )
    db.add(bookmark)
    db.commit()
    db.refresh(bookmark)
    return bookmark

def get_bookmarks(db: Session, user_id: int) -> List[models.UserBookmark]:
    return db.query(models.UserBookmark).filter(models.UserBookmark.user_id == user_id).all()

def delete_bookmark(db: Session, user_id: int, bookmark_id: int) -> bool:
    b = db.query(models.UserBookmark).filter(
        models.UserBookmark.id == bookmark_id,
        models.UserBookmark.user_id == user_id
    ).first()
    if b:
        db.delete(b)
        db.commit()
        return True
    return False

# Notes operations
def save_note(db: Session, user_id: int, n: schemas.NoteCreate) -> models.UserNote:
    note = db.query(models.UserNote).filter(
        models.UserNote.user_id == user_id,
        models.UserNote.country_id == n.country_id
    ).first()

    if note:
        note.note_content = n.note_content
        note.updated_at = datetime.datetime.utcnow()
    else:
        note = models.UserNote(
            user_id=user_id,
            country_id=n.country_id,
            note_content=n.note_content,
            updated_at=datetime.datetime.utcnow()
        )
        db.add(note)
    db.commit()
    db.refresh(note)
    return note

def get_notes(db: Session, user_id: int) -> List[models.UserNote]:
    return db.query(models.UserNote).filter(models.UserNote.user_id == user_id).all()

# Flashcard SM-2 Spaced Repetition operations
def create_flashcard(db: Session, user_id: int, f: schemas.FlashcardCreate) -> models.UserFlashcard:
    card = models.UserFlashcard(
        user_id=user_id,
        front=f.front,
        back=f.back,
        easiness=2.5,
        interval=1,
        repetitions=0,
        next_review=datetime.datetime.utcnow()
    )
    db.add(card)
    db.commit()
    db.refresh(card)
    return card

def get_due_flashcards(db: Session, user_id: int) -> List[models.UserFlashcard]:
    now = datetime.datetime.utcnow()
    return db.query(models.UserFlashcard).filter(
        models.UserFlashcard.user_id == user_id,
        models.UserFlashcard.next_review <= now
    ).all()

def review_flashcard_sm2(db: Session, user_id: int, card_id: int, q: int) -> Optional[models.UserFlashcard]:
    card = db.query(models.UserFlashcard).filter(
        models.UserFlashcard.id == card_id,
        models.UserFlashcard.user_id == user_id
    ).first()
    
    if not card:
        return None

    # q represents the quality response from 0 to 5.
    # Standard SuperMemo-2 (SM-2) algorithm
    if q < 3:
        # Incorrect response, reset repetitions and interval
        card.repetitions = 0
        card.interval = 1
    else:
        # Correct response, update repetitions and interval
        if card.repetitions == 0:
            card.interval = 1
        elif card.repetitions == 1:
            card.interval = 6
        else:
            card.interval = int(round(card.interval * card.easiness))
        
        card.repetitions += 1

    # Update easiness factor
    card.easiness = card.easiness + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
    if card.easiness < 1.3:
        card.easiness = 1.3

    # Schedule next review
    card.next_review = datetime.datetime.utcnow() + datetime.timedelta(days=card.interval)
    db.commit()
    db.refresh(card)
    return card

# News operations
def get_news(db: Session, limit: int = 30) -> List[models.NewsTracker]:
    return db.query(models.NewsTracker).order_by(models.NewsTracker.date_published.desc()).limit(limit).all()
