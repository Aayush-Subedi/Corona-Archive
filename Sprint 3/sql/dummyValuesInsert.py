# TO INSERT VALUES INTO SQLITE DATABASE TABLES
import sqlite3

conn = sqlite3.connect("db.sqlite")
cursor = conn.cursor()

# visitor
sql_query = """INSERT INTO Visitor (name, address, city, phoneNumber, email, device_ID, infected, password)
    VALUES ('Tom', '2103 Bridgewater ', 'Fairbanks', '123456789', 'Tom@email.com', 'duahiduh2uehad', 0, "test@123")
    """
cursor.execute(sql_query)

sql_query = """INSERT INTO Visitor (name, address, city, phoneNumber, email, device_ID, infected, password)
    VALUES ('John', '10929 Mccormick Rd', 'Keno', '987654321', 'John@email.com', 'dhaiuh12huieh', 0,"test@123")
    """
cursor.execute(sql_query)

sql_query = """INSERT INTO Visitor (name, address, city, phoneNumber, email, device_ID, infected, password)
    VALUES ('Fred', '313 E Lincoln Ave', 'Carrollton', '32136782', 'fred@email.com', '43dasdas23',0, "test@123")
    """
cursor.execute(sql_query)

sql_query = """INSERT INTO Visitor (name, address, city, phoneNumber, email, device_ID, infected, password)
    VALUES ('Tony', '20 Canning Ter', 'Dennis Port', '4283991', 'Tony@email.com', '8hhda7sh71d', 0, "test@123")
    """
cursor.execute(sql_query)

# ==================================================================================

# agent
sql_query = """INSERT INTO AGENT (username, password)
    VALUES ('Sam', 'password123') """
cursor.execute(sql_query)

sql_query = """INSERT INTO AGENT (username, password)
    VALUES ('John', 'happyDog123') """
cursor.execute(sql_query)

sql_query = """INSERT INTO AGENT (username, password)
    VALUES ('Zach', 'germany123') """
cursor.execute(sql_query)

sql_query = """INSERT INTO AGENT (username, password)
    VALUES ('Bob', 'bob123') """
cursor.execute(sql_query)

# ==================================================================================
# place

sql_query = """INSERT INTO Place (name, address,phoneNumber,email, password)
VALUES ('The Burger Shop', '2405 Regent St', '47837248', 'tbs@email.com', 'test@123')"""
cursor.execute(sql_query)

sql_query = """INSERT INTO Place (name, address,phoneNumber,email, password)
VALUES ('Smoothy Smoothy Smoothy', '60 Carona Ct', '1324523', 'smoothyx3@email.com', 'test@123')"""
cursor.execute(sql_query)

sql_query = """INSERT INTO Place (name, address,phoneNumber,email, password)
VALUES ('Fun Toys', 'Po Box 465', '7862109', 'funToys@email.com','test@123')"""
cursor.execute(sql_query)

sql_query = """INSERT INTO Place (name, address,phoneNumber,email, password)
VALUES ('Computer Repair', '2261 Al 89 Hwy', '7872981', 'computerHelp@email.com','test@123')"""
cursor.execute(sql_query)

# ==================================================================================

# hopsital
sql_query = """INSERT INTO Hospital (name, username ,password)
VALUES ('Grand Valley Clinic', 'GrandVC', 'healthIsCool')"""
cursor.execute(sql_query)

sql_query = """INSERT INTO Hospital (name, username,password)
VALUES ('White River General Hospital', 'WhiteRiverGH', 'helpingPeople!')"""
cursor.execute(sql_query)

sql_query = """INSERT INTO Hospital (name, username,password)
VALUES ('Cherry Blossom Medical Center', 'BlossomMedical', 'savingLives')"""
cursor.execute(sql_query)

sql_query = """INSERT INTO Hospital (name, username,password)
VALUES ('Progress Medical Center', 'PCMHopsital', 'MakingProgress')"""
cursor.execute(sql_query)

# ==================================================================================


conn.commit()
