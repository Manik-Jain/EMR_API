# -*- coding: utf-8 -*-

class Patient():
    def __init__(self):
        self.counter = 0
        self.name = ''
        self.patients = []
        
    def get(self, id):
        for patient in self.patients:
            if patients['id'] == id:
                return patient
        api.abort(404, "Patient {} doesn't exist".format(id))
        
    def create(self, data):
        patient = data
        patient['id'] = self.counter = self.counter + 1
        self.patients.append(patient)
        return patient