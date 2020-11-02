from dao.dbConnector import *
from dao.queries import *
from .employeeDao import *

class AdminDao:
    '''handles database operations for Admin'''

    def __init__(self):
        self.dbObject = DBConnector()
        self.connection, self.cursor = self.dbObject.getConnector()

    def fetchAllAdmins(self):
        admins = []
        self.cursor.execute(QUERIES['FETCH_ALL_ADMIN'])
        result = self.cursor.fetchall()

        for (id, fname, lname, dob, email_id, salary, status) in result:
            admin = {
                'id' : id,
                'first_name' : fname,
                'last_name' : lname,
                'dob' : dob,
                'email' : email_id,
                'salary' : salary,
                'status' : status
            }
            admins.append(admin)
        return admins

    def deleteAdmin(self, id):
        '''delete a specific admin from database'''
        self.cursor.execute(QUERIES['DELETE_ADMIN'].format(id))
        self.cursor.execute('commit')
        self.cursor.execute(QUERIES['DELETE_EMPLOYEE'].format(id))
        self.cursor.execute('commit')

    def addAdmin(self, id):
        '''add a new admin to database'''
        self.cursor.execute(QUERIES['ADD_ADMIN'].format(id))
        self.cursor.execute('commit')

    def updateAdmin(self, id):
        '''updates admin record in database'''
        self.cursor.execute(QUERIES['UPDATE_ADMIN'].format(id))
        self.cursor.execute('commit')
