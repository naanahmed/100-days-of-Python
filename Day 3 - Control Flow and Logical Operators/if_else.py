print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input('Please enter your age'))
    if age < 12:
        print('Please pay 5 birr')
    if age <= 18 :
        print('Please pay 7 birr')
    else:
        print('Please pay 12 birr')
else:
    print("Sorry, you have to be taller to ride.")