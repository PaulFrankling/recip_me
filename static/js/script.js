$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.modal').modal();

    let maxIngredients = 18;
	let ingredientsWrapper = $(".ingredient-wrapper");
	let addIngredient = $(".add-ingredient-button");
	
	let i = 1;
	$(addIngredient).click(function(e){
		e.preventDefault();
		if(i < maxIngredients){
            i++;
            $(ingredientsWrapper).append('<div><input type="text" name="recipe_ingredients"/><a class="waves-effect waves-light btn" id="remove-ingredient" <span>Remove Item</span><i class="fas fa-trash"></i></a>');
        }
    });
        
	$(ingredientsWrapper).on("click","#remove-ingredient", function(e){
		e.preventDefault(); $(this).parent('div').remove(); i--;
    })

    
    let maxMethod = 10;
	let methodsWrapper = $(".method-wrapper");
	let addMethod = $(".add-method-button");
	
	let m = 1;
	$(addMethod).click(function(e){
		e.preventDefault();
		if(m < maxMethod){
            m++;
            $(methodsWrapper).append('<div><input type="text" name="recipe_ingredients"/><a class="waves-effect waves-light btn" id="remove-method" <span>Remove Item</span><i class="fas fa-trash"></i></a>');
        }
	});
	
	$(methodsWrapper).on("click","#remove-method", function(e){
		e.preventDefault(); $(this).parent('div').remove(); m--;
    })
    
});