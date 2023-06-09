# Where Next?

## About

This website is a Travel Blog, a travel blog with a difference. There are lots of different blog articles to read to inspire the next adventure. 
Not only that! They can set up their own private Travel Bucket List, and also plan how to make each one a reality!!

The User has access to all the blogs on the site, once registered and logged in, they can interact with the each blog by liking and commenting. 

This site also allows them to store their very own Travel Bucket List, They can:
  - Create new items on their list.
  - Edit any of their ideas.
  - Delete any they longer want to achieve.
  - Mark off as done, when they have completed them.
  
Then they can take it a little further....
For each Item on their Bucket List, lets say "Want to travel to Rome". They can:
  - Add extra content. This is to make their wish into a reality and plan their trip. Any images they find, or links to hotels, flights etc. 
  Any information they come across can be stored here. Or a list of items they need to buy etc. Its like an online mood board 
  - They can view their plan, without going into edit mode, to see their plan come together.


You can find the live appliaction here: <a href ='https://pp4-where-next.herokuapp.com/'>Where Next?</a>

Repo link <a href ="https://github.com/AngMaher/PP4-Where-Next">Here</a>

![Am I responsive](/docs/readme/amiresponsive.png)



# Contents

  - [User Experience](#user-experience)

    - [Wireframes](#wireframes)

    - [Colour Scheme](#colour-scheme)

  - [Agile](#agile)

    - [The Ideal User Persona](#the-ideal-userpersona)

    - [User Goals](#user-goals)

    - [Developer Goals](#developer-goals)

    - [Goals not completed](#goals-not-completed)

  - [Logic and Features](#logic-and-features)

    - [Logic](#logic)
      
      - [Data Models](#data-model)

    - [Features](#features)

      - [About Page](#about-page)

      - [Home Page](#home-page)

      - [Blog Content Page](#blog-content-page)

      - [Register New User](#register-new-user)
      
      - [Sign In](#sign-in)

      - [Log Out](#log-out)

      - [Bucket List Page](#bucket-list-page)

      - [Add a Bucket List Item](#add-a-bucket-list-item)

      - [Edit a Bucket List Item](#edit-a-bucket-list-item)

      - [Add a plan to one bucket list item](#add-a-plan-to-one-bucket-list-item)

      - [View the plan to one bucket list item](#view-the-plan-to-one-bucket-list-item)

      - [Delete a Bucket List Item](#delete-a-bucket-list-item)

      - [Footer](#footer)
      
      - [Nav Bar When Logged Out](#nav-bar-when-logged-out)

      - [Nav Bar When Logged In](#nav-bar-when-logged-in)

  - [Tools and Technology](#tools-and-technology)

  - [Testing](#testing)

  - [Deployment](#deployment)

    - [ElephantSQL Database](#elephantsql-database)

    - [Cloudinary API](#cloudinary-api)

    - [Heroku Deployment](#heroku-deployment)

    - [Local Deployment](#local-deployment)

    - [Cloning](#cloning)

    - [Forking](#forking)

  - [Future Development](#future-development)

  - [Credits](#credits)

  - [Acknowledgements](#acknowledgements)


# User Experience

I wanted to keep the design clean, clear and simple to show a contempary and uncluttered design.  The site is mainly white for the background and blue a colour to premote travel.

## Wireframes

I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

### Home Page Wireframe

<details>
<summary>Click to View Home Page wireframes</summary>

![blog page](/docs/readme/wire-blogview.png)
</details>


### Blog Content Page

<details>
<summary>Click to View Blog Content wireframes</summary>

![blog content](/docs/readme/wire-blogcontent.png)
</details>

### Bucket List Wireframe

<details>
<summary>Click to View Bucket List wireframes</summary>

![bucketlist](/docs/readme/wire-bucketlist.png)
</details>

### Home Page Wireframe

<details>
<summary>Click to View Signin Page wireframes</summary>

![sign-in page](/docs/readme/wire-signin.png)
</details><br>

## Colour Scheme

I decided to keep the website bright with a main colour of blue throughout the site. 

  - #343434 - Jet, this colour is used a on the majority of the text throughout the site, and the footer.
  - #5799E1 - Blue, this is used on many features, buttons and highlighting links, popup messages.
  - #FFF - white, this is used as the main background colour of the site to keep things clean.



![colours used](/docs/readme/colours.png)

I used [coolors.co](https://coolors.co/343434-5799e1-fdf8f4-e64141) to pick my colours.

I've used CSS `:root` variables to easily update the global colour scheme by changing only one value, instead of everywhere in the CSS file.

```css
:root {
    --main-blue: #5799e1;
    --dark-gray: #343434;
    --background-colour: #fff;
    --messages: rgb(230, 65, 65, 0.6);
}
```
[Back to top &uarr;](#contents)

# Agile 

## The Ideal User/Persona

- This site is developed for people who have a thirst for travelling.
- They have a keen interest in learning about new places and are always on the lookout for new adventures.
- They like planning and want somewhere to keep their 'Travel Bucket List' and somewhere to plan, so that their
Bucket List dream becomes a reality.

## User Goals
  - As a Site User I can view a list of posts so that I can choose which post I want to view. `(MUST HAVE)`
  - As a Site User I can create and account so that Extend the features of the website to comment/like and create my own bucket list. `(MUST HAVE)`
  - As a Site User/ Admin I can view likes on posts so that I can see which posts are popular. `(MUST HAVE)`
  - As a Site User I can comment on a post so that I can feel part of the conversation. `(MUST HAVE)`
  - As a Site User I can create my own bucket list so that I can keep track of goals. `(MUST HAVE)`
  - As a Site User I can edit and delete items from my bucket list so that I can interact with the list. `(SHOULD HAVE)` `(MUST HAVE)`
  - As a Site User /Admin I can view comments on an individual post so that I can read the conversation. `(MUST HAVE)`
  - As a Site User I can like/unlike posts so that I can interact with the content. `(SHOULD HAVE)`
  - As a Site User I can mark of what I have achieved on my bucket list so that I can see my progress. `(COULD HAVE)`
  - As a Site User I can view an more detailed version of the post so that I can read the article in full. `(MUST HAVE)`
  - As a Site User I can create a mood-board/plan for each item on my bucket list so that I have a place 
      to store all the details I need to make my goal a reality. `(SHOULD HAVE)`
  - As a Site User I can View mood-board/plan so that I can view my plan so far without having to go into edit mode. `(SHOULD HAVE)`
  - As a Site User I can call up all blogs for a certain category so that I can filter the blogs to my needs `(SHOULD HAVE)`

## Developer Goals

 - As a Site Admin I can create, read and delete posts so that I can manage my blog content. `(MUST HAVE)`
 - As a Site Admin I can approve and disapprove comments so that I can filter out objectionable comments. `(SHOULD HAVE)`
 - As a Site Admin I can create draft posts so that I can finish writing the content later. `(SHOULD HAVE)`
 - As a Site Admin I can access the admin from a link on the web page so that I have easier access. `(SHOULD HAVE)`
 - As a Site Admin I can filter the comments by approved and not approve so that I can have a list of all unapproved comments together `(MUST HAVE)`
 - As a Site Admin I can search through posts, comments and Bucket List Items so that I can find what I am looking for with ease `(MUST HAVE)`

 ## Goals not completed

 - As a Site User I can save a post onto my account so that I can have a list of the most relevant posts to read later `(COULD HAVE)`


[Back to top &uarr;](#contents)


# Logic and Features

## Logic

### Data Model

- Allauth User Model

  - The User model was built using Django's Allauth library
    When a user is created, they're automatically assigned a profile through the Profile model.

Table: **Post**

| **PK** | **id** (unique) | Type | Notes |
| --- | --- | --- | --- |
| | title_tag | CharField | max_length=200, unique=True |
| | title_tag | CharField | max_length=200, default="Where Next? |
| | slug | SlugField | max_length=200, unique=True | 
| FK | author | Foreign Key | User, on_delete=models.CASCADE |
| | featured_image | CloudinaryField | 'image', default='placeholder' |
| | excerpt | TestField | Blank True |
| | updated_on |DateTimeField | auto_now_add true |
| | content | TextField | |
| FK | likes | Many to Many | User, related_name="blog_likes", blank=True |

***
Table: **Comment**

| **PK** | **id** (unique) | Type | Notes |
| --- | --- | --- | --- |
| FK | post | Foreign Key |  Post, on_delete=models.CASCADE |
| | name | CharField | max_lenght 80 |
| | email | EmailField | |
| | body | TestField | |
| | created_on | DateTimeField | auto_now_add=True |
| | approved | Boolean | Defaut False |

***

Table: **List**

| **PK** | **id** (unique) | Type | Notes |
| --- | --- | --- | --- |
| FK | user_name | Foreign Key | User, on_delete=models.CASCADE |
| | Title | CharField | max-lenght=300 |
| | planning | Text Field | blank=True, null=True |
| | updated_on | Date Time Field | Auto_now=True
| | created_om | Date Time Field | auto_now_add=True
| | done | Boolean Field |  null=False, blank=False, default=False |

***


[Back to top &uarr;](#contents)


## Features

- ### **About Page**
  - This is a page to tell the user about the site, about who created the site and show an example of a bucket list they could have if they sign up.

<details>
    <summary>Click to View About Page</summary>

  ![about page](/docs/readme/about-page.png)
  ![example of bucket list](/docs/readme/example-bucket-list.png)
</details>

***

- ### **Home Page**
  - This is the blog page, all users logged in or not see this page and get to scroll through the list of blogs.

<details>
    <summary>CLick to View Home Page</summary>

  ![Blog Page](/docs/readme/home-page.png)
</details>

***

 - ### **Blog Content Page**
  - This page shows the main content of any blog the user wishes to read.
<details>
    <summary>Click to View Blog Content Page</summary>

  ![Content Page](/docs/readme/blog-content.png)
</details>

***

- ### **Register New User**
  - This is where a new user can register to the site.
<details>
    <summary>Click here to View Registration Page</summary>

  ![register](/docs/readme/register.png)
</details>

***

- ### **Sign In** 
  - This is where the user signs in who already has an account.

<details>
    <summary>Click here to View Sign-in Page</summary>

  ![sign in](/docs/readme/sign-in.png)
</details>

***

- ### **Log Out** 
  - This is where the user signs out who.
<details>
    <summary>Click here to View Log Out Page</summary>

  ![log out](/docs/readme/log-out.png)
</details>

***

- ### **Bucket List Page**
  - This page show the logged in user all their own bucket list items.

<details>
    <summary>Click here to View the Bucket List</summary>

  ![bucket list](/docs/readme/bucket-list.png)
</details>

***

- ### **Add a Bucket List Item**
  - This page allows the logged in user to add a bucket list item.

<details>
    <summary>Click here to View Adding a Bucket List Item</summary>

  ![Add bucket list](/docs/readme/add-bucket-item.png)
</details>

***

- ### **Edit a Bucket List Item**
  - This page allows the logged in user to edit a bucket list item.
<details>
<summary>Click here to View Update Bucket List Item</summary>

  ![edit bucket list](/docs/readme/update-bucket-item.png)
</details>

***

- ### **Add a plan to one bucket list item**
  - This page allows the logged in user to add content to the bucket list item, allowing them to save information, links etc to help them plan how to make it reality.
<details>
<summary>Click here to View Add/Edit Plan</summary>

  ![plan bucket list](/docs/readme/edit-plan.png)
</details>

***

- ### **View the plan to one bucket list item**
  - This page allows the logged in user to view their plan on one bucket list item like a mood board to see how their plan is coming along.
<details>
<summary>Click here to View the Plan Page</summary>

  ![plan bucket list](/docs/readme/view-plan.png)
</details>

***

- ### **Delete a Bucket List Item**
  - This page allows the logged in user to delete a bucket list item.
<details>
<summary>Click here to View Delete Item Page</summary>

  ![delete bucket list](/docs/readme/delete-item.png)
</details>

***

- ### **Footer**
  - The footer of the site is kept simple with links to all socials.
<details>
<summary>Click here to View the Footer</summary>

  ![footer](/docs/readme/footer.png)
</details>

***

- ### **Nav Bar When Logged Out**
  - The navigation bar when user is not logged in.
<details>
<summary>Click here to View the Log Out NavBar</summary>

  ![logged out nav](/docs/readme/nav-logged-out.png)
</details>

***

- ### **Nav Bar When Logged In**
  - When a user logs in the nav bar changes to show the bucket list and also to welcome them by name.

<details>
  <summary>Click here to see the Log In NavBar</summary>

  ![logged in nav](/docs/readme/nav-logged-in.png)
</details>

***

[Back to top &uarr;](#table-of-contents)

##  Tools and Technology


- [HTML](https://www.w3schools.com/html/) - Used for the main site.
- [Markdown](https://www.markdownguide.org/cheat-sheet) - language used to write README and TESTING documents.
- [CSS](https://www.w3schools.com/css/) - Styling language, used for the styling of the website.
- [JavaScript](https://www.w3schools.com/js/default.asp) - used in nav bar for user to edit profile, and auto dissmiss of messages.
- [Python](https://www.python.org/) - high level programming language, used of the back end programming language.

- [LucidChart](https://lucidchart.com) - LucidChart was used to create flowchart for the project.
- [Git](https://git-scm.com/) - Git was used for version control by using the Gitpod terminal to commit to Git and push to Github.
- [Github](https://github.com/) - Github was used to write and store the projects code.
- [Google Sheets](https://www.google.com/sheets/about/) - Used to store all the data from the program.
- [Heroku](https://www.heroku.com/home) - Heroku was used to deploy the project.
- [Text ASCII Art Generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) - Used to create the logo for the project.
- [gspread](https://docs.gspread.org/en/v5.7.0/) - used for control of Google Sheets 
- [OAuthLib](https://oauthlib.readthedocs.io/en/latest/) - needed to access google sheets
- [os](https://www.geeksforgeeks.org/os-module-python-examples/) - used to write the clear screen function
- [time](https://docs.python.org/3/library/time.html) - python module - used to pause screen before continuing
- [sys](https://superfastpython.com/exit-process/#What_is_sysexit) - Python Module used to exit the program
- [random](https://www.w3schools.com/python/ref_random_random.asp) - Python Module used to generate random numbers for raffle
- [tabulate](https://www.statology.org/create-table-in-python/) - Used to create the table to print the data from the player worksheet
- [colorama](https://pypi.org/project/colorama/) - Used to colour the text in terminal output.
- [canva](https://www.canva.com/) - Usedto create the two images on the about page.
- [Nation wide.com](https://www.nationwide.com/lc/resources/home/articles/travel-safety-tips) - Used for Blog Content
- [getawayswithkids.ie](https://www.getawayswithkids.ie/2019/09/02/a-10-day-visit-to-sanguli-salou/) - Used for Blog Content
- [SFTravel.com](https://www.sftravel.com/article/san-francisco-screen-where-famous-films-and-tv-shows-were-shot-around-city) - Used for Blog Content
- [guidetoiceland.is](https://guidetoiceland.is/best-of-iceland/top-12-things-to-do-in-iceland) - Used for Blog Content
- [cntraveller.com](https://www.cntraveller.com/gallery/10-great-restaurants-in-rome) - Used for Blog Content
- [thetravelmagazine.net](https://www.thetravelmagazine.net/ski-resort-review-thyon-switzerland/) - Used for Blog Content
- [upgradedpoints.com](https://upgradedpoints.com/travel/best-tips-family-travel-with-kids/) - Used for Blog Content



[Back to top &uarr;](#contents)

## Testing

Please find Testing here: [Testing](TESTING.md)


***
## Deployment

The live deployed application can be found deployed on [Heroku](https://pp4-where-next.herokuapp.com/).

***
### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:
- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: tribe).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

[Back to top &uarr;](#content)

***
### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store docs assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.
- For *Primary interest*, you can choose *Programmable docs for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

[Back to top &uarr;](#content)

***
### Heroku Deployment

[Setting up basic Django Project and Deploying to Heroku CI Doc](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit)

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

1. Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
1. Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select *Create App*.
1. Further down, to support dependencies, select *Add Buildpack*.
1. The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)
1. From the new app *Settings*, click *Reveal Config Vars*, and set your environment variables.

    
    - CLOUNDINARY_URL: (Enter Cloudinary API URL)
    - DATABASE_URL: (Enter the database URL from ElephantSQL)
    - PORT: 8000
    - DISABLE_COLLECTSTATIC: 1 (must be removed before final deployment)
    - SECRET_KEY: (Enter your secret key)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's *requirements* (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The *Procfile* can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace *app_name* with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select *Automatic Deployment* from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <app_name>` (replace app_name with your app, without the angle-brackets)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

[Back to top &uarr;](#content)

***
### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "insert your own Cloudinary API key here")
os.environ.setdefault("DATABASE_URL", "insert your own ElephantSQL database URL here")
os.environ.setdefault("SECRET_KEY", "this can be any random secret key")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

[Back to top &uarr;](#contents)


***
#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/AngMaher/PP4-Where-Next) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/AngMaher/PP4-Where-Next.git`
7. Press Enter to create your local clone.


[Back to top &uarr;](#content)

***
#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
To make a copy or ‘fork’ the repository - 

1. Log into GitHub and locate the repository  
2. On the right-hand side of the page select the ‘fork’ option to create and copy the original

Alternatively, if using Gitpod, you can click below to create your workspace using this repository

[Back to top &uarr;](#content)

***

## Future Development

[Back to top &uarr;](#contents)

- Set up a forum section where members can connect and ask questions or start chats about anything Travel.
- Login through socails, and forget password
- Have Categories as drop down menu on the navigation bar

## Credits

Throughout the building process I found many helpful tutorials online.
I sometimes applied principles within them to the site, after fully understanding their code and modifying to fit the site's needs.

1. [Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template) - This repository was created using the template provided by Code Institute.
1. [Django Documentation](https://docs.djangoproject.com/en/4.0/) - Django step-by-step document to ensure everything is set up correctly. 
1. [Allauth Documentation](https://django-allauth.readthedocs.io/en/latest/faq.html) - referenced during development.
1. [Cloudinary Documentation](https://cloudinary.com) - referenced during development.
1. [Summernote Documentation](https://summernote.org/) and [Git](https://github.com/summernote/django-summernote) - referenced during development.
1. [Crispy Forms Documentation](https://django-crispy-forms.readthedocs.io/en/latest/) - referenced during development.
1. [John Elder - Django](https://www.youtube.com/playlist?list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy) - YouTube series that help me through project. 
1. [Stackoverflow](https://stackoverflow.com/) -Used to search issues I had.
1. [Slack](https://slack.com/intl/en-ie/) - I used Slack when I could to get answers to issues I had, it is a great resource when people are online.
1. [Markdown Builder by Tim Nelson](https://traveltimn.github.io/markdown-builder/) - tool to help generating some parts of the Markdown files
1. [W3Schools](https://www.w3schools.com/python/) - great for explaining topics.
1. [canva](https://www.canva.com/) - Used to create the images on the about page and logo for error pages.

[Back to top &uarr;](#contents)

 ## Acknowledgements
  
- I would like to thank my mentor Jubril for his guidance and help throughout the project and my many testers (family and friends).
- I would also like to mention Ed on tutor support, who helped me get my project over the finish line.

[Back to top &uarr;](#contents)