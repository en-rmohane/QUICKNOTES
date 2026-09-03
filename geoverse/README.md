# GeoVerse: 3D Interactive World Geography Learning Web App

GeoVerse is a comprehensive, production-grade 3D interactive world geography learning web application built entirely using the Python stack. It is designed to serve as a high-fidelity learning engine, focusing on physical, political, climatological, and economic geography parameters, specifically tailored for general education and UPSC civil services aspirants.

## Core Features

- **3D Interactive Globe:** Renders a fully interactive Earth globe (using Plotly Orthographic projections) with multiple layer toggles:
  - *Political:* Color-coded continents and capital city marker pins.
  - *Climate:* Köppen climate classification surface colorizations.
  - *Demographics:* Heatmap overlays representing population densities.
  - *Physical & Resources:* Custom overlays mapping mountain peaks, river basins, and key mineral deposits.
- **UPSC Detail Dossier Panels:** Granular dossiers for 50+ countries covering Physical divisions, Soil Pedology, Climate classifications, Mineral tracts, Demographic variables, and Geopolitical treaties.
- **Spaced Repetition Flashcards:** Integrated learning companion utilizing the **SuperMemo-2 (SM-2)** spaced repetition algorithm to schedule recall reviews dynamically.
- **Mock Test Quiz Engine:** A pool of **500+ questions** covering multiple choice, assertion-reason combinations, and authentic previous year UPSC questions (2010-2024).
- **India Ultra-Detailed Module:** Detailed geography dossiers covering all 28 States and 8 Union Territories alongside Interstate river water disputes and regional profiles.
- **Current Affairs Map:** Dynamic Folium map integration displaying coordinates-linked natural disaster bulletins and infrastructure project news.
- **Admin Panel & Auth:** JWT Token authentication with admin level panels to upload new quiz questions and manage dossiers.

---

## Technical Stack

- **Backend:** Python 3.12, **FastAPI** (async endpoints), **SQLAlchemy ORM**
- **Frontend:** **Streamlit**, **Plotly** (3D Scatter & Orthographic surfaces), **Folium** (2D maps via `streamlit-folium`)
- **Database:** **SQLite** (embedded, lightweight, no server config required)
- **Document Exporter:** **ReportLab** (on-the-fly PDF Dossier generation)
- **Authentication:** **Passlib** (Bcrypt password hashing) + **PyJWT** (JSON Web Tokens)

---

## Directory Structure

```text
geoverse/
├── backend/
│   ├── database.py         # SQLAlchemy engine connection
│   ├── models.py           # Database tables schemas
│   ├── schemas.py          # Pydantic validation models
│   ├── auth.py             # JWT authentication helpers
│   ├── crud.py             # Spaced repetition, user and country DB operations
│   ├── seed_data.py        # Database seeder (50+ countries, 500+ quizzes)
│   └── test_api.py         # Programmatic test script
├── frontend/
│   ├── app.py              # Streamlit landing page & routing manager
│   ├── api_client.py       # API consumer client
│   ├── styles/
│   │   └── custom.css      # Glassmorphism stylesheet
│   └── pages/
│       ├── globe_view.py   # Plotly 3D Globe page
│       ├── country_details.py # Comprehensive dossiers & PDF download
│       ├── compare.py      # Compare country panels
│       ├── quiz.py         # Quiz games & analytics dashboard
│       ├── study_desk.py   # SM-2 Flashcards, Bookmarks, and Notes
│       ├── india_special.py # Indian states & water disputes
│       ├── current_affairs.py # Folium mapped current affairs tracker
│       └── admin.py        # Question and country manager
└── requirements.txt        # Backend and Frontend dependencies
```

---

## Installation & Setup

### 1. Set Up Virtual Environment & Install Dependencies
First, ensure you are inside the `geoverse/` directory:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Seed the Database
Seed the SQLite database with 50+ countries, 36 Indian states/UTs, 500+ questions, and sample current affairs news:
```bash
python -m backend.seed_data
```
This creates the SQLite database file `backend/geoverse.db`.

### 3. Run the Backend API Server
Start the FastAPI server using Uvicorn:
```bash
uvicorn backend.main:app --reload --port 8000
```
The interactive Swagger API documentation will be available at `http://127.0.0.1:8000/docs`.

### 4. Run the Streamlit Web Application
In a separate terminal (with virtual environment active), start the Streamlit application:
```bash
streamlit run frontend/app.py
```
Open your browser and navigate to `http://localhost:8501`.

---

## Credentials
To log in, use the seeded admin credentials:
- **Username:** `admin`
- **Password:** `admin123`

You can also use the registration form to sign up as a new user.
