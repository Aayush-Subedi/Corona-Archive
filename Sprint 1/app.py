from asyncio.base_tasks import _task_get_stack
from flask import Flask, render_template, request, flash, redirect, url_for, session, send_file
from datetime import datetime
import sqlite3
import qrcode
from io import BytesIO
import os


app = Flask(__name__)
app.secret_key = "123"


def generate_qr_code(data, id):
    # Initialize the qr code generator with configuration like version, shape and size
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Add Data to the qr code
    qr.add_data(data)

    # Generate the qr code
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    """
    * IF you want to save the qr code as an image in the file system
    app.config['UPLOAD_FOLDER'] = 'static/qr_codes'
    print("2")
    path = os.path.join(app.config['UPLOAD_FOLDER'], "owner"+str(id) + '.png')
    print(path)
    print("3")
    img.save("owner"+str(id) + '.png')
    """
    # Return the qr code
    return img


# Database
con = sqlite3.connect("database.db")
# Owner
con.execute("create table if not exists owner(id integer primary key,name text,address text,phone text,email text)")
# Citizen
con.execute("create table if not exists citizen(id integer primary key,name text,address text,phone text,email text, city text)")

con.execute("""CREATE TABLE if not exists Agent (
            id integer primary key autoincrement not null,
            username text,
            password password
) """)

con.execute("""CREATE TABLE if not exists Hospital (
            id integer primary key autoincrement not null,
            username text,
            password password
) """)  # Creating various tables into our DB

con.execute("""INSERT INTO Agent(username,password)  
            VALUES('agent','123') """)  # inserting admin username and password for authentication

con.execute("""INSERT INTO Hospital(username,password) 
            VALUES('Foo','abc') """)  # inserting hospital(1) username and password(Could add more later since hospitals dont register themselves!)
con.commit()
con.close()


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/citizen', methods=['POST', 'GET'])
def citizen():
    if request.method == 'POST':
        try:
            task_name = request.form['name']
            task_address = request.form['address']
            task_city = request.form['city']
            task_phone = request.form['phone']
            # Taking values from input by user
            task_email = request.form['email']
            con = sqlite3.connect("database.db")
            cur = con.cursor()
            cur.execute("insert into citizen(name,address,phone,email,city)values(?,?,?,?,?)", (
                task_name, task_address, task_phone, task_email, task_city))  # Registering user info into DB
            con.commit()  # commiting the changes

            flash("Record Added  Successfully", "success")

        except:
            flash("Error in Insert Operation", "danger")
        finally:
            return redirect(url_for("index"))
            con.close()
    else:
        pass

    return render_template('citizen.html')


@app.route('/owner', methods=['POST', 'GET'])
def owner():
    if request.method == 'POST':
        try:
            task_name = request.form['name']
            task_address = request.form['address']
            task_phone = request.form['phone']
            task_email = request.form['email']

            con = sqlite3.connect("database.db")
            cur = con.cursor()
            cur.execute("insert into owner(name,address,phone,email)values(?,?,?,?)", (
                task_name, task_address, task_phone, task_email))  # inserting user info into DB

            con.commit()

            # Data to fill the qr code
            qr_data = task_name + " " + task_address + " " + task_phone + " " + task_email
            # Call the function to generate the qr code
            img = generate_qr_code(qr_data, cur.lastrowid)
            # BytesIO object
            byte_io = BytesIO()
            img.save(byte_io, 'PNG')
            byte_io.seek(0)

            # Return the qr code as a png image
            return send_file(byte_io, mimetype='image/png')

        except:
            flash("Error in Insert Operation", "danger")
        finally:
            con.close()

    else:
        pass

    return render_template('owner.html')


@app.route('/agent', methods=["GET", "POST"])
def agent():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        con = sqlite3.connect("database.db")  # connection with database
        cursor = con.cursor()
        query = "SELECT username, password FROM Agent WHERE username = '{u}' AND password = '{p}'".format(
            u=username, p=password)  # Checking username and password with database
        rows = cursor.execute(query)
        rows = rows.fetchall()
        if(len(rows) >= 1):  # if something is found with matching username and password succesfully logs in!
            return render_template('success.html')
        else:
            return 'Wrong username or password'
    return render_template("agent.html")


@app.route('/hospital', methods=["GET", "POST"])
def hospital():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        con = sqlite3.connect("database.db")  # connection with database
        cursor = con.cursor()
        query = "SELECT username, password FROM Hospital WHERE username = '{u}' AND password = '{p}'".format(
            u=username, p=password)  # Same logic as agent login
        rows = cursor.execute(query)
        rows = rows.fetchall()
        if(len(rows) >= 1):
            return render_template('success.html')
        else:
            return 'Wrong username or password'
    return render_template("hospital.html")


if __name__ == "__main__":
    app.run(debug=True)
