# with open("demo.file","r") as file:#with is used to open the file and it will automatically close the file after performing the operations on it and instead of demo.file we can give path of the file also like r"D:/PYTHON/PYTHON 2026/SKILL LAB --APR--2026/DAY 05/CLASS PROGRAM/demo.file"
#     print(file.readline())#reading the first line from the file and it will return the first line of the file and it will also move the file pointer to the next line
#     print(file.readline())#reading the second line from the file and it will return the second
#     print(file.readlines())#reading all the remaining lines from the file and it will return a list of all the remaining lines in the file and it will also move the file pointer to the end of the file
#     for line in file.readlines():#iterating through each line in the file and storing it in a variable called line
#         print(line)





words=[]
with open("demo.file","r") as f: #with is used to open the file and it will automatically close the file after performing the operations on it and instead of demo.file we can give path of the file also like r"D:/PYTHON/PYTHON 2026/SKILL LAB --APR--2026/DAY 05/CLASS PROGRAM/demo.file"
    for line in f.readlines():#iterating through each line in the file and storing it in a variable called line
        for word in line.split():#splitting the line into words and storing it in a variable called word and split method will split the line into words based on the space and it will return a list of words in the line
            words.append(word)#appending the word to the list of words and it will add the word to the end of the list

print(words)
print(len(words))