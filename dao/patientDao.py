from dao.dbConnector import *
from dao.queries import *
from .employeeDao import *

class PatientDao:
    '''handles database operations for Patient'''

    def __init__(self):
        self.dbObject = DBConnector()
        self.connection, self.cursor = self.dbObject.getConnector()

    def fetchAllPatients(self):
        patients = []
        self.cursor.execute(QUERIES['FETCH_ALL_PATIENTS'])
        result = self.cursor.fetchall()

        for (id, firstname, lastname, email, contactNumber, dob, consentToShare, age) in result:
            patient = {
                'id' : id,
                'firstName' : firstname,
                'lastName' : lastname,
                'email' : email,
                'contactNumber' : contactNumber,
                'dob' : dob,
                'consentToShare' : consentToShare,
                'age' : age
            }
            patients.append(patient)
        return patients

    def fetchPatient(self, patientId):
        for patient in self.fetchAllPatients():
            if patient['id'] == patientId:
                return patient
        return None

    def addNewPatient(self, patient):
        '''register a new patient in the system'''
        self.cursor.execute(QUERIES['ADD_PATIENT'], patient)
        self.cursor.execute('commit')
        self.cursor.execute(QUERIES['INIT_PATIENT_HISTORY'].format(patient['id']))
        self.cursor.execute('commit')

    def updatePatientInfo(self, patient):
        self.cursor.execute(QUERIES['UPDATE_PATIENT'].format(patient['id']), patient)
        self.cursor.execute('commit')

    def deletePatient(self, id):
        '''deleting a record sets the status to inactive in database'''
        self.cursor.execute(QUERIES['DELETE_PATIENT'].format(id))
        self.cursor.execute('commit')

    def getPatientAddress(self, id):
        '''return the patient address'''
        self.cursor.execute(QUERIES['FETCH_PATIENT_ADDRESS'].format(id))
        result = self.cursor.fetchone()

        return {
            'patientId' : id,
            'address_line_1': result[0],
            'address_line_2': result[1],
            'city': result[2],
            'postCode': result[3],
            'country': result[4],
        }

    def addAddress(self, input):
        '''register address for a patient'''
        self.cursor.execute(QUERIES['ADD_PATIENT_ADDRESS'], input)
        self.cursor.execute('commit')

    def updateAddress(self, address):
        '''update patient address in database'''
        self.cursor.execute(QUERIES['UPDATE_ADDRESS'], address)
        self.cursor.execute('commit')

    def getPatientNotes(self, id):
        '''returns a list of patient notes added by care Providers'''
        notes = []
        self.cursor.execute(QUERIES['FETCH_PATIENT_NOTES'].format(id))
        result = self.cursor.fetchall()

        for (id, patientId, note, writtenBy, writtenOn) in result :
            notes.append({
                'id' : id,
                'patientId' : patientId,
                'note' : note,
                'writtenBy' : writtenBy,
                'writtenOn' : writtenOn
            })
        return notes

    def addNote(self, input):
        '''add new note for patient'''
        self.cursor.execute(QUERIES['ADD_PATIENT_NOTE'], input)
        self.cursor.execute('commit')

    def getPatientAllergies(self, patientId):
        '''returns a list of patient allergies'''
        allergies = []
        self.cursor.execute(QUERIES['FETCH_PATIENT_ALLERGIES'].format(patientId))
        result = self.cursor.fetchall()

        for(id, allergicTo, onMedication) in result:
            allergies.append({
                'id' : id,
                'allergicTo' : allergicTo,
                'onMedication' : onMedication
            })
        return allergies

    def addNewAllergy(self, input):
        '''add new allergy details in the system for a given patient'''
        self.cursor.execute(QUERIES['ADD_NEW_ALLERGY'].format(input['patientId']), input)
        self.cursor.execute('commit')

    def deletePatientAllergy(self, id):
        '''delete an allergy record for a patient'''
        self.cursor.execute(QUERIES['DELETE_PATIENT_ALLERGY'].format(id))
        self.cursor.execute('commit')

    def getPatientIllness(self, patientId):
        '''returns a list of patient illness'''
        illnessDetails = []
        self.cursor.execute(QUERIES['FETCH_PATIENT_ILLNESS_DETAILS'].format(patientId))
        result = self.cursor.fetchall()

        for (id, illness, onMedication) in result:
            illnessDetails.append({
                'id': id,
                'illness': illness,
                'onMedication': onMedication
            })
        return illnessDetails

    def addNewIllness(self, input):
        '''add new illness details in the system for a given patient'''
        self.cursor.execute(QUERIES['ADD_NEW_ILLNESS'].format(input['patientId']), input)
        self.cursor.execute('commit')

    def getPatientImmunisation(self, patientId):
        '''returns a list of patient immunisation'''
        immunisationDetails = []
        self.cursor.execute(QUERIES['FETCH_PATIENT_IMMUNISATION_DETAILS'].format(patientId))
        result = self.cursor.fetchall()

        for (id, immunisation, onMedication) in result:
            immunisationDetails.append({
                'id': id,
                'immunisation': immunisation,
                'onMedication': onMedication
            })
        return immunisationDetails

    def addNewImmunisation(self, input):
        '''add new immunisation details in the system for a given patient'''
        self.cursor.execute(QUERIES['ADD_NEW_IMMUNISATION'].format(input['patientId']), input)
        self.cursor.execute('commit')

    def getPatientLabDetails(self, patientId):
        '''returns a list of patient lab tests'''
        labTests = []
        self.cursor.execute(QUERIES['FETCH_PATIENT_LAB_TEST_DETAILS'].format(patientId))
        result = self.cursor.fetchall()

        for (id, testName) in result:
            labTests.append({
                'id': id,
                'testName': testName
            })
        return labTests

    def addNewLabTest(self, input):
        '''add new lab test details in the system for a given patient'''
        self.cursor.execute(QUERIES['ADD_NEW_LAB_TEST'].format(input['patientId']), input)
        self.cursor.execute('commit')

    def getPatientHospitalisationDetails(self, patientId):
        '''return a list of patient hospitalisation'''
        details = []
        self.cursor.execute(QUERIES['FETCH_ADMISSION_DETAILS'].format(patientId))
        result = self.cursor.fetchall()

        for(id, admitDate, dischargeDate, isDischarged) in result:
            details.append({
                'id' : id,
                'admitDate' : admitDate,
                'dischargeDate' : dischargeDate,
                'isDischarged' : isDischarged
            })
        return details

    def admitPatient(self, patientId):
        '''admit a patient '''
        self.cursor.execute(QUERIES['ADMIT_PATIENT'].format(patientId))
        self.cursor.execute('commit')

    def dischargePatient(self, patientId):
        '''discharge a patient'''
        self.cursor.execute(QUERIES['DISCHARGE_PATIENT'].format(patientId))
        self.cursor.execute('commit')

    def getAdmissionDetail(self, patientId, admitId):
        for detail in self.getPatientHospitalisationDetails(patientId):
            if detail['id'] == admitId :
                return detail
        return None