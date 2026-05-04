file=open("demo.file","w")   #creating a file and opening it in write mode and instead of demo.file we can give path of the file also like r"D:/PYTHON/PYTHON 2026/SKILL LAB --APR--2026/DAY 05/CLASS PROGRAM/demo.file"
file.write("New value is added\n")   #writing some data into the file
file.write("hello world\n") 
file.close()   #closing the file and its important to close the file after performing the operations on it


file=open("demo.file","a")   # a is for append mode and it will not overwrite the existing data in the file and instead it will add the new data at the end of the file and instead of demo.file we can give path of the file also like r"D:/PYTHON/PYTHON 2026/SKILL LAB --APR--2026/DAY 05/CLASS PROGRAM/demo.file"
file.write("hello world\n")   #writing some data into the file
file.write("hello world\n") 
file.close()   #closing the file and its important to close the file after performing the operations on it
