from dao.dbConnector import *
from dao.queries import *
from .adminDao import *
from .careProviderDao import *
import hashlib

class EmployeeDao:
    '''handles database operations for Employee'''

    def __init__(self):
        self.dbObject = DBConnector()
        self.connection, self.cursor = self.dbObject.getConnector()

    def addNewEmployee(self, employee):
        '''add a new admin to database'''
        query = QUERIES['ADD_EMPLOYEE'].format(employee['isAdmin'])
        self.cursor.execute(query, employee)
        self.cursor.execute('commit')

        if employee['isAdmin'] == True:
            adminDao = AdminDao()
            adminDao.addAdmin(employee['id'])
            self.cursor.execute('commit')
            paswd = hashlib.sha256(str('admin_' + employee['id']).encode()).hexdigest()
        elif employee['isAdmin'] == False:
            careProviderDao = CareProviderDao()
            careProviderDao.addCareProvider(employee['id'])
            self.cursor.execute('commit')
            paswd = hashlib.sha256(str('careProvider_' + employee['id']).encode()).hexdigest()

        loginDetail = {
            'id' : employee['id'],
            'paswd' : paswd
        }

        self.cursor.execute(QUERIES['ADD_LOGIN_DETAILS'], loginDetail)
        self.cursor.execute('commit')

    def deleteEmployee(self, id):
        self.cursor.execute(QUERIES['DELETE_EMPLOYEE'].format(id))
        self.cursor.execute('commit')
