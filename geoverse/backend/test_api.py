import unittest
import sys
import os
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add geoverse root to path so we can import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.database import Base
from backend import models, crud, auth, schemas

class TestGeoVerseBackend(unittest.TestCase):
    def setUp(self):
        # Setup in-memory SQLite for isolated testing
        self.engine = create_engine("sqlite:///:memory:")
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        Base.metadata.create_all(bind=self.engine)
        self.db = self.SessionLocal()

    def tearDown(self):
        self.db.close()
        Base.metadata.drop_all(bind=self.engine)

    def test_user_creation_and_auth(self):
        # Create user schema
        user_in = schemas.UserCreate(
            username="test_student",
            email="student@geoverse.edu",
            password="secure_password_123"
        )
        
        # Save to DB
        db_user = crud.create_user(self.db, user_in)
        self.assertIsNotNone(db_user.id)
        self.assertEqual(db_user.username, "test_student")
        
        # Verify credentials hashing
        self.assertTrue(auth.verify_password("secure_password_123", db_user.hashed_password))
        self.assertFalse(auth.verify_password("wrong_password", db_user.hashed_password))

        # Test JWT signing
        token = auth.create_access_token(data={"sub": db_user.username})
        self.assertIsNotNone(token)
        
        # Decode and check sub
        payload = auth.jwt.decode(token, auth.SECRET_KEY, algorithms=[auth.ALGORITHM])
        self.assertEqual(payload.get("sub"), "test_student")

    def test_sm2_spaced_repetition_logic(self):
        # Create a mock user
        user_in = schemas.UserCreate(
            username="reviser",
            email="reviser@geoverse.org",
            password="mypassword"
        )
        user = crud.create_user(self.db, user_in)
        
        # Create flashcard
        card_in = schemas.FlashcardCreate(
            front="What is the Koppen code for Hot Desert climate?",
            back="BWh"
        )
        card = crud.create_flashcard(self.db, user_id=user.id, f=card_in)
        
        self.assertEqual(card.repetitions, 0)
        self.assertEqual(card.interval, 1)
        self.assertEqual(card.easiness, 2.5)
        
        # Simulate review 1: rating 4 (Good)
        card = crud.review_flashcard_sm2(self.db, user_id=user.id, card_id=card.id, q=4)
        self.assertEqual(card.repetitions, 1)
        self.assertEqual(card.interval, 1)
        self.assertTrue(card.easiness > 2.2) # easiness shifts slightly
        
        # Simulate review 2: rating 5 (Perfect)
        card = crud.review_flashcard_sm2(self.db, user_id=user.id, card_id=card.id, q=5)
        self.assertEqual(card.repetitions, 2)
        self.assertEqual(card.interval, 6) # second correct review interval is 6 days

        # Simulate review 3: rating 2 (Hard - incorrect memory recall)
        card = crud.review_flashcard_sm2(self.db, user_id=user.id, card_id=card.id, q=2)
        self.assertEqual(card.repetitions, 0) # repetitions reset on failure
        self.assertEqual(card.interval, 1) # interval reset to 1 day

    def test_country_seeding_structure(self):
        # Test inserting custom country dossier
        c_detail = models.Country(
            name="Nepal",
            code="NPL",
            continent="Asia",
            location_coords="28.3949, 84.1240",
            population=30000000,
            gdp=40.0,
            hdi=0.602
        )
        self.db.add(c_detail)
        self.db.commit()
        
        db_c = crud.get_country_by_code(self.db, "NPL")
        self.assertIsNotNone(db_c)
        self.assertEqual(db_c.name, "Nepal")

if __name__ == "__main__":
    unittest.main()
