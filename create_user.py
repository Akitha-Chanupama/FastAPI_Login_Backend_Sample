from database import SessionLocal
from models import User
from auth_utils import hash_password
from datetime import datetime

def create_user(username: str, email: str, password: str):
    db = SessionLocal()
    try:
        user = User(
            username=username,
            email=email,
            password_hash=hash_password(password),
            active=True,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.add(user)
        db.commit()
        print(f"User {username} created successfully.")
    except Exception as e:
        print("Error:", e)
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    # Replace with desired username, email and password
    create_user("testuser1122", "testuser1122@example.com", "testpassword1122")
    
