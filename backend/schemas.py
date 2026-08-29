from pydantic import BaseModel, EmailStr, Field


class ContactCreate(BaseModel):

    name: str = Field(min_length=2, max_length=100)

    email: EmailStr

    budget: str

    project_type: str

    message: str = Field(min_length=10, max_length=2000)