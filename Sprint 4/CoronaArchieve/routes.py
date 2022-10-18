from crypt import methods
from flask import render_template, session, url_for, flash, redirect
from CoronaArchieve.models import Visitor, Place, Agent, Hospital
from CoronaArchieve.forms import RegistrationForm, VisitorsLoginForm, AddHospitalForm, PlaceRegistrationForm, PlaceLoginForm, AgentLoginForm, HospitalLoginForm
from CoronaArchieve import app, db, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
import secrets
import qrcode

# routes for index page


@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html', title='Home')


@app.route('/logout')  # route to send to logout a user
def logout():
    session['UserType'] = 'Nooneloggedin'
    logout_user()
    return redirect(url_for('home'))


# registration and login for visitor
@app.route('/visitor', methods=['GET', 'POST'])
def visitor():
    # if user is authenticated, then send them to dashboard
    if current_user.is_authenticated:
        return redirect(url_for('user_dashboard'))

    form1 = VisitorsLoginForm()
    form2 = RegistrationForm()

    # if user has submitted a valid signup form
    if form2.validate_on_submit():

        # generate a hashed password
        hasshed_pwd = bcrypt.generate_password_hash(
            form2.password.data).decode('utf-8')

        # create a new visitor and add them to the database
        visitor = Visitor(id=form2.id.data,
                          visitor_name=form2.name.data,
                          visitor_phone_number=form2.phone_number.data,
                          visitor_email=form2.email.data,
                          visitor_password=hasshed_pwd,
                          visitor_address=form2.address.data
                          )
        db.session.add(visitor)
        db.session.commit()

        # notify user that they have have had a new account created and redirect them to login page
        flash(
            f'Account created for {form2.name.data}! You can now login.', 'success')
        return redirect(url_for('visitor'))

    # if user has submitted login form
    elif form1.validate_on_submit():

        # query for visitor in database and check if passwords match
        visitor = Visitor.query.filter_by(id=form1.id.data).first()
        if visitor and bcrypt.check_password_hash(visitor.visitor_password, form1.password.data):

            # if does match, log in and set session
            session['UserType'] = "Visitor"
            login_user(visitor, remember=form1.remember.data)

            # send to dashboard
            return redirect(url_for('user_dashboard'))

        else:
            # if unsuccessful, then send alert
            flash('Login Unsuccessful. Please try again', 'danger')

    return render_template('user_registration_login.html', title='Visitor', form1=form1, form2=form2)


@app.route('/user_dashboard')  # user dashboard
def user_dashboard():
    return render_template('user_dashboard.html')


@app.route('/place_dashboard')  # place dashboard
def place_dashboard():
    return render_template('place_home.html')


# registration and login for place
@app.route('/place', methods=['GET', 'POST'])
def place():

    # if user is authenticated send them to dashboard
    if current_user.is_authenticated:
        return redirect(url_for('place_dashboard'))

    form1 = PlaceLoginForm()
    form2 = PlaceRegistrationForm()

    # if form 2, sign up, is sent, decode values, and create a required values to be stored in database
    if form2.validate_on_submit():
        hasshed_pwd = bcrypt.generate_password_hash(
            form2.password.data).decode('utf-8')

        data1 = form2.username.data
        qrcode_image_name = f"{secrets.token_hex(10)}.png"
        image_path = f"{app.config['UPLOAD_PATH']}/{qrcode_image_name}"

        # try to create qrcode
        try:
            place_qrcode = qrcode.make(str(data1))
            place_qrcode.save(image_path)
        except Exception as excep:
            print(excep)

        place = Place(
            qr_code=qrcode_image_name,
            place_name=form2.name.data,
            place_address=form2.address.data,
            place_username=form2.username.data,
            place_password=hasshed_pwd

        )

        db.session.add(place)
        db.session.commit()

        # alert user of success and send to site with qrcode
        flash(f'Account created for {form2.name.data}!', 'success')
        return render_template("place_dashboard.html", title="Place-dashboard", image=qrcode_image_name)

    # if user has attempted loggin in
    elif form1.validate_on_submit():
        place = Place.query.filter_by(
            place_username=form1.username.data).first()

        # compare value and password to hashed password
        if place and bcrypt.check_password_hash(place.place_password, form1.password.data):
            # if correct, update session and login user
            session['UserType'] = "Place"
            login_user(place, remember=form1.remember.data)

            image_name = place.qr_code

            # render template of home with qr code
            return render_template('place_home.html', title='QR Code', image=image_name)

        else:
            flash('Login Unsuccessful. Please try again', 'danger')

    # if no forms are submitted, GET request
    return render_template('place_registration_login.html', title='Place', form1=form1, form2=form2)


# agent login for place
@app.route('/agent', methods=['GET', 'POST'])
def agent():
    if current_user.is_authenticated:
        return redirect(url_for('agent_dashboard'))
    form1 = AgentLoginForm()
    if form1.validate_on_submit():
        agent = Agent.query.filter_by(
            agent_username=form1.username.data).first()
        if agent and bcrypt.check_password_hash(agent.agent_password, form1.password.data):
            session['UserType'] = "Agent"
            login_user(agent, remember=form1.remember.data)
            return redirect(url_for('addhospital'))
        else:
            flash('Login Unsuccessful. Please try again', 'danger')

    return render_template('agent_login.html', title='Agent', form1=form1)


# registration  for hospital
@app.route('/hospitalregistration', methods=['GET', 'POST'])
def addhospital():
    form = AddHospitalForm()
    # if form is submitted, register new hopsital and commit to database
    if form.validate_on_submit():
        hasshed_pwd = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')

        hospital = Hospital(
            hospital_username=form.username.data,
            hospital_password=hasshed_pwd)

        db.session.add(hospital)
        db.session.commit()

        # alert user of successfull registration and send to addhospital
        flash(
            f'Hospital with username: { form.username.data }  Added!', 'success')
        return redirect(url_for('addhospital'))

    #  if no form is submitted, then send to AgentDashboard with the form that is to be submitted
    return render_template('AgentDashboard.html', title='Agent Dashboard', form=form)


@app. route('/hospita_dashboard')  # hospita_dashboard once logged in
def hospital_dashboard():
    return render_template('hospital_dashboard.html')


@app.route('/hospital', methods=['GET', 'POST'])  # hospital login for place
def hospital():
    # if user is logged in, then send to home
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    # if form is submutted then attemp to log in
    form1 = HospitalLoginForm()
    if form1.validate_on_submit():
        hospital = Hospital.query.filter_by(
            hospital_username=form1.username.data).first()

        # check passwords with saved hashed version. If same, then login and se session
        if hospital and bcrypt.check_password_hash(hospital.hospital_password, form1.password.data):

            session['UserType'] = "Hospital"
            login_user(hospital, remember=form1.remember.data)
            # send to hospital_dashboard
            return redirect(url_for('hospital_dashboard'))

        #  if login unsuccessful notify user
        else:
            flash('Login Unsuccessful. Please try again', 'danger')

    # if no form submitted, then send back form to submit
    return render_template('hospital_login.html', title='Hospital', form1=form1)
