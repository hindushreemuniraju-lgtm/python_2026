# def hi():
#     print("hiii")
#     print("hiii")
#     print("hiii")
#     print("hiii")
#     print("hiii")
#     print("hiii")

# hi()

#Positional arguments
# def add(a,b,c):
#     print(f"a is{a}and b is {b} and c is {c}")
# add(5,6,7)


#variable arguments
# def add(*b):
#     print(sum(b))

# add(5,6,7)

#keyword arguments
# def login(username,password):
#     print(f"username is {username} and password is {password}")

# login(username="divya",password="123")

#keyword variable arguments
# def register(**b):
#     print(b)
# register(username="mayank",age=35,mobile=1234567890)


#default arguments
# def register(age=18):
#     print(age)
# register(25)

#a = 5#global variable
# def hi():
#     a=10
#     print(a)
#     globals()['a']=15 #method to change global variable inside a function
#     def inner():
#         print(a) #non local varaible
#     inner() 
# hi()
# print(a)





