import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Contact
from schemas import ContactCreate


router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/contact")
def create_contact(
    contact: ContactCreate,
    db: Session = Depends(get_db)
):
    new_contact = Contact(
        name=contact.name,
        email=contact.email,
        budget=contact.budget,
        project_type=contact.project_type,
        message=contact.message
    )

    try:
        db.add(new_contact)
        db.commit()
        db.refresh(new_contact)

    except Exception:
        db.rollback()
        logger.exception("Failed to save contact message")

        raise HTTPException(
            status_code=500,
            detail="Unable to save contact message"
        )

    return {
        "message": "Contact message saved successfully",
        "id": new_contact.id
    }