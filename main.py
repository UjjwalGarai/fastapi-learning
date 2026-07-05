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

class Product(BaseModel):
    id: int
    name: str
    price: int


@app.post("/user")
def userCreate(user:dict):
    return {
        "message": "Data Creation Done",
        "Data": user
    }

@app.post("/product")
def create_product(product:Product):
    return {
        "message": "Data Creation Done",
        "Data": product
    }