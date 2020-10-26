# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode

class InitDb:

    '''
        This class aims at initial load of Database.
        It will create a default database in the SQL server
        with basic tables already created.
    '''

    def __init__(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root")

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            self.mycursor = connection.cursor()
            self.createDefaultDatabase()

    def createDefaultDatabase(self):
        print('creating database')
        #self.mycursor.execute("create database EMR")
        print('done')