import os

import pytest


os.environ["DB_NAME"] = "larbod_test"

from database import Base, engine
import models


@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    Base.metadata.create_all(bind=engine)

    yield

    Base.metadata.drop_all(bind=engine)