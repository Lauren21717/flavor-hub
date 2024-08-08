// Initialize the side navigation bar
$(document).ready(function () {
    $('.sidenav').sidenav({
        edge: "right"
    });
    // This is the function to display the flash message
    $('#flash-messages .flash-message').each(function () {
        alert($(this).text());
    });
});


