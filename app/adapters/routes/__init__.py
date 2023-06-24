from fastapi import APIRouter
from . import nasabah

api_router = APIRouter()

prefix = '/api/v1'

api_router.include_router(nasabah.router, prefix=prefix, tags=["Nasabah"])