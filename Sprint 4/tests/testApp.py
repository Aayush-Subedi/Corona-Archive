import os
import sys
import unittest
import string
import random

# allow importing from other directory
this_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(this_dir)
sys.path.append(parent_dir)

# only import after
from run import app  # nopep8 (from https://stackoverflow.com/a/57067521)


# get random words for testing values. From: https://stackoverflow.com/a/2030081
def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


class TestCoronaApp(unittest.TestCase):
    # ===========================================================================
    # The following tests deal with getting data from the page

    # Test going to landing page
    def test_home_page(self):
        client = app.test_client(self)
        response = client.get(
            '/', content_type="html/text")
        self.assertIn(b'Corona Archieve', response.data)

    # ----------------------------------------------------------

    # registration pages

    def test_visitor_register_page(self):
        client = app.test_client(self)
        response = client.get(
            '/reg_visitor', content_type="html/text")
        self.assertIn(b'New user?', response.data)

    def test_register_locale_page(self):
        client = app.test_client(self)
        response = client.get(
            '/reg_place', content_type="html/text")
        self.assertIn(b'Place Owner?', response.data)

    # ----------------------------------------------------------

    # login pages

    def test_agent_login_page(self):
        client = app.test_client(self)
        response = client.get(
            '/agent', content_type="html/text")
        self.assertIn(b'Agent Login', response.data)

    def test_hospital_login_page(self):
        client = app.test_client(self)
        response = client.get(
            '/hospital', content_type="html/text")
        self.assertIn(b'Hospital Login', response.data)

    def test_visitor_login_page(self):
        client = app.test_client(self)
        response = client.get(
            '/log_visitor', content_type="html/text")
        self.assertIn(b'Visitor Login', response.data)

    def test_place_login_page(self):
        client = app.test_client(self)
        response = client.get(
            '/log_place', content_type="html/text")
        self.assertIn(b'Place Login', response.data)

    # ----------------------------------------------------------

    # testing failures if tried to access agents pages without logging in

    def test_agent_dashboard_failure(self):
        testingClient = app.test_client(self)
        response = testingClient.get(
            '/dashboard_agent', content_type="html/text")
        self.assertIn(b'Redirecting', response.data)
        self.assertIn(b'/', response.data)

    def test_agent_hospital_registration_failure(self):
        testingClient = app.test_client(self)
        response = testingClient.get(
            '/reg_hospital', content_type="html/text")
        self.assertIn(b'Redirecting', response.data)
        self.assertIn(b'/', response.data)

    def test_agent_visitor_info_failure(self):
        testingClient = app.test_client(self)
        response = testingClient.get(
            '/agent/visitors', content_type="html/text")
        self.assertIn(b'Redirecting', response.data)
        self.assertIn(b'/', response.data)

    def test_agent_place_ifo_failure(self):
        testingClient = app.test_client(self)
        response = testingClient.get(
            '/agent/places', content_type="html/text")
        self.assertIn(b'Redirecting', response.data)
        self.assertIn(b'/', response.data)

    def test_agent_visitor_place_time_info_failure(self):
        testingClient = app.test_client(self)
        response = testingClient.get(
            '/agent/visitor_place', content_type="html/text")
        self.assertIn(b'Redirecting', response.data)
        self.assertIn(b'/', response.data)

    # ----------------------------------------------------------

    # testing failures if tried to access visitor pages without logging in

    def test_visitor_scan_qrcode_failure(self):
        testingClient = app.test_client(self)
        response = testingClient.get(
            '/scan_qrcode', content_type="html/text")
        self.assertIn(b'Redirecting', response.data)
        self.assertIn(b'/', response.data)

    # ----------------------------------------------------------

    # testing failures if tried to access place owner pages without logging in

    def test_place_dashboard_failure(self):
        testingClient = app.test_client(self)
        response = testingClient.get(
            '/place_dashboard', content_type="html/text")
        self.assertIn(b'Redirecting', response.data)
        self.assertIn(b'/', response.data)

    # ----------------------------------------------------------

    # testing failures if tried to access place owner pages without logging in

    def test_hospital_dashboard_failure(self):
        testingClient = app.test_client(self)
        response = testingClient.get(
            '/dashboard_hospital', content_type="html/text")
        self.assertIn(b'Redirecting', response.data)
        self.assertIn(b'/', response.data)

    def test_hospital_visitor_info_failure(self):
        testingClient = app.test_client(self)
        response = testingClient.get(
            '/hospital/visitor', content_type="html/text")
        self.assertIn(b'Redirecting', response.data)
        self.assertIn(b'/', response.data)

    # ==================================================================================================

    # ----------------------------------------------------------

    # testing sucess if tried to access agents pages after logging in

    def test_agent_dashboard_page_success(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['userType'] = 'Agent'
                sess['userId'] = '1'
            response = c.get(
                '/dashboard_agent', content_type="html/text",)
            self.assertIn(b'Redirecting', response.data)

    def test_agent_hospital_registration_page_success(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['userType'] = 'Agent'
                sess['userId'] = '1'
            response = c.get(
                '/reg_hospital', content_type="html/text",)
            self.assertIn(b'Redirecting', response.data)

    def test_agent_visitor_information_page_success(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['userType'] = 'Agent'
                sess['userId'] = '1'
            response = c.get(
                '/agent/visitors', content_type="html/text",)
            self.assertIn(b'Redirecting', response.data)

    def test_agent_places_information_page_success(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['userType'] = 'Agent'
                sess['userId'] = '1'
            response = c.get(
                '/agent/places', content_type="html/text",)
            self.assertIn(b'Redirecting', response.data)

    def test_agent_visitor_place_time_info_success(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['userType'] = 'Agent'
                sess['userId'] = '1'
            response = c.get(
                '/agent/visitor_place', content_type="html/text",)
            self.assertIn(b'Redirecting', response.data)
    # ----------------------------------------------------------

    # testing success if tried to access visitor pages without logging in

    def test_visitor_scan_qrcode_success(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['userType'] = 'Visitor'
                sess['userId'] = '1'
            response = c.get(
                '/scan_qrcode', content_type="html/text",)
            self.assertIn(b'Redirecting', response.data)

    # ----------------------------------------------------------

    # testing success if tried to access place owner pages with logging in

    def test_place_dashboard__success(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['userType'] = 'Visitor'
                sess['userId'] = '1'
            response = c.get(
                '/place_dashboard', content_type="html/text",)
            self.assertIn(b'Redirecting', response.data)

    # ----------------------------------------------------------

    # testing success if tried to access hospital pages with logging in

    def test_hospital_dashboard_success(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['userType'] = 'Visitor'
                sess['userId'] = '1'
            response = c.get(
                '/dashboard_hospital', content_type="html/text",)
            self.assertIn(b'Redirecting', response.data)

    def test_hospital_visitor_info__success(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['userType'] = 'Visitor'
                sess['userId'] = '1'
            response = c.get(
                '/hospital/visitor', content_type="html/text",)
            self.assertIn(b'Redirecting', response.data)

    # ==================================================================================================
    # The following tests deal with posting data

    # Test registration of visitor with dummy info

    def test_register_visitor_post(self):
        testingClient = app.test_client(self)
        response = testingClient.post('/reg_visitor', data=dict(name=randomword(10), address="testAddress",
                                                                city="testCity", phoneNumber="123456789", email="test@email.com", password="test@123"), follow_redirects=True)
        self.assertIn(b'scan_qrcode', response.data)

    # Test registration of place with dummy info
    def test_register_locale_post(self):
        testingClient = app.test_client(self)
        response = testingClient.post("/reg_place", data=dict(name="test_name", address="Test st. 123",
                                                              phoneNumber="12345678", email="test@email.com", password="test@123"), follow_redirects=True)
        self.assertIn(b'place', response.data)

    # Test agent login
    def test_agent_login_post(self):
        testingClient = app.test_client(self)
        response = testingClient.post("/agent", data=dict(username="Sam", password="password123",
                                                          ), follow_redirects=True)
        self.assertIn(b'Welcome', response.data)

    # test hospital login
    def test_hospital_login_post(self):
        testingClient = app.test_client(self)
        response = testingClient.post("/hospital", data=dict(username="GrandVC", password="healthIsCool",
                                                             ), follow_redirects=True)
        self.assertIn(b'Search Patient', response.data)

    # Test visitor login
    def test_visitor_login_post(self):
        testingClient = app.test_client(self)
        response = testingClient.post("/log_visitor", data=dict(email="Tom@email.com", password="test@123",
                                                                ), follow_redirects=True)
        self.assertIn(
            b'scan_qrcode', response.data)

    # Test place login
    def test_place_login_post(self):
        testingClient = app.test_client(self)
        response = testingClient.post("/log_place", data=dict(email="tbs@email.com", password="test@123",
                                                              ), follow_redirects=True)
        self.assertIn(b'place', response.data)

    # logout
    def test_logout(self):
        tester = app.test_client(self)
        response = tester.get(
            '/logout')
        self.assertIn(b'Redirecting', response.data)
        self.assertIn(b'/', response.data)

    # Logged in Agent
    def test_hospital_verification_page_for_admin(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['userType'] = 'Agent'
                sess['userId'] = '1'
            response = c.get(
                '/hospital/request/verify', content_type="html/text",)
            self.assertIn(b'Verify', response.data)

    # Not Logged in Agent
    def test_hospital_verification_page_for_admin_not_logged_in(self):
        tester = app.test_client(self)
        response = tester.get(
            '/hospital/request/verify', content_type="html/text",)
        self.assertIn(b'Redirecting', response.data)

   # ==================================================================================================
if __name__ == '__main__':
    unittest.main()
