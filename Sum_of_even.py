#Write your code below this row 👇
n = int(input("Enter a number (till where you want to add even numbers): "))
sum=0
for i in range(n):
  if i%2==0:
    sum = sum + i
  else:
    continue
print(sum)
    

