file=open("demo.file","r")   # r is for read mode and it will read the data from the file and instead of demo.file we can give path of the file also like r"D:/PYTHON/PYTHON 2026/SKILL LAB --APR--2026/DAY 05/CLASS PROGRAM/demo.file"
print(file.tell())   #printing the current position of the file pointer and it will be 0 because we have just opened the file and the file pointer is at the beginning of the file
content=file.read(6)   #reading the first 6 characters from the file and storing it in a variable called content
print(file.tell())#fter reading the first 6 characters from the file the file pointer will move to the 7th character and when we print the current position of the file pointer it will be 6 because we have read 6 characters from the file
file.seek(0)   #moving the file pointer to the beginning of the file and it will move the file pointer to the 0th position
print(content)   #printing the content which is read from the file and it will be the first 6 characters of the file
file.close()   #closing the file and its important to close the file after performing the operations on it