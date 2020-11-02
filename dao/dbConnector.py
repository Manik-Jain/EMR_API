# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode
from initialiseDatabase.initDB import *

class DBConnector:

    '''A common application level DB connectivity configuration'''

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(**config)
            self.connection.database = DB_NAME

        except mysql.connector.Error as err:
          if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
          elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
          else:
            print(err)
        else:
            self.mycursor = self.connection.cursor()

    def getConnector(self):
        return self.connection, self.mycursor
