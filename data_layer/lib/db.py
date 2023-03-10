from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import os

Base = declarative_base()
engine = create_engine(os.environ.get('SQL_URI'))
# use session_factory() to get a new Session
_SessionFactory = sessionmaker(bind=engine)

class DB:
    @staticmethod
    def session_factory():
        Base.metadata.create_all(engine)
        return _SessionFactory()




