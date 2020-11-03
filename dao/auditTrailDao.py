from dao.dbConnector import *
from dao.queries import *
from .employeeDao import *

class AuditTrailDao:
    '''handles audit trail for Entity updates'''

    def __init__(self):
        self.dbObject = DBConnector()
        self.connection, self.cursor = self.dbObject.getConnector()

    def insertAuditTrail(self, auditEntry):
        '''inserts a new record for each entity update'''
        self.cursor.execute(QUERIES['ADD_AUDIT'], auditEntry)
        self.cursor.execute('commit')

    def getAuditInfo(self, id):
        '''returns a list of audit trail for input entity Id'''
        auditRecords = []
        self.cursor.execute(QUERIES['GET_AUDIT_TRAIL'].format(id))
        result = self.cursor.fetchall()

        for(id, entityId, entityType, attributeUpdated, previousValue, newValue, changedBy, updatedOn) in result :
            auditRecords.append({
                'id': id,
                'entityId': entityId,
                'entityType': entityType,
                'attributeUpdated': attributeUpdated,
                'previousValue': previousValue,
                'newValue': newValue,
                'changedBy': changedBy,
                'updatedOn' : updatedOn
            })
        return auditRecords


