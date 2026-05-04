num=int(input("enter the number:"))
original=num
total=0

while num>0:
    last=num%10
    total=total*10+last
    num=num//10

if original==total:
    print("palindrome")

else:
    print("not palindrome")