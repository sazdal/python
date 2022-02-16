Bill=int(input("Enter your Bill: "))
Paid=int(input("Enter amount paid: "))
Balance=Paid-Bill
print("Balance = ",Balance)
if Balance>=50:
    fifty=int(Balance/50)
    print("£50: ", fifty)
    Balance=Balance-(fifty*50)
if Balance>=20:
    twenty=int(Balance/20)
    print("£20: ",twenty)
    Balance=Balance-(twenty*20)
if Balance>=10:
    print("£10: 1")
    Balance=Balance-10
if Balance>=5:
    print("£5: 1")
    Balance=Balance-5
if Balance>=2:
    two=int(Balance/2)
    print("£2: ",two)
    Balance=Balance-(two*2)
if Balance>=1:    
    print("£1: 1")
    