# Item Catalog Project
This Project is part of the Udacity[Fullstack Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) curriculum.

## Project Overview
This project is a RESTful web application which focus on developing an application that provides a list of items within a variety of categories as
well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.
utilizing the Flask framework which accesses a SQL database that populates categories and their items. OAuth2 provides authentication for further CRUD functionality on the application. Currently OAuth2 is implemented for Google Accounts.

## Project Walkthrough
It has a main Python module `project.py` which runs the Flask application. A SQL database is created using the `database_setup.py` module and you can populate the database with test data using `moreWebsites.py`.
The Flask application uses stored HTML templates in the tempaltes folder to build the front-end of the application.


## Installation
There are some Requirements and a few instructions on how to run the application.
Seperate instructions are provided to get GConnect working also.

## Requirements
- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## How to Install
1. Install Vagrant & VirtualBox
2. Clone the Udacity Vagrantfile
3. Go to Vagrant directory and either clone this repo or download and place zip here
3. Launch the Vagrant VM (`vagrant up`)
4. Log into Vagrant VM (`vagrant ssh`)
5. Navigate to `cd/vagrant` as instructed in terminal
6. The app imports requests which is not on this vm. Run sudo pip install requests
7. Setup application database `python /ItemCatalog/database_setup.py`
8. *Insert data `python /item-catalog/moreWebsites.py`
9. Run application using `python /item-catalog/app.py`
10. Access the application locally using http://localhost:5000

*Optional step(s)

## Using Google Login
To get the Google login working there are a few additional steps:

1. Go to [Google Dev Console](https://console.developers.google.com)
2. Sign up or Login if prompted
3. Go to Credentials
4. Select Create Crendentials > OAuth Client ID
5. Select Web application
6. Enter name 'Item-Catalog'
7. Authorized JavaScript origins = 'http://localhost:5000'
8. Authorized redirect URIs = 'http://localhost:5000/login' && 'http://localhost:5000/gconnect'
9. Select Create
10. Copy the Client ID and paste it into the `data-clientid` in login.html
11. On the Dev Console Select Download JSON
12. Rename JSON file to client_secrets.json
13. Place JSON file in item-catalog directory that you cloned from here
14. Run application using `python /item-catalog/app.py`

## JSON Endpoints
The following are open to the public:

Category JSON: `/category/<int:category_id>/website/JSON`
    - Displays the whole category websites.

Categories JSON: `/category/JSON`
    - Displays all categories

Website JSON: `/category/<int:category_id>/website/<int:website_id>/JSON`
    - Displays a specific Website item.
