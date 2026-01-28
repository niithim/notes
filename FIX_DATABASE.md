# Fix: Data Not Storing Issue

## Problem
Data (users, notes) are not being saved to the database.

## Solution Applied

I've fixed the database path issue. The database file will now always be created in the `backend` directory, regardless of where you run the server from.

## Steps to Fix

### 1. Stop the Backend Server
If it's running, press `Ctrl+C` to stop it.

### 2. Check Current Database Status
Run this to see what's in your database:
```bash
python check_database.py
```

This will show:
- Where the database file is located
- If tables exist
- How many users and notes are stored

### 3. Delete Old Database (if needed)
If the database file is in the wrong location, you can delete it:
- Look for `secure_notes.db` file
- Delete it (it will be recreated automatically)

### 4. Restart the Server
```bash
python start_server.py
```

You should now see:
```
Initializing database at: sqlite:///C:/Users/.../notes/backend/secure_notes.db
✅ Database tables created/verified
```

### 5. Test Data Storage
1. Sign up a new user
2. Create a note
3. Run `python check_database.py` again
4. You should see the data stored

## Verify It's Working

### Method 1: Use the Check Script
```bash
python check_database.py
```

### Method 2: Check Database File
- Go to `backend` folder
- Look for `secure_notes.db` file
- If it exists and has a size > 0, data is being stored

### Method 3: Test in Browser
1. Sign up a new account
2. Create a note
3. Logout and login again
4. Your note should still be there

## Common Issues

### Issue: Database file not found
**Solution:** The database will be created automatically on first use. Make sure the backend server is running.

### Issue: Data disappears after restart
**Solution:** This shouldn't happen. If it does:
1. Check that `secure_notes.db` file exists in `backend` folder
2. Make sure you're not running multiple instances of the server
3. Check file permissions

### Issue: "Database is locked" error
**Solution:** 
- Make sure only one instance of the server is running
- Close any database browser tools
- Restart the server

## Database File Location

The database file is now stored at:
```
backend/secure_notes.db
```

This is an absolute path, so it will always be in the same location regardless of where you run the server from.

## Still Not Working?

1. Run `python check_database.py` and share the output
2. Check the backend terminal for any error messages
3. Make sure you see "✅ Database tables created/verified" when starting the server
4. Check browser console (F12) for any API errors
