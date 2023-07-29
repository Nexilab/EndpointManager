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
