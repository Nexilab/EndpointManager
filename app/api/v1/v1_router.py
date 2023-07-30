from fastapi import APIRouter

from .adminApi import router as admin_router

v1_router = APIRouter()

v1_router.include_router(admin_router, prefix="/admin", tags=["admin"])