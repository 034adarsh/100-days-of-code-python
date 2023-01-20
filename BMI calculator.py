# 🚨 Don't change the code below 👇
import math
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight/height**2
BMI1 = round(BMI)
if BMI1<18.5:
    print(f"Your BMI is {BMI1}, you are underweight.")
elif 18.5<=BMI1<=25:
    print(f"Your BMI is {BMI1}, you have a normal weight.")
elif 25<BMI1<=30:
    print(f"Your BMI is {BMI1}, you are slightly overweight.")
elif 30<BMI1<=35:
    print(f"Your BMI is {BMI1}, you are obese.")
elif BMI1>35:
    print(f"Your BMI is {BMI1}, you are clinically obese.")
