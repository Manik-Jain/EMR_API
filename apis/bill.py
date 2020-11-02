from flask_restx import Namespace, Resource, fields
from uuid import uuid4
from datetime import datetime
from dao.billDao import *
from dao.patientDao import *
from dao.patientCareDao import *
import datetime

api = Namespace('bill', description='Billing related operations')
billDao = BillDao()
patientDao = PatientDao()
patientCareDao = PatientCareDao()

dollarToEthConversion = 0.0026
perDayDollarCharge = 38.5

newBill = api.model('Bill', {
    'patientId' : fields.String(required = True, description = 'unique patient Id'),
    'admissionId' : fields.Integer(description = 'unique admission Id'),
    'adminCharges' : fields.Float(required = True, description = 'admin charges'),
    'labCharges' : fields.Float(description = 'lab charges')
})

patientBill = api.inherit('PatientBill', newBill, {
    'id' : fields.Integer(required = True, description = 'unique bill Id'),
    'amount' : fields.Float(required = True, description = 'bill amount'),
    'etherAmount' : fields.Float(required = True, description = 'bill amount in Ethers'),
    'message' : fields.String(required = True, description = 'message to caller'),
    'isPaid' : fields.Boolean(required=True, description='true if bill is paid, False otherwise')
})

@api.route('bill')
class Bill(Resource) :

    @api.doc('generate bill')
    @api.marshal_with(patientBill)
    @api.expect(newBill)
    def post(self):
        '''Generate a new billing for a patient'''
        input = api.payload
        admissionDetail = patientDao.getAdmissionDetail(input['patientId'], input['admissionId'])

        print(admissionDetail)
        if admissionDetail['isDischarged'] == 1:
            input['message'] = 'Patient already discharged'
            return input, 400

        patientDetail = patientDao.fetchPatient(input['patientId'])

        print(patientDetail)

        #to add smart contract integration here
        # if patientDetail['consentToShare']:
        #     pass

        admittedDays = (datetime.datetime.today() - admissionDetail['admitDate']).days

        input['id'] = billDao.generateBillId()
        input['amount'] = input['adminCharges'] + input['labCharges'] + (perDayDollarCharge * admittedDays)
        input['etherAmount'] = input['amount'] * dollarToEthConversion
        billDao.generateBill(input)
        patientCareDao.updateBillingId(input)
        input['message'] = 'Bill generated successfully'
        return input, 201

    @api.doc('fetch all bill details')
    @api.marshal_with(patientBill)
    def get(self):
        '''return a list of all bills generated in system'''
        return billDao.fetchAllBills(), 200

@api.route('bill/<id>')
@api.param('id', 'bill identifier')
@api.response(404, 'Resource Not found')
class Billing(Resource) :

    @api.doc('get bill details')
    @api.marshal_with(patientBill)
    def get(self, id):
        '''return bill details for a specific id'''
        return billDao.fetchBillById(id), 200

    @api.doc('pay bill')
    def put(self, id):
        '''pay bill amount for a specific id'''
        billDao.payBill(id)
        return 'Bill {} paid successfully'.format(id), 200
