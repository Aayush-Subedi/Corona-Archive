# SE-Sprint01-Team05

# Sprint 1

-   Shronim Tiwari
-   Hannah McDermott

## About the Project

'Corona Archive' is a web application created for the course Software Engineering at Jacobs University of Bremen. This application is meant to help policy-makers in Germany with decisions regarding which corona restrictions to implement and which to disregard as too strict.

## Built With

-   HTML
-   CSS
-   Python3
-   SQLite

## Getting Started

Follow these steps to clone this repository and run the project in your local machine.

-   Flask

```
pip3 install Flask
```

-   Virtual Env

```
sudo pip3 install virtualenv
```

## Installation Guide

```zsh
# Cloning the repo
$ git clone https://github.com/Magrawal17/SE-Sprint01-Team05.git
$ cd SE-Sprint01-Team05

#Create Virtual Environment
$ virtualenv env

#Activate Virtual Environment
$ source env/bin/activate

#Installing Required Dependencies
$ pip3 install -r requirements.txt

#Setup SQLite Database
$ python db.py

#Run Flask server
$ python test01.py
```

## Access Webapp

Open following link in your browser to access webapp

```
http://127.0.0.1:5000
```

## View Documentation

The documentation can be viewed from following url after starting the server.

```
http://127.0.0.1:5000/docs
```

## Run test

Tests should be ran inside the environment with following command:

```zsh
$ python -m pytest
```

There are some UNIQUE elements in the table. So, if you rerun, some test might fail. If you remove coronatest.sqlite, and run 'python db.py', all test cases should pass.

## More information for next sprint (from Sprint 1)

-   inside /login.html, login as hospital is disabled as it couldn't be implemented
-   agents can be registered through /reg_agent.html. However, this should not be accessible to public but just for user. This is mainly implemented to test login.
-   through check-in (/scan_qrcode.html) scanning of qr-code should be performed. Currently, it is not correctly working
-   after agent or hospital logs in, they should be redirected to dashboard_agent.html or dashboard_hospital.html respectively. These are not implemented in this sprint
-   /reg_locale.html is to register the location. Needs to be implemented

# Sprint 2

-   Justin Morris
-   Manish Thapa

## Sprint Progress

✅ Organized sprint1's code and folders (check below at cleaned structure)<br>

-   Deleted unused files
-   Renamed files to descriptive names
-   Moved like files together
    <br>

✅ Added file structure<br>
✅ Added a git ignore <br>
✅ Added python formatter<br>
✅ Fixed create tables script with proper fields and types<br>
✅ Implement working tests (GET and POST)<br>

-   Works with sessions

✅ Cleanup html pages

-   Many pages - Remove unruly font family
-   index page - remove not needed tags<br>
-   login page - cleanup to adhere to database and flask request form names<br>
-   reg_agent page - cleanup, fix typos, and correctly format flask request names
-   reg_local page - add comments, and change names to fit with flask server request
-   reg_visitor page - Alter names of inputs
-   scan_qrcode page - format code
-   users page - Fix names to match with that of the values passed from the flask server
    <br>

✅ Implementation of sessions

-   Able to log out and session closed
-   Hospitals: Allow change of who is positive
    -   To be done in future sprint
-   Agents: Can search all visitors in database
    <br>

✅ Added working visitor and place registration page
<br>
✅ Login implemented with dashboard and appropriate navigation control 

-   Login implmented for Agent
-   Hospitals can now login with the credential provided by agent

✅ New features for Agent 

-   Search visitor by name
-   Search place by name
-   Register Hospitals 

✅ New features for Hospital 

-   Search patient(visitor) by name

✅ New features for Visitor 

-   Visitor can scan QR code of places they visit.
-   Scanning a QR code will lead visitor to time counter

✅ New features for Place 

-   QR code for places is generated
-   QR code can be downloaded

## New Project File Structure

