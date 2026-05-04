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

s1=student("Alice", "12345", 85, 90, 95)
s1.display()
