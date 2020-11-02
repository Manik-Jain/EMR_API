from flask_restx import Namespace, Resource, fields
from services.updateService import *

api = Namespace('patientAddress', description='Patients Address related operations')
patientDao = PatientDao()
updateService = UpdateService()

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

patientAddress = api.inherit('PatientAddress', address, {
        'patientId':fields.String(required=True, description = 'unique patient id')
})

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