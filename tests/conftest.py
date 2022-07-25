import os

import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

from adapters.orm import start_mappers, metadata


@pytest.fixture(scope="session")
def mappers():
    start_mappers()
    yield
    clear_mappers()


@pytest.fixture(scope="session")
def postgres_db():
    load_dotenv(f"{os.path.dirname(__file__)}/../postgres.env")

    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    s = f"postgresql://{user}:{password}@localhost:54321/postgres"
    engine = create_engine(s, isolation_level="READ COMMITTED")
    engine.connect()
    metadata.drop_all(engine, checkfirst=True)
    metadata.create_all(engine)
    return engine


@pytest.fixture
def postgres_session_factory(postgres_db):
    yield sessionmaker(bind=postgres_db)


@pytest.fixture
def postgres_session(postgres_session_factory):
    return postgres_session_factory()
