# Importing the functions from SQLAlchemy for database connection and session management.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Defining the database connection string for a SQLite database.
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Creating a database engine that provides connectivity to the database specified by the connection string.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Creating a configured "SessionLocal" class which will serve as a factory for new Session objects.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# A dependency function that will be used to generate database sessions.
def get_db():
    # Creating a new session instance from the session factory defined above.
    db = SessionLocal()
    try:
        # Yielding the session and engine to be used in the endpoint function.
        yield db,engine
    finally:
        # Ensuring the session is closed properly after the request is finished.
        db.close()
