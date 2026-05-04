num = 5

for row in range(num):
    for col in range(num):
        if col == 0 or col == num-1 or row == num//2:
            print("#", end="")
        else:
            print(" ", end="")
    print()
print(" ")



for row in range(num):        
    for col in range(num):    
        if row == 0 or row == num - 1 or col == num // 2:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()
print(" ")

for row in range(num):       
    for col in range(num):
        if col == 0 or col == num - 1 or row == col:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()
print(" ")





for row in range(num):
    for col in range(num):
        if col == 0 or \
           (row == 0 and col < num - 1) or \
           (row == num - 1 and col < num - 1) or \
           (col == num - 1 and row != 0 and row != num - 1):
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()
print(" ")



for row in range(num):
    for col in range(num):
        if col == 0 or col == num - 1 or row == num - 1:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()
print(" ")