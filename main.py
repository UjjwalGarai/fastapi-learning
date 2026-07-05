from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserDataResponseModel(BaseModel):
    name: str
    age: int

@app.get("/user", response_model=UserDataResponseModel)
def get_user():
    return {
        "name": "Ujjwal",
        "age": 24,
        "password": 12345
    }
