"""
Notes CRUD endpoints
All endpoints are protected with JWT authentication
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from pydantic import BaseModel
from typing import List
from datetime import datetime

from database.database import get_db
from database import models
from api.auth import verify_token

router = APIRouter()


# Pydantic models for request/response
class NoteCreate(BaseModel):
    title: str
    content: str


class NoteUpdate(BaseModel):
    title: str
    content: str


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# API Endpoints
@router.post("/notes", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
def create_note(
    note_data: NoteCreate,
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    """
    Create a new note
    - Requires JWT authentication
    - Associates note with logged-in user
    """
    # Validate input
    if not note_data.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Title cannot be empty"
        )

    # Create new note
    new_note = models.Note(
        user_id=user_id,
        title=note_data.title,
        content=note_data.content
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note


@router.get("/notes", response_model=List[NoteResponse])
def get_notes(
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    """
    Get all notes for the logged-in user
    - Requires JWT authentication
    - Returns only notes belonging to the user
    """
    stmt = select(models.Note).where(models.Note.user_id == user_id).order_by(models.Note.updated_at.desc())
    notes = db.scalars(stmt).all()
    return notes


@router.get("/notes/{note_id}", response_model=NoteResponse)
def get_note(
    note_id: int,
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    """
    Get a specific note by ID
    - Requires JWT authentication
    - Only returns note if it belongs to the user
    """
    stmt = select(models.Note).where(
        models.Note.id == note_id,
        models.Note.user_id == user_id
    )
    note = db.scalar(stmt)

    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found"
        )

    return note


@router.put("/notes/{note_id}", response_model=NoteResponse)
def update_note(
    note_id: int,
    note_data: NoteUpdate,
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    """
    Update an existing note
    - Requires JWT authentication
    - Only allows updating notes belonging to the user
    """
    # Find note
    stmt = select(models.Note).where(
        models.Note.id == note_id,
        models.Note.user_id == user_id
    )
    note = db.scalar(stmt)

    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found"
        )

    # Validate input
    if not note_data.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Title cannot be empty"
        )

    # Update note
    note.title = note_data.title
    note.content = note_data.content
    note.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(note)

    return note


@router.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(
    note_id: int,
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):
    """
    Delete a note
    - Requires JWT authentication
    - Only allows deleting notes belonging to the user
    """
    # Find note
    stmt = select(models.Note).where(
        models.Note.id == note_id,
        models.Note.user_id == user_id
    )
    note = db.scalar(stmt)

    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found"
        )

    # Delete note
    db.delete(note)
    db.commit()

    return None
