import mysql.connector
from mysql.connector import errorcode
from initialiseDatabase.initDB import *

#create database for the initial data load
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
        print("Database {} created successfully.".format(DB_NAME))
        print('User {} Connected to the database'.format(config['user']))
        cnx.database = DB_NAME
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

def createSequencers(cursor):
    print()
    print('-*-' * 5 + 'Creating Sequencers' + '-*-' * 5)
    for entry in SEQUENCERS:
        cursor.execute(SEQUENCERS[entry])
        print(entry + ' : OK.')
    print('-*-' * 5 + 'Sequencers created' + '-*-' * 5)
    print()
    print()

def createTables(cursor):
    print('-*-' * 5 + 'Creating Tables' + '-*-' * 5)
    for entry in TABLES:
        cursor.execute(TABLES[entry])
        print(entry + ' : OK.')
    print('-*-' * 5 + 'Tables created' + '-*-' * 5)
    print()
    print()

def createTableIndex(cursor):
    print('-*-' * 5 + 'Creating Indexes' + '-*-' * 5)
    for entry in INDEXES:
        cursor.execute(INDEXES[entry])
        print(entry + ' : OK.')
    print('-*-' * 5 + 'INDEXES created' + '-*-' * 5)
    print()
    print()

def createViews(cursor):
    print('-*-' * 5 + 'Creating Views' + '-*-' * 5)
    for entry in VIEWS:
        cursor.execute(VIEWS[entry])
        print(entry + ' : OK.')
    print('-*-' * 5 + 'Views created' + '-*-' * 5)
    print()
    print()

def loadDefaultLookups(cursor):
    print('-*-' * 5 + 'Loading default data' + '-*-' * 5)
    for entry in INSERTS:
        cursor.execute(INSERTS[entry])
        cursor.execute('commit')
        print(entry + ' : OK.')
    print('-*-' * 5 + 'Default data loaded' + '-*-' * 5)
    print()
    print()

try:
    cnx = mysql.connector.connect(**config)
    try:
        cnx.cursor().execute("USE {}".format(DB_NAME))
        print('User {} Connected to the database'.format(config['user']))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cnx.cursor())

    createSequencers(cnx.cursor())
    createTables(cnx.cursor())
    createTableIndex(cnx.cursor())
    createViews(cnx.cursor())
    loadDefaultLookups(cnx.cursor())

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    print('Initial Data load Done!!')

