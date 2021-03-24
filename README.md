# RecipMe

## Code Institute - Milestone Project 3

### User Experience (UX):

### Design:

### Wireframes:

### Technology used:

### Testing:

### Deployment:

This project was deployed by [Heroku](https://www.heroku.com/) through [GitHub](https://www.github.com/).

To begin with, the following files were added:

![Deployment-files](static/docs/deployment-files.png)

The **env.py** file is created to retain the environmental variables, and the **env.py** file needs to be added to the **.gitignore** file so these variables can't be pushed to GitHub.

#### Deployment Process:

1. After organising the **env.py**, **app.py** and **.gitignore** files, you need to add the **requirements.txt** file. This file tells Heroku the dependencies required in running the project.

    To add this file and its dependencies, you need to input into the Command Line Interface(CLI):

    `pip3 freeze --local > requirements.txt`

2. Next the **Procfile** needs creating. This is what Heroku looks for to run the app and how to run it.

    To add this file, you need to input into the CLI:

    `echo web: python app.py`

    It is important the **Procfile** has an uppercase 'P' and any blank line added needs to be deleted as it can cause problems running the app on Heroku. It should look like this:

    ![Procfile-example](static/docs/procfile-example.png)







### Credits: