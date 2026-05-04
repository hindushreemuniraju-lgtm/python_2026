students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i+1)
    
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    
    students[roll] = {"name": name, "age": age}

print("\nStudent Dictionary:")
print(students)