a=str(input("enter the character , name or anything in the fomate of string"))


if a==a[::-1]:
    print(f" {a} is palindromic ")

else:
    print(f"{a} is not palindromic")



a = input("Enter text: ").replace(" ", "").lower()

if a == a[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")