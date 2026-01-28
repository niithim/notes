/**
 * Forgot password page functionality
 */

let resetToken = null;

document.addEventListener('DOMContentLoaded', () => {
    const forgotPasswordForm = document.getElementById('forgotPasswordForm');
    const resetPasswordForm = document.getElementById('resetPasswordForm');

    forgotPasswordForm.addEventListener('submit', handleForgotPassword);
    resetPasswordForm.addEventListener('submit', handleResetPassword);
});

async function handleForgotPassword(e) {
    e.preventDefault();

    const email = document.getElementById('email').value;

    try {
        const response = await apiRequest('/forgot-password', {
            method: 'POST',
            body: JSON.stringify({
                email: email
            })
        });

        // Store the token (in production, this would come via email)
        resetToken = response.token;

        // Show token in alert (for development only)
        showAlert(
            `Reset token generated: ${resetToken}<br><small>In production, this would be sent via email.</small>`,
            'success'
        );

        // Show reset password form
        document.getElementById('requestTokenStep').style.display = 'none';
        document.getElementById('resetPasswordStep').style.display = 'block';

        // Pre-fill token if available
        if (resetToken) {
            document.getElementById('token').value = resetToken;
        }
    } catch (error) {
        showAlert(error.message || 'Failed to generate reset token.', 'danger');
    }
}

async function handleResetPassword(e) {
    e.preventDefault();

    const token = document.getElementById('token').value;
    const newPassword = document.getElementById('newPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    // Client-side validation
    if (newPassword !== confirmPassword) {
        showAlert('Passwords do not match!', 'danger');
        return;
    }

    if (newPassword.length < 6) {
        showAlert('Password must be at least 6 characters long!', 'danger');
        return;
    }

    try {
        await apiRequest('/reset-password', {
            method: 'POST',
            body: JSON.stringify({
                token: token,
                new_password: newPassword,
                confirm_password: confirmPassword
            })
        });

        showAlert('Password reset successfully! Redirecting to login...', 'success');

        // Redirect to login
        setTimeout(() => {
            window.location.href = 'index.html';
        }, 2000);
    } catch (error) {
        showAlert(error.message || 'Failed to reset password.', 'danger');
    }
}
