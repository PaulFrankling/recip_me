# RecipMe

## Code Institute - Milestone Project 3

[Click here to view my website](https://recipme-project.herokuapp.com/)

### User Experience (UX):

### Design:

#### Colour Scheme

![Colour-scheme](static/docs/colour-scheme.png)

The colour scheme used for this project was generated on [Coolor](https://coolors.co/ffffff-e71d36-033f63).

* White `#FFFFFF`
* Rose Madder `#E71D36`
* Indigo Dye `#033F63`

#### Typography

I have chosen the font **Dancing Script** for my project title; RecipMe. I have also used this font for the headings on each page.
The font **Lato** has been chosen for all the content of the project. **Lato** was used for the content as it is much clearer than 
**Dancing Script** for the user. The fonts were both taken from [Google Fonts](https://fonts.google.com/specimen/Dancing+Script?query=dancing#standard-styles).

### Wireframes:

### Technology used:

### Testing:

### Deployment:

This project was deployed by [Heroku](https://www.heroku.com/) through [GitHub](https://www.github.com/).

To begin with, the following files were added on the [Gitpod online IDE](https://www.gitpod.io/):

![Deployment-files](static/docs/deployment/deployment-files.png)

The **env.py** file is created to retain the environmental variables, and the **env.py** file needs to be added to the **.gitignore** file 
so these variables can't be pushed to GitHub.

#### Deployment Process:

1. After organising the **env.py**, **app.py** and **.gitignore** files, you need to add the **requirements.txt** file. 
   This file tells Heroku the dependencies required in running the project.

    To add this file and its dependencies, you need to input into the Command Line Interface(CLI):

    `pip3 freeze --local > requirements.txt`

1. Next the **Procfile** needs creating. This is what Heroku looks for to run the app and how to run it.

    To add this file, you need to input into the CLI:

    `echo web: python app.py`

    It is important the **Procfile** has an uppercase 'P' and any blank line added needs to be deleted as it 
    can cause problems running the app on Heroku. It should look like this:

    ![Procfile-example](static/docs/deployment/procfile-example.png)

1. After both the **Procfile** and **requirements.txt** file have been added and saved, sign in/sign up to [Heroku](https://www.heroku.com/) 
   and click on 'Create new app'.

1. Once you have created your new app, you need to go to the 'Deploy' section near the top of the page.

1. You now need to connect the Heroku app with your GitHub repository by firstly clicking on 'Connect to GitHub' as shown below:

    ![GitHub-connection](static/docs/deployment/github-connect.png)

1. Making sure your GitHub profile is displayed, add your repository into the box to the right of it and click 'Search'.

1. Once its found the repository, click 'Connect'.

1. Before clicking 'Enable Automatic Deploys', you need to go to the 'Settings' section on Heroku.

1. In the 'Settings' section you need to click 'Reveal Config Vars'. At this point, 
   you need to input all the environmental variables from the **env.py** file to tell Heroku which variables are required.

1. Once you have added the environmental variables and clicked 'Hide Config Vars', 
   you need to return to the [Gitpod online IDE](https://www.gitpod.io/) and push the **Procfile** and **requirements.txt** file to GitHub.

1. Once the files are pushed to GitHub, return to the 'Deploy' section on Heroku and click 'Enable Automatic Deploys' as shown below:

    ![Deployment-page](static/docs/deployment/deployment-page.png)

1. Then you need to click on 'Deploy Branch' and it will take a minute to build the app.

1. The app should now be deployed successfully and will update when code is pushed to GitHub. 
   You can open the app by selecting 'View' once its deployed. 

### Credits:

#### Media Used

* The background image of strawberries on **all pages** is by Nietjuh from [Pixabay](https://pixabay.com/photos/strawberries-red-fruit-fruit-red-4417296/).

##### Category images

* The Breakfast image is by Aline Ponce from [Pixabay](https://pixabay.com/photos/eggs-fried-sunny-side-up-sandwich-1467284/).
* The Starters image is by silviarita from [Pixabay](https://pixabay.com/photos/carrot-soup-bread-herbs-oil-soup-2192152/).
* The Mains image is by Free-Photo from [Pixabay](https://pixabay.com/photos/food-meal-soup-dish-peppers-spicy-1209007/).
* The Sides image is by  Jason Goh from [Pixabay](https://pixabay.com/photos/water-spinach-kangkong-sambal-chilli-1628620/).
* The Desserts image is by gefrorene_wand from [Pixabay](https://pixabay.com/photos/dessert-milk-product-delicious-1647468/).
* The Smoothies image is by NielsBB from [Pixabay](https://pixabay.com/photos/fruit-dessert-food-drink-snack-3222313/).