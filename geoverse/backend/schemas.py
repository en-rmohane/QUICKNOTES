from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict, Any
from datetime import datetime

# Auth schemas
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    is_admin: bool
    streak: int
    xp: int
    last_login: datetime

    class Config:
        from_attributes = True

# Country schemas
class CountrySummary(BaseModel):
    id: int
    name: str
    code: str
    continent: str
    location_coords: Optional[str] = None
    population: Optional[int] = None
    hdi: Optional[float] = None
    gdp: Optional[float] = None

    class Config:
        from_attributes = True

class CountryOut(BaseModel):
    id: int
    name: str
    code: str
    continent: str
    geometry_json: Optional[str] = None
    location_coords: Optional[str] = None
    area_sq_km: Optional[float] = None
    boundaries: Optional[str] = None
    mountains_json: Optional[str] = None
    peaks_json: Optional[str] = None
    rivers_json: Optional[str] = None
    lakes_json: Optional[str] = None
    plateaus_json: Optional[str] = None
    plains_json: Optional[str] = None
    deserts_json: Optional[str] = None
    straits_json: Optional[str] = None
    coastline_json: Optional[str] = None
    koppen_classification: Optional[str] = None
    temperature_avg_json: Optional[str] = None
    rainfall_json: Optional[str] = None
    winds_json: Optional[str] = None
    vegetation_json: Optional[str] = None
    parks_json: Optional[str] = None
    environmental_issues: Optional[str] = None
    disasters_json: Optional[str] = None
    soil_types_json: Optional[str] = None
    crops_json: Optional[str] = None
    farming_patterns: Optional[str] = None
    irrigation_json: Optional[str] = None
    green_rev_impact: Optional[str] = None
    gi_tags_json: Optional[str] = None
    minerals_json: Optional[str] = None
    mining_regions_json: Optional[str] = None
    industries_json: Optional[str] = None
    corridors_json: Optional[str] = None
    energy_resources_json: Optional[str] = None
    pipelines_refineries_json: Optional[str] = None
    power_plants_json: Optional[str] = None
    population: Optional[int] = None
    density: Optional[float] = None
    growth_rate: Optional[float] = None
    cities_json: Optional[str] = None
    urbanization_rate: Optional[float] = None
    ethnic_groups_json: Optional[str] = None
    languages_json: Optional[str] = None
    literacy_rate: Optional[float] = None
    sex_ratio: Optional[str] = None
    hdi: Optional[float] = None
    government_type: Optional[str] = None
    admin_divisions_json: Optional[str] = None
    currency: Optional[str] = None
    gdp: Optional[float] = None
    gdp_per_capita: Optional[float] = None
    trade_json: Optional[str] = None
    ports_json: Optional[str] = None
    airports_json: Optional[str] = None
    infrastructure_json: Optional[str] = None
    dams_json: Optional[str] = None
    timezones_json: Optional[str] = None
    border_disputes_json: Optional[str] = None
    geopolitical_significance: Optional[str] = None
    treaties_json: Optional[str] = None
    relations_json: Optional[str] = None
    citations_json: Optional[str] = None

    class Config:
        from_attributes = True

# India State schemas
class IndiaStateOut(BaseModel):
    id: int
    name: str
    type: str
    capital: str
    rivers_json: Optional[str] = None
    mountains_json: Optional[str] = None
    soils_json: Optional[str] = None
    crops_json: Optional[str] = None
    minerals_json: Optional[str] = None
    industries_json: Optional[str] = None
    dams_json: Optional[str] = None
    highways_json: Optional[str] = None
    tribal_areas_json: Optional[str] = None
    special_focus_json: Optional[str] = None

    class Config:
        from_attributes = True

# Quiz schemas
class QuizOut(BaseModel):
    id: int
    question_text: str
    question_type: str
    options_json: str
    explanation: Optional[str] = None
    topic: str
    difficulty: str

    class Config:
        from_attributes = True

class QuizAnswerSubmit(BaseModel):
    quiz_id: int
    selected_answer: str # index or key
    time_taken: int

class QuizResult(BaseModel):
    is_correct: bool
    correct_answer: str
    explanation: Optional[str] = None

# Progress schemas
class UserProgressUpdate(BaseModel):
    country_id: int
    section: str

class UserProgressOut(BaseModel):
    country_id: int
    topics_completed_json: str
    last_studied: datetime

    class Config:
        from_attributes = True

# Bookmark schemas
class BookmarkCreate(BaseModel):
    country_id: int
    section: str
    fact_key: str
    fact_value: str

class BookmarkOut(BaseModel):
    id: int
    country_id: int
    country_name: Optional[str] = None
    section: str
    fact_key: str
    fact_value: str

    class Config:
        from_attributes = True

# Note schemas
class NoteCreate(BaseModel):
    country_id: int
    note_content: str

class NoteOut(BaseModel):
    id: int
    country_id: int
    country_name: Optional[str] = None
    note_content: str
    updated_at: datetime

    class Config:
        from_attributes = True

# Flashcard schemas
class FlashcardCreate(BaseModel):
    front: str
    back: str

class FlashcardReview(BaseModel):
    card_id: int
    rating: int # SM-2 score 0 to 5

class FlashcardOut(BaseModel):
    id: int
    front: str
    back: str
    easiness: float
    interval: int
    repetitions: int
    next_review: datetime

    class Config:
        from_attributes = True

# News Tracker schemas
class NewsOut(BaseModel):
    id: int
    title: str
    summary: str
    url: Optional[str] = None
    date_published: datetime
    coordinates_json: Optional[str] = None
    category: str

    class Config:
        from_attributes = True
