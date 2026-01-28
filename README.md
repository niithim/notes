# Secure Notes App

A full-stack web application for creating and managing personal notes with secure authentication.

## 🚀 Quick Start

**New to this project?** Start here:
- **📖 Step-by-Step Guide:** See [RUN_STEPS.md](RUN_STEPS.md) for detailed instructions
- **⚡ Quick Reference:** See [QUICK_START.txt](QUICK_START.txt) for a one-page guide
- **🔧 Having Issues?** See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for solutions

**Just want to run it?**
1. `pip install -r requirements.txt`
2. `python start_server.py` (or double-click `run_backend_safe.bat` on Windows)
3. Open `frontend/index.html` in your browser

## Features

- ✅ User registration and login
- ✅ JWT-based authentication
- ✅ Password reset functionality
- ✅ Create, read, update, and delete notes
- ✅ User-specific note isolation
- ✅ Responsive Bootstrap UI
- ✅ Secure password hashing with bcrypt

## Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript (ES6+)
- Bootstrap 5.3

### Backend
- Python 3.8+
- FastAPI
- SQLAlchemy ORM
- JWT Authentication
- Bcrypt for password hashing

### Database
- SQLite (default) or PostgreSQL

## Project Structure

```
notes/
├── backend/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth.py          # Authentication endpoints
│   │   └── notes.py         # Notes CRUD endpoints
│   ├── database/
│   │   ├── __init__.py
│   │   ├── database.py      # Database configuration
│   │   └── models.py        # SQLAlchemy models
│   └── main.py              # FastAPI application
├── frontend/
│   ├── css/
│   │   └── style.css        # Custom styles
│   ├── js/
│   │   ├── auth.js          # Authentication utilities
│   │   ├── login.js         # Login page logic
│   │   ├── signup.js        # Signup page logic
│   │   ├── forgot-password.js  # Password reset logic
│   │   └── dashboard.js     # Dashboard and notes logic
│   ├── index.html           # Login page
│   ├── signup.html          # Signup page
│   ├── forgot-password.html # Password reset page
│   └── dashboard.html       # Notes dashboard
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- A modern web browser

### Backend Setup

1. **Navigate to the project directory:**
   ```bash
   cd notes
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the backend server:**

   **Option 1: From project root (Recommended)**
   ```bash
   python start_server.py
   ```
   
   **Option 2: From backend directory**
   ```bash
   cd backend
   python main.py
   ```
   
   **Option 3: Using uvicorn directly**
   ```bash
   cd backend
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

   The API will be available at `http://localhost:8000`

   - API Documentation: `http://localhost:8000/docs`
   - Alternative docs: `http://localhost:8000/redoc`

### Frontend Setup

1. **Open the frontend files:**
   - Simply open `frontend/index.html` in your web browser
   - Or use a local web server (recommended):
     
     **Using Python:**
     ```bash
     cd frontend
     python -m http.server 8080
     ```
     Then open `http://localhost:8080` in your browser
     
     **Using Node.js (if installed):**
     ```bash
     cd frontend
     npx http-server -p 8080
     ```

2. **Update API URL (if needed):**
   - If your backend is running on a different port, edit `frontend/js/auth.js`
   - Change the `API_BASE_URL` constant

### Database Setup

The application is configured to use **MySQL** by default with the following settings:
- **Host:** localhost
- **Port:** 3306
- **User:** root
- **Password:** Nithin@123
- **Database:** secure_notes

**MySQL Setup Steps:**

1. **Make sure MySQL server is installed and running**

2. **Install MySQL Python driver:**
   ```bash
   pip install -r requirements.txt
   ```
   This installs `pymysql` which is required for MySQL connection.

