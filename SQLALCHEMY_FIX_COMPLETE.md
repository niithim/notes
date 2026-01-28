# SQLAlchemy 2.0 Query Syntax Fix

## Problem
Error e3q8 from SQLAlchemy indicates deprecated `session.query()` usage. SQLAlchemy 2.0 requires using `select()` statements instead.

## Fix Applied

### Changed From (Old SQLAlchemy 1.x):
```python
user = db.query(models.User).filter(models.User.email == email).first()
notes = db.query(models.Note).filter(models.Note.user_id == user_id).all()
```

### Changed To (SQLAlchemy 2.0):
```python
from sqlalchemy import select

stmt = select(models.User).where(models.User.email == email)
user = db.scalar(stmt)

stmt = select(models.Note).where(models.Note.user_id == user_id)
notes = db.scalars(stmt).all()
```

## Files Updated

1. **backend/api/auth.py**
   - All `db.query()` calls replaced with `select()` statements
   - 4 locations fixed

2. **backend/api/notes.py**
   - All `db.query()` calls replaced with `select()` statements
   - 4 locations fixed

## Key Changes

- `db.query(Model).filter(...).first()` → `db.scalar(select(Model).where(...))`
- `db.query(Model).filter(...).all()` → `db.scalars(select(Model).where(...)).all()`
- Added `from sqlalchemy import select` to both files

## Verification

After these changes:
- ✅ All queries use SQLAlchemy 2.0 syntax
- ✅ No more deprecated `query()` calls
- ✅ Error e3q8 should be resolved

## Next Steps

1. Restart the backend server
2. The SQLAlchemy error should be gone
3. All database operations should work correctly
