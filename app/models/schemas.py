from pydantic import BaseModel
from app.type.types import BlockchainEnum,UserTypeEnum
from sqlalchemy import DateTime,BigInteger

class EndpointSchema(BaseModel):
    id: BigInteger
    company: str
    blockchain: BlockchainEnum
    rpcUrl: str
    apikey: str
    created_at: DateTime
    updated_at: DateTime
    class Config:
        arbitrary_types_allowed = True
        orm_mode = True
    
    
class EndpointReq(BaseModel):
    company: str
    blockchain: str
    rpcUrl: str
    apikey: str
    class Config:
        orm_mode = True
    
