import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Query
from app.api.v1.v1_router import v1_router
from app.models.models import engine,create_db_and_tables,fill_all_endpoints

from typing import Annotated

load_dotenv()

webappPort = int(os.getenv("PORT"))

app = FastAPI()
app.include_router(v1_router, prefix="/v1")

def main():
    print("۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱۱")
    create_db_and_tables()
    print("oooooooooooooooookkkkkkkkkkkkkkkkkkkkkkkkkkk")
    fill_all_endpoints()
    #uvicorn.run("main:app", host="0.0.0.0", port=webappPort)


if __name__ == "__main__":
    main()