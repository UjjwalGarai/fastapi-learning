from fastapi import FastAPI, Header, HTTPException, status, Depends


app = FastAPI()

def verifyToken(token: str = Header(None)):
    if token != "security-code12345":
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail="User Unauthorized")
    return {
        "Status": "User Authorized"
    }

@app.get("/user")
def getUserDetails(token = Depends(verifyToken)):
    return {
        "User": "Ujjwal",
        "token": token
    }