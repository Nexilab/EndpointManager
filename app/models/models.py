from datetime import datetime
from enum import Enum
from dotenv import load_dotenv
import os

from sqlalchemy import Boolean, BigInteger,Column, DateTime, ForeignKey, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.pool import StaticPool

load_dotenv()
database_url = os.getenv("DATABASEURL")

Base = declarative_base()

engine = create_engine(
    database_url,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # Use a static pool to persist state with an in memory instance of sqlite
)

_inc = 1


def _get_str_inc():
    global _inc
    s = str(_inc)
    _inc = _inc + 1
    return s


def _reset_inc():
    global _inc
    _inc = 1

class BlockchainEnum(Enum):
    BSC = "bsc"
    ETHEREUM = "Ethereum"
    LITECOIN = "Litecoin"
    POLYGON  = "Polygon"
    MUMBAI   = "Mumbai"

class UserTypeEnum(Enum):
    USER = "user"
    ADMIN = "ADMIN"
    GOD = "GOD"


class Endpoint(Base):
    __tablename__ = "tblEndpoint"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    company = Column(String(255), nullable=False)
    blockchain = Column(Enum(BlockchainEnum), nullable=False)
    rpcUrl= Column(String(255), unique=True, nullable=False)
    apikey= Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime)

class User(Base):
    __tablename__ = "tblUser"
    userId = Column(BigInteger, primary_key=True, autoincrement=True)
    emailAddress = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    apiKey = Column(String(255), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime)

Base.metadata.create_all(engine)

