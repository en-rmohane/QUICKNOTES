import datetime
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List, Optional
import json

from backend.database import get_db, engine, Base
from backend import models, schemas, crud, auth

app = FastAPI(title="GeoVerse API", description="UPSC Geography Learning Platform Backend API", version="1.0.0")

# CORS middleware config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Database on Startup (if seeder hasn't been run)
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

# --- AUTH ENDPOINTS ---

@app.post("/api/auth/register", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    db_email = crud.get_user_by_email(db, email=user.email)
    if db_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/api/auth/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username=form_data.username)
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Update login streak
    crud.update_user_streak(db, user)
    
    access_token_expires = datetime.timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/api/auth/me", response_model=schemas.UserOut)
def read_users_me(current_user: models.User = Depends(auth.get_current_user)):
    return current_user


# --- COUNTRIES ENDPOINTS ---

@app.get("/api/countries", response_model=List[schemas.CountrySummary])
def read_countries(
    continent: Optional[str] = None,
    koppen: Optional[str] = None,
    db: Session = Depends(get_db)
):
    countries = crud.get_countries(db, continent=continent, koppen=koppen)
    return countries

@app.get("/api/countries/{country_id}", response_model=schemas.CountryOut)
def read_country(country_id: int, db: Session = Depends(get_db)):
    db_country = crud.get_country_by_id(db, country_id=country_id)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return db_country

@app.get("/api/countries/by-name/{name}", response_model=schemas.CountryOut)
def read_country_by_name(name: str, db: Session = Depends(get_db)):
    db_country = crud.get_country_by_name(db, name=name)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return db_country


# --- INDIA SPECIAL MODULES ---

@app.get("/api/india/states", response_model=List[schemas.IndiaStateOut])
def read_india_states(db: Session = Depends(get_db)):
    return crud.get_india_states(db)

@app.get("/api/india/states/{state_id}", response_model=schemas.IndiaStateOut)
def read_india_state(state_id: int, db: Session = Depends(get_db)):
    db_state = crud.get_india_state_by_id(db, state_id=state_id)
    if db_state is None:
        raise HTTPException(status_code=404, detail="State/UT not found")
    return db_state


# --- QUIZ ENDPOINTS ---

@app.get("/api/quizzes/random", response_model=List[schemas.QuizOut])
def read_random_quizzes(
    topic: Optional[str] = None,
    difficulty: Optional[str] = None,
    limit: int = 5,
    db: Session = Depends(get_db)
):
    return crud.get_quizzes(db, topic=topic, difficulty=difficulty, limit=limit)

@app.post("/api/quizzes/submit", response_model=schemas.QuizResult)
def submit_quiz_answer(
    answer: schemas.QuizAnswerSubmit,
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    db_quiz = crud.get_quiz_by_id(db, quiz_id=answer.quiz_id)
    if not db_quiz:
        raise HTTPException(status_code=404, detail="Quiz question not found")
    
    is_correct = (db_quiz.correct_answer == answer.selected_answer)
    crud.record_quiz_attempt(
        db, 
        user_id=current_user.id, 
        quiz_id=answer.quiz_id, 
        is_correct=is_correct, 
        time_taken=answer.time_taken
    )
    
    return {
        "is_correct": is_correct,
        "correct_answer": db_quiz.correct_answer,
        "explanation": db_quiz.explanation
    }

@app.get("/api/quizzes/stats")
def read_user_quiz_stats(
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    return crud.get_user_quiz_stats(db, user_id=current_user.id)


# --- STUDY DESK ENDPOINTS (Bookmarks, Notes, Flashcards) ---

@app.post("/api/study/bookmarks", response_model=schemas.BookmarkOut)
def create_bookmark(
    bookmark: schemas.BookmarkCreate,
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    return crud.add_bookmark(db, user_id=current_user.id, b=bookmark)

@app.get("/api/study/bookmarks", response_model=List[schemas.BookmarkOut])
def read_bookmarks(
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    db_bookmarks = crud.get_bookmarks(db, user_id=current_user.id)
    # Map country names to return
    result = []
    for b in db_bookmarks:
        country = db.query(models.Country).filter(models.Country.id == b.country_id).first()
        b_dict = schemas.BookmarkOut.from_orm(b)
        b_dict.country_name = country.name if country else "Global"
        result.append(b_dict)
    return result

@app.delete("/api/study/bookmarks/{bookmark_id}")
def delete_user_bookmark(
    bookmark_id: int,
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    success = crud.delete_bookmark(db, user_id=current_user.id, bookmark_id=bookmark_id)
    if not success:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return {"detail": "Bookmark deleted successfully"}

@app.post("/api/study/notes", response_model=schemas.NoteOut)
def create_or_update_note(
    note: schemas.NoteCreate,
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    db_note = crud.save_note(db, user_id=current_user.id, n=note)
    country = db.query(models.Country).filter(models.Country.id == db_note.country_id).first()
    res = schemas.NoteOut.from_orm(db_note)
    res.country_name = country.name if country else "Unknown"
    return res

@app.get("/api/study/notes", response_model=List[schemas.NoteOut])
def read_notes(
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    db_notes = crud.get_notes(db, user_id=current_user.id)
    result = []
    for n in db_notes:
        country = db.query(models.Country).filter(models.Country.id == n.country_id).first()
        n_dict = schemas.NoteOut.from_orm(n)
        n_dict.country_name = country.name if country else "Unknown"
        result.append(n_dict)
    return result

@app.post("/api/study/flashcards", response_model=schemas.FlashcardOut)
def add_flashcard(
    card: schemas.FlashcardCreate,
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    return crud.create_flashcard(db, user_id=current_user.id, f=card)

@app.get("/api/study/flashcards/due", response_model=List[schemas.FlashcardOut])
def read_due_flashcards(
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    return crud.get_due_flashcards(db, user_id=current_user.id)

@app.post("/api/study/flashcards/review", response_model=schemas.FlashcardOut)
def review_flashcard(
    review: schemas.FlashcardReview,
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    card = crud.review_flashcard_sm2(
        db, 
        user_id=current_user.id, 
        card_id=review.card_id, 
        q=review.rating
    )
    if not card:
        raise HTTPException(status_code=404, detail="Flashcard not found")
    return card


# --- NEWS TRACKER ENDPOINTS ---

@app.get("/api/news", response_model=List[schemas.NewsOut])
def read_news(limit: int = 15, db: Session = Depends(get_db)):
    return crud.get_news(db, limit=limit)


# --- PROGRESS TRACKER ENDPOINTS ---

@app.post("/api/progress", response_model=schemas.UserProgressOut)
def study_progress_update(
    prog: schemas.UserProgressUpdate,
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    return crud.update_user_progress(
        db, 
        user_id=current_user.id, 
        country_id=prog.country_id, 
        section=prog.section
    )

@app.get("/api/progress", response_model=List[schemas.UserProgressOut])
def read_my_progress(
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    return crud.get_user_progress(db, user_id=current_user.id)
