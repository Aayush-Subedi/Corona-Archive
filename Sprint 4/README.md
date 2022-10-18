# Corona Base

# Sprint 4

## Contributors

Aayush Subedi

Karen Arzumanyan

## Additions
During this sprint, the following features were added.

Agent 
* Agent can see the list of the visitors which are registered. 
* Agent can see the list of the places owners which are registered. 
* The place, the time and the date when a visitor entered a place and when they left that  place must be shown in the agent’s page. 
* Agent can be able to search by person with the option of also adding a time interval. 
* Agent can be able to search by place with the option of also adding a time interval. 
* Agent can track the people who were present at a particular place.  
* Agent can see with whom a particular person was at a particular place.  

Place
* (Navbar) Dashboard for Hospital
* QR stores Place ID
* Login for place
* QR code available in the dashboard
* Multiple users possible at a time in the same place
* Entry and Exit time based on time zones

Visitor 
* (Navbar) Dashboard for Visitors
* QR code Scanning 
* The visitor after scanning the QR code and clicking Submit button, will be redirected to  the “You’re in” page with timer (Timer Continues even when the page is refreshed). 
* The user shall leave by clicking a button.
* When clicking Leave button, the visitor must be redirected to the main page. 
* After registering, the visitors must be directed to the scanning page. 
* If visitor is corona positive they are not allowed to scan QR code

Hospital
* (Navbar) Dashboard for Hospital
* Hospital must see the list of visitors registered.
* The hospital shall search the visitors by name. 
* Hospital must be able to check or uncheck the status of healthiness of a particular visitor. 
* Hospital can request agent for registration.

Other
* Authorisation feature
* Front-end pages

Old unit tests were updated, and new ones implemented.
They can be found in
`
se-04-team-04/tests/testApp.py
`
```
Login Informations:
Visitor (Infected): 
    email: Tom@email.com
    password: test@123
Visitor (Not Infected): 
    email: John@email.com
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
They can be run by executing
```bash
python3 testApp.py
```
While the virtual environment is active (mentioned in Installation Updated)

Or by running
```bash
./env/bin/python3 testApp.py
```

## Installation Updated
First we need to clone the repository to your machine and proceed into its directory. Use
```bash
#To clone the repository locally
git clone https://github.com/Magrawal17/se-04-team-04.git

#To enter the newly created directory
cd se-04-team-04
```

Now we must create a virtual environment for the Python packages to be isolated from your global system.
To do so we shall use the method that comes with Python3
```bash
#To create the virtual environment
python3 -m venv env

#To activate the virtual environment
. ./env/bin/activate
```

After activating the virtual environment, any packages installed through pip will be confined to the virtual environment.

Now we need to install the required Python packages for the app itself. Simply use
```bash
#To install all the required packages
pip3 install -r requirements.txt
```

__WARNING: DO NOT USE__ ```sudo``` __WITH__ ```pip``` __WHILE THE VIRTUAL ENVIRONMENT IS ACTIVE, AS IT WILL INSTALL THE PACKAGES GLOBALLY!__ 

## Running
After completing all of the steps in the _Setup_ section, you should be able to run the Flask debug server by typing while the virtual environment is active
```bash
python3 run.py
```

However, if you wish to run the Flask app without activating the virtual environment, while in the directory of the project (or with the absolute path to the directory) you can type
```bash
./env/bin/python3 run.py
```
# Sprint 4 Readme end

## Introduction:

Corona Archive is a Corona control platform designed to track and reduce the prevalence of active cases of the Covid-19. The entire platform revolves around gamifying the mundane but important
task of taking active prevention measures against spread of communicable disease, like COVID-19. For users, it notifies them of any positive test cases based on their recent location history. For both users and establishments, it gives a metric of how safe a place/person is. For evaluation clients, it can provide analytics and data on demand. Hospitals can also update user’s and infection status. The system takes a score based approach to measure safety and manage access.

The app is composed of the following four entities:

-   Visitors
-   Establishments(Places)
-   Evaluation Client or Agent(generates reports for Governments and institutions)
-   Hospital

## Instructions:

Clone the repositary

```
git clone https://github.com/Magrawal17/SE-Sprint01-Team04.git

