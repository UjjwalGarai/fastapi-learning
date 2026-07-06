from fastapi import FastAPI, Request
from time import time

app = FastAPI()

@app.middleware("http")
async def timeTracking(req: Request, call_next):
    start_time = time()
    print(start_time)
    response = await call_next(req)
    processTime = time() - start_time
    print (f"Path {req.url.path} \ntime taken: {processTime}")
    return response
