from EmployeeClass import Employee

from PayrollDeductionClass import PayrollDeduction

employee = Employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800)

deduction1 = PayrollDeduction('food court', '8/14/2022', 22.50, 39119)
deduction2 = PayrollDeduction('gift contribution', '8/12/2022', 25.00, 58475)
deduction3 = PayrollDeduction('food court', '8/17/2022', 15.25, 21547)
deduction4 = PayrollDeduction('vending machine', '8/22/2022', 3.00, 58475)
deduction5 = PayrollDeduction('vending machine', '8/5/2022', 2.75, 58475)

print()
print('* * * * Employee Pay * * * *')
print('Name:         ', employee.getname())
print('ID Number:    ', employee.getID())
print('Department:   ', employee.getdepartment())
print('Gross Pay     $', float(employee.getsalary()), sep = '')
print('Net Pay:      $', employee.getsalary() - deduction2.getcharge() - deduction4.getcharge() - deduction5.getcharge(), sep = '')
print()