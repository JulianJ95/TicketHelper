import os
from selenium import webdriver
from tkinter import *


ChromeDriverPath = os.path.join(os.getcwd(), "bin", "chromedriver.exe")


def function():
    Browser = webdriver.Chrome(ChromeDriverPath)
    Browser.get('http://www.google.com/xhtml')
window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

btn = Button(window, text="Click Me", command=function)

btn.grid(column=1, row=0)

window.mainloop()

