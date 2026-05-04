# n = int(input("Enter a number: "))

# if n <= 1:
#     print("Not a prime number")
# else:
#     i = 2
#     is_prime = True

#     while i <= n // 2:
#         if n % i == 0:
#             is_prime = False
#             break
#         i += 1

#     if is_prime:
#         print("Prime number")
#     else:
#         print("Not a prime number")



num=int(input("Enter a number:"))
for num in range(10,61):
   for i in range(2,num):
      if num%i==0:
         break
   else:
    print(num)