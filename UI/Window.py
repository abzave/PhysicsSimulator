from tkinter import Tk
from tkinter import mainloop
from tkinter import Button
from UI.Canvas import Canvas

class Window():

    def __init__(self, name, width = 854, height = 480):
        self._instance = Tk()
        self._instance.title(name)
        self._instance.geometry(str(width) + 'x' + str(height))

    def setResizable(self, x, y):
        self._instance.resizable(x, y)

    def createCanvas(self, width = 854, height = 480):
        canvas = Canvas(self._instance, width, height)
        canvas.pack()
        return canvas

    def createButton(self, x, y, width, height, text, function):
        button = Button(self._instance, text = text, command = function)
        button.place(x = x, y = y, width = width, height = height)
        return button

    def exec(self):
        mainloop()

    def close(self):
        self._instance.destroy()
