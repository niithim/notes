"""
Secure Notes App - FastAPI Backend
Main application entry point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from database import models
from database.database import engine, DATABASE_URL
from api import auth, notes
import os

# Create database tables
# Mask password in URL for security when printing
display_url = DATABASE_URL
if "@" in DATABASE_URL and ":" in DATABASE_URL.split("@")[0]:
    # Mask password in connection string
    parts = DATABASE_URL.split("@")
    if len(parts) == 2:
        user_pass = parts[0].split("://")[1] if "://" in parts[0] else parts[0]
        if ":" in user_pass:
            user = user_pass.split(":")[0]
            display_url = DATABASE_URL.replace(f":{user_pass.split(':')[1]}@", f":****@")
print(f"Initializing database at: {display_url}")
models.Base.metadata.create_all(bind=engine)
print("✅ Database tables created/verified")

# Initialize FastAPI app
app = FastAPI(
    title="Secure Notes API",
    description="A secure notes application with JWT authentication",
    version="1.0.0"
)

# CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api", tags=["Authentication"])
app.include_router(notes.router, prefix="/api", tags=["Notes"])


@app.get("/")
def root():
    """Root endpoint"""
    return {"message": "Secure Notes API is running"}


@app.get("/api/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import sys
    import os
    # Ensure we can import from backend directory
    if os.path.dirname(__file__) not in sys.path:
        sys.path.insert(0, os.path.dirname(__file__))
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
