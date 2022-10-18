import base64
from io import BytesIO
import qrcode
import sqlite3
from flask import Flask, render_template, request, url_for, redirect, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from views import auth
from views import agency
from views import hospital
import os
from os.path import join, dirname, realpath


# Create a flask instance
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/uploads/qrcodes')
app.secret_key = "superSecretKey"
app.config['UPLOAD_FOLDER'] = UPLOADS_PATH


# connect to sqlite database in SQL folder
database = "coronaArchive.db"


# Login Route
app.add_url_rule('/login', methods=('GET', 'POST'), view_func=auth.login)

# Logout Route
app.add_url_rule('/logout', methods=('GET', 'POST'), view_func=auth.logout)

# Agency Visior Info Route
app.add_url_rule('/visitor_info', methods=('GET',),
                 view_func=agency.visitorinfo)

# Agency Visior Info Route
app.add_url_rule('/visitor_info', methods=('GET',),
                 view_func=agency.visitorinfo)


# Agency Place Info Info Route
app.add_url_rule('/place_info', methods=('GET',), view_func=agency.placeinfo)


# Agency Hospital Registration Reoute Info Info Route
app.add_url_rule('/hospital_registration', methods=('GET', 'POST'),
                 view_func=agency.hospital_registration)

#  Hospital Visitor View
app.add_url_rule('/hospital_visitor', methods=('GET',),
                 view_func=hospital.hospital_visitor)

app.add_url_rule('/change_corona_status', methods=('POST',),
                 view_func=hospital.change_corona_status)


def generate_qr(id):
    img = qrcode.make(id)
    filename = f'qr{id}.png'
    img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


#  Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Removes any existing flash messages which may be carried over from redirects
    session.pop('_flashes', None)

    # establish a connection with database
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    # execute query and get all responces as a list. Example: [(1, 'bob', 'password123', 'Bob@bob', 'Chicago', 'somePhoneNum', 0), (2, 'Joe', 'password5678', 'joe@email.com', 'New York', 'somePhoneNum', 0) ]
    # users = cursor.execute("SELECT * FROM Visitors").fetchall()
    # for user in users:
    # index to get the first element, (example, as seen below: so to get the users primary key, use index 0)
    # app.logger.info(user[0])

    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        city = request.form['city']
        password = request.form['password']
        hashedPassword = generate_password_hash(password)
        userType = request.form['userType']

        # app.logger.info('usertype: ', userType)
        # app.logger.info('usertype: %s', userType)
        # app.logger.info('hashedPassword: %s', hashedPassword)

        # Make sure order of params is the same as the order of columns in database
        if userType == 'visitor':
            # Test if user already exists in database, if not, then flash error message on template
            existingUser = cursor.execute(
                f"SELECT * FROM Visitors WHERE email='{email}'").fetchone()
            # app.logger.info("existing user: ")
            # app.logger.info(existingUser)

            if existingUser:
                flash("User already exists.")

            else:
                params = (name, hashedPassword, address, city, phone,
                          email, "0")
                # NULL is placeholder for primary key
                cursor.execute(
                    "INSERT INTO Visitors VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)", params)

                connection.commit()
                flash("Successfully registered!")

                newVisitor = cursor.execute(
                    f"SELECT * FROM Visitors WHERE email='{email}'").fetchone()
                session['userId'] = newVisitor[0]
                session['userType'] = 'Visitors'

                return redirect(url_for('index'))

        elif userType == 'place':
            existingUser = cursor.execute(
                f"SELECT * FROM Places WHERE email='{email}'").fetchone()
            # app.logger.info("existing user: ")
            # app.logger.info(existingUser)
            if existingUser:
                flash("User already exists.")

            else:
                params = (name, hashedPassword, address, phone,
                          email, "none")
                cursor.execute(
                    "INSERT INTO Places VALUES (NULL, ?, ?, ?, ?, ?, ?)", params)
                # Commit insert statments to the database
                connection.commit()

                # Get ID of the new place
                newPlace = cursor.execute(
                    f"SELECT * FROM Places WHERE email='{email}'").fetchone()

                # Generate QR code for the new place
                generate_qr(newPlace[0])

                session['userId'] = newPlace[0]
                session['userType'] = 'Places'

                flash("Successfully registered!")
                return redirect(url_for('show_qrcode'))

        elif userType == 'agency':
            existingUser = cursor.execute(
                f"SELECT * FROM Agency WHERE name='{name}'").fetchone()
            # app.logger.info("existing user: ")
            # app.logger.info(existingUser)
            if existingUser:
                flash("User already exists.")

            else:
                params = (name, hashedPassword)
                cursor.execute(
                    "INSERT INTO Agency VALUES (NULL, ?, ?)", params)
                connection.commit()
                flash("Successfully registered!")

    return render_template("register.html")


