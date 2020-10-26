# -*- coding: utf-8 -*-

from flask_restx import Namespace, Resource, fields
from uuid import uuid4
from dao.adminDao import *
from dao.employeeDao import *

adminDao = AdminDao()
employeeDao = EmployeeDao()
api = Namespace('admin', description='Admin related operations')

newAdmin = api.model('NewAdmin', {
        'first_name' : fields.String(required = True, description = 'admin first name'),
        'last_name' : fields.String(required = True, description = 'admin last name'),
        'dob' : fields.String(required = True, description = 'admin date of birth'),
        'email' : fields.String(required = True, description = 'admin email id')        
        })

admin = api.inherit('Admin', newAdmin, {
        'id':fields.String(required=True, description = 'unique admin id'),
        'status' : fields.String(required=True, description = 'admin status')
        })

updateAdmin = api.inherit('UpdateAdmin', newAdmin, {
    'status' : fields.String(required=True, description = 'admin status')
})

ADMINS = [
        {'id' : '1', 'first_name' : 'admin_1'}
        ]

@api.route('admin')
class AdminList(Resource):
    @api.doc('list admins')
    @api.marshal_list_with(admin)
    def get(self):
        '''returns a list of all admins'''
        return adminDao.fetchAllAdmins()
    
    @api.doc('onboard new Employee Admin')
    @api.expect(newAdmin)
    @api.marshal_with(admin)
    def post(self):
        '''onboard a new Admin employee'''
        input = api.payload
        input['id'] = str(uuid4())
        input['status'] = 'active'
        input['isAdmin'] = True
        employeeDao.addNewEmployee(input)
        return input, 201
        
    
@api.route('admin/<id>')
@api.param('id', 'admin identifier')
@api.response(404, 'Resource Not found')
class Admin(Resource):
    
    @api.doc('get admin')
    @api.marshal_with(admin)
    def get(self, id):
        '''get admin by input id'''
        for admin in adminDao.fetchAllAdmins():
            if admin['id'] == id:
                return admin
        api.abort(404, "Admin {} doesn't exist".format(id))
        
    @api.doc('update admin detail')
    @api.expect(updateAdmin)
    @api.marshal_with(admin)
    def put(self, id):
        '''update an admin details'''
        admin = self.get(id)
        admin.update(api.payload)
        #audit admin update
        ADMINS.append(admin)
        return admin,200
    
    @api.doc('delete an admin')
    def delete(self, id):
        '''Delete an Admin'''
        adminDao.deleteAdmin(id)
        return 'admin {} deleted successfully'.format(id), 200

    @api.doc('grant admin access to an employee')
    def post(self, id):
        '''add a new admin to system'''
        adminDao.addAdmin(id)
        return 'Admin {} added successfully'