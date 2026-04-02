from fastapi import APIRouter, HTTPException
from app.database import load_users, save_users
from app.security import hash_password, verify_password
from app.auth import create_access_token

router = APIRouter()

@router.post("/register")
def register(email: str, password: str):
    users = load_users()

    for u in users:
        if u["email"] == email:
            raise HTTPException(status_code=400, detail="User already exists")

    users.append({
        "email": email,
        "password": hash_password(password)
    })

    save_users(users)

    return {"message": "User registered"}


@router.post("/login")
def login(email: str, password: str):
    users = load_users()

    for u in users:
        if u["email"] == email and verify_password(password, u["password"]):
            token = create_access_token({"sub": email})
            return {"access_token": token}

    raise HTTPException(status_code=401, detail="Invalid credentials")