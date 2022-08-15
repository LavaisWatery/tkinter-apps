from fileinput import filename
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("Image Selector")

def reopen():
    global image
    global imageLabel
    global statusVariable
    root.filename = filedialog.askopenfilename(initialdir="images/", title="Select an image to open")
    image = ImageTk.PhotoImage(Image.open(root.filename))
    imageLabel = Label(image=image)
    statusVariable.set(root.filename)
    imageLabel.grid(row=0, column=1)

mainLabel = Label()
mainLabel.grid(row=1, column=2, columnspan=3)

button_back = Button(root, text="Reopen Image", command=lambda: reopen()).grid(row=1, column=0)

statusVariable = StringVar()

imageStatus = Label(root, textvariable=statusVariable)
imageStatus.grid(row=2, column=0, columnspan=3)

root.filename = filedialog.askopenfilename(initialdir="images/", title="Select an image to open")
statusVariable.set(root.filename)
image = ImageTk.PhotoImage(Image.open(root.filename))
imageLabel = Label(image=image)
imageLabel.grid(row=0, column=1)

root.mainloop()