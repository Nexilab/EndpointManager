import os
from datetime import datetime
from contextlib import contextmanager
from enum import StrEnum
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Boolean, BigInteger,Integer,Column, DateTime, ForeignKey, String, create_engine, Enum
from app.type.types import BlockchainEnum
from app.models.global_vars import addNewRpcUrl

from sqlalchemy.pool import StaticPool

load_dotenv()
database_url = os.getenv("DATABASEURL")

Base = declarative_base()

engine = create_engine(
    database_url,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # Use a static pool to persist state with an in memory instance of sqlite
)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


_inc = 1


def _get_str_inc():
    global _inc
    s = str(_inc)
    _inc = _inc + 1
    return s


def _reset_inc():
    global _inc
    _inc = 1



class Endpoint(Base):
    __tablename__ = "tblEndpoint"
    id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True, autoincrement=True)
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

def create_db_and_tables():
    Base.metadata.create_all(engine)


@contextmanager
def get_session():
    session = Session(bind=engine)
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def fill_all_endpoints():
    # Get all existing endpoints from the database
    idx = 0
    session = Session(bind=engine)
    endpoints = session.query(Endpoint).all()

    # Call addNewRpcUrl for each endpoint to add them to the global map
    for endpoint in endpoints:
        addNewRpcUrl(endpoint.blockchain, endpoint.rpcUrl)
        idx = idx + 1
    print(f"{idx} rpc url has been added.")



    def close_database_connection():
        engine.dispose()
    