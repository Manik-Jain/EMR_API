# -*- coding: utf-8 -*-

from flask_restx import Namespace, Resource, fields
from dao.careProviderDao import *
from dao.employeeDao import *
from uuid import uuid4

api = Namespace('careProvider', description='Care Providers related operations')
careProviderDao = CareProviderDao()
employeeDao= EmployeeDao()

newCareProvider = api.model('NewCareProvider', {
        'first_name' : fields.String(required = True, description = 'CareProvider first name'),
        'last_name' : fields.String(required = True, description = 'CareProvider last name'),
        'dob' : fields.String(required = True, description = 'CareProvider date of birth'),
        'email' : fields.String(required = True, description = 'CareProvider email id')
        })

careProvider = api.inherit('CareProvider', newCareProvider, {
        'id':fields.String(required=True, description = 'unique careProvider id'),
        'per_visit_charges' : fields.String(required=True, description = 'careProvider per_visit_charges'),
        'status' : fields.String(required=True, description = 'careProvider status')
        })

updateCareProvider = api.inherit('UpdateCareProvider', newCareProvider, {
    'per_visit_charges' : fields.String(required=True, description = 'careProvider per_visit_charges')
})

@api.route('careProvider')
class CareProviderList(Resource):
    @api.doc('list careProviders')
    @api.marshal_list_with(careProvider)
    def get(self):
        '''returns a list of all careProviders'''
        return careProviderDao.fetchAllCareProviders()

    @api.doc('onboard a new care Provider employee')
    @api.marshal_with(careProvider)
    @api.expect(newCareProvider)
    def post(self):
        '''onboard a new care provider employee'''
        input = api.payload
        input['id'] = str(uuid4())
        input['per_visit_charges'] = '40'
        input['isAdmin'] = False
        employeeDao.addNewEmployee(input)
        return input, 201
    
@api.route('careProvider/<id>')
@api.param('id', 'careProvider identifier')
@api.response(404, 'Resource Not found')
class CareProvider(Resource):

    @api.doc('get careProvider')
    @api.marshal_with(careProvider)
    def get(self, id):
        '''get careProvider by input id'''
        for careProvider in careProviderDao.fetchAllCareProviders():
            if careProvider['id'] == id:
                return careProvider
        api.abort(404, "Care Provider {} doesn't exist".format(id))

    @api.doc('delete a care provider')
    def delete(self, id):
        '''delete a care provider from system'''
        careProviderDao.deleteCareProvider(id)
        return 'careProvider {} deleted successfully'.format(id), 200


