from pydantic import BaseModel
from app.type.types import BlockchainEnum,UserTypeEnum

class EndpointSchema(BaseModel):
    id: int
    company: str
    blockchain : BlockchainEnum
