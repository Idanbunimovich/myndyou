from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine('mysql+pymysql://root:qwerasdf@localhost:3306/myndyou')
# use session_factory() to get a new Session
_SessionFactory = sessionmaker(bind=engine)


def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()
