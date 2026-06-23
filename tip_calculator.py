#welcome to the tip calculator
bill= float(input("what is the bill in indian rupees?"))
tip_percent=int(input("what is the percent of your tip? 10,15 or 20?"))
people=int(input("what is the number of spitting people?"))
tip_amount=bill*tip_percent/100
total_bill=bill+tip_amount
bill_per_person=bill*people/100

print("\n-------Bill Summary--------")
print(f"Total bill is:rs {total_bill} ")
print(f"total amount is: rs {tip_amount} ")
print(f"Total bill  each person should pay is: rs{bill_per_person } ")