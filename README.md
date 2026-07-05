# FastAPI Learning

## Notes

 -- FastAPI: API is a bridge between frontend and bakend, It transfer the data JSON light weight format
 -- It has automatic documentation, Asynchronous support and fast compare to other services


## Create venv
python -m venv .venv
.venv/Scripts/activate

## Installation

pip install fastapi uvicorn

pip install -r requirements.txt

### Create requirements.txt file using pip

pip freeze > requirements.txt

## Run

uvicorn main:app --reload