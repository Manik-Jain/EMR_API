from flask_restx import Namespace, Resource, fields
from services.updateService import *

api = Namespace('patientNote', description='Patients Note related operations')
patientDao = PatientDao()
updateService = UpdateService()

newPatientNote = api.model('NewPatientNote', {
    'note' : fields.String(required = True, desctiption = 'note to be added'),
    'writtenBy' : fields.String(required = True, description = 'care Provider Id')
})

patientNotes = api.inherit('PatientNotes', newPatientNote, {
        'id' : fields.Integer(description = 'note id'),
        'patientId' : fields.String(required = True, desctiption = 'patient id'),
        'writtenOn' : fields.String(description = 'date when the note was written')
        })

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

