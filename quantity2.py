quantity=20
price=30
bill=quantity*price
vat=bill*20/100
print("Quantity:",quantity)
print("Unit Price:",price)
print("---------------------------")
print("Total exc. VAT:",bill)
print("VAT: $",vat)
print("Total to pay: $",bill+vat)
print("---------------------------")