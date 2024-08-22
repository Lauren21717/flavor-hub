$(document).ready(function () {
    // Initialize the side navigation bar
    $('.sidenav').sidenav({
        edge: "right"
    });
    $('select').formSelect();

    // This is the function to display the flash message
    $('#flash-messages .flash-message').each(function () {
        swal($(this).text());
    });

    let ingredientCount = 1;
    let stepCount = 1;
    /**
     * Event handler for the "Add Ingredient button"
     * When the button click 
     * it create a new input element for ingredients
     */
    $('#add-ingredient').on('click', function () {
        ingredientCount++;
        let ingredientDiv = $('<div>', {
            class: 'input-field'
        });
        let ingredientInput = $('<input>', {
            type: 'text',
            id: 'ingredient_' + ingredientCount, 
            name: 'ingredients',
            class: 'validate',
            minlength: '5',
            maxlength: '50',
            required: true
        });
        let ingredientLabel = $('<label>', {
            for: 'ingredient_' + ingredientCount,
            text: 'ingredient ' + ingredientCount
        });
        ingredientDiv.append(ingredientInput, ingredientLabel);
        $('#ingredients-section').append(ingredientDiv);

        ingredientLabel.addClass('active');
        M.updateTextFields();
    });

    /**
     * Event handler for the "Add Step" button
     * it create a new textarea element for preparation steps
     */
    $('#add-step').on('click', function () {
        stepCount++;
        let stepDiv = $('<div>', {
            class: 'input-field'
        });
        let stepTextarea = $('<textarea>', {
            id: 'step_' + stepCount,
            name: 'preparation_step',
            class: 'materialize-textarea',
            minlength: '5',
            maxlength: '200',
            required: true
        });
        let stepLabel = $('<label>', {
            for: 'step_' + stepCount,
            text: 'Step ' + stepCount
        });
        stepDiv.append(stepTextarea, stepLabel);
        $('#preparation-section').append(stepDiv);

        stepTextarea.trigger('autoreasize');
        stepLabel.addClass('active');
        M.textareaAutoResize(stepTextarea[0]);

        setTimeout(function() {
            stepTextarea.focus();
        }, 0);
    });

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
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
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
    }
});