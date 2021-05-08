$(document).ready(function () {
    $('.sidenav').sidenav(); // Sidenav trigger initialisation
    $('select').formSelect(); // Form select fields initialisation
    $('.modal').modal(); // Modal initialisation

    let maxIngredients = 18; // Max number of ingredient input fields that can be added
    let ingredientsWrapper = $(".ingredient-wrapper"); // Ingredients input field wrapper
    let addIngredient = $(".add-ingredient-button"); // Add ingredients button

    let i = 1; // Initial input field count
    $(addIngredient).click(function (e) { // Adds input field
        e.preventDefault();
        if (i < maxIngredients) { // Max ingredients allowed
            i++; // Input field increment
            $(ingredientsWrapper).append('<div><input type="text" name="recipe_ingredients"/><a class="waves-effect waves-light btn" id="remove-ingredient" <span>Remove Item</span><i class="fas fa-trash"></i></a>');
        } // Adds input field
    });

    $(ingredientsWrapper).on("click", "#remove-ingredient", function (e) {
        e.preventDefault(); $(this).parent('div').remove(); i--; // Remove ingredient on click
    });


    let maxMethod = 10; // Max number of method input fields that can be added
    let methodsWrapper = $(".method-wrapper"); // Method input field wrapper
    let addMethod = $(".add-method-button"); // Add method step button

    let m = 1; // Initial input field count
    $(addMethod).click(function (e) { // Adds input field
        e.preventDefault();
        if (m < maxMethod) { // Max method steps allowed
            m++; // Input field increment
            $(methodsWrapper).append('<div><input type="text" name="recipe_method"/><a class="waves-effect waves-light btn" id="remove-method" <span>Remove Item</span><i class="fas fa-trash"></i></a>');
        } // Adds input field
    });

    $(methodsWrapper).on("click", "#remove-method", function (e) {
        e.preventDefault(); $(this).parent('div').remove(); m--; // Removes method on click
    });

});