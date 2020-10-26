# -*- coding: utf-8 -*-

from flask_restx import Namespace, Resource, fields
from uuid import uuid4
from datetime import datetime

api = Namespace('patient', description='Patients related operations')

patientNotes = api.model('PatientNotes', {
        'note' : fields.String('patient Note'),
        'writtenOn' : fields.String('date when the note was written') 
        })

newPatient = api.model('NewPatient', {
        'name' : fields.String(required = True, description = 'patient name'),
        'age' : fields.Integer(required = True, description = 'patient age'),
        'notes' : fields.List(fields.Nested(patientNotes))
        })

updatePatient = api.model('UpdatePatient', {
        'name' : fields.String(description = 'patient name'),
        'age' : fields.Integer(description = 'patient age'),
        'notes' : fields.List(fields.Nested(patientNotes))
        })

patient = api.inherit('Patient', newPatient, {
        'id':fields.String(required=True, description = 'unique patient id'),
        'updatedOn':fields.String(description = 'patient update time')
        })

PATIENTS = [
        {'id' : '1', 'name' : 'patient_1', 'age' : 25}
        ]

@api.route('patient')
class PatientList(Resource):
    
    @api.doc('list patients')
    @api.marshal_list_with(patient)
    def get(self):
        '''returns a list of all patients'''
        return PATIENTS
    
    @api.doc('add patient')
    @api.marshal_with(patient)
    @api.expect(newPatient)
    def post(self):
        '''Add a new patient'''
        input = api.payload
        input['id'] = str(uuid4())
        #handle patient note date
        PATIENTS.append(input)
        return input, 201
    
@api.route('patient/<id>')
@api.param('id', 'patient identifier')
@api.response(404, 'Resource Not found')
class Patient(Resource):
    
    @api.doc('get Patient')
    @api.marshal_with(patient)
    def get(self, id):
        '''get patient by input id'''
        for patient in PATIENTS:
            if patient['id'] == id:
                return patient
        api.abort(404, "Patient {} doesn't exist".format(id))
        
    @api.doc('delete patient')
    def delete(self, id):
        '''delete a specific patient'''
        patient = self.get(id)
        PATIENTS.remove(patient)
        return "patient {} deleted successfully".format(id), 200
    
    @api.doc('Update Patient record')
    @api.marshal_with(patient)
    @api.expect(updatePatient)
    def put(self, id):
        '''Update a patient record'''
        patient = self.get(id)
        patient.update(api.payload)
        patient['updatedOn'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        PATIENTS.append(patient)
        return patient, 200