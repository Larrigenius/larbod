import os

# Select the dedicated test database before importing application modules.
os.environ["DB_NAME"] = "larbod_test"

import pytest  # type: ignore[import-not-found]

from database import Base, engine
import models


@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    if engine.url.database != "larbod_test":
        raise RuntimeError(
            f"Tests must use larbod_test, not {engine.url.database!r}"
        )

    Base.metadata.create_all(bind=engine)

    yield

    Base.metadata.drop_all(bind=engine)
