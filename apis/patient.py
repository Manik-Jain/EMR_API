# -*- coding: utf-8 -*-

from flask_restx import Namespace, Resource, fields
from uuid import uuid4
from datetime import datetime
from dao.patientDao import *
from dao.billDao import *
from services.updateService import *
from dao.patientCareDao import *

api = Namespace('patient', description='Patients related operations')
patientDao = PatientDao()
billDao = BillDao()
updateService = UpdateService()
patientCareDao = PatientCareDao()

newPatientNote = api.model('NewPatientNote', {
    'note' : fields.String(required = True, desctiption = 'note to be added'),
    'writtenBy' : fields.String(required = True, description = 'care Provider Id')
})

patientNotes = api.inherit('PatientNotes', newPatientNote, {
        'id' : fields.Integer(description = 'note id'),
        'patientId' : fields.String(required = True, desctiption = 'patient id'),
        'writtenOn' : fields.String(description = 'date when the note was written')
        })

address = api.model('Address', {
    'address_line_1' : fields.String(required = True, description = 'patient address line 1'),
    'address_line_2' : fields.String(description = 'patient address line 2'),
    'city' : fields.String(required = True, description = 'patient city'),
    'postCode' : fields.Integer(required = True, description = 'patient postCode'),
    'country' : fields.String(required = True, description = 'patient country')
})

updateAddress = api.inherit('UpdateAddress', address, {
    'changedBy' : fields.String(required = True, description = 'the updating user id')
})

newPatient = api.model('NewPatient', {
        'firstName' : fields.String(required = True, description = 'patient first name'),
        'lastName' : fields.String(required = True, description = 'patient last name'),
        'email' : fields.String(required = True, description = 'patient email address'),
        'contactNumber' : fields.Integer(required = True, description = 'patient contact Number'),
        'consentToShare' : fields.Boolean(required = True, description = 'patient consent to share information'),
        'dob' : fields.String(required = True, description = 'patient date of birth'),
        'age' : fields.Integer(required = True, description = 'patient age')
        })

updatedPatient = api.inherit('Update Patient', newPatient, {
    'changedBy' : fields.String(required = True, description = 'the updating user id')
})

patient = api.inherit('Patient', newPatient, {
        'id':fields.String(required=True, description = 'unique patient id')
        })

patientAddress = api.inherit('PatientAddress', address, {
        'patientId':fields.String(required=True, description = 'unique patient id')
})

newAlleryDetail = api.model('NewAllergy', {
    'allergicTo' : fields.String(required = True, description = 'patient is allergic to'),
    'onMedication' : fields.Boolean(required=True, description=' true if patient is using medication, false otherwise')
})

patientAllergies = api.inherit('PatientAllergy', newAlleryDetail, {
    'id' : fields.Integer(required = True, description = 'unique identifier')
})

newIllnessDetail = api.model('NewIllness', {
    'illness' : fields.String(required = True, description = 'patient having illness'),
    'onMedication' : fields.Boolean(required=True, description=' true if patient is using medication, false otherwise')
})

patientIllness = api.inherit('PatientIllness', newIllnessDetail, {
    'id' : fields.Integer(required = True, description = 'unique identifier')
})

newImmunisationDetail = api.model('NewImmunisation', {
    'immunisation' : fields.String(required = True, description = 'patient immunisation'),
    'onMedication' : fields.Boolean(required=True, description=' true if patient is using medication, false otherwise')
})

patientImmunisation= api.inherit('PatientImmunisation', newImmunisationDetail, {
    'id' : fields.Integer(required = True, description = 'unique identifier')
})

newLabTestDetail = api.model('NewLabTest', {
    'testName' : fields.String(required = True, description = 'lab test prescribed to patient')
})

patientLabTests = api.inherit('PatientLabTest', newLabTestDetail, {
    'id' : fields.Integer(required = True, description = 'unique identifier')
})

patientHospitalisationDetails = api.model('PatientHospitalisationDetails', {
    'id' : fields.Integer(required=True, description = "unique admission id"),
    'admitDate' : fields.DateTime(required = True, description = "patient admit date"),
    'dischargeDate' : fields.DateTime(description = "patient discharge date"),
    'isDischarged' : fields.Boolean(required=True, description='true if patient has been discharged, false otherwise')
})

admitPatient = api.model('Admit Patient', {
    'careProviderId' : fields.String(required = True, description = 'care provider id')
})

patientCareDetails = api.model('PatientCare', {

})

dischargePatient = api.model('dischargePatient', {
    'admissionId' : fields.Integer(required = True, description = 'admission id of patient'),
    'followUpDate' : fields.String(description = 'the patient followUp date')
})

@api.route('patient')
class PatientList(Resource):
    
    @api.doc('list patients')
    @api.marshal_list_with(patient)
    def get(self):
        '''returns a list of all patients'''
        return patientDao.fetchAllPatients()
    
    @api.doc('add patient')
    @api.marshal_with(patient)
    @api.expect(newPatient)
    def post(self):
        '''Add a new patient'''
        input = api.payload
        input['id'] = str(uuid4())
        patientDao.addNewPatient(input)
        return input, 201
    
@api.route('patient/<id>')
@api.param('id', 'patient identifier')
@api.response(404, 'Resource Not found')
class Patient(Resource):
    
    @api.doc('get Patient')
    @api.marshal_with(patient)
    def get(self, id):
        '''get patient by input id'''
        for patient in patientDao.fetchAllPatients():
            if patient['id'] == id:
                return patient
        api.abort(404, "Patient {} doesn't exist".format(id))
        
    @api.doc('delete patient')
    def delete(self, id):
        '''delete a specific patient'''
        patient = self.get(id)
        patientDao.deletePatient(id)
        return "patient {} deleted successfully".format(id), 200
    
    @api.doc('Update Patient record')
    @api.marshal_with(patient)
    @api.expect(updatedPatient)
    def put(self, id):
        '''Update a patient record'''
        currPatient = self.get(id)
        updatedPatient = api.payload
        updateService.updatePatientBasicInfo(currPatient, updatedPatient)
        return updatedPatient, 200

