from dao.dbConnector import *
from dao.queries import *

class BillDao:
    '''handles database operations for Billing'''

    def __init__(self):
        self.dbObject = DBConnector()
        self.connection, self.cursor = self.dbObject.getConnector()

    def generateBillId(self):
        self.cursor.execute(QUERIES['GENERATE_BILL_ID'])
        result = self.cursor.fetchone()
        return result[0]

    def generateBill(self, input):
        '''generate a billing in the system'''
        print(input)
        self.cursor.execute(QUERIES['GENERATE_BILL'], input)
        self.cursor.execute('commit')

    def fetchAllBills(self):
        bills = []
        self.cursor.execute(QUERIES['FETCH_ALL_BILLS'])
        result = self.cursor.fetchall()

        for(id, patientId, admissionId, adminCharges, labCharges, amount, createdOn, etherAmount, isPaid) in result:
            bills.append({
                'id' : id,
                'patientId' : patientId,
                'admissionId' : admissionId,
                'adminCharges' : adminCharges,
                'labCharges' : labCharges,
                'amount' : amount,
                'createdOn' : createdOn,
                'etherAmount' : etherAmount,
                'isPaid' : isPaid
            })
        return bills

    def fetchBillById(self, id):
        for bill in self.fetchAllBills():
            if str(bill['id']) == id:
                return bill

    def payBill(self, id):
        self.cursor.execute(QUERIES['PAY_BILL'].format(int(id)))
        self.cursor.execute('commit')

    def getBillIdByPatientId(self, dischargeDetail):
        '''check if patient has paid the bill'''
        self.cursor.execute(QUERIES['GET_BILL_ID_BY_PATIENT'], dischargeDetail)
        billId = self.cursor.fetchone()
        return billId