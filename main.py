from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = [
    {
        "Name":"Ujjwal",
        "Age": 30
    },
    {
        "Name":"Sampa",
        "Age": 30
    },
    {
        "Name":"Tiyasa",
        "Age": 2
    },
    {
        "Name":"Jaydeb",
        "Age": 59
    },
    {
        "Name":"Rekha",
        "Age": 52
    },
 
    ]

class Address(BaseModel):
    city: str
    pin:int

class User(BaseModel):
    name: str
    age:int
    address:Address

@app.post("/user")
def create_User(user: User):
    return user