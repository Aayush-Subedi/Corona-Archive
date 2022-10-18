import sqlite3

# help from: https://stackoverflow.com/a/54290631
# establish a connection with database
connection = sqlite3.connect("coronaArchive.db")

# create cursor to execute script
cursor = connection.cursor()

# read our sql file and save content into script.
with open('./createTables.sql', 'r') as SQL_Create_Tables:
    # execute the read SQL script
    cursor.executescript(SQL_Create_Tables.read())

# commit changes and close the connection to the database
connection.commit()
connection.close()
