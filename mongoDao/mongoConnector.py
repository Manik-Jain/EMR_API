import pymongo
from initialiseDatabase.initDB import *

class MongoConnector:
    '''handles connection to MongoDb cluster'''

    def __init__(self):
        self.client = pymongo.MongoClient(MONGO_URL)

    def getMongoClient(self):
        return self.client
