# -*- coding: utf-8 -*-

from flask_restx import Api

from .patient import api as ns1
from .careProvider import api as ns2
from .admin import api as ns3

api = Api (
        title='EMR API',
        version='1.0.0',
        description='An API to manage EMR operations'
        )

api.add_namespace(ns1, path='/')
api.add_namespace(ns2, path='/')
api.add_namespace(ns3, path='/')