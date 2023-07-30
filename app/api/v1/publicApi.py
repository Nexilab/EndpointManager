import requests
import random
import json

from fastapi import APIRouter, HTTPException, Body
from app.models.global_vars import getRandomRpcUrl

router = APIRouter()


@router.post("/publicApi/{blockchain}")
def sendReq(blockchain: str, payload: dict = Body(...)):
    max_retries = 500
    retry_count = 0

    while retry_count < max_retries:
        rpcUrl = getRandomRpcUrl(blockchain)
        print(f"Selected rpcurl is : {rpcUrl}")
        headers = {'Content-Type': 'application/json'}

        try:
            response = requests.post(rpcUrl, json=payload, headers=headers, timeout=(30, 30))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            retry_count += 1
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON data: {e}")
            raise HTTPException(status_code=400, detail="Invalid JSON data!")

    # If max retries reached and no successful response, raise an error
    raise HTTPException(status_code=500, detail="Failed to get a valid response after multiple retries.")
