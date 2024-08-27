const contactForm = document.getElementById("contact-form");

/**
 * Function to handle form submission and send an email using EmailJS.
 * @param {HTMLFormElement} contactForm - The form element containing user input.
 * @returns {boolean} - Returns false to prevent default form submission if validation fails.
 */
function sendMail(contactForm) {
    if (ValidateContact(this)) {
        emailjs.send("service_f5s5ulu", "flavor_hub", {
            from_name: contactForm.name.value,
            from_email: contactForm.email.value,
            message: contactForm.message.value,
        })
            .then(
                (response) => {
                    console.log("SUCCESS", response);
                    swal({
                        title: "Success!",
                        text: "Your message has been sent successfully!",
                        icon: "success",
                        button: {
                            text: 'OK',
                            className: 'blue-button'
                        },
                    });
                },
                (error) => {
                    console.log("FAILED", error);
                    swal({
                        title: "Error!",
                        text: "There was an error sending your message. Please try again later.",
                        icon: "error",
                        button: {
                            text: 'OK',
                            className: 'blue-button'
                        },
                    });
                }
            );
        return false;
    }
    else 
    {
        this.addEventListener('submit', function (event) {
            event.preventDefault();
        });
        console.log("ERROR: Unable to send form as the required fields have not been completed");
    }
}

/**
 * Function to validate the contact form fields.
 * @param {HTMLFormElement} contactForm - The form element containing user input.
 * @returns {boolean} - Returns true if all fields are filled, otherwise false.
 */
function ValidateContact(contactForm) {
    if (contactForm.name.value === "" || contactForm.email.value === "" || contactForm.message.value === "") {
        console.log("Validation failed: All fields are required");
        return false;
    }
    console.log("Validation passed");
    return true;
}