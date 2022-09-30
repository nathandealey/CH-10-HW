class PayrollDeduction:
    def __init__(self, desrciption, date, charge, employeeID):
        self.empdescription = desrciption
        self.empdate = date
        self.empcharge = charge
        self.empemployeeID = employeeID

    def getdescription(self):
        return self.empdescription
    
    def getdate(self):
        return self.empdate
    
    def getcharge(self):
        return self.empcharge
    
    def getemployeeID(self):
        return self.empemployeeID