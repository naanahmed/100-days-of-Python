print("Welcome to the tip calculator.")
total_bill=input("What was the total bill?\t")
tip_percentage=input("What percentage tip would you like to give?\t")
num_people=input("How many people to split the bill?\t")

total_bill_as_float=float(total_bill)
tip_percentage_as_float=float(tip_percentage)/100
num_people_as_float=float(num_people)

total_tip= total_bill_as_float * tip_percentage_as_float;
total_bill_to_be_paid_by_each_person=total_bill_as_float / num_people_as_float
tip_to_be_paid_by_each_person= total_tip/num_people_as_float;
total_paid_by_each_person= total_bill_to_be_paid_by_each_person + tip_to_be_paid_by_each_person

print(f"Each person should pay : {round(total_paid_by_each_person,2)}")

#Better Solution

print("Welcome to the tip calculator.")
total_bill=input("What was the total bill?\t")
tip_percentage=input("What percentage tip would you like to give?\t")
num_people=input("How many people to split the bill?\t")

total_bill_as_float=float(total_bill)
tip_percentage_as_float=float(tip_percentage)
num_people_as_float=float(num_people)

total_to_be_paid_by_each_person="{:.2f}".format((total_bill_as_float/num_people_as_float) * (1 + (tip_percentage_as_float/100)),2)
print(f"Each person should pay : {total_to_be_paid_by_each_person}")