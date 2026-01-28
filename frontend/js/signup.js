/**
 * Signup page functionality
 */

// Redirect if already logged in
document.addEventListener('DOMContentLoaded', () => {
    redirectIfAuthenticated();

    const signupForm = document.getElementById('signupForm');
    signupForm.addEventListener('submit', handleSignup);
});

async function handleSignup(e) {
    e.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    // Client-side validation
    if (password !== confirmPassword) {
        showAlert('Passwords do not match!', 'danger');
        return;
    }

    if (password.length < 6) {
        showAlert('Password must be at least 6 characters long!', 'danger');
        return;
    }

    try {
        const response = await apiRequest('/signup', {
            method: 'POST',
            body: JSON.stringify({
                name: name,
                email: email,
                password: password,
                confirm_password: confirmPassword
            })
        });

        // Store token and user info
        TokenManager.setToken(response.access_token);
        TokenManager.setUserInfo(response.user_id, response.user_name);

        // Show success message
        showAlert('Account created successfully! Redirecting...', 'success');

        // Redirect to dashboard
        setTimeout(() => {
            window.location.href = 'dashboard.html';
        }, 1000);
    } catch (error) {
        showAlert(error.message || 'Signup failed. Please try again.', 'danger');
    }
}
