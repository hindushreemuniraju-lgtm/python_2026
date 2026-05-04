a = float(input("Enter the first side length of the triangle: "))
b = float(input("Enter the second side length of the triangle: "))
c = float(input("Enter the third side length of the triangle: "))

if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
