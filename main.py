from fastapi import FastAPI

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

@app.get("/users")
def getUsers():
    return users

@app.get("/home")
def home():
    return {
        "Message": "This is a home page"
    }

@app.get("/about")
def about():
    return {
        "Message": "This is a about page"
    }