from config import settings
from datetime import datetime, timedelta, timezone
import secrets

from dependencies import get_current_user

from fastapi import APIRouter, Cookie, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from models import User, UserSession
from schemas import UserCreate, UserLogin
from security import hash_password, verify_password


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    existing_user = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )

    user = User(
        email=user_data.email,
        password_hash=hash_password(user_data.password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "message": "User registered successfully",
        "user_id": str(user.id),
        "email": user.email,
    }

@router.post("/login")
def login(
    user_data: UserLogin,
    response: Response,
    db: Session = Depends(get_db),
):
    user = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )

    if not user or not verify_password(
        user_data.password,
        user.password_hash,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    session_token = secrets.token_urlsafe(48)

    session = UserSession(
        user_id=user.id,
        session_token=session_token,
        expires_at=datetime.now(timezone.utc) + timedelta(hours=24),
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    response.set_cookie(
        key="larbod_session",
        value=session_token,
        httponly=True,
        secure=settings.is_production,
        samesite="lax",
        max_age=24 * 60 * 60,
        path="/",
    )

    return {
        "message": "Login successful",
        "user_id": str(user.id),
        "email": user.email,
    }

@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user),
):
    return {
        "user_id": str(current_user.id),
        "email": current_user.email,
        "is_active": current_user.is_active,
    }

@router.post("/logout")
def logout(
    response: Response,
    larbod_session: str | None = Cookie(default=None),
    db: Session = Depends(get_db),
):
    if larbod_session:
        session = (
            db.query(UserSession)
            .filter(UserSession.session_token == larbod_session)
            .first()
        )

        if session:
            db.delete(session)
            db.commit()

    response.delete_cookie(
        key="larbod_session",
        httponly=True,
        secure=settings.is_production,
        samesite="lax",
        path="/",
    )

    return {
        "message": "Logout successful"
    }
