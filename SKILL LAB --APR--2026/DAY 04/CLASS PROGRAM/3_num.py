num = int(input("Enter the number: "))

for row in range(num):
    for col in range(row+1):
        print(col+1, end=" ")
    print("")
