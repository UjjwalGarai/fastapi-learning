from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test3.db"

engine = create_engine(DATABASE_URL, connect_args={
    "check_same_thread": False
})

sessionLocal = sessionmaker(bind=engine)

db = sessionLocal()
db.close()

# print(type(engine))
# print(type(sessionLocal))
# print(type(db))
db2 = sessionLocal()
# print(id(engine))
print(id(db))
print(id(db2))

db = sessionLocal
print(db)