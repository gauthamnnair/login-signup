// Function to toggle the visibility of the password
function togglePassword() {
    // Get the password field and the "See" button
    var passwordField = document.querySelector('.password-field');
    var button = document.querySelector('.see-btn');

    // Toggle the password field type between 'password' and 'text'
    if (passwordField.type === 'password') {
        passwordField.type = 'text'; // Make password visible
        button.textContent = 'Hide'; // Change button text to "Hide"
    } else {
        passwordField.type = 'password'; // Hide password
        button.textContent = 'See'; // Change button text back to "See"
    }
}