```
\--SE-Sprint01-Team06
        \--static                   # JS, CSS files and any other assets (ex. images)
            \-- CSS
                \-- form_style.css
                \-- style.css
            \-- js
                \-- main.js
        \--templates                # HTML templates (jinja2)
            \-- agent_dash.html
            \-- agent_dashboard_baselayout.html
            \-- agent_login.html
            \-- all_visitors.html
            \-- baselayout.html
            \-- dashboard_agent.html
            \-- dashboard_hopsital.html
            \-- display_camera.html
            \-- hospital_login.html
            \-- hospital_registration.html
            \-- imprint.html
            \-- index.html
            \-- login.html
            \-- place_dashboard.html
            \-- place_registration.html
            \-- reg_locale.html
            \-- scan_qrcode.html
            \-- visitor_registration.html
            \-- visitor_timer.html
        \--SQL                   # SQLite database initialization files
            \-- createTables.py
            \-- db_insert.py
        \--tests                    # Python based tests
            \-- tests.py
        -- Customer_Requirements.pdf    # Project
        -- app.py                   # Main python (flask) app
        -- db.sqlite                # database
        -- README.md                # This file
        -- requirements.txt         # Flask dependency list (see below)
        -- .gitignore               # files to ignore when committing
```

## New Installation and How to Run (changed post organization)

