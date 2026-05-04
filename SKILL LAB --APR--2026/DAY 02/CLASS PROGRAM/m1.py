num = int(input("Enter a number: "))

count = 0
temp = num

if temp == 0:
    count = 1
else:
    if temp < 1:    
        temp = -temp
    while temp > 0:
        temp //= 10   
        count += 1

print("Number of digits:", count)