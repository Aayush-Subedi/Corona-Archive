from re import template
from CoronaArchieve.errors.handlers import errors
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
import sqlite3
from flask_selfdoc import Autodoc
import os
import json
import datetime


import qrcode
import secrets

templatesLocation = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), 'CoronaArchieve', 'templates')
staticLocation = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), 'CoronaArchieve', 'static')
app = Flask(__name__, template_folder=templatesLocation,
            static_folder=staticLocation)
auto = Autodoc(app)

# secrete key for sessions in flask
app.config['SECRET_KEY'] = os.urandom(64).hex()


# setting path for qr codes
location = os.path.dirname(os.path.realpath(__file__))
app.config.update(
    UPLOAD_PATH=os.path.join(location, "CoronaArchieve", "static")
)

app.register_blueprint(errors)


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("db.sqlite")
    except sqlite3.error as e:
        # catch error if can't connect to database
        print(e)
    return conn


def get_users():
    # connect to database and execute select statement
    conn = db_connection()
    cursor = conn.cursor()
    visitors = cursor.execute("SELECT * FROM Visitor").fetchall()

    # create list and for each row create a dictionary to be sent
    returnVisitors = []
    for row in visitors:
        completeRow = dict(id=row[0], name=row[1], address=row[2], city=row[3], phoneNumber=row[4], email=row[5],
                           device_ID=row[6], infected=row[7])
        returnVisitors.append(completeRow)

    return returnVisitors


# ======================================================================
# Gerneral pages and logged in


@app.route("/", methods=['GET', 'POST'])
@auto.doc()
def index():
    userType = session.get('userType')
    if(userType == 'Hospital'):
        return redirect(url_for('dashboard_hospital'))
    elif(userType == 'Visitor'):
        return redirect(url_for('scan_qrcode'))
    elif(userType == 'Agent'):
        return redirect(url_for('dashboard_agent'))
    elif(userType == 'Place'):
        return redirect(url_for('place_dashboard'))
    else:
        return render_template("index.html")


@app.route("/agent", methods=['GET', 'POST'])
def agent_login():

    if request.method == 'POST':
        session.pop("username", None)
        session.pop("userType", None)

        username = request.form["username"]
        password = request.form["password"]
        conn = db_connection()

        print("Logging in as Agent:\nUsername: {}\nPassword: {}".format(
            password, username))

        sql_agent = "SELECT username,password from Agent"
        agents = conn.execute(sql_agent).fetchall()

        # Format:
        # [('Agent_username', 'agent_password'), ('Agent_username2', 'agent_password2')]

        # go through all agents and check credentials
        for agent in agents:
            if(username == agent[0] and password == agent[1]):

                session['username'] = username
                session['userType'] = 'Agent'

                print("Logged in as agent")
                return redirect(url_for('dashboard_agent'))

        flash("Invalid credentials. Please check your credentials and try again.")
        return render_template("agent_login.html")
    else:
        return render_template("agent_login.html")


@app.route("/hospital", methods=["GET", "POST"])
def hospital_login():
    if request.method == 'POST':
        session.pop("username", None)
        session.pop("userType", None)

        username = request.form["username"]
        password = request.form["password"]
        conn = db_connection()

        print("Logging in as Hospital with:\nUsername: {}\nPassword: {}".format(
            password, username))

        sql_hospital = "SELECT username,password,is_verified from Hospital"
        hospitals = conn.execute(sql_hospital).fetchall()

        # Format
        # [('Agent_username', 'agent_password'), ('Agent_username2', 'agent_password2')]

        # go through all hospitals and check credentials
        for hopsital in hospitals:
            if(username == hopsital[0] and password == hopsital[1]):
                if(hopsital[2] == 0):
                    flash("Your account is not verified. Please contact the admin.")
                    return render_template("hospital_login.html")

                session['username'] = username
                session['userType'] = 'Hospital'

                print("Logged in as hopsital")
                return redirect(url_for('dashboard_hospital'))

        flash("Invalid credentials. Please check your credentials and try again.")
        return render_template("hospital_login.html")

    return render_template("hospital_login.html")


