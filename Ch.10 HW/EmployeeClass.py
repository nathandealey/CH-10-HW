class Employee:
    def __init__(self, name, ID, department, jobtitle, salary):
        self.empName = name
        self.empID = ID
        self.empDepartment = department 
        self.empJobtitle = jobtitle
        self.empSalary = salary

    def getname(self):
        return self.empName

    def getID(self):
        return self.empID

    def getdepartment(self):
        return self.empDepartment

    def getjobtitle(self):
        return self.empJobtitle
        
    def getsalary(self):
        return self.empSalary
