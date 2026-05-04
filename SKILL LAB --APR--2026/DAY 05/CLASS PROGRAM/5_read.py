file=open("demo.file","r")# r is for read mode and instead of demo.file we can give path of the file also like r"D:/PYTHON/PYTHON 2026/SKILL LAB --APR--2026/DAY 05/CLASS PROGRAM/demo.file"
content=file.read()  #reading the data from the file and storing it in a variable called data
print(content)   #printing the data which is read from the file
print(type(content))  #printing the type of the data which is read from the file and it will be string because read method returns a string 
file.close()   #closing the file and its important to close the file after performing the operations on it