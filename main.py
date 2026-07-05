from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = [
    {
        "id": 1,
        "Name": "Ujjwal",
        "Age": 30
    },
    {
        "id": 2,
        "Name": "Sampa",
        "Age": 30
    },
    {
        "id": 3,
        "Name": "Tiyasa",
        "Age": 2
    },
    {
        "id": 4,
        "Name": "Jaydeb",
        "Age": 59
    },
    {
        "id": 5,
        "Name": "Rekha",
        "Age": 52
    },

]


class User(BaseModel):
    id: int
    Name: str
    Age: int


@app.post("/user")
def createUser(user: User):
    users.append(user)
    return {
        "Message": "New User Data Created",
        "Data": user
    }


@app.get("/users")
def getUsers():
    return users


@app.get("/user/{user_id}")
def getUser(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return {
                "Message": "New User Data Created",
                "Data": user
            }
    return {
        "Message": "User not found",
    }

@app.put("/userModification/{user_id}")
def userModification(user_id: int, updatedUser:User):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            users[index] = updatedUser
            return {
                "Message": "User Data modified",
                "Data": updatedUser
            }
    return {
        "Message": "User not found",
    }

@app.delete("/user/{user_id}")
def delete_user(user_id:int):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            users.pop(index)
            return {
                "Message": "User deleted",
            }
    return {
                "Message": "User not found",
            }
