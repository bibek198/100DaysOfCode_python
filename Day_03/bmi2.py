print("Welcome to BMI 2.0")

weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in m : "))

bmi = round((weight / (height ** 2)), 2)

if (bmi < 18.5):
    print(f"Your BMI is {bmi} and you are underweight.")
elif (bmi < 25):
    print(f"Your BMI is {bmi} and you are normal weight.")
elif (bmi < 30):
    print(f"Your BMI is {bmi} and you are over weight.")
elif(bmi < 35):
    print(f"Your BMI is {bmi} and you are obese.")
else:
    print(f"Your BMI is {bmi} and you are clinically obese.")