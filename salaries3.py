salaries=[300,3982,845,920,46]

i=1
big=salaries[0]

while i<len(salaries):
    if salaries[i]>big:
        big=salaries[i]
    
    i=i+1

print("Highest number is:",big)
