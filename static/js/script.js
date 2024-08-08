$(document).ready(function () {
    // Initialize the side navigation bar
    $('.sidenav').sidenav({
        edge: "right"
    });
    $('select').formSelect();

    // This is the function to display the flash message
    $('#flash-messages .flash-message').each(function () {
        alert($(this).text());
    });

    let ingredientCount = 1;
    let stepCount = 1;
    /**
     * Event handler for the "Add Ingredient button"
     * When the button click 
     * it create a new input element for ingredients
     */
    $('#add-ingredient').on('click', function() {
        ingredientCount++;
        let ingredientInput = $('<input>', {
            type: 'text',
            name: 'ingredients',
            class: 'validate',
            minlength: '5',
            maxlength: '50',
            required: true
        });
        $('#ingredients-section').append(ingredientInput)
    });
    
    /**
     * Event handler for the "Add Step" button
     * it create a new textarea element for preparation steps
     */
    $('#add-step').on('click', function() {
        stepCount++;
        let stepTextarea = $('<textarea>', {
            name: 'preparation_steps',
            class: 'validate materialize-textarea',
            minlength: '5',
            maxlength: '200',
            required: true
        });
        $('#preparation-section').append(stepTextarea);
    });

});


