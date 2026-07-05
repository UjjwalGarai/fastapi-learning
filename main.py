from fastapi import FastAPI, status, HTTPException


app = FastAPI()


@app.post("/usercreation", status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "User data created"
    }


@app.get("/user/{user_id}", status_code=status.HTTP_200_OK)
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return {
        "message": "User found"
    }