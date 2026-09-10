from typing import Literal
from pydantic import BaseModel, EmailStr, Field
class ContactCreate(BaseModel):

    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    budget: Literal[
        "Under $500",
        "$500 - $1,000",
        "$1,000 - $5,000",
        "$5,000+",
    ]
    project_type: Literal[
        "Website Development",
        "Automation",
        "API Development",
        "AI Solutions",
    ]

    message: str = Field(min_length=10, max_length=2000)