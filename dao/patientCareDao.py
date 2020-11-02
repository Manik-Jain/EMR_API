from dao.dbConnector import *
from dao.queries import *
from .employeeDao import *

class PatientCareDao:
    '''handles database operations for Patient Care'''

    def __init__(self):
        self.dbObject = DBConnector()
        self.connection, self.cursor = self.dbObject.getConnector()

    def insertPatientCare(self, patientCareInfo):
        print(patientCareInfo)
        self.cursor.execute(QUERIES['INIT_PATIENT_CARE'], patientCareInfo)
        self.cursor.execute('commit')

    def updateBillingId(self, billInfo):
        '''update billing Id once the billing has been initiated'''
        self.cursor.execute(QUERIES['UPDATE_PATIENT_CARE_BILLING'], billInfo)
        self.cursor.execute('commit')

    def updateFollowUpDate(self, followUp):
        self.cursor.execute(QUERIES['UPDATE_FOLLOWUP_DATE'], followUp)
        self.cursor.execute('commit')