```

CD intro the directory

```
cd SE-Sprint01-Team04/
```

Install the required packages using pip

```
pip install -r requirements.txt
```

Run the run.py script

```
python run.py
```

Credential For Agent:

```
Username: admin
Password: admin
```

# Documenting Feature for Sprint 1:

-   Registration feature of all Entities(Visitor, Place, Hospital) except Agent.
-   Login possible of all four Entities(Visitor, Place, Hospital, Agent).
-   Unique QR-code for Places generated and available for downlaods .
-   Password encryption using hashing.
-   System wide credential management using a login manager.
-   Entities that require unique data are checked in the databse as well.

## Architechture Used:

-   HTML, CSS and Javascript are used for Frontend Designs.
-   Python is used for Backend along with Flask Web Framework.
-   Sqlite is used for database with an open-source SQL toolkit known as SQLAlchemy.

## Contributors:

-   Manish Thapa
-   Riley Edwin Sexton

# Documenting Feature for Sprint 2:

-   Error Handler Pages for 404, 403, 500
-   Hospital Center python class for register/remove hospital list for back end
-   Place Center python class for register/remove python list for back end
-   Syntax improvement
-   Commenting on code to make it better understandable
-   Some CSS changes to make website more easily readable

## Architechture Used:

-   HTML, CSS and Javascript are used for Frontend Designs.
-   Python is used for Backend along with Flask Web Framework.
-   Class in Python for centralized properties adminstration

## Suggestions for next sprint

-   Both Place/Hospital Center class improvement for center adminstration
-   Unit Test Cases
-   Error Page direction for each certain error

## Contributors:

-   Haolan Zheng
-   Hannah Andrea McDermott

# Sprint 3

With this weeks sprint, the goal was cleaning up and progressing the codebase to a more manageable state. Much cleanup, bug fixes, comments, and added SQL scripts.

Contributor: Justin Morris

## File structure

```
\--se-03-team-04
    \--CoronaArchieve                       # JS, CSS files and any other assets
        \--errors
            \-- __init__.py
            \-- handlers.py
    \--SQL                                  # database creating files
        \-- createTables.py
        \-- insertValues.py

    \--static                               # JS, CSS files and any other assets (ex. images)
        \-- CSS
            \-- form_style.css
            \-- style.css
        \-- images
            \-- corona.png
        \-- js
            \-- main.js
        \-- dynamic images
        \-- .
        \-- ..
        \-- ...


    \--templates                             # HTML templates
        \-- errors
            \-- 403.html
            \-- 404.html
            \-- 500.html
        \-- agent_login.html
        \-- AgentDashboard.html
        \-- baselayout.html
        \-- hospital_dashboard.html
        \-- hospital_login.html
        \-- index.html
        \-- login.html
        \-- place_dashboard.html
        \-- place_home
        \-- place_registration_login.html
        \-- user_dashboard.html
        \-- user_registration_login.html

        \-- __init__.py                     # initializing file
        \-- database.db                     # database
        \-- forms.py                        # contains flask forms
        \-- models.py                       # models for the database
        \-- routes.py                       # contains all routes and logic

    \--tests                                # Python based tests
        \-- tests.py

    \-- run.py                              # Main python (flask) app
    \-- README.md                           # This file
    \-- requirements.txt                    # Flask dependency list (see below)
    \-- .gitignore                          # files to ignore when committing
```

## Setup and How to Run

We assume python us installed.

1. Install VirtualEnv

```
pip3 install virtualenv
```

2. Setup

-   Clone or download repository
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

6. Create the sql database and insert data.

```
cd CoronaArchieve && python3 sql/createTables.py && python3 sql/insertValues.py
```

7. Run development server

```
cd ../ && python3 run.py
```

## Tasks Completed

-   Add documentation to all code
-   Created GET and POST test cases
-   Added a gitignore
-   Create sql tables script
-   Create dummy value insert script

## To run tests

In total 9 GET and POST tests have been implemented.

1. Ensure in root of project

2. Source environment using

```
source myEnv/bin/activate
```

3. Run tests

```
python3 tests/testApp.py
```

## Suggestions for future sprints

-   Improved dashboards functionality for agents and hospitals
-   Allow hospitals to designate someone as infected
-   Allow agents to contact trace infected person
-   Only allow access to dashboards when logged in
-   Implement contact tracing searching
