from sqlalchemy import Boolean, Column, Integer, String  # noqa: I001
from sqlalchemy.orm import declarative_base

from short_linker.db.session import engine

Base = declarative_base()

class Reference(Base):
    __tablename__ = 'references'

    ref_id = Column(Integer(), primary_key=True)
    short_url = Column(String(), nullable=False)
    original_url = Column(String(), nullable=False)
    is_private = Column(Boolean(), nullable=False, default=False)


def init_db() -> None:
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    init_db()

    from short_linker.db.session import make_session

    session = make_session()

    for i in session.query(Reference).all():
        print(i)