# =====================================================================================
# register users

@app.route("/reg_visitor", methods=["GET", "POST"])
@auto.doc()
def visitor_registration():

    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "POST":
        name = request.form["name"]
        address = request.form["address"]
        city = request.form["city"]
        phoneNumber = request.form["phoneNumber"]
        email = request.form["email"]
        password = request.form["password"]

        device_ID = os.urandom(32).hex()
        infected = 0
        sql = """INSERT INTO Visitor (name,address, city, phoneNumber, email, device_ID,infected,password)
                 VALUES (?,?, ?, ?, ?, ?,?,?)"""
        cursor = cursor.execute(
            sql, (name, address, city, phoneNumber, email, device_ID, infected, password))
        conn.commit()

        # Find User Id
        cursor.execute(
            "SELECT id from Visitor WHERE email=?", (email,))
        user_id = cursor.fetchone()[0]

        session['username'] = email
        session['userId'] = user_id
        session['userType'] = 'Visitor'
        return redirect(url_for('scan_qrcode'))

    else:
        return render_template("visitor_registration.html")


@app.route("/log_visitor", methods=["GET", "POST"])
@auto.doc()
def visitor_login():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        sql_visitor = "SELECT email,password,id from Visitor"
        visitors = conn.execute(sql_visitor).fetchall()
        passwordMatch = False
        for visitor in visitors:
            if(email == visitor[0] and password == visitor[1]):

                session['username'] = email
                print(visitor[2])
                session['userId'] = visitor[2]
                session['userType'] = 'Visitor'
                passwordMatch = True
                break

        if passwordMatch:
            return redirect(url_for('scan_qrcode'))

        else:
            flash("Invalid credentials. Please check your credentials and try again.")
            return render_template("log_visitor.html")

    else:
        return render_template("log_visitor.html")


@app.route("/reg_hospital", methods=["GET", "POST"])
@auto.doc()
def hospital_registration():
    if('username' in session and str(session['userType']) == "Agent"):
        conn = db_connection()
        cursor = conn.cursor()
        if request.method == "POST":
            name = request.form["name"]
            username = request.form["username"]
            password = request.form["pass"]
            sql = """INSERT INTO Hospital (name,username, password)
                    VALUES (?,?, ?)"""
            cursor = cursor.execute(
                sql, (name, username, password))
            conn.commit()
            return redirect(url_for('dashboard_agent'))
        else:
            return render_template("hospital_registration.html")
    else:
        flash("You are not authorized to register hospital")
        return redirect(url_for('index'))


@app.route("/log_place", methods=["GET", "POST"])
@auto.doc()
def place_login():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        sql_visitor = "SELECT email,password,id from Place"
        visitors = conn.execute(sql_visitor).fetchall()
        print(visitors)
        for visitor in visitors:
            if(email == visitor[0] and password == visitor[1]):

                session['username'] = email
                session['userType'] = 'Place'
                session['userId'] = visitor[2]
                print("Logged in as Visitor")
                return redirect(url_for('place_dashboard'))

        flash("Invalid credentials. Please check your credentials and try again.")
        return render_template("log_place.html")

    else:
        return render_template("log_place.html")


