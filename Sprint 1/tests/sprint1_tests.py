
import os
import sys
import string
import random
import unittest

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from app import app

class FlaskTestCase(unittest.TestCase):
    # Please note that this test cases depend on your computer as well as well.
    # Checking home page
    def test_home_page(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type="html/text")
        self.assertIn(b'Home', response.data)

    # Checking Agent Page
    def test_agent_page(self):
        tester = app.test_client(self)
        response = tester.get('/agent', content_type="html/text")
        self.assertIn(b'Agent', response.data)

    # The login is successful for an agent
    def test_agent_login_successful(self):
        tester = app.test_client(self)
        response = tester.post(
            '/agent', data=dict(username="agent", password="123"), follow_redirects=True)
        self.assertIn(b'agent', response.data)

    # The login is not successful for incorrect credentials
    def test_agent_login_unsuccessful(self):
        tester = app.test_client(self)
        response = tester.post(
            '/agent', data=dict(username="wrong1", password="wrong"), follow_redirects=True)
        self.assertIn(b'Wrong username or password', response.data)

    # Checking Citizen Page
    def test_citizen_page(self):
        tester = app.test_client(self)
        response = tester.get('/citizen', content_type="html/text")
        self.assertIn(b'Citizen', response.data)

    # Citizen Registration
    def test_citizen_registration(self):
        tester = app.test_client(self)
        response = tester.post('/citizen', data=dict(name='hello', address="hii",
                               phone="9898098909", email="hello@hello.com", city="bremen"))
        self.assertIn(b'Redirecting', response.data)

    # Checking Owner Page

    def test_owner_page(self):
        tester = app.test_client(self)
        response = tester.get('/owner', content_type="html/text")
        self.assertIn(b'Owner', response.data)

    # Owner Registration
    def test_owner_registration(self):
        tester = app.test_client(self)
        response = tester.post('/owner', data=dict(name='Aayush', address="Jacobs",
                               phone="2312112", email="mymail@wmail.com"), follow_redirects=True)
        # Returns QR Code so using PNG
        self.assertIn(b'PNG', response.data)

    # Checking Hospial Page
    def test_hospital_page(self):
        tester = app.test_client(self)
        response = tester.get('/hospital', content_type="html/text")
        self.assertIn(b'hospital', response.data)

    # The login is not successful for incorrect credentials

    def test_hospital_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/hospital', data=dict(username="wrong1", password="wrong"), follow_redirects=True)
        self.assertIn(b'Wrong username or password', response.data)

    # The login is successful for a hospital
    def test_hospital_login_successful(self):
        tester = app.test_client(self)
        response = tester.post(
            '/hospital', data=dict(username="Foo", password="abc"), follow_redirects=True)
        self.assertIn(b'hospital', response.data)


if __name__ == '__main__':
    unittest.main()
