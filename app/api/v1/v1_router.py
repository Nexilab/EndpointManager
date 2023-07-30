from fastapi import APIRouter

from .adminApi import router as admin_router
from .publicApi import router as public_router

v1_router = APIRouter()

v1_router.include_router(admin_router, prefix="/admin", tags=["admin"])
v1_router.include_router(public_router, prefix="/public", tags=["public"])