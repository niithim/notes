/**
 * Authentication utility functions
 * Handles token storage and API base URL
 */

const API_BASE_URL = 'http://localhost:8000/api';

// Token management
const TokenManager = {
    setToken(token) {
        localStorage.setItem('access_token', token);
    },

    getToken() {
        return localStorage.getItem('access_token');
    },

    removeToken() {
        localStorage.removeItem('access_token');
        localStorage.removeItem('user_name');
        localStorage.removeItem('user_id');
    },

    setUserInfo(userId, userName) {
        localStorage.setItem('user_id', userId);
        localStorage.setItem('user_name', userName);
    },

    getUserInfo() {
        return {
            userId: localStorage.getItem('user_id'),
            userName: localStorage.getItem('user_name')
        };
    },

    isAuthenticated() {
        return !!this.getToken();
    }
};

// Check authentication and redirect
function checkAuth() {
    if (!TokenManager.isAuthenticated()) {
        window.location.href = 'index.html';
    }
}

// Redirect if already authenticated
function redirectIfAuthenticated() {
    if (TokenManager.isAuthenticated()) {
        window.location.href = 'dashboard.html';
    }
}

// Show alert message
function showAlert(message, type = 'info') {
    const alertContainer = document.getElementById('alertContainer');
    if (!alertContainer) return;

    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    alertContainer.innerHTML = '';
    alertContainer.appendChild(alertDiv);

    // Auto dismiss after 5 seconds
    setTimeout(() => {
        alertDiv.remove();
    }, 5000);
}

// API request helper
async function apiRequest(endpoint, options = {}) {
    const token = TokenManager.getToken();
    const headers = {
        'Content-Type': 'application/json',
        ...options.headers
    };

    if (token) {
        headers['Authorization'] = `Bearer ${token}`;
    }

    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
            ...options,
            headers
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || 'An error occurred');
        }

        return data;
    } catch (error) {
        throw error;
    }
}
