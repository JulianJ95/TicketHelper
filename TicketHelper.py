import os
from selenium import webdriver
from tkinter import *


ChromeDriverPath = os.path.join(os.getcwd(), "bin", "chromedriver.exe")

def function():
    browser = webdriver.Chrome(ChromeDriverPath)
    browser.get('http://www.google.com/xhtml')


window = Tk()
window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

btn = Button(window, text="Click Me", command=function)
btn.grid(column=1, row=0)
radiobtn = Radiobutton(window, text="Python1", value=0, command=function)

radiobtn.grid(column=0, row=1)


window.mainloop()
