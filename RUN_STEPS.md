# Step-by-Step Guide to Run Secure Notes App

## 📋 Prerequisites Check

First, make sure you have Python installed:
```bash
python --version
```
You should see Python 3.8 or higher. If not, install Python from [python.org](https://www.python.org/downloads/)

---

## 🚀 Quick Start (3 Steps)

### Step 1: Install Dependencies

Open terminal/command prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

**What this does:** Installs all required Python packages (FastAPI, SQLAlchemy, etc.)

**Expected output:** You'll see packages being installed. Wait until it finishes.

---

### Step 2: Start the Backend Server

**Option A: Using the batch file (Windows - Easiest)**
- Double-click `run_backend_safe.bat`
- OR run in terminal: `run_backend_safe.bat`

**Option B: Using Python script**
```bash
python start_server.py
```

**Option C: Manual start**
```bash
cd backend
python main.py
```

**What this does:** Starts the FastAPI server on port 8000

**Expected output:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**✅ Success indicator:** You should see "Uvicorn running on http://0.0.0.0:8000"

**Keep this terminal window open!** The server must keep running.

---

### Step 3: Open the Frontend

**Option A: Direct file opening (Simplest)**
1. Navigate to the `frontend` folder
2. Double-click `index.html`
3. It will open in your default browser

**Option B: Using a local server (Recommended)**
1. Open a **NEW** terminal/command prompt
2. Navigate to the frontend folder:
   ```bash
   cd frontend
   ```
3. Start a simple HTTP server:
   ```bash
   python -m http.server 8080
   ```
4. Open your browser and go to: `http://localhost:8080`

**What this does:** Serves the frontend files so they can communicate with the backend

---

## 🎯 Testing the Application

### 1. Create an Account
- Click "Sign Up" on the login page
- Fill in:
  - Name: Your name
  - Email: your.email@example.com
  - Password: (at least 6 characters)
  - Confirm Password: (same as password)
- Click "Sign Up"
- You'll be automatically logged in and redirected to the dashboard

### 2. Create a Note
- On the dashboard, you'll see "Create New Note" section
- Enter a title and content
- Click "Create Note"
- Your note will appear in the list below

### 3. Edit a Note
- Click "Edit" button on any note
- Modify the title or content
- Click "Save Changes"

### 4. Delete a Note
- Click "Delete" button on any note
- Confirm the deletion

### 5. Logout
- Click "Logout" button in the top right
- You'll be redirected to the login page

---

## 🔍 Verify Everything is Working

### Check Backend is Running:
- Open browser and go to: `http://localhost:8000`
- You should see: `{"message":"Secure Notes API is running"}`

### Check API Documentation:
- Go to: `http://localhost:8000/docs`
- You should see the Swagger UI with all API endpoints

### Check Frontend:
- Login page should load without errors
- You should be able to sign up and login

---

## ⚠️ Troubleshooting

### Problem: "ModuleNotFoundError" or "No module named..."
**Solution:**
```bash
pip install -r requirements.txt
```

### Problem: "Port 8000 already in use"
**Solution:**
- Close other applications using port 8000
- Or change port in `backend/main.py` (line 56) to 8001

### Problem: "Cannot connect to backend" or CORS errors
**Solution:**
- Make sure backend is running (Step 2)
- Check that backend shows "Uvicorn running on http://0.0.0.0:8000"
- Make sure you're using the correct API URL in frontend (default: http://localhost:8000)

### Problem: Backend starts but immediately closes
**Solution:**
- Run `python diagnose.py` to check for errors
- Check `error_log.txt` file for details
- Make sure all `__init__.py` files exist in:
  - `backend/__init__.py`
  - `backend/api/__init__.py`
  - `backend/database/__init__.py`

### Problem: Frontend shows errors in browser console
**Solution:**
- Make sure backend is running
- Check that API URL in `frontend/js/auth.js` is `http://localhost:8000/api`
- Open browser developer tools (F12) to see specific errors

---

## 📝 Summary

**To run the app, you need 2 terminal windows:**

**Terminal 1 (Backend):**
```bash
cd backend
python main.py
```
Keep this running!

**Terminal 2 (Frontend - Optional):**
```bash
cd frontend
python -m http.server 8080
```
Or just open `index.html` directly in browser.

---

## 🎉 You're All Set!

Once both are running:
- Backend: http://localhost:8000
- Frontend: http://localhost:8080 (or open index.html)

Start creating your secure notes! 📝
