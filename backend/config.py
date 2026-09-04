import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    def __init__(self):
        self.app_name = os.getenv("APP_NAME", "Larbod")
        self.environment = os.getenv("ENVIRONMENT", "development")

        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_host = os.getenv("DB_HOST", "localhost")
        self.db_port = os.getenv("DB_PORT", "5432")
        self.db_name = os.getenv("DB_NAME")

        self.validate()

    def validate(self):
        required_settings = {
            "DB_USER": self.db_user,
            "DB_PASSWORD": self.db_password,
            "DB_NAME": self.db_name,
        }

        missing = [
            name
            for name, value in required_settings.items()
            if not value
        ]

        if missing:
            raise RuntimeError(
                "Missing required environment variables: "
                + ", ".join(missing)
            )


settings = Settings()