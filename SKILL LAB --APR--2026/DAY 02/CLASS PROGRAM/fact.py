num = int(input("Enter a non-negative integer: "))

factorial = 1

if num < 0:
    print("Factorial doesn't exist for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    i = 1
    while i <= num:
        factorial *= i   
        i += 1
    print(f"Factorial of {num} is {factorial}")