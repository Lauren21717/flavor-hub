$(document).ready(function () {
    // Initialize the side navigation bar
    $('.sidenav').sidenav();
    $('select').formSelect();

    //https://sweetalert.js.org/guides/
    // This is the function to display the flash message
    $('#flash-messages .flash-message').each(function () {
        swal({
            text: $(this).text(),
            button: {
                text: 'OK',
                className: 'blue-button'
            }
        });
    });

    //https://sweetalert.js.org/guides/
    // Delete Recipe
    $('.delete-recipe').on('click', function (e) {
        e.preventDefault();
        var recipeId = $(this).data('id');

        swal({
            title: "Are you sure?",
            text: "Once deleted, you will not be able to recover this recipe!",
            icon: "warning",
            buttons: {
                cancel: {
                    text: "Cancel",
                    value: null,
                    visible: true,
                    className: "orange-light-button",
                },
                confirm: {
                    text: "Yes, delete it!",
                    value: true,
                    visible: true,
                    className: "blue-button",
                }
            },
            dangerMode: true,
        })
            .then((willDelete) => {
                if (willDelete) {
                    $.ajax({
                        url: '/delete_recipe/' + recipeId,
                        type: 'GET',
                        success: function (response) {
                            if (response.success) {
                                swal("Poof! Your recipe has been deleted!", {
                                    icon: "success",
                                }).then(() => {
                                    window.location.href = "/"; 
                                });
                            } else {
                                swal("Oops!", "Something went wrong. Please try again.", "error");
                            }
                        },
                        error: function () {
                            swal("Oops!", "Something went wrong. Please try again.", "error");
                        }
                    });
                } else {
                    swal({
                        text: "Your recipe is safe!",
                        button: {
                            text: 'OK',
                            className: 'blue-button'
                        }
                    });
                }
            });
    });

    /**
    * Adds a new input field for an ingredient.
    * 
    * This function dynamically creates a new input field for the user to enter an ingredient.
    * It generates a new input element, a corresponding label, and a delete icon.
    * The new input field is appended to the ingredients section of the form.
    * After adding the new ingredient field, it updates all ingredient labels to ensure proper numbering.
    */
    function addIngredientField() {
        let ingredientDiv = $('<div>', {
            class: 'input-field'
        });
        let ingredientTextarea = $('<textarea>', {
            name: 'ingredients',
            class: 'materialize-textarea validate',
            minlength: '5',
            required: true
        });
        let ingredientLabel = $('<label>', {
            text: 'Ingredient ' + ($('#ingredients-section .input-field').length + 1)
        });
        let deleteIcon = $('<i>', {
            class: 'fa-solid fa-times delete-ingredient'
        });
        ingredientDiv.append(ingredientTextarea, ingredientLabel, deleteIcon);
        $('#ingredients-section').append(ingredientDiv);

        ingredientLabel.addClass('active');
        ingredientTextarea.trigger('autoresize');
        M.textareaAutoResize(ingredientTextarea[0]);
        M.updateTextFields();

        setTimeout(function () {
            ingredientTextarea.focus();
        }, 0);
        updateIngredientLabels();
    }

    // Event handler for the "Add Ingredient" button
    $('#add-ingredient').on('click', function () {
        addIngredientField();
    });

    /**
     * Adds a new textarea field for a preparation step.
     * 
     * This function dynamically creates a new textarea field for the user to enter a preparation step.
     * It generates a new textarea element, a corresponding label, and a delete icon.
     * The new textarea field is appended to the preparation steps section of the form.
     * After adding the new step field, it updates all step labels to ensure proper numbering.
     */
    function addStepField() {
        let stepDiv = $('<div>', {
            class: 'input-field'
        });
        let stepTextarea = $('<textarea>', {
            name: 'preparation_step',
            class: 'materialize-textarea validate',
            minlength: '5',
            required: true
        });
        let stepLabel = $('<label>', {
            text: 'Step ' + ($('#preparation-section .input-field').length + 1)
        });
        let deleteIcon = $('<i>', {
            class: 'fa-solid fa-times delete-step'
        });
        stepDiv.append(stepTextarea, stepLabel, deleteIcon);
        $('#preparation-section').append(stepDiv);

        stepTextarea.trigger('autoresize');
        stepLabel.addClass('active');
        M.textareaAutoResize(stepTextarea[0]);

        setTimeout(function () {
            stepTextarea.focus();
        }, 0);
        updateStepLabels();
    };
    // Event handler for the "Add Step" button
    $('#add-step').on('click', function () {
        addStepField();
    });

    //Delete Ingredient
    $(document).on('click', '.delete-ingredient', function () {
        $(this).closest('.input-field').remove();
        updateIngredientLabels();
    });

    // Delete Step
    $(document).on('click', '.delete-step', function () {
        $(this).closest('.input-field').remove();
        updateStepLabels();
    });

    //Update Ingredient Lables 
    function updateIngredientLabels() {
        $('#ingredients-section .input-field').each(function (index) {
            $(this).find('label').text('Ingredient ' + (index + 2));
        });
    }

    //Update Step Labels
    function updateStepLabels() {
        $('#preparation-section .input-field').each(function (index) {
            $(this).find('label').text('Step ' + (index + 2));
        });
    }


    // This code was copied from Code Institude on 08-08-2024.
    // Original Author: Tim Nelson
    // Source: https://github.com/Code-Institute-Solutions/TaskManagerAuth/blob/main/04-AddingATask-WritingToTheDatabase/02-materialize-select-validation/static/js/script.js
    validateMaterializeSelect();

    function validateMaterializeSelect() {
        let classValid = {
            "border-bottom": "1px solid #4caf50",
            "box-shadow": "0 1px 0 0 #4caf50"
        };
        let classInvalid = {
            "border-bottom": "1px solid #f44336",
            "box-shadow": "0 1px 0 0 #f44336"
        };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({
                "display": "block",
                "height": "0",
                "padding": "0",
                "width": "0",
                "position": "absolute"
            });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    };
    M.AutoInit();
    M.updateTextFields();
});