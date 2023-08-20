import os  # noqa: I001

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from short_linker.config import settings

DEBUG: bool = os.environ.get('DEBUG', False)

if DEBUG:
    DB_NAME = 'foo.db'

    engine = create_engine('sqlite:///{}'.format(DB_NAME))
else:
    url = URL.create(
        drivername='postgresql',
        username=settings.db.username,
        host=settings.db.host,
        database=settings.db.database
    )
    engine = create_engine(url)

Session = sessionmaker(bind=engine)

def make_session() -> Session:
    return Session()

def check_engine() -> None:
    conn = engine.connect()
    conn.close()
