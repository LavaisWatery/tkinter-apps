print("Basic Image Viewer - maybe add ability to distort, etc")
print("Also idk, these images are troll")

from ctypes import sizeof
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Basic Image Viewer")

def next():
    global statusVariable
    global imageLabel
    global imageIndex
    global images
    global imageStatus

    imageIndex += 1
    if len(images) <= imageIndex:
        imageIndex = 0
    imageLabel.grid_forget()
    imageLabel = Label(image=images[imageIndex])
    imageLabel.grid(row=0, column=0, columnspan=3)
    statusVariable.set("Image: " + imageNames[imageIndex])

def back():
    global images
    global imageIndex
    global imageLabel
    global imageStatus
    global statusVariable

    imageIndex -= 1
    if imageIndex < 0:
        imageIndex = len(images) - 1
    
    imageLabel.grid_forget()
    imageLabel = Label(image=images[imageIndex])
    imageLabel.grid(row=0, column=0, columnspan=3)
    statusVariable.set("Image: " + imageNames[imageIndex])

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("images/") if isfile(join("images/", f))]

print(onlyfiles)
images = []
imageNames = []
imageIndex = 0

for file in onlyfiles:
    images.append(ImageTk.PhotoImage(Image.open("images/" + file)))
    imageNames.append(file)

imageLabel = Label(image=images[0])
imageLabel.grid(row=0, column=0, columnspan=3)
print(images[0])

button_back = Button(root, text="<-", command=lambda: back()).grid(row=1, column=0)
button_next = Button(root, text="->", command=lambda: next()).grid(row=1, column=2)

statusVariable = StringVar()
statusVariable.set("Image: " + imageNames[0])

imageStatus = Label(root, textvariable=statusVariable)
imageStatus.grid(row=2, column=0, columnspan=3)

root.mainloop()