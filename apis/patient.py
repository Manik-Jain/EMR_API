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