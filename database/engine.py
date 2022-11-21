from sqlalchemy.engine import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker

from models import Base

engine: Engine = None
DBsession = sessionmaker()


def init_db(file: str):
    engine = create_engine(file, max_overflow=-1)
    Base.metadata.bind = engine
    DBsession.bind = engine
