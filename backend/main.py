from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas import ContactCreate


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Larbod backend is running!"}


@app.post("/contact")
def create_contact(contact: ContactCreate):

    return {
        "message": "Contact message received",
        "data": contact
    }