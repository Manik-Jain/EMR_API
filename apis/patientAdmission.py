from flask_restx import Namespace, Resource, fields
from dao.billDao import *
from services.updateService import *
from dao.patientCareDao import *

api = Namespace('patientAdmission', description='Patients Admission related operations')
patientDao = PatientDao()
updateService = UpdateService()
patientCareDao = PatientCareDao()
billDao = BillDao()

patientHospitalisationDetails = api.model('PatientHospitalisationDetails', {
    'id' : fields.Integer(required=True, description = "unique admission id"),
    'admitDate' : fields.DateTime(required = True, description = "patient admit date"),
    'dischargeDate' : fields.DateTime(description = "patient discharge date"),
    'isDischarged' : fields.Boolean(required=True, description='true if patient has been discharged, false otherwise')
})

admitPatient = api.model('Admit Patient', {
    'careProviderId' : fields.String(required = True, description = 'care provider id')
})

dischargePatient = api.model('dischargePatient', {
    'admissionId' : fields.Integer(required = True, description = 'admission id of patient'),
    'followUpDate' : fields.String(description = 'the patient followUp date')
})

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