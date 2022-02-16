def salaryslip(name, salary):
    if salary>=2000:
        tax=salary*20/100
    else:
        tax=salary*15/100
    netsalary=salary-tax
    print("Name of Employee:", name)
    print("Salary:", salary)
    print("Tax:", tax)
    print("Net Salary:", netsalary)

salaryslip("James",5000)
salaryslip("Peter",4000)
salaryslip("Emma",1000)
salaryslip("Brenda",1500)
