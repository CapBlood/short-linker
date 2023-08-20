import uuid

from short_linker.config import settings
from short_linker.db.orm import Reference
from short_linker.db.session import make_session


class ReferencesManager:
    def __init__(self) -> None:
        self.__session = make_session()

    def create_short_link(self, original_url: str, is_private: bool=False) -> str:
        short_url = uuid.uuid1()
        reference = Reference(
            short_url=short_url, original_url=original_url, is_private=is_private)

        self.__session.add(reference)
        self.__session.commit()

        return "{}/{}".format(settings.server.domain, short_url)

    def get_original_url(self, short_url: str) -> str:
        return self.__session.query(
             Reference).filter_by(short_url=short_url).first().original_url
