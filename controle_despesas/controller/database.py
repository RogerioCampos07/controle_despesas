from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from controle_despesas.settings import Settings

engine = create_engine(Settings().DATABASE_URL, future=True)


def get_session():
    with Session(engine) as session:
        yield session
