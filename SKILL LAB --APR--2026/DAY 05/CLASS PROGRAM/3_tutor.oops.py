class student:
    def __init__(self,name,reg,subject1,subject2,subject3):
        self.name = name
        self.reg = reg
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3
    def display(self):
        print(f"Name: {self.name}")
        print(f"Reg No: {self.reg}")
        print(f"Subject 1: {self.subject1}")
        print(f"Subject 2: {self.subject2}")
        print(f"Subject 3: {self.subject3}")
        print(f"Average: {(self.subject1 + self.subject2 + self.subject3)/3}")

count=int(input("Enter the number of students: "))
students_lst = []
for i in range(count):
    name = input("Enter student name: ")
    reg = input("Enter registration number: ")
    subject1 = float(input("Enter marks for subject 1: "))
    subject2 = float(input("Enter marks for subject 2: "))
    subject3 = float(input("Enter marks for subject 3: "))
    
    student_obj = student(name, reg, subject1, subject2, subject3)
    students_lst.append(student_obj)

for student in students_lst:
    student.display()
    