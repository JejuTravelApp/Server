import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


app = FastAPI()

@app.get("/")
async def root():
    test_env = os.environ["TEST_ENV"]
    return test_env

if __name__ == "__main__":
    uvicorn.run()