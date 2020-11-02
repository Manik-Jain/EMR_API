# -*- coding: utf-8 -*-

from flask_restx import Api

from .patient import api as patient
from .careProvider import api as careProvider
from .admin import api as admin
from .login import api as login
from .bill import api as bill
from .audit import api as audit
from .patientAddress import api as patientAddress
from .patientAdmission import api as patientAdmission
from .patientMedicalHistory import api as patientMedicalHistory
from .patientNote import api as patientNote

api = Api (
        title='EMR API',
        version='1.0.0',
        description='An API to manage EMR operations'
        )

api.add_namespace(patient, path='/')
api.add_namespace(careProvider, path='/')
api.add_namespace(admin, path='/')
api.add_namespace(login, path='/')
api.add_namespace(bill, path='/')
api.add_namespace(audit, path='/')
api.add_namespace(patientAddress, path = '/')
api.add_namespace(patientAdmission, path = '/')
api.add_namespace(patientMedicalHistory, path = '/')
api.add_namespace(patientNote, path = '/')