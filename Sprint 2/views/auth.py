import sqlite3
from flask import Flask, render_template, request, url_for, redirect, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import os
import urllib.request

database = "coronaArchive.db"


def login():
    # Removes any existing flash messages which may be carried over from redirects
    # session.pop('_flashes', None)
    email = None
    password = None
    userType = None
    if request.method == 'POST':
        # Removes all session values whenever post method is called (on login form submission)
        session.pop('user', None)
        session.pop('userType', None)

        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        userType = request.form['userType']
        # app.logger.info('usertype login: %s', userType)
    else:
        return render_template("login.html")

    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    if(userType == "visitor"):
        # app.logger.info("reached visitor if block")
        Visitors = cursor.execute("SELECT * FROM Visitors").fetchall()
        for singleUser in Visitors:
            # When form email and password matches with data base values
            if(singleUser[6] == email and check_password_hash(singleUser[2], password)):
                # Adds session values for following keys. Used in identifying if user is logged in or not
                # adds id (primary key) of matched user
                session['userId'] = singleUser[0]
                # Stores the sql table name of relevant usertype, used later in homepage
                session['userType'] = 'Visitors'

                # app.logger.info("logged in (places)!")
                return redirect(url_for("scan_qrcode"))
        # if fails to redirect (whenever user is not matched), then flash error message
        flash("Username or password is incorrect, please try again.")

    elif(userType == "place"):
        places = cursor.execute("SELECT * FROM Places").fetchall()
        for singleUser in places:
            if(singleUser[5] == email and check_password_hash(singleUser[2], password)):
                session['userId'] = singleUser[0]
                session['userType'] = 'Places'
                # app.logger.info("logged in (places)!")
                # return redirect(url_for("generate_qrcode"))
                return redirect(url_for("generate_qrcode"))

        flash("Username or password is incorrect, please try again.")

    elif(userType == "agency"):
        agencies = cursor.execute("SELECT * FROM Agency").fetchall()
        for singleUser in agencies:
            if(singleUser[1] == name and check_password_hash(singleUser[2], password)):
                session['userId'] = singleUser[0]
                session['userType'] = 'Agency'
                # app.logger.info("logged in (agencies)!")
                return redirect(url_for("index"))
        flash("Username or password is incorrect, please try again.")

    elif(userType == "hospital"):
        hospital = cursor.execute("SELECT * FROM Hospital").fetchall()
        for singleUser in hospital:
            if(singleUser[1] == name and check_password_hash(singleUser[2], password)):
                session['userId'] = singleUser[0]
                session['userType'] = 'Hospital'
                return redirect(url_for("index"))
        flash("Username or password is incorrect, please try again.")

    # only for debugging purposes:
    # else:
    #     app.logger.info("unknown user type!")
    return render_template("login.html")


def logout():
    session.pop('userId', None)
    session.pop('userType', None)
    return redirect(url_for('index'))