# Renders homepage
@app.route('/')
def index():
    app.logger.info("TESTING if userid exists")
    app.logger.info(session.get('userId'))
    if 'userId' in session:
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        # Obtain logged in user's attributes from database
        loggedInUser = cursor.execute(
            f"SELECT name FROM {session.get('userType')} WHERE id='{session.get('userId')}'").fetchone()
        app.logger.info("FETCHED USER: ")
        app.logger.info(loggedInUser[0])
        return render_template("index.html", userName=loggedInUser[0])
    else:
        return render_template("try.html")

# Renders '404.html' error page whenever URL is not found

# Show QRCODe by Aayush


@app.route('/qrcode', methods=['GET', 'POST'])
def show_qrcode():
    usertype = session.get('userType')
    if usertype != 'Places':
        flash("SORRY NOT AUTHORIZED")
        return redirect(url_for('login'))
    if 'userId' in session:
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        # Obtain logged in user's attributes from database
        loggedInUser = cursor.execute(
            f"SELECT * FROM {session.get('userType')} WHERE id='{session.get('userId')}'").fetchone()

        #  Get User Id
        userIdString = str(loggedInUser[0])
        return render_template("qr_viewer.html", userIdString=userIdString)
    else:
        flash("You need to login to access the homegoit page.")


@app.route('/generate_qrcode', methods=['GET', 'POST'])
def generate_qrcode():
    submitted = False
    qr_value = session.get('userId')
    img = qrcode.make(qr_value)
    data = BytesIO()
    img.save(data, "JPEG")
    encoded_img_data = base64.b64encode(data.getvalue())
    # if request.method == "POST":
    #     qr_value = request.form["data"]
    # #    qr_value = "test_data"
    #     img = qrcode.make(qr_value)
    #     # img.save('recent_qrcode.png')
    #     data = BytesIO()
    #     img.save(data, "JPEG")
    #     encoded_img_data = base64.b64encode(data.getvalue())
    #     submitted = True
    # if submitted:
    #     return render_template('qrcode_generator.html', image_data=encoded_img_data.decode('utf-8'))
    return render_template('qrcode_generator.html', image_data=encoded_img_data.decode('utf-8'))
    # qr_value = "test_data"
    # img = qrcode.make(qr_value)
    # img.save('recent_qrcode.png')
    # data = BytesIO()
    # img.save(data, "JPEG")
    # encoded_img_data = base64.b64encode(data.getvalue())

    # return render_template('qrcode_generator.html', image_data = encoded_img_data.decode('utf-8'))

@app.route('/imprint', methods=['GET', 'POST'])
def imprint():
    return render_template('imprint.html')
  

@app.route('/scan_qrcode', methods=['GET', 'POST'])
def scan_qrcode():
    if 'userId' in session:
        return render_template('scan_qrcode.html')
    else:
        flash("You need to Login or Register to access QR scan.")
        return redirect(url_for('login'))

# if 'userId' in session:
#         connection = sqlite3.connect(database)
#         cursor = connection.cursor()
#         # Obtain logged in user's attributes from database
#         loggedInUser = cursor.execute(
#             f"SELECT name FROM {session.get('userType')} WHERE id='{session.get('userId')}'").fetchone()
#         app.logger.info("FETCHED USER: ")
#         app.logger.info(loggedInUser[0])
#         return render_template("index.html", userName=loggedInUser[0])
#     else:
#         return render_template("try.html")


@app.route('/try')
def try_page():
    return render_template('try.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":  # enable hot reload and specify port to run on
    app.run(port=8000, debug=True)
