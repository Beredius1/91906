'''Purpose: This is a program that will upskill the mathmatical abilities of
pre-schoolers.
Name: Mr Wright
Date: 22 July 2024
'''


import random
import tkinter import*

num = [1, 2, 3, 4, 5, 6, 7, 8, 9 }

app = Tk()
app.title("Math4Kids")
app.geometry("800x600")
app.resizable(True, True)

start = Button(app, text = "Start")
start.place()

solving = Entry(app)
solving.place()

submit = Button(app, text ='Submit')
