"""
Database configuration and session management
"""

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os

# Get the directory where this file is located (backend/database/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# MySQL Database Configuration
# You can override these with environment variables
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "Nithin@123")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "secure_notes")

# Construct database URL
# IMPORTANT: Don't manually concatenate credentials into a URL string because
# special characters in passwords (like @, :, /) must be URL-encoded.
# SQLAlchemy's URL.create() handles this safely.
DEFAULT_DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username=MYSQL_USER,
    password=MYSQL_PASSWORD,
    host=MYSQL_HOST,
    port=int(MYSQL_PORT),
    database=MYSQL_DATABASE,
)

# Allow full override via env var if user wants to provide DATABASE_URL themselves.
# If you set DATABASE_URL manually and your password contains special chars,
# ensure it is URL-encoded (e.g. @ => %40).
DATABASE_URL = os.getenv("DATABASE_URL") or DEFAULT_DATABASE_URL.render_as_string(hide_password=False)

# Create engine
# For MySQL, we use pymysql driver
# For SQLite (if needed), use different connection args
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    # MySQL connection with connection pooling
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,  # Verify connections before using
        pool_recycle=3600,   # Recycle connections after 1 hour
        echo=False  # Set to True for SQL query logging
    )

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models (SQLAlchemy 2.0 style)
class Base(DeclarativeBase):
    pass


def get_db():
    """
    Dependency function to get database session
    Yields a database session and closes it after use
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
