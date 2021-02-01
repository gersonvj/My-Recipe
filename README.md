![multi platform](https://#")

## **Project Goal**

This is a web application that implements the principles of the C.R.U.D. cycle are defined as CREATE, READ/RETRIEVE, UPDATE, and DELETE, the application allows users to add recipes to the panel, update it and eventually delete them. A user needs to registrate to be able to add recipes.


  ## Table of contents 
* [UX](#ux)🎯
    * [User Goals](#user-goals)
    * [User Stories](#user-stories)
    * [Site Owners Goals](#site-owners-goals)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
        * [Requirements](#requirements)
        * [Expectations](#expectations)    
* [Wireframes and Flowcharts](#wireframes-and-flowcharts)👨‍🔧
    * [Wireframes](#wireframes)
    * [Flowcharts](#flowcharts)
    * [Database Structure](#database-structure)
* [Features](#features)🤖
    * [Existing Features](#existing-features)
    * [Features to be implemented](#features-to-be-implemented)
* [Technologies used](#technologies-used)👀
    * [Languages](#languages)
    * [Libraries and Frameworks](#libraries-and-frameworks)
    * [Tools](#tools)
* [Testing](#testing)
* [Deployment](#deployment)
    * [Local Deployment](#local-deployment)
    * [Heroku Deployment](#heroku-deployment)
* [Credits](#credits)
    
### **User Goals**

* This web application has to work well on all kind of devices like mobile phones, tables and desktops.
* I want to have a profile for me where I can see all the different recipes I have created and create, update and delete recipes.
* I want to see the recipes even if I don't have registered. 
* The web application has to be user friendly.


### **User Stories**

* As a user, I would like to be able to register for the web application so I can have my personal environment.
* As a user, I want a profile dashboard page that shows the latest recipes added.
* As a user, I want to see the recipes without log in.
* As a user, I want to be able to search recipes.
* As a user, I want the web application to be easy to use. 
* As a user, I want the process to add / edit / delete info to be easy.

### **Site owners Goals**
* To have an appealing web application where recipes can be shared between users.
* To have a great functionality so the user feels like this web application helps them in their day-to-day life. 
* To make the web application where people can share experience about their recipes.

### **User Requirements and Expectations**

#### Requirements

* Easy to navigate by using the few buttons.
* Easy way to add a recipe
* Ability to edit and delete existing recipes.


#### Expectations

* When you have multiple recipes, it should be easy to navigate between them.
* To have a dashboard where all the necessary information is visible.
* It should be easy to add another recipe.


#### Structure

I have chosen to use [Materialize](https://materializecss.com/) to create an overall structure for my website. 
Materialize provides various elements of CSS and Javascript which is very helpful to keep a good structure on your page. 


## **Wireframes and Flowcharts**👨‍🔧

### **Wireframes**
I used [Balsamic](https://balsamiq.com/wireframes/) to create wireframes for my website. 

You can find my wireframes below:

#### Desktop Wireframes
* [Wireframes](wireframes/desktop.pdf)

#### Mobile Wireframes
* [Wireframes](wireframes/mobile.pdf)

### **Database Structure**

I have used MongoDB to set up the database for this project with the following collections: 

#### **Users:**

Key      | Value
---------|-----------
_id      | ObjectId
name     | String
password | String

#### **ingredients:**

Key             | Value
----------------|-----------
_id             | ObjectId
category_name   | String
recipe          | String
ingredients     | String
cooking         | String
description     | String
username        | String

#### **Category:**

Key             | Value
----------------|-----------
_id             | ObjectId
name            | String

## **Features**🤖

### **Existing Features**

* Registration functionality
* Sign-In and Out functionality
* Add multiple recipes per user 
* CRUD Functions:
    * Create: possibility to add various recipes and reviews.
    * Read: dashboard where you can view the recipes and its reviews.
    * Update: possibility to update the recipes.
    * Delete: possibility to delete the recipes.
* Search recipes.

### **Features to be implemented**

* Have a fucionality to insert images within the recipes.
* Have a more extensive user profile with, profile image, preferences and email to which you can send updates, newsletters etc.
* Have a 'forget password' functionality.
* Have a functionality to rate the recipes.

## **Technologies used**👀

### **Languages**

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://www.python.org/)

### **Libraries and Frameworks**

* [MongoDB Atlas](https://www.mongodb.com/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [PyMongo](https://api.mongodb.com/python/current/tutorial.html)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
* [Font Awesome](https://fontawesome.com/)
* [Materialize](https://materializecss.com/)
* [jQuery](https://jquery.com/)

### **Tools**
* [Git](https://git-scm.com/)
* [Heroku](https://www.heroku.com/)
* [W3C HTML Validation Service](https://validator.w3.org/)
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)


## **Testing**

### **Registration**

#### User story: As a user, I would like to be able to register for the website so I can add my recipes

* **Plan**  
I want to create a account to be able to add, read, update and delete recipes.

* **Implementation**  
I created a form where the user can add their name and choose a password. 
I have used the pattern attribute to only allow certain characters for the name, email, and password. 
Before creating the new account, I will check in the database if the email already exists. 
If so, correct feedback will be displayed to the user so he can choose another username. 
Password will be stored with the help of the password generate hash so it is stored safely.
After the registration was succesfull, the user will be redirected to the Profile page to add their first recipe.
In case the user wrongfully clicked on register instead of sign-in, a link to the sign-in page is provided so the user doesn't have to go back. 


* **Test**  
I have tried to create an account with an already existing email. Correct feedback is displayed.
User acccount is created whenever all criteria was met and user is being redirect to Profile page.


* **Result**  
Registration form is working as planned and user information is stored safely in the mongodb Users collection.
Feedback provided stands out nicely to inform the user. 
Redirection to blank My Recipe works as well as planned so the user can choose to add its recipe right away. 
Tested the registration on various browers and devices and the form is responsive and userfriendly. 

* **Verdict**
The test has passed all the criteria and works like planned.


### **Sign In**

#### User story: As a user, I want to login after I created an account and see my previous inserted information.

* **Plan**  
My plan is to create a login form where the user can fill in its name and password.
After signing in, the user will be redirected to the Profile page where the user can see the previously inserted recipes.

* **Implementation**  
I created a form where the user can fill in its name and password which will be verified with the information stored in the database. 
When the wrong information is being filled in, the correct feedback will be provided to the user. 
In case the user wrongfully clicked on sign-in instead of register, a link to the register page is provided so the user doesn't have to go back. 

* **Test**  
Signing in with the correct email and password works as planned and the correct page will be displayed. 
When the user fills in the wrong email and/or password, the same message is being displayed on the screen. 


* **Result**  
Sign-in form is working as planned and the input is being verified correctly with the stored information of the database.
Redirection to the correct page works as well as planned so the user can either add a recipe on Profile page or view its previously inserted recipes.
Tested the sign-in form on various browers and devices and the form is responsive and userfriendly. 
Feedback provided to the user stands out nicely. 

* **Verdict**    
The test has passed all the criteria and works like planned.


#### User story: As a user, I want to be able to search recipes.

* **Plan**
The plan is create a search bar where users can search recipes by name of the recipe.

* **Implementation** 
First I added a search bar to home and recipes pages, then I created indexes to search in mongo db so that user can search by name of the recipe.

* **Test** 
I have testing the search functionality with empty field, with a wrong word, and with a word in the database and all response was correct.
 
 * **Result** 
 The result was satisfactory it shows the correct output depends on the input.
 
 * **Verdict**
 The test has passed all the criteria and works like planned.


https://www.shutterstock.com/image-photo/table-food-top-view-467823860

Heroku APP - 

Heroku needs to setup some files before you to run the app.

First, we need to tell Heroku which applications and dependencies are required to run our app:
"pip3 freeze --local > requirements.txt".
Next, the Procfile is what Heroku looks for to know which file runs the app, and how to
run it, so we'll use the echo command: "echo web: python app.py > Procfile".
Remember that the Procfile has a capital 'P', and no file extension.
We can check that the files were created successfully, and as you can see, the requirements.txt file
lists the dependencies that are needed for Flask.
One of these is called Werkzeug, which we'll learn more about later when setting up User
Authentication on our project.
The Procfile might add a blank line at the bottom, and sometimes this can cause problems
when running our app on Heroku, so just delete that line and save the file.
Let's head over to Heroku.com, and once you're logged in on your dashboard, we can click
to 'Create a New App'.
If you recall from our previous lessons, the Heroku app must be unique, and generally use
a 'dash' or 'minus' instead of spaces, and all lowercase letters.
I'm going to call my app "flask-task-manager-project", which means that's no longer available for
you to use, so try something similar, perhaps try including your name.
Next, select the region closest to you, and since I'm in Ireland, I'll select Europe,
then click 'Create App'.
In order to connect our app, we can do one of a few different options.
As you've learned from the previous project using Heroku, we could use the Heroku CLI
to connect our app using the steps outlined below.
However, to simplify the process, we'll setup Automatic Deployment from our GitHub repository.
Make sure your GitHub profile is displayed, then add your repository name, which I've
named exactly the same as my Heroku app, then click 'Search'.
Once it finds your repo, click to connect to this app.
Before we click to Enable Automatic Deployment, we still have a few more steps to do, otherwise
we'll get unwanted application errors.
Since we've contained our environment variables within a hidden env.py file, Heroku won't
be able to read those variables.
Click on the 'Settings' tab for your app, and then click on 'Reveal Config Vars', where
we can securely tell Heroku which variables are required.
Our env.py file contains a few different variables.
Make sure not to include any "quotes" for the key, or the value.
The first variable is IP, with the value of 0.0.0.0.
Next, the PORT, which is 5000.
For the SECRET_KEY, let's copy that from the env.py file, then paste it into Heroku.
We don't have the MONGO_URI string yet, so we'll leave that blank for now.
Finally, the MONGO_DBNAME is the name of our database, so task_manager.
Let's go back to the 'Deploy' tab, but before we connect it, we need to push our two new
files to the repository.
Back within the terminal, I've typed 'git status' just to confirm that those are the
only pending changes.
Add the requirements file to the staging area: "git add requirements.txt".
Then commit the file: "git commit -m "Add requirements.txt".
Next, add the Procfile: "git add Procfile".
Then commit that file as well: "git commit -m "Add Procfile".
Finally, "git push" in order to send those files to GitHub.
When we head back over to Heroku, we can now safely 'Enable Automatic Deployment', as everything
should be available on our repository.
I've only got the main branch for the project, so click 'Deploy Branch'.
Heroku will now receive the code from GitHub, and start building the app using our required
packages.
That should take a minute to build, and hopefully once it's done, you'll also see "Your app
was successfully deployed."
Click "View" to launch your new app.
Wonderful, the deployed site is now available, and should automatically update whenever we
push changes to the GitHub repository.