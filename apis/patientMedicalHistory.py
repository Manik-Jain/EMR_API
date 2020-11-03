from flask_restx import Namespace, Resource, fields
from services.updateService import *

api = Namespace('patientMedicalHistory', description='Patients Medical history related operations')
patientDao = PatientDao()
updateService = UpdateService()

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