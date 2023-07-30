from fastapi import APIRouter, HTTPException
from sqlalchemy import exists
from app.models.schemas import EndpointReq
from app.models.models import Endpoint,get_session
from app.type.types import getBlockchainEnum

router = APIRouter()


@router.post("/admin/addNewRpcurl")
def add_new_rpc_url(data: EndpointReq):
    try:
        # Validate input data using Pydantic schema
        if not data:
            raise HTTPException(status_code=400, detail="Data is null!")
        if not data.company:
            raise HTTPException(status_code=400, detail="company is null!")
        if not data.rpcUrl:
            raise HTTPException(status_code=400, detail="rpcUrl is null!")
        if not data.apikey:
            raise HTTPException(status_code=400, detail="apikey is null!")

        # Convert blockchain string to enum using getBlockchainEnum function
        blockchain_enum = getBlockchainEnum(data.blockchain)
        if blockchain_enum is None:
            raise HTTPException(status_code=400, detail="Invalid blockchain!")

        # Create a new Endpoint object
        endpoint = Endpoint(
            company=data.company,
            blockchain=blockchain_enum,
            rpcUrl=data.rpcUrl,
            apikey=data.apikey,
        )

        # Add the new Endpoint to the database using a session context manager
        with get_session() as session:
            exists_query = session.query(exists().where(Endpoint.rpcUrl == data.rpcUrl)).scalar()
            if exists_query:
                raise HTTPException(status_code=400, detail="rpcUrl already exists!")
            session.add(endpoint)
            session.commit()

        return {"message": "New RPC URL added successfully!"}

    except HTTPException as ex:
        raise ex
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
