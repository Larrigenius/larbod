from datetime import datetime

from uuid import uuid4

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID

from database import Base


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(254), nullable=False)

    budget = Column(String(50), nullable=False)

    project_type = Column(String(50), nullable=False)

    message = Column(Text, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

class User(Base):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    email = Column(
        String(254),
        nullable=False,
        unique=True,
        index=True
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )