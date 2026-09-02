import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    app_name = os.getenv("APP_NAME", "Larbod")
    environment = os.getenv("ENVIRONMENT", "development")

    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME")


settings = Settings()