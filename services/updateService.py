from dao.auditTrailDao import *
from dao.employeeDao import *
from dao.adminDao import *
from dao.patientDao import *
from dao.careProviderDao import *

import datetime

class UpdateService:

    def __init__(self):
        '''common update service for updating records in database'''

    def updateAdmin(self, currAdmin, newAdmin):
        '''update Admin records in database'''
        auditEntries = []
        auditEntry = {
            'entityId': currAdmin['id'],
            'entityType': 'ADMIN',
            'changedBy': newAdmin['changedBy']
        }

        if currAdmin['first_name'].lower() != newAdmin['first_name'].lower():
            firstNameAduit =  {
                'previousValue' : currAdmin['first_name'],
                'newValue' : newAdmin['first_name'],
                'auditType' : 'NAME'
            }
            auditEntries.append({**auditEntry, **firstNameAduit})

        if currAdmin['last_name'].lower() != newAdmin['last_name'].lower():
            lastNameAduit = {
                'previousValue': currAdmin['last_name'],
                'newValue': newAdmin['last_name'],
                'auditType': 'NAME'
            }

            auditEntries.append({**auditEntry, **lastNameAduit})

        if newAdmin['dob'].upper() != str(datetime.datetime.strptime(currAdmin['dob'], '%Y-%m-%d').strftime("%d-%b-%Y")):
            print('inside')
            dobAudit = {
                'previousValue': str(datetime.datetime.strptime(currAdmin['dob'], '%Y-%m-%d').strftime("%d-%b-%Y")).upper(),
                'newValue': str(newAdmin['dob']).upper(),
                'auditType': 'DOB'
            }

            auditEntries.append({**auditEntry, **dobAudit})

        if currAdmin['email'].lower() != newAdmin['email'].lower():
            emailAudit = {
                'previousValue': currAdmin['email'],
                'newValue': newAdmin['email'],
                'auditType': 'CONTACT_INFO'
            }
            auditEntries.append({**auditEntry, **emailAudit})

        if currAdmin['status'].lower() != newAdmin['status'].lower():
            statusAudit = {
                'previousValue': currAdmin['status'],
                'newValue': newAdmin['status'],
                'auditType': 'STATUS'
            }
            auditEntries.append({**auditEntry, **statusAudit})

        if len(auditEntries) > 0 :
            employeeDao = EmployeeDao()
            adminDao = AdminDao()

            employeeDao.updateEmployee(newAdmin, currAdmin['id'])
            adminDao.updateAdmin(currAdmin['id'])

            audtTrailDao = AuditTrailDao()
            for entry in auditEntries:
                audtTrailDao.insertAuditTrail(entry)

    def updateCareProvider(self, currCareProvider, newCareProvider):
        '''update care Provider details in database'''
        auditEntries = []
        auditEntry = {
            'entityId': currCareProvider['id'],
            'entityType': 'CARE_PROVIDER',
            'changedBy': newCareProvider['changedBy']
        }

        if currCareProvider['first_name'].lower() != newCareProvider['first_name'].lower():
            firstNameAduit = {
                'previousValue': currCareProvider['first_name'],
                'newValue': newCareProvider['first_name'],
                'auditType': 'NAME'
            }
            auditEntries.append({**auditEntry, **firstNameAduit})

        if currCareProvider['last_name'].lower() != newCareProvider['last_name'].lower():
            lastNameAduit = {
                'previousValue': currCareProvider['last_name'],
                'newValue': newCareProvider['last_name'],
                'auditType': 'NAME'
            }
            auditEntries.append({**auditEntry, **lastNameAduit})

        if newCareProvider['dob'].upper() != str(datetime.datetime.strptime(currCareProvider['dob'], '%Y-%m-%d').strftime("%d-%b-%Y")):
            print('inside')
            dobAudit = {
                'previousValue': str(datetime.datetime.strptime(currCareProvider['dob'], '%Y-%m-%d').strftime("%d-%b-%Y")).upper(),
                'newValue': str(newCareProvider['dob']).upper(),
                'auditType': 'DOB'
            }

            auditEntries.append({**auditEntry, **dobAudit})

        if currCareProvider['email'].lower() != newCareProvider['email'].lower():
            emailAudit = {
                'previousValue': currCareProvider['email'],
                'newValue': newCareProvider['email'],
                'auditType': 'CONTACT_INFO'
            }
            auditEntries.append({**auditEntry, **emailAudit})

        if currCareProvider['per_visit_charges'].lower() != newCareProvider['per_visit_charges'].lower():
            salaryAudit = {
                'previousValue': currCareProvider['per_visit_charges'],
                'newValue': newCareProvider['per_visit_charges'],
                'auditType': 'SALARY'
            }
            auditEntries.append({**auditEntry, **salaryAudit})

        if len(auditEntries) > 0 :
            employeeDao = EmployeeDao()
            careProviderDao = CareProviderDao()
            auditTrailDao = AuditTrailDao()

            employeeDao.updateEmployee(newCareProvider, newCareProvider['id'])
            careProviderDao.updateCareProvider(newCareProvider)

            for entry in auditEntries:
                auditTrailDao.insertAuditTrail(entry)

    #update patient basic info in database
    def updatePatientBasicInfo(self, currPatient, newPatient):
        '''update patient basic info'''
        auditEntries = []
        auditEntry = {
            'entityId': currPatient['id'],
            'entityType': 'PATIENT',
            'changedBy': newPatient['changedBy']
        }

        if currPatient['firstName'].lower() != newPatient['firstName'].lower():
            firstNameAduit =  {
                'previousValue' : currPatient['firstName'],
                'newValue' : newPatient['firstName'],
                'auditType' : 'NAME'
            }
            auditEntries.append({**auditEntry, **firstNameAduit})

        if currPatient['lastName'].lower() != newPatient['lastName'].lower():
            lastNameAduit =  {
                'previousValue' : currPatient['lastName'],
                'newValue' : newPatient['lastName'],
                'auditType' : 'NAME'
            }
            auditEntries.append({**auditEntry, **lastNameAduit})

        if newPatient['dob'].upper() != str(datetime.datetime.strptime(currPatient['dob'], '%Y-%m-%d').strftime("%d-%b-%Y")):
            print('inside')
            dobAudit = {
                'previousValue': str(datetime.datetime.strptime(currPatient['dob'], '%Y-%m-%d').strftime("%d-%b-%Y")).upper(),
                'newValue': str(newPatient['dob']).upper(),
                'auditType': 'DOB'
            }

            auditEntries.append({**auditEntry, **dobAudit})

        if currPatient['email'].lower() != newPatient['email'].lower():
            emailAduit =  {
                'previousValue' : currPatient['email'],
                'newValue' : newPatient['email'],
                'auditType' : 'CONTACT_INFO'
            }
            auditEntries.append({**auditEntry, **emailAduit})

        if currPatient['contactNumber'] != newPatient['contactNumber']:
            contactNumberAduit =  {
                'previousValue' : currPatient['contactNumber'],
                'newValue' : newPatient['contactNumber'],
                'auditType' : 'CONTACT_INFO'
            }
            auditEntries.append({**auditEntry, **contactNumberAduit})

        if currPatient['age'] != newPatient['age']:
            ageAduit =  {
                'previousValue' : currPatient['age'],
                'newValue' : newPatient['age'],
                'auditType' : 'AGE'
            }
            auditEntries.append({**auditEntry, **ageAduit})

        if len(auditEntries) > 0:
            patientDao = PatientDao()
            audtTrailDao = AuditTrailDao()
            newPatient['id'] = currPatient['id']
            patientDao.updatePatientInfo(newPatient)

            for entry in auditEntries:
                audtTrailDao.insertAuditTrail(entry)

    def updatePatientAddressInfo(self, currAddress, newAddress):
        '''update patient address in database'''

        auditEntries = []
        auditEntry = {
            'entityId': newAddress['patientId'],
            'entityType': 'PATIENT',
            'changedBy': newAddress['changedBy'],
            'auditType': 'ADDRESS'
        }

        print(currAddress)
        print(newAddress)
        if currAddress['address_line_1'].lower() != newAddress['address_line_1'].lower():
            auditLine1 = {
                'previousValue' : currAddress['address_line_1'],
                'newValue' : newAddress['address_line_1']
            }
            auditEntries.append({**auditEntry, **auditLine1})

        if currAddress['address_line_2'].lower() != newAddress['address_line_2'].lower():
            auditLine2 = {
                'previousValue': currAddress['address_line_2'],
                'newValue': newAddress['address_line_2']
            }
            auditEntries.append({**auditEntry, **auditLine2})

        if currAddress['city'].lower() != newAddress['city'].lower():
            auditCity = {
                'previousValue': currAddress['city'],
                'newValue': newAddress['city']
            }
            auditEntries.append({**auditEntry, **auditCity})

        if currAddress['postCode'] != newAddress['postCode']:
            auditPostCode = {
                'previousValue': currAddress['postCode'],
                'newValue': newAddress['postCode']
            }
            auditEntries.append({**auditEntry, **auditPostCode})

        if currAddress['country'].lower() != newAddress['country'].lower():
            auditCountry = {
                'previousValue': currAddress['country'],
                'newValue': newAddress['country']
            }
            auditEntries.append({**auditEntry, **auditCountry})

        if len(auditEntries) > 0:
            patientDao = PatientDao()
            audtTrailDao = AuditTrailDao()
            patientDao.updateAddress(newAddress)

            for entry in auditEntries:
                audtTrailDao.insertAuditTrail(entry)




