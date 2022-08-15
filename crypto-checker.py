print("Very Basic Crypto Checker")

from tkinter import *
import requests

root = Tk()
root.wm_title("Very Basic Crypto Checker")

entry = Entry(root, width=50, bg="gray")
entry.pack()

def clicked():
    response = requests.get("https://api.coincap.io/v2/assets/" + entry.get().lower())
    responseJSON = response.json()
    
    label = Label(root, text=responseJSON['data']['symbol'] + " is at price " + responseJSON['data']['priceUsd'])
    label.pack()
    entry.delete(0, END)
    
    print(responseJSON)

entry.bind('<Return>', lambda click: clicked())

butt = Button(root, command=clicked, text="+", padx=50, pady=50)
butt.pack()

root.mainloop()