@api.route('patient/<id>/address')
@api.param('id', 'patient identifier')
@api.response(404, 'Resource Not found')
class PatientAddress(Resource):

    @api.doc('get Patient address')
    @api.marshal_with(patientAddress)
    def get(self, id):
        '''returns the address for a specific patient'''
        return patientDao.getPatientAddress(id), 200

    @api.doc('add patient address')
    @api.expect(address)
    @api.marshal_with(patientAddress)
    def post(self, id):
        '''add a address for patient'''
        input = api.payload
        input['patientId'] = id
        patientDao.addAddress(input)
        return input, 201

    @api.doc('update patient address')
    @api.expect(updateAddress)
    @api.marshal_with(patientAddress)
    def put(self, id):
        '''update patient address'''
        currAddress = patientDao.getPatientAddress(id)
        newAddress = api.payload
        newAddress['patientId'] = id
        updateService.updatePatientAddressInfo(currAddress, newAddress)
        return newAddress, 200

@api.route('patient/<id>/note')
@api.param('id', 'patient identifier')
@api.response(404, 'Resource Not found')
class PatientNote(Resource):

    @api.doc('get Patient notes')
    @api.marshal_with(patientNotes)
    def get(self, id):
        '''returns the notes for a specific patient'''
        return patientDao.getPatientNotes(id), 200

    @api.doc('add patient note')
    @api.expect(newPatientNote)
    def post(self, id):
        '''add a Note for patient'''
        input = api.payload
        input['patientId'] = id
        patientDao.addNote(input)
        return input, 201

@api.route('patient/<id>/allergyDetails')
@api.param('id', 'patient identifier')
@api.response(404, 'Resource Not found')
class PatientAllergy(Resource):

    @api.doc('get patient allergies')
    @api.marshal_with(patientAllergies)
    def get(self, id):
        '''returns the allergies that a patient is allergic to'''
        return patientDao.getPatientAllergies(id), 200

    @api.doc('add new patient allergy')
    @api.expect(newAlleryDetail)
    def post(self, id):
        '''add new patient allergy'''
        input = api.payload
        input['patientId'] = id
        patientDao.addNewAllergy(input)
        return input, 201

@api.route('patient/<id>/illnessDetails')
@api.param('id', 'patient identifier')
@api.response(404, 'Resource Not found')
class PatientIllness(Resource):

    @api.doc('get patient illness details')
    @api.marshal_with(patientIllness)
    def get(self, id):
        '''returns the illness details for a patient'''
        return patientDao.getPatientIllness(id), 200

    @api.doc('add new patient illness')
    @api.expect(newIllnessDetail)
    def post(self, id):
        '''add new patient illness'''
        input = api.payload
        input['patientId'] = id
        patientDao.addNewIllness(input)
        return input, 201

@api.route('patient/<id>/immunisationDetails')
@api.param('id', 'patient identifier')
@api.response(404, 'Resource Not found')
class PatientImmunisation(Resource):

    @api.doc('get patient immunisation details')
    @api.marshal_with(patientImmunisation)
    def get(self, id):
        '''returns the immunisation details for a patient'''
        return patientDao.getPatientImmunisation(id), 200

    @api.doc('add new patient immunisation')
    @api.expect(newImmunisationDetail)
    def post(self, id):
        '''add new patient immunisation'''
        input = api.payload
        input['patientId'] = id
        patientDao.addNewImmunisation(input)
        return input, 201

@api.route('patient/<id>/labTestDetails')
@api.param('id', 'patient identifier')
@api.response(404, 'Resource Not found')
class PatientLabTests(Resource):

    @api.doc('get patient labTest details')
    @api.marshal_with(patientLabTests)
    def get(self, id):
        '''returns the labTest details for a patient'''
        return patientDao.getPatientLabDetails(id), 200

    @api.doc('add new patient labTest details')
    @api.expect(newLabTestDetail)
    def post(self, id):
        '''add new patient labTest'''
        input = api.payload
        input['patientId'] = id
        patientDao.addNewLabTest(input)
        return input, 201

@api.route('patient/<id>/hospitalisation')
@api.param('id', 'patient identifier')
@api.response(404, 'Resource Not found')
class PatientAdmission(Resource):

    @api.doc('get patient hospitalisation details')
    @api.marshal_with(patientHospitalisationDetails)
    def get(self, id):
        '''returns the hospitalisation details for a patient'''
        return patientDao.getPatientHospitalisationDetails(id), 200

    @api.doc('admit new patient')
    @api.expect(admitPatient)
    def post(self, id):
        '''admit a new patient'''
        patientDao.admitPatient(id)
        patientInfo = api.payload
        patientInfo['patientId'] = id
        print(patientInfo)
        patientCareDao.insertPatientCare(patientInfo)
        return 'Patient {} has been admitted successfully'.format(id), 201

    @api.expect(dischargePatient)
    @api.doc('discharge patient')
    def put(self, id):
        '''discharge a new patient'''
        followUpDate = api.payload
        followUpDate['patientId'] = id
        billId = billDao.getBillIdByPatientId(followUpDate)
        if billId == None:
            return 'Please proceed to billing first.', 400
        patientDao.dischargePatient(id)

        if followUpDate['followUpDate'] is not None :
            followUpDate['billId'] = billId[0]
            patientCareDao.updateFollowUpDate(followUpDate)
        return 'Patient {} discharged successfully'.format(id), 200