from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
import bcrypt
from database import SessionLocal
from models import User
from auth_utils import verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, hash_password
from datetime import timedelta

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    print(f"🔍 Login attempt for email: '{email}'")
    print(f"🔍 Password length: {len(password)}")
    
    # Query user by email instead of username
    user = db.query(User).filter(User.email == email).first()
    
    if not user:
        print(f"❌ User not found in database for email: '{email}'")
        # Let's see what emails actually exist
        all_users = db.query(User.email).all()
        print(f"📋 Available emails in database: {[u.email for u in all_users]}")
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    print(f"✅ User found: {user.email} (username: {user.username})")
    
    # ENHANCED DEBUGGING - Add this section
    print(f"🔍 Raw stored hash: {repr(user.password_hash)}")
    print(f"🔍 Hash length: {len(user.password_hash)}")
    print(f"🔍 Hash starts with $2b$: {user.password_hash.startswith('$2b$')}")
    print(f"🔍 Provided password: {repr(password)}")
    
    # Test hash/verify with a known password
    test_password = "test123"
    test_hash = hash_password(test_password)
    test_verify = verify_password(test_password, test_hash)
    print(f"🧪 Hash/verify test (should be True): {test_verify}")
    
    # Try to create a hash of the current password and compare
    current_password_hash = hash_password(password)
    print(f"🔍 New hash of current password: {current_password_hash[:30]}...")
    
    # Check if there are any encoding issues
    try:
        password_bytes = password.encode('utf-8')
        hash_bytes = user.password_hash.encode('utf-8')
        manual_check = bcrypt.checkpw(password_bytes, hash_bytes)
        print(f"🔍 Manual bcrypt check: {manual_check}")
    except Exception as e:
        print(f"❌ Manual bcrypt error: {e}")
    
    # Verify password
    password_valid = verify_password(password, user.password_hash)
    print(f"🔍 Password verification result: {password_valid}")
    
    if not password_valid:
        print(f"❌ Password verification failed for email: '{email}'")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    print(f"✅ Login successful for email: '{email}'")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)

    return {
        "access_token": access_token, 
        "token_type": "bearer",
        "username": user.username,
        "email": user.email
    }

