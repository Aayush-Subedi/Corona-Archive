# General Info

-   SE-Sprint01-Team06 deadline: 18 March 2022
    <br>

-   Group members:
    -   Justin Morris
    -   Muhammad Umar Shakeel

# About project

The purpose of this project is to build a web service for Corona disease management which
enables digital tracking of citizens which enter certain places and keeping the records in case of a
Covid infection spread. The web service will be accessible to 4 types of users: visitors, place owners, health agencies and hospitals.

### Built with...

-   Python3 (Project developed with 3.9.10)
-   Flask
-   SQLite
-   HTML (using jinja2 template engine)
-   CSS
-   Javascript

# Project File Structure

```
SE-Sprint01-Team06
├── README.md                       # This file
├── app.py                          # Main python (flask) app
├── coronaArchive.db
├── requirements.txt                # Flask dependency list (see below)
├── sql                             # SQLite database initialization files
│   ├── createTables.py
│   └── createTables.sql
├── static
│   ├── css
│   │   ├── base.css
│   │   ├── form.css
│   │   ├── navbar.css
│   │   ├── search_box.css
│   │   ├── table.css
│   │   └── try.css
│   ├── images
│   │   ├── index_try.svg
│   │   ├── login_try.svg
│   │   ├── register_try.svg
│   │   ├── try2.svg
│   │   ├── try3.svg
│   │   └── try4.svg
│   ├──  js
│   │   ├── changeStatus.js
│   │   ├── loginForm.js
│   │   ├── registerForm.js
│   │   └── search_visitor.js
│   └── uploads                      # generated QR codes are stored
│       └── qrcodes
├── templates                        # HTML templates (jinja2)
│   ├── 404.html
│   ├── base.html
│   ├── hospital_registration.html
│   ├── hospital_visitor_info.html
│   ├── index.html
│   ├── login.html
│   ├── login_form.html
│   ├── navbar.html
│   ├── place_owner_info.html
│   ├── qr_viewer.html
│   ├── qrcode_generator.html
│   ├── register.html
│   ├── registration_form.html
│   ├── scan_qrcode.html
│   ├── try.html
│   └── visitor_info.html
├── tests                            # Python based tests
│   ├── coronaArchive.db
│   ├── testSprint1.py              #from previous sprint (NOT USED)
│   └── testSprint2.py
└── views
    ├── __init__.py
    ├── agency.py
    ├── auth.py
    └── hospital.py
```

# Installation and How to Run

Note, it is assumed as a pre-requisite, that you have [Python](https://www.python.org/downloads/) installed.

1. Install VirtualEnv

```
pip3 install virtualenv
```

2. Setup

```zsh
# Cloning the repo 
$ git clone https://github.com/Magrawal17/se-02-team-06.git
$ cd SE-Sprint01-Team05
```

3. Create your virtual environment

```
python3 -m venv myEnv
```

4.  Source into virtual environment

```
source myEnv/bin/activate
```

5.  Install required project dependencies

```
pip3 install -r requirements.txt
```

6.  Run development server

```
python3 app.py
```

7.  Open flask application in the web browser

```
http://localhost:8000/
```

```
Login Informations:
Visitor: 
    email: test@test.com
    password: test
Agency:
    name: agency
    password: agency
Hospital:
    name: hamrohospital
    password: hamrohospital
Place Owner:
    email: test@test.com
    password: test
```

# Testing

### How to test

1. From the root folder, source into proper environment by using,

```
source myEnv/bin/activate
```

2. Run test (must be from the root folder!) using,

```
python3 tests/testSprint2.py
```

# Sprint Progress

## Sprint 1: Justin Morris and Muhammad Umar Shakeel

✅ Added front-end homepage/index, login and registration pages, alongside CSS styling  
✅ Implemented database using SQLite  
✅ Added front-end forms for login and registration pages  
✅ Using flask to communicate between front-end forms and using obtained form data to insert/query sqlite database  
✅ If user tries to access homepage without logging in, user is redirected to login page and asked to login  
✅ Registration supports insertion of 4 different user types into database: visitor, place, agency and hospital  
✅ All passwords given during registration are hashed using werkzeug (werkzeug is natively available in flask, no pip install required) and only hashed passwords are stored on database. This is to maintain user secuirity  
✅ Registration page checks if an exisiting user with those credentials exists. If so, then flashes error message. If not, then registers successfully, and redirects to login page  
✅ Login supports 3 user types: visitor, place, agency  
✅ Once login form is submitted, a check is made against the database if user exists in selected usertype category, and if exists, it checks form password input data against the encrypted password hash stored in the database. If it matches, user is logged in and redirected to homepage. If not, flashes error message to retry login process  
✅ Once redirected to homepage/index, user is greeted by a screen that tells them their userid, their usertype, and username  
✅ User has ability to logout from the top right button inside the top navigation bar  
✅ Login implementation:

-   User login functionality is implemented using flask session (built-in to flask, no pip install needed)
-   When app is initially started, it goes to homepage/index and checks if current session has a 'userId' in it. If not, it redirects to the login page and asks user to login
-   In the login page, when user successfully logs in, 2 new sessions keys 'userId' and 'userType' are created, which store the newly created user's primary key (id) and their usertype. User is then redirected to homepage
-   Now that homepage can see that session 'userId' key is not empty, it renders the homepage template. Here, it uses this id and usertype to perform sql query to
    get the user's name. This is then displayed on the template
-   If user wants to loggout, they can click on the loggout button on the top nav bar, and the 'userId' and 'userType' sessions keys are flushed out, and user is redirected to login page

## Sprint 2: Aayush Subedi and Shronim Tiwari

### Improved to previous sprint
  
✅ Hospital and Agency were allowed to register themselves. This is fixed.  
✅ When registering, required fields could be left blank. This is fixed. Blank entry cannot be submited for required fields anymore.  


### Added functionalities
*  **Changes in front-end**    
    * The design for form was reused
    * ✅Homepage is added 
    * ✅SVG images used for better asthetics     
    * ✅Design for displaying tables is added
    * ✅Generated separate display page for all users   
*  **For Place Owner**  
    * ✅ Implemented the generation of QR code
    * ✅ QR code is generated based on primary key of place-owner
    * ✅ When Place-owner logs in, QR code is displayed 
    * ✅ Place-owner can download QR code after they login
* **For Visitors**
    * ✅ Implemented scanning of QR code for visitors             
* **For Agency**
    * ✅ Separate page when logged in as agency  
    * ✅ Agency can retrieve the information from database and view the list of visitors and places  
    * ✅ Separate page to view visitors and places  
    * ✅ Agency can search visitors and places by name
    * ✅ Only agency can register hospital  
* **For Hospital**
    * ✅ The data of visitors is retrieved and displayed in the table.
    * ✅ Hospital can update/change the covid status of visitors
* **Database**
    * ✅ Written statement to create table for VisitortoPlaces to record the information when visitor visits places      
