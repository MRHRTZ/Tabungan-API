import structlog

from fastapi import FastAPI
from .routes import api_router

app = FastAPI(title="Tabungan API", version="1.0.0")
log = structlog.get_logger('uvicorn')

app.include_router(api_router)

def start():
    import uvicorn
    log.info('Initialize FastAPI ...')
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")