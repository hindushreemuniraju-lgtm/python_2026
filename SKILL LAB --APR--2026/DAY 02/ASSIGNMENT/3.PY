n = input("Enter a number: ")

digits = list(set(n))   
digits.sort()             

if len(digits) < 2:
    print("No second smallest digit")
else:
    print("Second smallest digit is:", digits[1])