"""
Secure Notes App - FastAPI Backend
Main application entry point
"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
import uvicorn

from database import models, database
from database.database import SessionLocal, engine
from api import auth, notes

# Create database tables
models.Base.metadata.create_all(bind=engine)

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

# Security scheme for JWT
security = HTTPBearer()

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


import os

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )

