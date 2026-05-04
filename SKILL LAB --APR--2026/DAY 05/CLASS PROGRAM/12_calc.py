from tkinter import *

window = Tk()
window.geometry("350x550")
window.config(bg="#0B0D0E")

# Variable
expression = StringVar()
expression.set("")

# Function
def click(value):
    current = expression.get()

    if value == "=":
        try:
            result = str(eval(current))
            expression.set(result)
        except:
            expression.set("Error")

    elif value == "C":
        expression.set("")

    else:
        expression.set(current + value)

# Display
Label(window, textvariable=expression,
      height=3, width=20,
      bg="#0B0D0E", fg="white",
      font=("Arial",16,"bold")).grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    ("9","8","7","/"),
    ("6","5","4","*"),
    ("3","2","1","-"),
    ("C","0","=","+")
]

# Create buttons using loop (cleaner but same idea)
for i in range(4):
    for j in range(4):
        text = buttons[i][j]
        Button(window,
               text=text,
               width=5,
               height=3,
               bg="#1976D2",
               fg="white",
               font=("Arial",16,"bold"),
               command=lambda t=text: click(t)
        ).grid(row=i+1, column=j)

window.mainloop()