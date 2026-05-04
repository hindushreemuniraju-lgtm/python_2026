num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))

if num1>num2 and num1>num3:               # multiple statement or conditions are used 
   print("largest number is : ", num1)

elif num2>num1 and num2>num3:
   print("largest number is : ", num2)    # logical operator used in conditions i.e only when both the conditions are true condition statement is exceuted

else:
   print("largest number is : ", num3)
   
c=num1+num2+num3    # arithmetic operator is used + 
d=num1*num2*num3
e=c/2

print(c)
print(d)
print(e)