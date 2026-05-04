num=int(input("enter the number:"))

total=0
original=num

while num>0:
    last=num%10
    total=total+last**3
    num=num//10

if original==total:
    print("ANGSTROM")

else:
    print("not angstrom")