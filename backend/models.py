from sqlalchemy import Column, Integer, String, Text

from database import Base


class Contact(Base):

    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(254), nullable=False)

    budget = Column(String(50), nullable=False)

    project_type = Column(String(50), nullable=False)

    message = Column(Text, nullable=False)