num=int(input("Enter the number:"))
mid=num//2
left=mid
right=mid

for row in range (num):
    for col in range(num):
        if col==left or col==right:
            print("#",end=" ")
            
        else:
            print(" ",end=" ")
    if row>=mid:
        left+=1
        right-=1
    else:
        left-=1
        right+=1
    print()
