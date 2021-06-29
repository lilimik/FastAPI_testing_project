from fastapi import APIRouter

from app.api.v1 import devices, checks

api_router = APIRouter()
api_router.include_router(devices.router, prefix='/devices', tags=['devices'])
api_router.include_router(checks.router, prefix='/check', tags=['check'])
