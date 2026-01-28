# MySQL Database Setup Guide

## Prerequisites

1. **MySQL Server installed and running**
   - Download from: https://dev.mysql.com/downloads/mysql/
   - Or use XAMPP/WAMP which includes MySQL

2. **Create the database**
   - Open MySQL command line or MySQL Workbench
   - Run this command:
   ```sql
   CREATE DATABASE secure_notes CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

## Configuration

The application is now configured to use MySQL with:
- **Host:** localhost (default)
- **Port:** 3306 (default)
- **User:** root (default)
- **Password:** Nithin@123
- **Database:** secure_notes (default)

## Installation Steps

### Step 1: Install MySQL Driver
```bash
pip install -r requirements.txt
```

This will install `pymysql` which is the MySQL driver for Python.

### Step 2: Create MySQL Database

**Option A: Using MySQL Command Line**
```bash
mysql -u root -p
```
Then enter your MySQL root password and run:
```sql
CREATE DATABASE secure_notes CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

**Option B: Using MySQL Workbench**
1. Open MySQL Workbench
2. Connect to your MySQL server
3. Create a new schema named `secure_notes`
4. Set character set to `utf8mb4` and collation to `utf8mb4_unicode_ci`

### Step 3: Configure Database Connection (Optional)

If you need to change the default settings, create a `.env` file in the `backend` folder:

```env
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=Nithin@123
MYSQL_DATABASE=secure_notes
```

Or use the full DATABASE_URL:
```env
DATABASE_URL=mysql+pymysql://root:Nithin@123@localhost:3306/secure_notes
```

### Step 4: Start the Backend Server

```bash
python start_server.py
```

The tables will be created automatically when the server starts.

## Verify Connection

### Check if tables are created:
1. Connect to MySQL:
   ```bash
   mysql -u root -p
   ```
2. Use the database:
   ```sql
   USE secure_notes;
   ```
3. Show tables:
   ```sql
   SHOW TABLES;
   ```
   You should see `users` and `notes` tables.

4. Check table structure:
   ```sql
   DESCRIBE users;
   DESCRIBE notes;
   ```

## Troubleshooting

### Error: "Access denied for user"
**Solution:**
- Check MySQL username and password
- Make sure MySQL user has privileges to create databases/tables
- Try: `GRANT ALL PRIVILEGES ON secure_notes.* TO 'root'@'localhost';`

### Error: "Can't connect to MySQL server"
**Solution:**
- Make sure MySQL server is running
- Check if MySQL is running on port 3306
- Verify host and port settings

### Error: "Unknown database 'secure_notes'"
**Solution:**
- Create the database first (see Step 2)
- Or change MYSQL_DATABASE in .env file

### Error: "No module named 'pymysql'"
**Solution:**
```bash
pip install pymysql cryptography
```

### Error: "Table doesn't exist"
**Solution:**
- The tables are created automatically on first run
- Make sure the database user has CREATE TABLE privileges
- Check server logs for error messages

## Testing the Connection

Run this script to test your MySQL connection:
```bash
python check_database.py
```

## Current Configuration

- **Database Type:** MySQL
- **Driver:** PyMySQL
- **Host:** localhost
- **Port:** 3306
- **User:** root
- **Password:** Nithin@123
- **Database Name:** secure_notes

## Security Note

⚠️ **Important:** In production:
1. Don't use root user - create a dedicated database user
2. Use strong passwords
3. Store credentials in environment variables, not in code
4. Use SSL connections for remote MySQL servers

## Changing Back to SQLite (if needed)

If you want to switch back to SQLite, set the DATABASE_URL:
```env
DATABASE_URL=sqlite:///./secure_notes.db
```

Or comment out the MySQL configuration in `database.py`.
