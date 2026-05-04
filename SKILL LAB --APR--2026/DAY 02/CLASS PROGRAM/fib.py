num=int(input("enter the number :"))
total=0
while num>0:
    last=num%10
    total=total*10+last
    num=num//10
print(total)