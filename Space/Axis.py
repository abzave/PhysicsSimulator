from UI.Canvas import Canvas
from tkinter import LAST

class Axis:

    def __init__(self, canvas, name):
        self.__name = name
        self.__canvas = canvas
        self.__line = self.__draw()
        self.__label = self.__drawLabel()

    def __getOrientation(self):
        if self.__name == 'x':
            y = self.__canvas.getHeight() - 7
            return 5, y, self.__canvas.getWidth() - 2, y
        elif self.__name == 'y':
            return 5, self.__canvas.getHeight() - 7, 5, 0
        else:
            raise Exception('Axis not supported')

    def __draw(self):
        x1, y1, x2, y2 = self.__getOrientation()
        return self.__canvas.drawLine(x1, y1, x2, y2, arrow = LAST)

    def __drawLabel(self):
        x, y = self.__getLabelPosition()
        return self.__canvas.drawText(x, y, self.__name)

    def __getLabelPosition(self):
        if self.__name == 'x':
            return self.__canvas.getWidth() - 8, self.__canvas.getHeight() - 16
        elif self.__name == 'y':
            return 16, 4
        else:
            raise Exception('Axis not supported')
    
