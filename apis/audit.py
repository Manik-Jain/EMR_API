from flask_restx import Namespace, Resource, fields
from dao.auditTrailDao import *

api = Namespace('auditTrail', description='Audit operations')
auditTrailDao = AuditTrailDao()

auditTrail = api.model('AuditTrail', {
    'id' : fields.Integer(required = True, description = 'audit trail id'),
    'entityId' : fields.String(required = True, description = 'entity (Patient/Admin/CareTaker) id'),
    'entityType' : fields.String(required = True, description = 'the entity Type (Patient/Admin/CareTaker)'),
    'attributeUpdated' : fields.String(required=True, description = 'signify the updated attribute'),
    'previousValue' : fields.String(description = 'the previous value for the attribute'),
    'newValue' : fields.String(required = True, description = 'the updated attribute value'),
    'changedBy' : fields.String(required = True, description = 'the name of the updating user'),
    'updatedOn' : fields.DateTime(required = True, description = 'the date when this attribute was updated')
})

@api.route('audit/<id>')
@api.param('id', 'entity identifier')
@api.response(404, 'Resource Not found')
class AuditTrail(Resource):

    @api.doc('get audit trail info')
    @api.marshal_list_with(auditTrail)
    def get(self, id):
        '''get audit trail by input entity id'''
        print('audit trail accessed')
        return auditTrailDao.getAuditInfo(id), 200