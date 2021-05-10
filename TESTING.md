## Testing

### Validation:

#### HTML

[W3C Markup Validation](https://validator.w3.org/#validate_by_uri) was used to validate the projects HTML code through its URI.
Validating through the URI produced no errors as shown below:

![HTML validation](static/docs/testing/html-validation.png)

Each HTML page was also validated through the use of the [direct input](https://validator.w3.org/#validate_by_input) option. 
Warnings and Errors were only produced for each of the 12 HTML pages due to the use of Jinja.

#### CSS

[W3C CSS Validation](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to validate the `style.css` file through direct input.
By inputting my own CSS, the validator found no errors as shown below:

![CSS Validation](static/docs/testing/css-validation.png)

The CSS of the project was also validated through its URI. By doing so, it did produce one error. This error though is due to Materialize and not an error from my own CSS.

![Materialize-CSS Error](static/docs/testing/materialize-css-error.png)

#### JavaScript

[JShint](https://jshint.com/) was used to validate both my `scripts.js` and `topButton.js` files and came back with no errors.
The `scripts.js` file needed two semi colons added and they were implemented.

#### Python

![Pep8 Validation](static/docs/testing/pep8-results.png)

### Testing of User Stories in UX section: