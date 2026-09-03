import datetime
from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from backend.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    streak = Column(Integer, default=0)
    xp = Column(Integer, default=0)
    last_login = Column(DateTime, default=datetime.datetime.utcnow)

    progress = relationship("UserProgress", back_populates="user", cascade="all, delete-orphan")
    quiz_stats = relationship("UserQuizStat", back_populates="user", cascade="all, delete-orphan")
    bookmarks = relationship("UserBookmark", back_populates="user", cascade="all, delete-orphan")
    notes = relationship("UserNote", back_populates="user", cascade="all, delete-orphan")
    flashcards = relationship("UserFlashcard", back_populates="user", cascade="all, delete-orphan")

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    code = Column(String(3), unique=True, index=True, nullable=False)
    continent = Column(String, index=True, nullable=False)
    geometry_json = Column(Text, nullable=True) # GeoJSON boundary for rendering

    # Physical Geography
    location_coords = Column(String, nullable=True) # e.g. "20.5937, 78.9629"
    area_sq_km = Column(Float, nullable=True)
    boundaries = Column(Text, nullable=True)
    mountains_json = Column(Text, nullable=True)
    peaks_json = Column(Text, nullable=True)
    rivers_json = Column(Text, nullable=True)
    lakes_json = Column(Text, nullable=True)
    plateaus_json = Column(Text, nullable=True)
    plains_json = Column(Text, nullable=True)
    deserts_json = Column(Text, nullable=True)
    straits_json = Column(Text, nullable=True)
    coastline_json = Column(Text, nullable=True)

    # Climate & Environment
    koppen_classification = Column(String, nullable=True)
    temperature_avg_json = Column(Text, nullable=True)
    rainfall_json = Column(Text, nullable=True)
    winds_json = Column(Text, nullable=True)
    vegetation_json = Column(Text, nullable=True)
    parks_json = Column(Text, nullable=True)
    environmental_issues = Column(Text, nullable=True)
    disasters_json = Column(Text, nullable=True)

    # Soil & Agriculture
    soil_types_json = Column(Text, nullable=True)
    crops_json = Column(Text, nullable=True)
    farming_patterns = Column(Text, nullable=True)
    irrigation_json = Column(Text, nullable=True)
    green_rev_impact = Column(Text, nullable=True)
    gi_tags_json = Column(Text, nullable=True)

    # Minerals & Industries
    minerals_json = Column(Text, nullable=True)
    mining_regions_json = Column(Text, nullable=True)
    industries_json = Column(Text, nullable=True)
    corridors_json = Column(Text, nullable=True)
    energy_resources_json = Column(Text, nullable=True)
    pipelines_refineries_json = Column(Text, nullable=True)
    power_plants_json = Column(Text, nullable=True)

    # Population & Demography
    population = Column(Integer, nullable=True)
    density = Column(Float, nullable=True)
    growth_rate = Column(Float, nullable=True)
    cities_json = Column(Text, nullable=True)
    urbanization_rate = Column(Float, nullable=True)
    ethnic_groups_json = Column(Text, nullable=True)
    languages_json = Column(Text, nullable=True)
    literacy_rate = Column(Float, nullable=True)
    sex_ratio = Column(String, nullable=True)
    hdi = Column(Float, nullable=True)

    # Political & Economic Geography
    government_type = Column(String, nullable=True)
    admin_divisions_json = Column(Text, nullable=True)
    currency = Column(String, nullable=True)
    gdp = Column(Float, nullable=True) # in Billion USD
    gdp_per_capita = Column(Float, nullable=True) # in USD
    trade_json = Column(Text, nullable=True)
    ports_json = Column(Text, nullable=True)
    airports_json = Column(Text, nullable=True)
    infrastructure_json = Column(Text, nullable=True)

    # Special Features
    dams_json = Column(Text, nullable=True)
    timezones_json = Column(Text, nullable=True)
    border_disputes_json = Column(Text, nullable=True)
    geopolitical_significance = Column(Text, nullable=True)
    treaties_json = Column(Text, nullable=True)
    relations_json = Column(Text, nullable=True)
    citations_json = Column(Text, nullable=True)

class IndiaState(Base):
    __tablename__ = "india_states"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    type = Column(String, nullable=False) # "State" or "UT"
    capital = Column(String, nullable=False)
    rivers_json = Column(Text, nullable=True)
    mountains_json = Column(Text, nullable=True)
    soils_json = Column(Text, nullable=True)
    crops_json = Column(Text, nullable=True)
    minerals_json = Column(Text, nullable=True)
    industries_json = Column(Text, nullable=True)
    dams_json = Column(Text, nullable=True)
    highways_json = Column(Text, nullable=True)
    tribal_areas_json = Column(Text, nullable=True)
    special_focus_json = Column(Text, nullable=True)

class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(Text, nullable=False)
    question_type = Column(String, nullable=False) # e.g. multiple_choice, assertion_reason, match_following, outline_id
    options_json = Column(Text, nullable=False) # JSON list or dict representing choices
    correct_answer = Column(Text, nullable=False) # Correct index or matching sequence
    explanation = Column(Text, nullable=True)
    topic = Column(String, index=True, nullable=False) # e.g. Physical, Climate, Economic, India, etc.
    difficulty = Column(String, index=True, nullable=False) # Easy, Medium, Hard, UPSC_Level

class UserProgress(Base):
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    country_id = Column(Integer, ForeignKey("countries.id", ondelete="CASCADE"), nullable=False)
    topics_completed_json = Column(Text, default="[]") # List of sections completed
    last_studied = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="progress")

class UserQuizStat(Base):
    __tablename__ = "user_quiz_stats"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    quiz_id = Column(Integer, ForeignKey("quizzes.id", ondelete="CASCADE"), nullable=False)
    is_correct = Column(Boolean, nullable=False)
    time_taken = Column(Integer, nullable=False) # seconds
    answered_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="quiz_stats")

class UserBookmark(Base):
    __tablename__ = "user_bookmarks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    country_id = Column(Integer, ForeignKey("countries.id", ondelete="CASCADE"), nullable=False)
    section = Column(String, nullable=False) # e.g. Physical, Climate
    fact_key = Column(String, nullable=False)
    fact_value = Column(Text, nullable=False)

    user = relationship("User", back_populates="bookmarks")

class UserNote(Base):
    __tablename__ = "user_notes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    country_id = Column(Integer, ForeignKey("countries.id", ondelete="CASCADE"), nullable=False)
    note_content = Column(Text, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    user = relationship("User", back_populates="notes")

class UserFlashcard(Base):
    __tablename__ = "user_flashcards"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    front = Column(Text, nullable=False)
    back = Column(Text, nullable=False)
    easiness = Column(Float, default=2.5)
    interval = Column(Integer, default=1) # days
    repetitions = Column(Integer, default=0)
    next_review = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="flashcards")

class NewsTracker(Base):
    __tablename__ = "news_tracker"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    summary = Column(Text, nullable=False)
    url = Column(String, nullable=True)
    date_published = Column(DateTime, default=datetime.datetime.utcnow)
    coordinates_json = Column(String, nullable=True) # e.g. "28.6139, 77.2090"
    category = Column(String, nullable=False) # Disaster, Infrastructure, Geopolitics, Climate
