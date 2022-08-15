print("Basic Image Viewer - maybe add ability to distort, etc")
print("Also idk, these images are troll")

from ctypes import sizeof
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Basic Image Viewer")

def next():
    global imageLabel
    global imageIndex
    global images

    imageIndex += 1
    if len(images) <= imageIndex:
        imageIndex = 0
    imageLabel.grid_forget()
    imageLabel = Label(image=images[imageIndex])
    imageLabel.grid(row=0, column=0, columnspan=2)

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("images/") if isfile(join("images/", f))]

print(onlyfiles)
images = []
imageIndex = 0

for file in onlyfiles:
    images.append(ImageTk.PhotoImage(Image.open("images/" + file)))

imageLabel = Label(image=images[0])
imageLabel.grid(row=0, column=0, columnspan=2)

button_back = Button(root, text="<-").grid(row=1, column=0)
button_next = Button(root, text="->", command=lambda: next()).grid(row=1, column=1)

root.mainloop()