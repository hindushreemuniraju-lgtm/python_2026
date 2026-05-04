num = int(input("Enter the number: "))

for row in range(num):
    for col in range(num):
        if (col == 0 or 
            (row == 0 and col < num-1) or 
            (row == num//2 and col < num-1) or 
            (col == num-1 and row > 0 and row < num//2)):
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()