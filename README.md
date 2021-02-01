### [View My Recipe APP in Heroku.com](https://myrecipeproject.herokuapp.com/)


## **Project Goal**

This is a web application that implements the principles of the C.R.U.D. cycle are defined as CREATE, READ/RETRIEVE, UPDATE, and DELETE, the application allows users to add recipes to the panel, update it and eventually delete them. A user needs to registrate to be able to add recipes.


  ## Table of contents 
* [UX](#ux)
    * [User Goals](#user-goals)
    * [User Stories](#user-stories)
    * [Site Owners Goals](#site-owners-goals)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
        * [Requirements](#requirements)
        * [Expectations](#expectations)    
* [Wireframes](#wireframes)
    * [Wireframes](#wireframes)
    * [Database Structure](#database-structure)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Features to be implemented](#features-to-be-implemented)
* [Technologies used](#technologies-used)
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


## **Wireframes

### **Wireframes**

* [Wireframes](wireframe/recipe1.jpg) - First concept of the APP
* [Wireframes](wireframe/screencapture-materializecss-parallax-demo-html-2021-01-28-23_52_41.pdf) - Home page concept
* [Wireframes](wireframe/wireframe_app.jpg) - APP concept

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

## **Features**

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

## **Technologies used**

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
 
 ### Deployment

Following the documentation in the course for deploying to Heroku, and also the following guide [Getting Started With Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python#define-a-procfile) allowed me to relatively easily deploy the application to Heroku:

- I was required to set up an alternative git remote using `git remote -a heroku louis-g-ms3` so that I was able to push changes to Heroku
- I was required to set up some config (environment) variables that could be used to get the port used by the application/connection strings etc
- I was required to create a Procfile in the root of my project with the following `web: python runserver.py 0.0.0.0:5000`
- Once I had the Heroku CLI installed, I had to create a master branch in GIT and use `git push heroko master` to try deploying the application
- This flagged up a number of errors that required fixing, including missing dependencies from the requirements.txt file, specifically dnspython and flask-mongoengine, as well as the missing config variables above (it couldn't connect to the port after 30 seconds)

- To connect to the application locally, ensure you have all of the requirements installed (you can use `pip install -r requirements.txt`)


Deployed using GitHub Pages accessed via the link below
 - https://gersonvj.github.io/TWC---THE-WEATHER-CHANNEL/index.html is main content page - all other navigatable via this webpage

  **Process**
   1. Created a Github account at https://github.com My account: https://github.com/gersonvj

   2. Synced folder on local machine to Github Repo via VsCode: https://gersonvj.github.io/My-Recipe/

   3. To publish the project to see it on the web go to Settings on Repo , scroll down to the heading, GitHub Pages. Under the Source setting, Use drop-down menu to select master branch as a publishing source and save. Refreshed the github page, and you are then given a url where your page is published; The site is now published on gitHub pages at https://gersonvj.github.io/My-Recipe/

   4. To run this code on your local machine, you would go to my respository at https://gersonvj.github.io/My-Recipe/ and on the home page on the right hand side just above all the files, you will see a green button that says, "Clone or download", this button will give you options to clone with HTTPS, open in desktop or download as a zip file. Then --> click the clipboard item to copy the Https address of the repo.
   
   5. Open Git Bash/Terminal: 
   CD the working directory to the location where you want the cloned directory to be made.you can use mkdir command to make a new directory, then cd into it.Type git clone, and then paste the URL: https://github.com/gersonvj/My-Recipe.git Press Enter. The clone is created.
   For more information about the above process; https://help.github.com/en/github/using-git/which-remote-url-should-i-use



# Credits

* To complete this project I used Code Institute student template: [gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template)


<h5>Media</h5>
<ul>
  <li>The artwork used in this site were obtained from: www.shutterstock.com</li>
</ul>

<h5>Acknowledgements</h5>
<ul>
  <li>I would like to thank Tim Nelson from Code Institute for the brilliant flask/mongoDB lessons.</li>
</ul>



