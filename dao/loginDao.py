from dao.dbConnector import *
from dao.queries import *

class LoginDao:

    def __init__(self):
        self.dbObject = DBConnector()
        self.connection, self.cursor = self.dbObject.getConnector()

    def authenticate(self, userId):
        '''validate that a valid user exists and returns a hashed passwd'''
        self.cursor.execute(QUERIES['FETCH_LOGIN'])
        result = self.cursor.fetchall()

        for (id, passwd) in result:
            if id == userId :
                return passwd
        return None