# README for SE-Sprint01-Team07-



### Contributors

Sprint 1
- Aayush Subedi
- Siddhartha Chhabra


## About the Project

In this sprint we started the programming phase. We started by creating various html files for our web services such as registration, login, index etc. and beautified it with the help of CSS. After that we started using flask a web framework which helped us develop and host our web service. Then we created various queries and ran them through python SQLite which is a self-contained file-based SQL database that will store all our important data like citizens, owners, hospitals, and admin’s information.

### Built with
* HTML
* CSS
* [Python3](https://www.python.org/download/releases/3.0/)
* [Flask](https://www.fullstackpython.com/flask.html)
* [SQLite](https://www.sqlite.org/)

## File Structure
```
\--SE-SPRINT01-TEAM07
        \--static
            \--css                  # All the CSS Files used
            \--img                  # All the images used 
        \--templates    
            \--                     # Main HTML files    
        \--tests
           |--sprint1_tests.py      # Main Testing Python Code
        -- app.py                    # Main Python Code
        -- README.md
        -- requirements.txt          # Required dependencies
        -- SE Sprint 1.docx          # external documentation (docx)
        -- SE Sprint 1.pdf           # external documentation (pdf)
        -- .gitignore    
```

## Getting Started

The following are the list of things to be installed in order to run the project. It also provides the ways to install it.


### Prerequisites


* Flask 
```
pip3 install Flask
```
* Virtual Env
```
sudo pip3 install virtualenv 
```
* Pillow
```
python3 -m pip install --upgrade Pillow
```


## Installation Guide

```bash

# Clone the repository.
git clone https://github.com/Magrawal17/SE-Sprint01-Team07.git

# Then go to this folder where it is. 
cd SE-Sprint01-Team07/

# Create virtual environment
$ virtualenv env

# Start virtual environment
$ source env/bin/activate

# Install all the dependencies
$ pip3 install -r requirements.txt

# Run python server
$ python -m flask run

```

# Run tests

Run this code once you are entire the environment

```sh
$ python3 tests/test_sprint1.py
```

## Sprint 1 features added

✅   Successfully implemented registration page for Visitor and Place Owner like asking them for information and safely putting it in our database.

✅   Giving Visitor (Citizen) an option to choose if he wants to provide phone number or email or both.

✅   Creating a QR code for scanning after completing the registration process of Owner.

✅   Successfully creating a login page for Hospital and Agent. (The agent’s credential – username and password are already created by us).

✅   Place Owner receives a QR code as soon as he registers with us.
