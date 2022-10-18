#from typing_extensions import Self
from flask import session
from CoronaArchieve import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id):
    if Visitor.query.filter_by(id=id):
        return Visitor.query.filter_by(id=id).first()
    elif Place.query.filter_by(place_id=id):
        return Place.query.filter_by(place_id=id).first()
    elif Hospital.query.filter_by(hospital_ID=id):
        return Hospital.query.filter_by(hospital_ID=id).first()
    elif Agent.query.filter_by(agent_ID=id).first():
        return Agent.query.filter_by(agent_ID=id).first()


class Visitor(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    visitor_name = db.Column(db.String(40), nullable=False)
    visitor_phone_number = db.Column(db.Integer, nullable=False)
    visitor_email = db.Column(db.String(40), nullable=False)
    visitor_password = db.Column(db.String(60), nullable=False)
    visitor_address = db.Column(db.String(40))
    is_infected = db.Column(db.Boolean)
    device_ID = db.Column(db.String(60), unique=True)

    def is_authenticated(self):
        return True

    def __repr__(self):
        return f"User('{self.id}','{self.visitor_name}')"

    def get_id(self):
        return self.id


class Place(db.Model, UserMixin):
    place_id = db.Column(db.Integer, primary_key=True)
    place_name = db.Column(db.String(40), nullable=False)
    place_address = db.Column(db.String(40))
    qr_code = db.Column(db.String(40))
    place_username = db.Column(db.String(40), nullable=False)
    place_password = db.Column(db.String(60), nullable=False)

    def is_authenticated(self):
        return True

    def __repr__(self):
        return f"Place('{self.place_id}','{self.place_name}')"

    def get_id(self):
        return self.place_id


class PlaceCenter:
    PlaceList = []

    def __init__(self, List):
        self.PlaceList = List

    def AddNewPlace(place_id):
        if(place_id in PlaceCenter.PlaceList):
            return False
        PlaceCenter.PlaceList.append(place_id)
        return True

    # check if certain place is valid by checking if its in the list
    def Check_Place_Valid(place_id):
        if(place_id in PlaceCenter.PlaceList):
            return True
        else:
            return False


class Hospital(db.Model, UserMixin):
    hospital_ID = db.Column(db.Integer, unique=True)
    hospital_username = db.Column(
        db.String(40), nullable=False, primary_key=True)
    hospital_password = db.Column(db.String(60), nullable=False)

    def is_authenticated(self):
        return True

    def __repr__(self):
        return f"Place('{self.hospital_ID}','{self.hospital_username}')"

    def get_id(self):
        return self.hospital_ID


class HospitalCenter:
    HospitalList = []

    def __init__(self, List):
        self.HospitalList = List

    def AddNewHospital(hospital_ID):
        if(hospital_ID in HospitalCenter.HospitalList):
            return False
        HospitalCenter.HospitalList.append(hospital_ID)
        return True

    # check if certain hosptial is valid by checking if its in the list
    def Check_Hospital_Valid(hospital_ID):
        if(hospital_ID in HospitalCenter.HospitalList):
            return True
        else:
            return False


class Agent(db.Model, UserMixin):
    agent_ID = db.Column(db.Integer, primary_key=True)
    agent_username = db.Column(db.String(40), nullable=False, unique=True)
    agent_password = db.Column(db.String(60), nullable=False)

    def is_authenticated(self):
        return True

    def __repr__(self):
        return f"Place('{self.agent_ID}','{self.agent_username}')"

    def get_id(self):
        return self.agent_ID
