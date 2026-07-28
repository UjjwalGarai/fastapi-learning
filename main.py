from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={
    "check_same_thread": False
})

class Base(DeclarativeBase):
    pass

class Todos(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    status = Column(String)

Base.metadata.create_all(bind=engine)

sessionLocal = sessionmaker(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todo")
def createTodo(title, db: Session = Depends(get_db)):
    todo = Todos(title = title, status = "False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "Message": "Data save completed",
        "Data": todo
    }

@app.get("/todos")
def get_all_todos(db: Session = Depends(get_db)):
    todos = db.query(Todos).all()
    return {
        "Total Count": len(todos),
        "Data": todos
    }

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int,db: Session = Depends(get_db)):
    todos = db.query(Todos).filter(Todos.id == todo_id).first()
    if not todos:
        raise HTTPException(404, "Todo not found")
    return {
        # "Total Count": len(todos),
        "Data": todos
    }
@app.put("/todo/{id}")
def modify_todo(id: int, title:str, status:str, db: Session = Depends(get_db)):
    todos = db.query(Todos).filter(Todos.id == id).first()
    if not todos:
            raise HTTPException(404, "Todo not found")
    todos.title = title
    todos.status = status
    db.commit()
    return{
        "Message": f"id {id} modified"
    }

@app.delete("/todo/{id}")
def delete_todo(id: int,db: Session = Depends(get_db)):
    todos = db.query(Todos).filter(Todos.id == id).first()
    if not todos:
            raise HTTPException(404, "Todo not found")
    db.delete(todos)
    db.commit()
    return{
        "Message": f"id {id} Deleted"
    }


