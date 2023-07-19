size = input("Which size of pizza ? S, M or L : ")
pepperoni = input("Do you want pepperoni? Y or N : ")
cheese = input("Do you want extra cheese ? Y or N : ")

bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25

if pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if cheese == 'Y':
    bill += 1

print(f"Your total bill is {bill}.")