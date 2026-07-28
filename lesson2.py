from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///./test2.db"

engine = create_engine(DATABASE_URL, connect_args={
    "check_same_thread": False
})

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(bind=engine)

sessionLocal = sessionmaker(bind=engine)
db = sessionLocal()

student = Student(name = "Ujjwal", age = 30)

db.add(student)
db.refresh(student)
print(student.id)
db.commit()