Note, it is assumed as a pre-requisite, that you have [Python](https://www.python.org/downloads/) installed.

1. Install VirtualEnv

```
pip3 install virtualenv
```

2. Setup

-   Clone/Download entire repository
-   Navigate to repository base folder, open bash/command prompt

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

6. Create the sql database and insert data

```
python3 sql/createTables.py && python3 sql/dummyValuesInsert.py
```

7.  Run development server

```
python3 app.py
```

8.  Open flask application in the web browser

```
http://localhost:5000/
```

## Testing

Note: The login features of the testing file require certain credentials to be present to login agents and hospitals. Such credentials are inserted into the database upon the run of the `dummyValuesInsert.py`.

0. Source into the environment

1. If no database file exists, from the root folder, run

```
python3 sql/createTables.py && python3 sql/dummyValuesInsert.py
```

2. If the database already exists, check if the values inserted in `dummyValuesInsert.py` are present. If not, from the root folder, run

```
python3 dummyValuesInsert.py
```

3. Ensure the flask server is running
4. Run the test file (Must be run from the root folder)

```
python3 tests/tests.py
```

# Sprint 3

-   Haolan Zheng
-   Aayush Subedi

## Sprint Progress

✅ Error Page Update
-   404 Page Not Found  
-   403 Permission Error  
-   500 Something went wrong  
    
✅ SQL createtable py file update  
-   table update for:  
-   create places  
-   Place visited  
-   Agent  
-   Hospital:  
        -   some values insert for: visitor, place
    
✅ html page update:  
-   baselayout, display camera, index html update  
-   log place & log visitor html create  
-   css file update for table, style, form_style files  
-   info html page create: my info, place info, visitor info, place info   
-   navbar, footer html pages added  
-   some htmls moved to unused folder  
-   for login display:  
        -   hospital, agent, visitor updated  
    
✅ js file udpate:
-   place searching function added  
-   data convert function added  

✅ route file update:
-   Agent:  
    - Agent can see the list of the visitors which are registered. 
    - Agent can see the list of the places owners which are registered. 
    - The place, the time and the date when a visitor entered a place and when they left that place is shown in the agent’s page. 
    - Agent can search by person with the option of also adding a time interval. 
    - Agent can search by place with the option of also adding a time interval. 
    - Agent can track the people who were present at a particular place.  
    - Agent can see with whom a particular person was at a particular place. 

- Visitor 
    - The visitor after scanning the QR code and clicking Submit button, will be redirected to the “You’re in” page. 
    - The user can leave by clicking a button.
    - When clicking Leave button, the visitor is redirected to the main page. 
    - After registering, the visitors is directed to the scanning page. 
    - Login possible for visitor
  
- Hospital
    - Hospital must see the list of visitors registered.
    - The hospital shall search the visitors by name. 
    - Hospital must be able to check or uncheck the status of healthiness of a particular visitor. 

- Place
    - Login for place
    - QR code available in the dashboard
    - QR code stores Place_ID
    - Hours added to the timer that starts after scanning QR code
    - Time runs in the background even if the web page is closed
    - Multiple visitors can visit the same place
    - Entry and Exit date/time are stored according to time zone

- Other Funtionality
    - Only authorized entities can acces their data.
```
Login Informations:
Visitor: 
    email: Tom@email.com
    password: test@123
Agency:
    username: Sam
    password: password123
Hospital:
    name: GrandVC
    password: healthIsCool
Place Owner:
    email: tbs@email.com
    password: test@123

```

## New File Structure 
```
    \--SE-Sprint01-Team06
        ├── app.py
        ├── Customer_Requirements.pdf
        ├── db.sqlite
        ├── errors
        │   ├── handlers.py
        │   ├── __init__.py
        │   └── __pycache__
        │       ├── handlers.cpython-38.pyc
        │       └── __init__.cpython-38.pyc
        ├── README.md
        ├── requirements.txt
        ├── sql
        │   ├── createTables.py
        │   └── dummyValuesInsert.py
        ├── static
        │   ├── 05adeb9935d8b0113309.png
        │   ├── 3c957d8bb092bd8a9e47.png
        │   ├── 4243ac12bff05767ef6d.png
        │   ├── 788a7c685d66778d6b46.png
        │   ├── 87f77167b42ba1a75693.png
        │   ├── a08ab65d6549395b0791.png
        │   ├── a3ee7a54e0e15e25127d.png
        │   ├── a5418c95b3960a6f9a47.png
        │   ├── c35d851f001627a849bb.png
        │   ├── images
        │   │   └── corona.png
        │   └── style
        │       ├── css
        │       │   ├── form_style.css
        │       │   ├── style.css
        │       │   └── table.css
        │       └── js
        │           ├── date_convert.js
        │           ├── main.js
        │           ├── place_search.js
        │           └── visitor_place_search.js
        ├── templates
        │   ├── agent_dashboard_baselayout.html
        │   ├── agent_login.html
        │   ├── baselayout.html
        │   ├── dashboard_agent.html
        │   ├── dashboard_hospital.html
        │   ├── display_camera.html
        │   ├── errors
        │   │   ├── 403.html
        │   │   ├── 404.html
        │   │   └── 500.html
        │   ├── footer.html
        │   ├── hospital_login.html
        │   ├── hospital_registration.html
        │   ├── hospital_visitor_info.html
        │   ├── imprint.html
        │   ├── index.html
        │   ├── log_place.html
        │   ├── log_visitor.html
        │   ├── navbar.html
        │   ├── place_dashboard.html
        │   ├── place_info.html
        │   ├── place_registration.html
        │   ├── reg_locale.html
        │   ├── scan_qrcode.html
        │   ├── unused html
        │   │   ├── all_visitors.html
        │   │   ├── login.html
        │   │   ├── my_info.html
        │   │   ├── search_patient.html
        │   │   ├── search_place.html
        │   │   ├── search_visitor.html
        │   │   └── visitor_timer.html
        │   ├── visitor_dashboard_baselayout.html
        │   ├── visitor_info.html
        │   ├── visitor_place.html
        │   └── visitor_registration.html
        └── tests
            ├── db.sqlite
            └── tests.py

```

## New Installation and Run the project


1. Install VirtualEnv

```
pip3 install virtualenv
```

2. Setup

-   Clone/Download entire repository

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

6. Create the sql database and insert data

```
python3 sql/createTables.py && python3 sql/dummyValuesInsert.py
```

7.  Run development server

```
python3 app.py
```

8.  Open flask application in the web browser

```
http://localhost:5000/
```

## Testing

0. Source into the environment, check dummy values insert file

1. If no database file exists, from the root folder, run

```
python3 sql/createTables.py && python3 sql/dummyValuesInsert.py
```

2. If the database already exists, check if the values inserted in `dummyValuesInsert.py` are present. If not, from the root folder, run

```
python3 dummyValuesInsert.py
```

3. Ensure the flask server is running
4. Run the test file (Must be run from the root folder) Note that more than 20 tests had added

```
python3 tests/tests.py
```

