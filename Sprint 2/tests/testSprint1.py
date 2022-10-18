
# NOTE: AS SOME TEST WERE NOT RUNNING WE HAVE MADE A NEW TESTCASE FILE (testSprint2.py)
# Plese Do NoT USE THESE TEST CASES

# import os
# import sys
# import unittest
# import random
# import string

# # obtain current directory
# getCurrentDir = os.path.dirname(os.path.realpath(__file__))
# # get the parent of the current directory
# getParentDir = os.path.dirname(getCurrentDir)
# # allow to reference modules in this directory
# sys.path.append(getParentDir)
# # only import after
# from app import app  # nopep8 (from https://stackoverflow.com/a/57067521)

# # get random words for testing values. From: https://stackoverflow.com/a/2030081


# def randomword(length):
#     letters = string.ascii_lowercase
#     return ''.join(random.choice(letters) for i in range(length))


# class TestFlaskApp(unittest.TestCase):
#     # test access to login page
#     def test_login_page(self):
#         testingClient = app.test_client(self)
#         response = testingClient.get(
#             '/login', content_type="html/text")
#         self.assertIn(b'Log in', response.data)

#     # test access the after the redirection as this test client is not signed in
#     def test_index_page(self):
#         # load a test client
#         testingClient = app.test_client(self)
#         # get the base route with the content being the html text
#         response = testingClient.get(
#             '/', content_type="html/text", follow_redirects=True)
#         # assertIn(what to look for, where to look)
#         self.assertIn(b'You need to login', response.data)

#     # test access to registration page
#     def test_Register_page(self):
#         testingClient = app.test_client(self)
#         response = testingClient.get('/register', content_type="html/text")
#         self.assertIn(b'Register', response.data)

#     # ------------------------------------------------------------------------------------------------

#     # test logging in as a visitor
#     def test_logging_in_Visitor(self):
#         testingClient = app.test_client(self)
#         # name is null as it can be anything as we are logging in and name is not needed for logging in visitor
#         response = testingClient.post(
#             '/login', data=dict(email="bob@email.com", password="test", name="null", userType="visitor"), follow_redirects=True)
#         self.assertIn(b'Welcome!', response.data)

#     # test logging in as a place
#     def test_logging_in_Place(self):
#         testingClient = app.test_client(self)
#         # name is null as it can be anything as we are logging in and name is not needed for logging in visitor
#         response = testingClient.post(
#             '/login', data=dict(email="SCC@JUB.com", password="test", name="SCC", userType="place"), follow_redirects=True)
#         self.assertIn(b'Welcome!', response.data)

#     # test logging in as a Agency
#     def test_logging_in_Agency(self):
#         testingClient = app.test_client(self)
#         # name is null as it can be anything as we are logging in and name is not needed for logging in visitor
#         response = testingClient.post(
#             '/login', data=dict(email="null", password="test", name="Health Dept.", userType="agency"), follow_redirects=True)
#         self.assertIn(b'Welcome!', response.data)

#     # ------------------------------------------------------------------------------------------------

#     # test registration of visitor
#     def test_registration_visitor(self):
#         testingClient = app.test_client(self)
#         response = testingClient.post(
#             '/register', data=dict(email=randomword(10)+"@email.com", password="test", name=randomword(60), phone="123456789", address="testAddress", city="testCity", userType="visitor"), follow_redirects=True)
#         self.assertIn(b'Register', response.data)

#         # test registration of place
#     def test_registration_place(self):
#         testingClient = app.test_client(self)
#         response = testingClient.post(
#             '/register', data=dict(email=randomword(10)+"@email.com", password="test", name=randomword(60), phone="123456789", address="testAddress", city="testCity", userType="place"), follow_redirects=True)
#         self.assertIn(b'Register', response.data)

#     # test registration of agency
#     def test_registration_agency(self):
#         testingClient = app.test_client(self)
#         response = testingClient.post(
#             '/register', data=dict(email=randomword(10)+"@email.com", password="test", name=randomword(60), phone="123456789", address="testAddress", city="testCity", userType="agency"), follow_redirects=True)
#         self.assertIn(b'Register', response.data)

#     # test registration of hospital
#     def test_registration_hospital(self):
#         testingClient = app.test_client(self)
#         response = testingClient.post(
#             '/register', data=dict(email=randomword(10)+"@email.com", password="test", name=randomword(60), phone="123456789", address="testAddress", city="testCity", userType="hospital"), follow_redirects=True)
#         self.assertIn(b'Register', response.data)
    



# if __name__ == '__main__':
#     unittest.main()
