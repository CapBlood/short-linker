import os

import uvicorn
from fastapi import APIRouter, FastAPI  # noqa: F401, I001
from fastapi.responses import RedirectResponse
from sqlalchemy.exc import DatabaseError

from short_linker.config import settings
from short_linker.db.orm import init_db
from short_linker.db.referencesmanager import ReferencesManager
from short_linker.db.session import check_engine

app: FastAPI = FastAPI(title='Short Linker')


@app.get('/{uid}')
def root(uid: str) -> RedirectResponse:
    original_url = ReferencesManager().get_original_url(uid)
    return RedirectResponse(original_url)


@app.get("/ping")
async def ping() -> dict:
    try:
        check_engine()
    except DatabaseError:
        return {"db_connect": "not ok"}

    return {"db_connect": "ok"}


@app.post("/create_short_link")
async def create_short_link(url: str, is_private: bool=False) -> dict:
    ref_manager = ReferencesManager()
    short_url = ref_manager.create_short_link(url, is_private)
    return {'short_link': short_url}


def run_server() -> None:
    init_db()

    DEBUG: bool = os.environ.get('DEBUG', False)

    uvicorn.run(
        "{}:{}".format('short_linker.server', 'app'), host=settings.server.host,
        port=settings.server.port, reload=DEBUG, workers=settings.server.workers
    )


if __name__ == '__main__':
    run_server()
