def Tax(salary):
    T=salary*21/100
    return T

salary=int(input("Enter your salary: "))
netsalary=salary-Tax(salary)

print("Gross Salary",salary)
print("Tax",Tax(salary))
print("Net Salary", netsalary)