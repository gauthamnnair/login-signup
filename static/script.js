// Function to toggle the visibility of the password
function togglePassword() {
    var passwordField = document.getElementById("password");
    var button = document.getElementById("toggle-password-btn");

    // Toggle the password field type between 'password' and 'text'
    if (passwordField.type === "password") {
        passwordField.type = "text";
        button.textContent = "Hide"; // Change the button text to "Hide"
    } else {
        passwordField.type = "password";
        button.textContent = "Show"; // Change the button text back to "Show"
    }
}

// Function to toggle the visibility of the confirm password
function toggleConfirmPassword() {
    var confirmPasswordField = document.getElementById("confirm_password");
    var button = document.getElementById("toggle-confirm-password-btn");

    // Toggle the confirm password field type between 'password' and 'text'
    if (confirmPasswordField.type === "password") {
        confirmPasswordField.type = "text";
        button.textContent = "Hide"; // Change the button text to "Hide"
    } else {
        confirmPasswordField.type = "password";
        button.textContent = "Show"; // Change the button text back to "Show"
    }
}

// Function to check if password and confirm password match before submitting
function validatePasswords() {
    var passwordField = document.getElementById("password");
    var confirmPasswordField = document.getElementById("confirm_password");
    var errorContainer = document.getElementById("error-container");

    // Check if passwords match
    if (passwordField.value !== confirmPasswordField.value) {
        // Display the error message container
        errorContainer.style.display = "block";
        return false; // Prevent form submission
    } else {
        // Hide the error message container if passwords match
        errorContainer.style.display = "none";
        return true; // Allow form submission
    }
}

// Attach event listener to form submit event
document.querySelector("form").addEventListener("submit", function (event) {
    if (!validatePasswords()) {
        event.preventDefault(); // Prevent form submission if validation fails
    }
});
