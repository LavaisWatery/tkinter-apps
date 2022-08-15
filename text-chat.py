from tkinter import *
print("Very Basic Text App")
from webbrowser import get

root = Tk()
root.wm_title("Basic Text Chat")

entry = Entry(root, width=50, bg="gray")
entry.pack()

def enter():
    label = Label(root, text=entry.get())
    label.pack()
    entry.delete(0, END)

entry.bind('<Return>', lambda entr: enter())

root.mainloop()