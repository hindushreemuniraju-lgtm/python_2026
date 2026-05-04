file=open("demo.file","r")# r is for read mode and instead of demo.file we can give path of the file also like r"D:/PYTHON/PYTHON 2026/SKILL LAB --APR--2026/DAY 05/CLASS PROGRAM/demo.file"
index=1
for line in file:   #iterating through each line in the file and storing it in a variable called line
    print(f"Line {index}: {line}",end="")   #printing the line number and the line which is read from the file and end="" is used to avoid adding a new line after each line is printed because each line already has a new line character at the end of it
    index+=1   #incrementing the index by 1 after printing each line
file.close()   #closing the file and its important to close the file after performing the operations on it