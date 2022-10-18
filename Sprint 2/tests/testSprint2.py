
import os
import sys
import string
import random
import unittest

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from app import app

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


class FlaskTestCase(unittest.TestCase):
    # Please note that this test cases depend on your computer as well.
    # Checking home page

    def test_home_page(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type="html/text")
        self.assertIn(b'Corona Archive', response.data)
        self.assertIn(b'Login', response.data)

    def test_login_page(self):
        testingClient = app.test_client(self)
        response = testingClient.get(
            '/login', content_type="html/text")
        self.assertIn(b'Login', response.data)
        self.assertIn(b'Don\'t have an account?', response.data)

    def test_register_page(self):
        testingClient = app.test_client(self)
        response = testingClient.get(
            '/register', content_type="html/text")
        self.assertIn(b'Register', response.data)
        self.assertIn(
            b'What account type are you registering for?', response.data)

    def test_visitor_info_page_failure(self):
        testingClient = app.test_client(self)
        response = testingClient.get(
            '/visitor_info', content_type="html/text")
        self.assertIn(b'Redirecting', response.data)
        self.assertIn(b'/login', response.data)

    def test_place_info_page_failure(self):
        testingClient = app.test_client(self)
        response = testingClient.get(
            '/visitor_info', content_type="html/text")
        self.assertIn(b'Redirecting', response.data)
        self.assertIn(b'/login', response.data)

    def test_hospital_registration_page_failure(self):
        testingClient = app.test_client(self)
        response = testingClient.get(
            '/hospital_registration', content_type="html/text")
        self.assertIn(b'Redirecting', response.data)
        self.assertIn(b'/login', response.data)

    def test_hospital_visitor_page_failure(self):
        testingClient = app.test_client(self)
        response = testingClient.get(
            '/hospital_visitor', content_type="html/text")
        self.assertIn(b'Redirecting', response.data)
        self.assertIn(b'/', response.data)

    def test_scan_qrcode_page(self):
        testingClient = app.test_client(self)
        response = testingClient.get(
            '/scan_qrcode', content_type="html/text")
        self.assertIn(b'Redirecting', response.data)
        self.assertIn(b'/login', response.data)

    def test_place_registration(self):
        testingClient = app.test_client(self)
        response = testingClient.post(
            '/register', data=dict(email=randomword(5)+"test.com", password="Test@123", userType="place", phone="79879789", name=randomword(4), address="fromtestaddress", city="jlkfdjs"), follow_redirects=True)
        # Redirecting to QR Page after Place registration
        self.assertIn(b'QR Page', response.data)

    def test_visitor_registration(self):
        testingClient = app.test_client(self)
        response = testingClient.post(
            '/register', data=dict(email=randomword(5)+"test.com", password="Test@12334324", userType="visitor", phone="32423", name=randomword(4), address="visitoraddress", city="visitor_city"), follow_redirects=True)
        # When visitor is registered redirect to index page where user information is displayed
        self.assertIn(b'Welcome', response.data)

    # When user is not logged in
    def test_corona_status_fail(self):
        tester = app.test_client(self)
        response = tester.post(
            '/change_corona_status', data=dict(visitorId="1", visitorStatus=0), follow_redirects=True)
        self.assertIn(b'Login', response.data)
        self.assertIn(b'Don\'t have an account?', response.data)

    def test_logout(self):
        tester = app.test_client(self)
        response = tester.get(
            '/logout')
        self.assertIn(b'Redirecting', response.data)
        self.assertIn(b'/', response.data)

    def test_generate_qrcode_page(self):
        testingClient = app.test_client(self)
        response = testingClient.get(
            '/generate_qrcode', content_type="html/text")
        self.assertIn(b'Download!', response.data)
        self.assertIn(b'data:image/jpeg;base64', response.data)

    def test_qrcode_page_failure(self):
        testingClient = app.test_client(self)
        response = testingClient.get(
            '/qrcode', content_type="html/text")
        self.assertIn(b'Redirecting', response.data)
        self.assertIn(b'/login', response.data)

    # When logged In user in Agency
    def test_visitor_info_page_success(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['userType'] = 'Agency'
                sess['userId'] = '1'
            response = c.get(
                '/visitor_info', content_type="html/text")
            self.assertIn(b'Search Visitor', response.data)
            self.assertIn(b'Visitor Information', response.data)

    # When logged In user in as Agency
    def test_place_info_page_sucess(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['userType'] = 'Agency'
                sess['userId'] = '1'
            response = c.get(
                '/place_info', content_type="html/text")
            self.assertIn(b'Search', response.data)
            self.assertIn(b'Place Owner', response.data)
            self.assertIn(b'Information', response.data)

    # When logged In user in as Agency
    def test_get_hospital_registration_page_success(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['userType'] = 'Agency'
                sess['userId'] = '1'
            response = c.get(
                '/hospital_registration', content_type="html/text")
            self.assertIn(b'Hospital Registration', response.data)
            self.assertIn(b'Name', response.data)
            self.assertIn(b'Password', response.data)
            self.assertIn(b'Register', response.data)

    # When logged In user in as Visitor
    def test_scan_qrcode_page(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['userType'] = 'Visitor'
                sess['userId'] = '1'
            response = c.get(
                '/scan_qrcode', content_type="html/text")
            self.assertIn(b'qrcode.min_.js', response.data)
            self.assertIn(b'QR Code', response.data)
            self.assertIn(b'SCAN', response.data)

    # When logged In user in as Hospital

    def test_hospital_visitor_page(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['userType'] = 'Hospital'
                sess['userId'] = '1'
            response = c.get(
                '/hospital_visitor', content_type="html/text")
            self.assertIn(b'Search Visitor', response.data)
            self.assertIn(b'Visitor Information', response.data)

    # When logged In user in as Place Owner
    def test_qrcode_page(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['userType'] = 'Places'
                sess['userId'] = '1'
            response = c.get(
                '/qrcode', content_type="html/text")
            self.assertIn(b'img', response.data)
            self.assertIn(b'Download', response.data)

    # When logged In user in as Agency
    def test_post_hospital_registration(self):
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['userType'] = 'Agency'
                sess['userId'] = '1'
            response = c.post(
                '/hospital_registration', data=dict(name=randomword(8), password=randomword(8)))
            self.assertIn(b'Hospital Registration', response.data)
            self.assertIn(b'Successfully registered!', response.data)


    # test access to login page
    def test_login_page(self):
        testingClient = app.test_client(self)
        response = testingClient.get(
            '/login', content_type="html/text")
        self.assertIn(b'Log in', response.data)

    # test access the after the redirection as this test client is not signed in
    def test_index_page(self):
        # load a test client
        testingClient = app.test_client(self)
        # get the base route with the content being the html text
        response = testingClient.get(
            '/', content_type="html/text", follow_redirects=True)
        # assertIn(what to look for, where to look)
        self.assertIn(b'Login', response.data)

    # test access to registration page
    def test_Register_page(self):
        testingClient = app.test_client(self)
        response = testingClient.get('/register', content_type="html/text")
        self.assertIn(b'Register', response.data)

    # ------------------------------------------------------------------------------------------------

    # test logging failure in as a visitor
    def test_logging_in_Visitor(self):
        testingClient = app.test_client(self)
        # name is null as it can be anything as we are logging in and name is not needed for logging in visitor
        response = testingClient.post(
            '/login', data=dict(email="testcase3@1.com", password="testcase3", name="testcase3", userType="visitor"), follow_redirects=True)
        self.assertIn(b'Username or password is incorrect,', response.data)

    # test logging failure in as a place
    def test_logging_in_Place(self):
        testingClient = app.test_client(self)
        # name is null as it can be anything as we are logging in and name is not needed for logging in visitor
        response = testingClient.post(
            '/login', data=dict(email="testcase3@1.com", password="testcase3", name="testcase3", userType="place"), follow_redirects=True)
        self.assertIn(b'Username or password is incorrect,', response.data)

    # test logging in as a Agency
    def test_logging_in_Agency(self):
        testingClient = app.test_client(self)
        # name is null as it can be anything as we are logging in and name is not needed for logging in visitor
        response = testingClient.post(
            '/login', data=dict(email="null", password="test", name="Health Dept.", userType="agency"), follow_redirects=True)
        self.assertIn(b'Username or password is incorrect', response.data)

    # ------------------------------------------------------------------------------------------------

    # test registration of visitor
    def test_registration_visitor(self):
        testingClient = app.test_client(self)
        response = testingClient.post(
            '/register', data=dict(email=randomword(10)+"@email.com", password="test", name=randomword(10), phone="123456789", address="testAddress", city="testCity", userType="visitor"), follow_redirects=True)
        self.assertIn(b'Welcome!', response.data)

        # test registration of place
    def test_registration_place(self):
        testingClient = app.test_client(self)
        response = testingClient.post(
            '/register', data=dict(email=randomword(10)+"@email.com", password="test", name=randomword(10), phone="123456789", address="testAddress", city="testCity", userType="place"), follow_redirects=True)
        self.assertIn(b'QR Page', response.data)

    # test registration of agency
    def test_registration_agency(self):
        testingClient = app.test_client(self)
        response = testingClient.post(
            '/register', data=dict(email=randomword(10)+"@email.com", password="test", name=randomword(10), phone="123456789", address="testAddress111", city="testCity", userType="agency"), follow_redirects=True)
        self.assertIn(b'Register', response.data)

    # test registration of hospital
    def test_registration_hospital(self):
        testingClient = app.test_client(self)
        response = testingClient.post(
            '/register', data=dict(email=randomword(10)+"@email.com", password="test", name=randomword(10), phone="123456789", address="testAddress1", city="testCity", userType="hospital"), follow_redirects=True)
        self.assertIn(b'Register', response.data)


if __name__ == '__main__':
    unittest.main()
