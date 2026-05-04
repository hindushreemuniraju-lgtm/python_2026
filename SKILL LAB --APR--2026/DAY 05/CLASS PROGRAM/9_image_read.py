with open("images.jpg","rb") as file:
    content=file.read()   #reading the data from the file and storing it in a variable called content
    
    with open ("dem1.jpg","wb") as file:
        file.write(content)