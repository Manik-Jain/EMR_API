from flask_restx import Namespace, Resource, fields
from dao.loginDao import *
from flask import request

loginDao = LoginDao()
api = Namespace('login', description='allows to authenticate user')

@api.route('login/<id>')
class PatientList(Resource):

    @api.doc('validate')
    def get(self, id):
        '''returns a hash of stored password for input id'''
        print(request.headers)
        print('accessing api with id : {}'.format(id))
        return {'response' : loginDao.authenticate(id)}, 200