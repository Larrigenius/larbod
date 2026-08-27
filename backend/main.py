from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel, EmailStr, Field


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContactMessage(BaseModel):

    name: str = Field(min_length=2, max_length=100)

    email: EmailStr

    budget: str

    project_type: str

    message: str = Field(min_length=10, max_length=2000)


@app.get("/")
def home():
    return {"message": "Larbod backend is running!"}


@app.post("/contact")
def create_contact(contact: ContactMessage):

    return {
        "message": "Contact message received",
        "data": contact
    }