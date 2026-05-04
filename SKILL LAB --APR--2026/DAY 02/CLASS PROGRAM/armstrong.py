num = int(input("Enter a number: "))

temp = num
sum = 0

while temp > 0:
    d = temp % 10
    sum = sum + d**3
    temp = temp // 10

    print(sum)
    print(num)

if num == sum:
    print("Armstrong number")
else:
    print("Not Armstrong")