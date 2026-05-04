num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % 2 != 0:
    num1 += 1

i = num1

while i <= num2:
    print(i)
    i += 2