from dao.dbConnector import *
from dao.queries import *

class CareProviderDao:
    '''handles database operations for Admin'''

    def __init__(self):
        self.dbObject = DBConnector()
        self.connection, self.cursor = self.dbObject.getConnector()

    def fetchAllCareProviders(self):
        '''returns a list of all care Providers in the system'''
        careProviders = []
        self.cursor.execute(QUERIES['FETCH_ALL_CAREPROVIDER'])
        result = self.cursor.fetchall()

        for (id, fname, lname, dob, email_id, status, per_visit_charges) in result:
            careProvider = {
                'id': id,
                'first_name': fname,
                'last_name': lname,
                'dob': dob,
                'email': email_id,
                'per_visit_charges': per_visit_charges,
                'status' : status
            }
            careProviders.append(careProvider)
        return careProviders

    def addCareProvider(self, id):
        '''add a new Care Provider to database'''
        query = QUERIES['ADD_CARE_PROVIDER'].format(id)
        self.cursor.execute(query)
        self.cursor.execute('commit')

    def deleteCareProvider(self, id):
        '''delete a specific careProvider from database'''
        self.cursor.execute(QUERIES['DELETE_CARE_PROVIDER'].format(id))
        self.cursor.execute('commit')
        self.cursor.execute(QUERIES['DELETE_EMPLOYEE'].format(id))
        self.cursor.execute('commit')

    def updateCareProvider(self, careProvider):
        '''update care provider detail in database'''
        self.cursor.execute(QUERIES['UPDATE_CARE_PROVIDER'], careProvider)
        self.cursor.execute('commit')