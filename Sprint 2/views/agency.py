import sqlite3
from flask import Flask, render_template, request, url_for, redirect, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

database = "coronaArchive.db"


def visitorinfo():
    usertype = session.get('userType')
    if usertype != 'Agency':
        flash("SORRY NOT AUTHORIZED")
        return redirect(url_for('login'))
    if 'userId' in session:
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        # Obtain logged in user's attributes from database
        loggedInUser = cursor.execute(
            f"SELECT name FROM {session.get('userType')} WHERE id='{session.get('userId')}'").fetchone()

        #  Obtain all visitors from database
        visitors = cursor.execute("SELECT * FROM Visitors").fetchall()

        return render_template("visitor_info.html", visitors=visitors)
    else:
        flash("You need to login to access the home page.")
        return redirect(url_for('login'))


def placeinfo():
    usertype = session.get('userType')

    if usertype != 'Agency':
        flash("SORRY NOT AUTHORIZED")
        return redirect(url_for('login'))
    if 'userId' in session:
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        # Obtain logged in user's attributes from database
        loggedInUser = cursor.execute(
            f"SELECT name FROM {session.get('userType')} WHERE id='{session.get('userId')}'").fetchone()

        #  Obtain all visitors from database
        place_owners = cursor.execute("SELECT * FROM Places").fetchall()

        return render_template("place_owner_info.html", places=place_owners)
    else:
        flash("You need to login to access the home page.")
        return redirect(url_for('login'))


def hospital_registration():

    usertype = session.get('userType')

    if usertype != 'Agency':
        flash("SORRY NOT AUTHORIZED")
        return redirect(url_for('login'))
    if 'userId' in session:
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        # Obtain logged in user's attributes from database
        loggedInUser = cursor.execute(
            f"SELECT name FROM {session.get('userType')} WHERE id='{session.get('userId')}'").fetchone()

        if request.method == 'POST':
            name = request.form['name']
            password = request.form['password']
            hashedPassword = generate_password_hash(password)

            existingUser = cursor.execute(
                f"SELECT * FROM Hospital WHERE name='{name}'").fetchone()
            if existingUser:
                flash("Hospital already exists.")

            else:
                params = (name, hashedPassword)
                cursor.execute(
                    "INSERT INTO Hospital VALUES (NULL, ?, ?)", params)
                connection.commit()
                flash("Successfully registered!")

        return render_template("hospital_registration.html")
    else:
        flash("You need to login to access the home page.")
        return redirect(url_for('login'))
