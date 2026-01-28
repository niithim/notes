# Secure Notes App - Architecture & API Flow

## Architecture Overview

The Secure Notes App follows a **client-server architecture** with a clear separation between frontend and backend:

```
┌─────────────┐         HTTP/REST API         ┌─────────────┐
│   Browser   │ ◄──────────────────────────► │   FastAPI   │
│  (Frontend) │         (JSON + JWT)         │  (Backend)  │
└─────────────┘                               └──────┬──────┘
                                                     │
                                                     ▼
                                              ┌─────────────┐
                                              │  Database   │
                                              │ (SQLite/    │
                                              │ PostgreSQL)  │
                                              └─────────────┘
```

### Components

1. **Frontend (Client-Side)**
   - Static HTML/CSS/JavaScript files
   - Bootstrap 5 for responsive UI
   - Communicates with backend via REST API
   - Stores JWT tokens in localStorage

2. **Backend (Server-Side)**
   - FastAPI framework (Python)
   - RESTful API endpoints
   - JWT authentication middleware
   - SQLAlchemy ORM for database operations

3. **Database**
   - SQLite (default) or PostgreSQL
   - Two main tables: Users and Notes
   - Foreign key relationship between tables

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Notes Table
```sql
CREATE TABLE notes (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

## API Flow Explanation

### 1. User Registration Flow

```
User → Frontend (signup.html)
  ↓
Fill form (name, email, password, confirm_password)
  ↓
POST /api/signup
  ↓
Backend validates:
  - Email uniqueness
  - Password match
  - Password length
  ↓
Hash password with bcrypt
  ↓
Create user in database
  ↓
Generate JWT token
  ↓
Return token + user info
  ↓
Frontend stores token in localStorage
  ↓
Redirect to dashboard
```

### 2. User Login Flow

```
User → Frontend (index.html)
  ↓
Fill form (email, password)
  ↓
POST /api/login
  ↓
Backend:
  - Find user by email
  - Verify password with bcrypt
  ↓
Generate JWT token
  ↓
Return token + user info
  ↓
Frontend stores token
  ↓
Redirect to dashboard
```

### 3. Password Reset Flow

```
User → Frontend (forgot-password.html)
  ↓
Step 1: Enter email
  ↓
POST /api/forgot-password
  ↓
Backend generates reset token
  ↓
Store token (in-memory, expires in 1 hour)
  ↓
Return token (in production: send via email)
  ↓
Step 2: Enter token + new password
  ↓
POST /api/reset-password
  ↓
Backend:
  - Validate token
  - Check expiration
  - Hash new password
  ↓
Update user password
  ↓
Delete token
  ↓
Redirect to login
```

### 4. Create Note Flow

```
User → Dashboard
  ↓
Fill note form (title, content)
  ↓
POST /api/notes
  Headers: Authorization: Bearer <JWT_TOKEN>
  ↓
Backend:
  - Verify JWT token
  - Extract user_id from token
  - Create note with user_id
  ↓
Save to database
  ↓
Return created note
  ↓
Frontend refreshes notes list
```

### 5. Get Notes Flow

```
User → Dashboard (on page load)
  ↓
GET /api/notes
  Headers: Authorization: Bearer <JWT_TOKEN>
  ↓
Backend:
  - Verify JWT token
  - Extract user_id from token
  - Query notes WHERE user_id = token.user_id
  ↓
Return user's notes only
  ↓
Frontend renders notes list
```

### 6. Update Note Flow

```
User → Dashboard
  ↓
Click "Edit" on a note
  ↓
Open modal with note data
  ↓
Modify title/content
  ↓
PUT /api/notes/{id}
  Headers: Authorization: Bearer <JWT_TOKEN>
  Body: {title, content}
  ↓
Backend:
  - Verify JWT token
  - Find note by ID
  - Verify note belongs to user (user_id check)
  - Update note
  ↓
Save to database
  ↓
Return updated note
  ↓
Frontend refreshes notes list
```

### 7. Delete Note Flow

```
User → Dashboard
  ↓
Click "Delete" on a note
  ↓
Confirm deletion
  ↓
DELETE /api/notes/{id}
  Headers: Authorization: Bearer <JWT_TOKEN>
  ↓
Backend:
  - Verify JWT token
  - Find note by ID
  - Verify note belongs to user
  - Delete note
  ↓
Return 204 No Content
  ↓
Frontend refreshes notes list
```

## Security Features

### 1. Password Security
- **Hashing**: Passwords are hashed using bcrypt with salt
- **Never stored in plain text**: Only hashed passwords in database
- **Minimum length**: 6 characters enforced

### 2. JWT Authentication
- **Token-based**: No session storage on server
- **Expiration**: Tokens expire after 30 minutes
- **Stateless**: Server doesn't store token state
- **Signed**: Tokens are cryptographically signed

### 3. User Isolation
- **Foreign key constraint**: Notes linked to users
- **Query filtering**: All note queries filter by user_id
- **Authorization check**: Every note operation verifies ownership

### 4. Input Validation
- **Server-side validation**: All inputs validated on backend
- **Email format**: Validated using EmailStr
- **Required fields**: Enforced at API level
- **SQL injection protection**: SQLAlchemy ORM prevents SQL injection

## Request/Response Examples

### Signup Request
```http
POST /api/signup
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepass123",
  "confirm_password": "securepass123"
}
```

### Signup Response
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user_id": 1,
  "user_name": "John Doe"
}
```

### Create Note Request
```http
POST /api/notes
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
  "title": "My First Note",
  "content": "This is the content of my note."
}
```

### Create Note Response
```json
{
  "id": 1,
  "title": "My First Note",
  "content": "This is the content of my note.",
  "created_at": "2024-01-15T10:30:00",
  "updated_at": "2024-01-15T10:30:00"
}
```

## Error Handling

### Authentication Errors
- **401 Unauthorized**: Invalid or expired token
- **401 Unauthorized**: Invalid email/password

### Validation Errors
- **400 Bad Request**: Invalid input data
- **400 Bad Request**: Passwords don't match
- **400 Bad Request**: Email already exists

### Resource Errors
- **404 Not Found**: Note not found
- **404 Not Found**: Note doesn't belong to user

## Frontend-Backend Communication

### Token Storage
- JWT tokens stored in `localStorage`
- Sent in `Authorization` header: `Bearer <token>`
- Automatically included in all authenticated requests

### API Helper Function
```javascript
async function apiRequest(endpoint, options = {}) {
    const token = TokenManager.getToken();
    const headers = {
        'Content-Type': 'application/json',
        ...options.headers
    };
    
    if (token) {
        headers['Authorization'] = `Bearer ${token}`;
    }
    
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
        ...options,
        headers
    });
    
    return await response.json();
}
```

## Deployment Considerations

1. **Environment Variables**: Use `.env` for sensitive data
2. **CORS Configuration**: Restrict origins in production
3. **HTTPS**: Always use HTTPS in production
4. **Secret Key**: Use strong, random secret key
5. **Database**: Use PostgreSQL for production
6. **Email Service**: Implement proper email for password reset
7. **Token Storage**: Consider httpOnly cookies for better security
8. **Rate Limiting**: Add rate limiting to prevent abuse
