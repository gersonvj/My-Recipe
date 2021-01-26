
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