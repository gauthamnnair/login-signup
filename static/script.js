// General function to toggle visibility of the password field
function togglePassword(passwordId, buttonId) {
    var passwordField = document.getElementById(passwordId);  // Get the password field by its ID
    var button = document.getElementById(buttonId);  // Get the button by its ID

    // Check if the password is hidden
    if (passwordField.type === "password") {
        passwordField.type = "text";  // Show password
        button.textContent = "Hide";  // Change button text to "Hide"
    } else {
        passwordField.type = "password";  // Hide password
        button.textContent = "Show";  // Change button text back to "Show"
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
