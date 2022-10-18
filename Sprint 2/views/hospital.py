import sqlite3
from flask import Flask, render_template, request, url_for, redirect, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

database = "coronaArchive.db"


def hospital_visitor():
    usertype = session.get('userType')
    if usertype != 'Hospital':
        flash("SORRY NOT AUTHORIZED")
        return redirect(url_for('index'))
    if 'userId' in session:
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        # Obtain logged in user's attributes from database
        loggedInUser = cursor.execute(
            f"SELECT name FROM {session.get('userType')} WHERE id='{session.get('userId')}'").fetchone()

        #  Obtain all visitors from database
        visitors = cursor.execute("SELECT * FROM Visitors").fetchall()

        return render_template("hospital_visitor_info.html", visitors=visitors)
    else:
        flash("You need to login to access the home page.")
        return redirect(url_for('index'))


def change_corona_status():
    usertype = session.get('userType')
    if usertype != 'Hospital':
        flash("SORRY NOT AUTHORIZED")
        return redirect(url_for('index'))
    if 'userId' in session:
        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        if request.method == "POST":
            visitorId = request.form['visitorId']
            coronaStatus = request.form['coronaStatus']
            isVisitorExist = cursor.execute(
                f"SELECT * FROM Visitors WHERE id='{visitorId}'").fetchone()
            
            if isVisitorExist:
                cursor.execute(
                    f"UPDATE Visitors SET has_covid='{coronaStatus}' WHERE id='{visitorId}'")
                connection.commit()
            else:
                flash("Visitor does not exist")

        return redirect(url_for('hospital_visitor'))

    else:
        flash("You need to login to access the home page.")
        return redirect(url_for('index'))
