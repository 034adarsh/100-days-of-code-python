# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
x = name1.lower()
y = name2.lower()
total1 = x.count("t") + x.count("r") + x.count("u") + x.count("e") + y.count("t") + y.count("r") + y.count("u") + y.count("e")
total2 = x.count("l") + x.count("o") + x.count("v") + x.count("e") + y.count("l") + y.count("o") + y.count("v") + y.count("e")
score = str(total1)+str(total2)
final = int(score)
if 10>final or final>=90:
    print(f"Your score is {final}, you go together like coke and mentos.")
elif 40<=final<=50:
    print(f"Your score is {final}, you are alright together.")
else:
    print(f"Your score is {final}.")