3. **Create the database:**
   ```bash
   python setup_mysql.py
   ```
   This script will create the database automatically.

   Or manually create it:
   ```sql
   CREATE DATABASE secure_notes CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

4. **The tables will be created automatically** when you start the backend server.

**To change MySQL settings:**
- Create a `.env` file in the `backend` folder (see `backend/.env.example`)
- Or set environment variables: `MYSQL_HOST`, `MYSQL_USER`, `MYSQL_PASSWORD`, etc.

**For detailed MySQL setup instructions, see [MYSQL_SETUP.md](MYSQL_SETUP.md)**

## Usage

1. **Start the backend server** (see Backend Setup above)

2. **Open the frontend** in your browser (see Frontend Setup above)

3. **Sign Up:**
   - Click "Sign Up" on the login page
   - Fill in your name, email, and password
   - You'll be automatically logged in after signup

4. **Login:**
   - Enter your email and password
   - Click "Login"

5. **Create Notes:**
   - After logging in, you'll see the dashboard
   - Enter a title and content
   - Click "Create Note"

6. **Edit Notes:**
   - Click "Edit" on any note
   - Modify the title or content
   - Click "Save Changes"

7. **Delete Notes:**
   - Click "Delete" on any note
   - Confirm the deletion

8. **Reset Password:**
   - Click "Forgot Password" on the login page
   - Enter your email to receive a reset token
   - Enter the token and new password

## API Endpoints

### Authentication
- `POST /api/signup` - User registration
- `POST /api/login` - User login
- `POST /api/forgot-password` - Request password reset token
- `POST /api/reset-password` - Reset password with token

### Notes (Protected - Requires JWT)
- `GET /api/notes` - Get all user's notes
- `GET /api/notes/{id}` - Get a specific note
- `POST /api/notes` - Create a new note
- `PUT /api/notes/{id}` - Update a note
- `DELETE /api/notes/{id}` - Delete a note

## Security Features

- **Password Hashing:** All passwords are hashed using bcrypt
- **JWT Tokens:** Secure token-based authentication
- **User Isolation:** Users can only access their own notes
- **Input Validation:** Server-side validation for all inputs
- **CORS Protection:** Configured for secure cross-origin requests

## Environment Variables

Create a `.env` file in the `backend` directory (optional):

```env
DATABASE_URL=sqlite:///./secure_notes.db
SECRET_KEY=your-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**Note:** In production, always use a strong `SECRET_KEY` and store it securely.

## Troubleshooting

### Backend Issues

1. **ModuleNotFoundError or ImportError:**
   - Make sure you're running from the correct directory
   - If running `python main.py`, you must be in the `backend` directory
   - Or use `python start_server.py` from the project root
   - Make sure all `__init__.py` files exist in `backend/`, `backend/api/`, and `backend/database/`

2. **Port already in use:**
   - Change the port in `backend/main.py` or use: `uvicorn main:app --port 8001`
   - Or kill the process using port 8000

3. **Database errors:**
   - Delete `secure_notes.db` (in backend directory) and restart the server to recreate tables

4. **Import errors:**
   - Make sure you're in the virtual environment
   - Reinstall dependencies: `pip install -r requirements.txt`
   - Check that all packages are installed: `pip list`

5. **"No module named 'jwt'" or similar:**
   - Install missing packages: `pip install PyJWT bcrypt`
   - Or reinstall all: `pip install -r requirements.txt`

### Frontend Issues

1. **CORS errors:**
   - Make sure the backend is running
   - Check that `API_BASE_URL` in `frontend/js/auth.js` matches your backend URL

2. **Token not working:**
   - Clear browser localStorage and login again
   - Check browser console for errors

## Production Deployment

### Important Security Notes:

1. **Change SECRET_KEY:** Update the secret key in `backend/api/auth.py`
2. **Use Environment Variables:** Store sensitive data in environment variables
3. **Enable HTTPS:** Always use HTTPS in production
4. **Configure CORS:** Update CORS settings in `backend/main.py` to allow only your domain
5. **Email Service:** Implement proper email service for password reset tokens
6. **Database:** Use PostgreSQL or another production database
7. **Error Handling:** Implement proper logging and error handling

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please check the code comments or refer to the FastAPI documentation at https://fastapi.tiangolo.com/
