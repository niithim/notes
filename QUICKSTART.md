# Quick Start Guide

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Start the Backend

```bash
cd backend
python main.py
```

The backend will start at `http://localhost:8000`

## Step 3: Open the Frontend

### Option 1: Direct File Opening
Simply open `frontend/index.html` in your web browser.

### Option 2: Using Python HTTP Server (Recommended)
```bash
cd frontend
python -m http.server 8080
```

Then open `http://localhost:8080` in your browser.

## Step 4: Test the Application

1. Click "Sign Up" to create a new account
2. After signup, you'll be automatically logged in
3. Create your first note
4. Try editing and deleting notes

## API Documentation

Once the backend is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Troubleshooting

- **Backend won't start**: Make sure port 8000 is not in use
- **CORS errors**: Ensure backend is running before opening frontend
- **Database errors**: Delete `secure_notes.db` and restart the server
