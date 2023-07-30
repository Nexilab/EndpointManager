from fastapi import APIRouter, HTTPException
from app.models.schemas import EndpointReq
from app.models.models import Endpoint,get_session
from app.type.types import getBlockchainEnum

router = APIRouter()