@app.route("/reg_place", methods=["GET", "POST"])
# nopep8
@auto.doc()
def locale_registration():
    # if method post is used we input data into database
    if(request.method == "POST"):
        # grab data from html
        name = request.form["name"]
        address = request.form["address"]
        phoneNumber = request.form["phoneNumber"]
        email = request.form["email"]
        password = request.form["password"]

        # connect to database, create cursor, execute sql, and return message
        conn = db_connection()
        cursor = conn.cursor()
        sql = """INSERT INTO Place (name,address,phoneNumber,email,password)
                 VALUES (?,?,?,?,?)"""
        cursor = cursor.execute(
            sql, (name, address, phoneNumber, email, password))
        conn.commit()
        session['userType'] = 'Place'

        # Find Id of the inserted row
        sql_id = "SELECT id from Place WHERE email = ?"
        cursor = cursor.execute(sql_id, (email,))
        id = cursor.fetchone()[0]
        session['userId'] = id

        qrcode_image_name = f"{id}.png"
        image_path = f"{app.config['UPLOAD_PATH']}/{qrcode_image_name}"
        try:
            place_qrcode = qrcode.make(str(id))
            place_qrcode.save(image_path)
        except Exception as excep:
            print(excep)

        return redirect(url_for('place_dashboard'))
        # return render_template("place_dashboard.html", image=qrcode_image_name)

    else:
        return render_template("place_registration.html")

# =====================================================================================
# log user our by popping their sessions


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('userType', None)
    session.pop('userId', None)
    return redirect(url_for('index'))


# ======================================================================================================
# dashboards

@app.route("/dashboard_agent")
def dashboard_agent():

    # if user logged in then ONLY as Agent allow to dashboard
    if('username' in session and str(session['userType']) == "Agent"):
        # return agent data on users

        return render_template("dashboard_agent.html", value={"visitors": get_users()})
    else:
        # if user not logged in return to index page
        flash("You are not authorized to access Agent Dashboard")
        return redirect(url_for('index'))


@app.route("/dashboard_hospital")
def dashboard_hospital():
    # if user logged in then ONLY as hopsital allow to dashboard
    if('username' in session and str(session['userType']) == "Hospital"):
        return render_template("dashboard_hospital.html")
    else:
        # if user not logged successfully in return to index page
        flash("You are not authorized to access hospital dashboard")
        return redirect(url_for('index'))

# route to redirect user to scan a qr code


@app.route("/scan_qrcode")
def scan_qrcode():
    # Get User Id from session
    if('username' in session and str(session['userType']) == "Visitor"):
        user_id = session.get('userId')
        print(user_id)
        if user_id == None:
            return redirect(url_for('visitor_login'))

        conn = db_connection()
        cursor = conn.cursor()
        not_exited_place = cursor.execute(
            "SELECT * from Visitor_Place WHERE visitor_id=? and exit_time is null", (user_id,)).fetchone()

        # Get Current User
        current_user = cursor.execute(
            "SELECT * from Visitor WHERE id=?", (user_id,)).fetchone()


        print(not_exited_place)
        # Not Exited Place
        if (not_exited_place and len(not_exited_place) > 0):
            # FInd Place name with id
            place_id = not_exited_place[2]
            print(place_id)
            place_name = cursor.execute(
                "SELECT name from Place WHERE id=?", (place_id,)).fetchone()[0]
            return render_template("scan_qrcode.html", remaining_place=json.dumps(not_exited_place), place_name=place_name, session=session)

        return render_template("scan_qrcode.html", has_corona=current_user[7])
    else:
        flash("You are not authorized to scan")
        return redirect(url_for('index'))


# route to redirect user to timer
@app.route("/timer")
def timer():
    return render_template("visitor_timer.html")


@app.route("/place_dashboard")
def place_dashboard():
    if('userId' in session and str(session['userType']) == "Place"):
        # Generate QR Code and send to place
        user_id = session.get('userId')
        print(user_id)
        if user_id == None:
            return redirect(url_for('place_login'))

        qrcode_image_name = f"{user_id}.png"
        image_path = f"{app.config['UPLOAD_PATH']}/{qrcode_image_name}"
        try:
            place_qrcode = qrcode.make(str(user_id))
            place_qrcode.save(image_path)
        except Exception as excep:
            print(excep)

        return render_template("place_dashboard.html", image=qrcode_image_name)

    else:
        flash("You are not authorized to access place dashboard")
        return redirect(url_for('index'))


