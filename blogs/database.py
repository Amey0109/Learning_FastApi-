from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Creating Database Connection 
Base= declarative_base()

SQLALCHEMY_DATABASE_URL='sqlite:///./blog.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args= {"check_same_thread": False})

SessionLocal= sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()        # Create a new database session
    try:
        yield db               # Give it to the path operation function (temporarily)
    finally:
        db.close()             # Close the session when the request is done