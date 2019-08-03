from tkinter import Tk
from tkinter import mainloop
from tkinter import Button
from UI.Canvas import Canvas

class Window():

    def __init__(self, name, width = 854, height = 480):
        self.__instance = Tk()
        self.__instance.title(name)
        self.__instance.geometry(str(width) + 'x' + str(height))

    def setResizable(self, x, y):
        self.__instance.resizable(x, y)

    def createCanvas(self, width = 854, height = 480):
        canvas = Canvas(self.__instance, width, height)
        canvas.pack()
        return canvas

    def createButton(self, x, y, width, height, text, function):
        button = Button(self.__instance, text = text, command = function)
        button.place(x = x, y = y, width = width, height = height)
        return button

    def exec(self):
        mainloop()

    def close(self):
        self.__instance.destroy()