@app.route("/searchvisitor", methods=['GET', 'POST'])
def searchvisitor():

    if('username' in session and str(session['userType']) == "Agent"):
        conn = db_connection()
        cursor = conn.cursor()
        if request.method == "POST":
            book = request.form['book']
            # search by author or book
            cursor.execute("SELECT * from Visitor WHERE name=?", (book,))

            data = cursor.fetchone()

            return render_template('search_visitor.html', data=data)
        return render_template("search_visitor.html")
    else:
        flash("You are not authorized to search")
        return redirect(url_for('index'))


@app.route("/searchplace", methods=['GET', 'POST'])
def searchplace():
    if('username' in session and str(session['userType']) == "Agent"):
        conn = db_connection()
        cursor = conn.cursor()
        if request.method == "POST":
            book = request.form['book']
            # search by author or book
            cursor.execute("SELECT * from Place WHERE name=?", (book,))

            data = cursor.fetchall()

            return render_template('search_place.html', data=data)
        return render_template("search_place.html")
    else:
        flash("You are not authorized to search")
        return redirect(url_for('index'))


@app.route("/searchpatient", methods=['GET', 'POST'])
def searchpatient():
    if('username' in session and str(session['userType']) == "Hospital"):
        conn = db_connection()
        cursor = conn.cursor()
        if request.method == "POST":
            book = request.form['book']
            # search by author or book
            cursor.execute("SELECT * from Visitor WHERE name=?", (book,))

            data = cursor.fetchall()

            return render_template('search_patient.html', data=data)
        return render_template("search_patient.html")
    else:
        flash("You are not authorized to search")
        return redirect(url_for('index'))


@app.route("/scan_place", methods=['POST', ])
def visitor_scan_qrcode():
    records = json.loads(request.data)

    placeId = records['placeId']
    visitorId = records['userId']
    entryTime = records['entryTime']

    # Insert into database
    conn = db_connection()
    cursor = conn.cursor()

    sql = """INSERT INTO Visitor_Place (visitor_id,place_id,entry_time)
                 VALUES (?,?,?)"""
    cursor = cursor.execute(
        sql, (visitorId, placeId, entryTime))
    conn.commit()

    return jsonify({"status": "success"})


@app.route("/exit_place", methods=['POST', ])
def visitor_exit_place():
    if('username' in session and str(session['userType']) == "Visitor"):
        records = json.loads(request.data)

        vis_place_id = records['id']
        exittime = records['exitTime']

        # insert into database
        conn = db_connection()
        cursor = conn.cursor()

        sql = """update visitor_place set exit_time=? where id=?"""
        cursor = cursor.execute(
            sql, (exittime, vis_place_id))
        conn.commit()

        return jsonify({"status": "success"})
    else:
        flash("You are not authorized to access Visitor content")
        return redirect(url_for('index'))


@app.route("/agent/places", methods=['GET', ])
def agent_list_places():
    if('username' in session and str(session['userType']) == "Agent"):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id,name,address,phoneNumber,email from Place")
        data = cursor.fetchall()
        print(data)

        return render_template('place_info.html', places=data)
    else:
        flash("You are not authorized to access hospital dashboard")
        return redirect(url_for('index'))


@app.route("/agent/visitors", methods=['GET', ])
def agent_list_visitors():
    if('username' in session and str(session['userType']) == "Agent"):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id,name,address,city,phoneNumber,email,infected from Visitor")
        data = cursor.fetchall()
        print(data)

        return render_template('visitor_info.html', visitors=data)
    else:
        flash("You are not authorized to access agent's content")
        return redirect(url_for('index'))


