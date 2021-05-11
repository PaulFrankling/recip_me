## Testing

### Validation:

#### HTML

[W3C Markup Validation](https://validator.w3.org/#validate_by_uri) was used to validate the projects HTML code through its URI.
Validating through the URI produced no errors as shown below:

![HTML validation](static/docs/testing/validation/html-validation.png)

Each HTML page was also validated through the use of the [direct input](https://validator.w3.org/#validate_by_input) option. 
Warnings and Errors were only produced for each of the 12 HTML pages due to the use of Jinja.

#### CSS

[W3C CSS Validation](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to validate the `style.css` file through direct input.
By inputting my own CSS, the validator found no errors as shown below:

![CSS Validation](static/docs/testing/validation/css-validation.png)

The CSS of the project was also validated through its URI. By doing so, it did produce one error. This error though is due to Materialize and not an error from my own CSS.

![Materialize-CSS Error](static/docs/testing/validation/materialize-css-error.png)

#### JavaScript

[JShint](https://jshint.com/) was used to validate both my JavaScript files; `scripts.js` and `topButton.js`. Both JavaScript files came back with no errors.
The only thing brought to my attention was that the `scripts.js` file needed two semi colons added and they have been implemented.

#### Python

[PEP8 online](http://pep8online.com/) was used to make sure my `app.py` file was PEP8 compliant and the website received the following result:

![PEP8 Validation](static/docs/testing/validation/pep8-results.png)

### Testing of User Stories in UX section of [README.md](https://github.com/PaulFrankling/recip_me#readme):

  * #### First Time Visitor Goals

    * *As a First Time Visitor, I want to understand the purpose of the website and view some of the recipes.*

      * **On first view of the website, the user is taken to the Home page and can easily view recipes from the selection of recipe categories as well as visiting the Recipes page to view all the recipes.**

      ![Homepage UX Test Image](static/docs/testing/ux-testing/homepage-ux-test.png)

    * *As a First Time Visitor, I want to easily navigate around the website.*

      * **The user can easily find each page through the navigation bar. The logo at the top left of the website always directs the user to the Home page.**

      ![Navigation Bar UX Test Image](static/docs/testing/ux-testing/navbar-ux-test.png)

    * *As a First Time Visitor, I want to be able to easily create an account and sign in to it.*

      * **The user can easily create an account by visiting the Register page by either using the navigation bar or using the CTA button on the Home page.**

      ![Homepage CTA Button Test Image](static/docs/testing/ux-testing/homepage-cta.png)

      * **The user has clear instructions on the requirements needed to create an account successfully below the Username and Password input fields.**

      ![Register Page Test Image](static/docs/testing/ux-testing/register-ux-test.png)

    * *As a First Time Visitor, I want to be able to log out of my account once finished on the website.*

      * **The user can log out from their account at anytime by clicking 'Log Out' on the navigation bar.**

      ![Logout Test Image](static/docs/testing/ux-testing/logout-ux-test.png)

  * #### Returning Visitor Goals

    * *As a Returning Visitor, I want to be able to easily log in to my account.*

      * **The user can easily log in to their account by visiting the Login page and inputting their accounts Username and Password.**

      ![Login Page Test Image](static/docs/testing/ux-testing/login-ux-test.png)

    * *As a Returning Visitor, I want to see if any new recipes have been added.*

      * **The user can see if any new recipes are added by visiting the Recipes page.**
      * **The user can also see new recipes by looking at the categories on the Home page.**

    * *As a Returning Visitor, I would like to be able to find a particular recipe through the use of a search engine.*

      * **The user can view recipes through the use of the search bar on the Recipes page.**

      ![Search Bar Test Image](static/docs/testing/ux-testing/search-bar-ux-test.png)

      * **The user can view recipes by category name, recipe name or recipe ingredients, giving the user a better chance to find something specific to their taste.**

  * #### Frequent Visitor Goals

    * *As a Frequent User, I want to be able to add and share a recipe of my own.*

      * **The user, when registered and logged in, can add a recipe by visiting the Add Recipe page from the navigation bar.**

      ![Add Recipe Page Test Image](static/docs/testing/ux-testing/add-recipe-ux-test.png)

    * *As a Frequent User, I want easily find my added recipes via the Profile page.*

      * **Every time the user adds a recipe, it is added to their Profile page to view any time.**

      ![Profile Page Test Image](static/docs/testing/ux-testing/profile-ux-test.png)

    * *As a Frequent User, I would like to be able to edit my own recipes.*

       * **When viewing their own recipe, the user has the option to edit their recipe by clicking on the 'Edit Recipe' button and they're then redirected to the Edit Recipe page to be able to edit it.**

       ![Edit Recipe Button Test Image](static/docs/testing/ux-testing/edit-recipe-ux-test.png)

    * *As a Frequent User, I want to be able to delete any of my recipes.*

       * **When viewing their own recipe, the user has the option to delete their recipe by clicking on the 'Delete Recipe' button. 
       The user is then met with a Modal offering them a chance to change their mind and select 'No', or choose to go ahead with the deletion by selecting 'Yes'.**

       ![Delete Button Test Image](static/docs/testing/ux-testing/delete-button-ux-test.png) 
       
       ![Delete Modal Test Image](static/docs/testing/ux-testing/modal-ux-test.png)

    * *As a Frequent User, I'd like to visit the social media accounts through the links in the 
    footer to look for updates and interact with others on a public forum.*

       * **The user has the option to visit social media accounts through the icons on the footer of the website.**

       ![Footer Test Image](static/docs/testing/ux-testing/footer-ux-test.png)

### Testing Process:

Family members and Friends were asked to test the website and were able to lend me their devices to let me test the website too.

The website was tested on the following devices:

* ASUS ZENBOOK UX434
* iPhone 7
* iPhone X
* iPad
* Huawei P Smart
* Acer Laptop

The website was tested on the following web browsers:

* Safari
* Google Chrome
* Firefox
* Microsoft Edge

The projects responsiveness was established through the framework [Materialize](https://materializecss.com/).
The project was tested on numerous devices and presented no responsiveness issues.

The website was thoroughly tested and a detailed account of each tested feature is documented below:

#### Navigation Bar

* All navigation bar links were tested one by one and worked properly. &check;
* The website logo correctly redirects the user to the Home page. &check;
* The log out function works correctly and redirects the user to the Login page as expected. &check;
* The navigation bar shows the 'Log In' page and 'Register' page links when the user is logged out. &check;
* The navigation bar shows the 'Add Recipe' page, 'Profile' page links and 'Log Out' function when the user is logged in. &check;
* The mobile side navigation bar redirects the user to each page correctly. &check;

#### Flash Messages

* All Flash messages appear after the appropriate action is taken:

  * User registers an account: "You have successfully registered with RecipMe!". &check;
  * User logs into their account: "Hello { username }!". &check;
  * User logs out of their account: "You have successfully logged out!". &check;
  * User inputs a username that already exists: "This username already exists!". &check;
  * User inputs the wrong username or password when logging in: "Incorrect Username and/or Password!". &check;
  * User successfully adds a recipe: "Recipe successfully added!". &check;
  * User successfully edits a recipe: "Recipe successfully updated!". &check;
  * User successfully deletes a recipe: "Recipe successfully deleted!". &check;

#### Footer

* If the user clicks on any of the social media links in the footer, they are taken to that respective social media site on a new tab whilst retaining RecipMe on the previous tab. &check;
* The circular background of the social media icons turn `#033F63` when they are hovered over. &check;

#### Back to Top Button

* The button takes the user to the top of the page and fades in and out when scrolling up and down the screen. &check;

#### Home Page

* When the user is logged out, the 'Log In' and 'Register' CTA buttons both redirect the user to their respective pages. &check;
* When the user is logged in, the 'Profile' and 'Recipes' CTA buttons both redirect the user to their respective pages. &check;
* Each category card on the Home page takes the user to the correct respective category. &check;

#### Category Page

* When the user selects any of the recipe categories on the Home page, the correct recipes belonging to that category show on its particular category page. &check;
* Any added recipes appear on its particular category page. &check;

#### Recipes Page

The Recipes page has a search engine and as mentioned in the [README.md](https://github.com/PaulFrankling/recip_me#readme), the indexes created with [MongoDB](https://cloud.mongodb.com/) were category_name, recipe_name and recipe_ingredients.

* All categories were searched and all came back with the correct results. &check;
* Numerous recipes were searched and the appropriate results came back. &check;
* Searched 10 different ingredients and the search engine returned the correct recipes with those ingredients. &check;
* If the search engine can't find the requested search query, it correctly returns a "No Results Found" message. &check;
* Reset button works correctly by resetting the search query. &check;

#### Register Page

* Input fields correctly notify the user if the Username or Password is too short or contains a symbol. &check;
* Login page link works correctly. &check;
* When the user registers their account, it adds their credentials to [MongoDB](https://cloud.mongodb.com/). 
It shows the Username of each user but hashes the Password with the use of Werkzeug. &check;
* Once registered, it correctly takes the user to their Profile page. &check;

#### Login Page

* Input fields work correctly by resetting the page when the user inputs the wrong login details. &check;
* When the user logs in, it correctly takes the user to their Profile page. &check;
* Register page link works correctly. &check;

#### Profile Page

* The Profile page correctly shows the logged in accounts Username in the page title. &check;
* If the user has just registered or hasn't added any recipes, the page correctly shows an 'Add Recipe' CTA button. &check;
* When the user adds a recipe, it removes the 'Add Recipe' CTA button as expected. &check;
* The Profile page only displays the recipes the user has added and no other users. &check;

#### Add Recipe Page

* All input fields work correctly, ensuring each one is filled in with correct amount of characters. &check;
* The Food Image input field correctly doesn't require input. &check;
* The select options work correctly. &check;
* Both ingredients and method fields can be added and removed appropriately. &check;
* 'Add Recipe' submit button works correctly. &check;
* When the user adds a recipe it adds all the information in the correct format. i.e. The ingredients are presented in bullet points and the method steps are ordered. &check;
* The recipe is successfully added to [MongoDB](https://cloud.mongodb.com/). &check;

#### Edit Recipe Page

* All input fields are prepopulated with the chosen recipes existing information. &check;
* All input fields and select options can be edited. &check;
* All validation and requirements work as expected. &check;
* 'Edit Recipe' submit button works correctly. &check;
* Cancel button works as expected. &check;
* Recipe is edited correctly on submission in [MongoDB](https://cloud.mongodb.com/). &check;

#### Show Recipe Page

* All recipe cards correctly link to their respective `show_recipe.html` page. &check;
* If the user isn't logged in or the recipe doesn't belong to them, it does not allow them to edit or delete it. &check;
* All recipes are layed out correctly. &check;
* If the user who added the recipe doesn't input an Image URL, the recipe correctly shows the [default image](https://github.com/PaulFrankling/recip_me/blob/master/static/images/recipe-alt.png) set. &check;
* The particular recipe selected shows the correct user who added it towards the bottom of the screen. &check;
* If the user is logged in and the recipe belongs to them, it shows the 'Edit Recipe' and 'Delete Recipe' buttons. &check;
* The 'Edit Recipe' button takes the user to the Edit Recipe page. &check;
* The 'Delete Recipe' button opens up a modal to either confirm deletion or cancel action. &check;
* The modal can be closed by clicking outside of it or selecting 'No'. &check;
* When selecting 'Yes' on the modal, it successfully deletes the recipe and takes the user back to the Recipes page. &check;
* The recipe is also deleted in [MongoDB](https://cloud.mongodb.com/). &check;

#### Error Pages

* Both links back to the Home page work. &check;

### Defensive Programming

* When the user tries to log into their account and inputs the wrong information, it tells them: "Incorrect Username and/or Password!" 
which helps in preventing someone from brute forcing the account.
* If the user tries to access the Add Recipe page, Edit Recipe page, or another users Profile, they are redirected to a 404 Error page. (`404.html`).
* If the user presses back when they have logged in, they are redirected to their Profile page. This stops the user from logging in twice.

### Existing Bugs:

* If the user inputs the wrong URL in the Food Image input field, then this happens to the image card on the far right of the picture below:

  ![Image Card Bug](static/docs/testing/bugs/image-bug.png)

  The `alt` tag fortunately gives a brief description of what the image is. However the image card title doesn't cover the full length of the card. 
This is why I didn't give the Food Image input field the `required` attribute. Instead the user can use the [default image](https://github.com/PaulFrankling/recip_me/blob/master/static/images/recipe-alt.png)
which will display when nothing is inputted.

  > If the user has difficulty with inputting the image URL they want to use, they just need to right click on the image on the internet. They then need to select 'Copy image address' and paste it into the Food Image input field on the Add Recipe page or Edit Recipe page.

* The next bug is on the Add Recipe page:

  ![Add Recipe Page Bug](static/docs/testing/bugs/add-recipe-bug.png)

  When the user needs to add more input fields for more ingredients or method steps, they have to go back up the screen to select the 'Add Item' button and then back down the screen to add an item to it.
  This isn't a good UX feature and appears an inconvenience to the user.

* The Edit Recipe page also has a bug in which the user can't remove an item from the ingredients or method steps prepopulated input fields.

  ![Edit Recipe Page Bug](static/docs/testing/bugs/edit-recipe-bug.png)

  As shown in the image above, the red line appears showing the user must input something in an existing input field.
  The user can edit the prepopulated input fields but just can't remove them.

#### Gitpod Bugs/Errors

* Every HTML page produces the same warning except for the `base.html` page.

  ![Doctype Warning](static/docs/testing/bugs/doctype-warning.png)

  This is due to the use of Jinja and can't be altered.

* The `env.py` file produces this error:

  ![env.py Error](static/docs/testing/bugs/env-py-error.png)

  This error is due to there being a very long required string that can't be split effectively as there is no space to split it.

* The `app.py` file produces this error:

  ![app.py Error](static/docs/testing/bugs/app-py-error.png)

  This is just because the `env.py` file sets environment variables and isn't used beyond that. 
