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

@app.get("/user/{user_name}")
def getUsers(user_name: str):
    for user in users:
        if user["Name"] == user_name:
            return user
    return {
        "Message": "User not found"
    }