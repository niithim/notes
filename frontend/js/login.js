/**
 * Login page functionality
 */

// Redirect if already logged in
document.addEventListener('DOMContentLoaded', () => {
    redirectIfAuthenticated();

    const loginForm = document.getElementById('loginForm');
    loginForm.addEventListener('submit', handleLogin);
});

async function handleLogin(e) {
    e.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        const response = await apiRequest('/login', {
            method: 'POST',
            body: JSON.stringify({
                email: email,
                password: password
            })
        });

        // Store token and user info
        TokenManager.setToken(response.access_token);
        TokenManager.setUserInfo(response.user_id, response.user_name);

        // Show success message
        showAlert('Login successful! Redirecting...', 'success');

        // Redirect to dashboard
        setTimeout(() => {
            window.location.href = 'dashboard.html';
        }, 1000);
    } catch (error) {
        showAlert(error.message || 'Login failed. Please check your credentials.', 'danger');
    }
}