@app.route("/agent/visitor_place", methods=['GET', ])
def agent_list_visitor_place():
    if('username' in session and str(session['userType']) == "Agent"):
        conn = db_connection()
        cursor = conn.cursor()
        # Join visitor and place table with visitor_place
        # cursor.execute("SELECT  v.name,p.name,vp.entry_time,vp.exit_time FROM Visitor_Place vp INNER JOIN Visitor v ON v.id=vp.visitor_id INNER JOIN Place p ON p.id=vp.place_id")
        cursor.execute(
            "SELECT v.name, p.name, vp.entry_time, vp.exit_time FROM Visitor_Place vp INNER JOIN Visitor v ON v.id = vp.visitor_id INNER JOIN Place p ON p.id=vp.place_id")
        data = cursor.fetchall()
        print(data)

        return render_template('visitor_place.html', data=data)
    else:
        flash("You are not authorized to access agent's content")
        return redirect(url_for('index'))


@app.route('/hospital/visitor', methods=['GET', ])
def hospital_visitor_list():
    if('username' in session and str(session['userType']) == "Hospital"):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id,name,address,city,phoneNumber,email,infected from Visitor")
        data = cursor.fetchall()

        return render_template('hospital_visitor_info.html', visitors=data)
    else:
        flash("You are not authorized to view this page")
        return redirect(url_for('index'))


@app.route('/change_corona_status', methods=['POST', ])
def change_corona_status():
    if('username' in session and str(session['userType']) == "Hospital"):
        conn = db_connection()
        cursor = conn.cursor()
        visitorId = request.form['visitorId']
        coronaStatus = request.form['coronaStatus']
        isVisitorExist = cursor.execute(
            f"SELECT * FROM Visitor WHERE id='{visitorId}'").fetchone()

        if isVisitorExist:
            cursor.execute(
                f"UPDATE Visitor SET infected='{coronaStatus}' WHERE id='{visitorId}'")
            conn.commit()
        else:
            print("error")

        return redirect(url_for('hospital_visitor_list'))
    else:
        flash("You are not authorized to chanage corona status")
        return redirect(url_for('hospital_visitor_list'))


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


@app.route('/docs')
def documentation():
    return auto.html(title='Corona Archive API Documentation')


@app.route('/imprint')
def imprint():
    return render_template("imprint.html")


def search():
    conn = db_connection()
    cursor = conn.cursor()
    name = request.form['name']
    # search by name
    cursor.execute("SELECT * from Visitor WHERE name=?", (name,))
    data = cursor.fetchall()
    return data


@app.route('/hospital/request', methods=['GET', 'POST'])
def request_hospital_registration():
    if request.method == 'POST':
        conn = db_connection()
        cursor = conn.cursor()
        name = request.form['name']
        address = request.form['username']
        password = request.form['pass']
        cursor.execute("INSERT INTO Hospital(name,username,password,is_verified) VALUES(?,?,?,0)",
                       (name, address, password))
        conn.commit()
        flash("Your request has been sent to admin. You can access once your request is approved.")
        return redirect(url_for('index'))
    return render_template('request_reg.html')


@app.route('/hospital/request/verify', methods=['GET', 'POST'])
def verify_hospital_registration():
    usertype = session.get('userType')
    if usertype != 'Agent':
        flash("SORRY NOT AUTHORIZED")
        return redirect(url_for('index'))
    if request.method == 'POST':
        conn = db_connection()
        cursor = conn.cursor()
        hospitalId = request.form['hospitalId']
        hospitalStatus = request.form['hospitalStatus']
        print(hospitalStatus)
        print(int(hospitalStatus) == 0)

        if (int(hospitalStatus) == 0):
            cursor.execute(
                f"DELETE FROM Hospital WHERE id={hospitalId}")
            conn.commit()
            flash("Hospital request has been rejected")
            return redirect(url_for('verify_hospital_registration'))

        else:
            cursor.execute(
                "UPDATE Hospital SET is_verified=1 WHERE id=?", (hospitalId,))

        conn.commit()
        flash("Hospital Request has been approved")
        return redirect(url_for('verify_hospital_registration'))

    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Hospital WHERE is_verified=0")
    data = cursor.fetchall()
    return render_template('verify_hospital.html', data=data)


# if __name__ == "__main__":
if __name__ == "__main__":
    app.run(debug=True, port=5000)
