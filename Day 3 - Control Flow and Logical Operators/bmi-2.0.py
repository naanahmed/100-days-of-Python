height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print (f'Your bmi is {bmi}, You are underweight')
elif bmi < 25:
    print (f'Your bmi is {bmi}, Your weight is normal')
elif bmi < 30:
    print (f'Your bmi is {bmi}, You are overweight')
elif bmi < 35:
    print (f'Your bmi is {bmi}, You are obese')
else:
    print (f'Your bmi is {bmi}, You are clinically obese')