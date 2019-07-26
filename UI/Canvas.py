from tkinter import Canvas as tkCanvas

class Canvas:

    def __init__(self, window, width = 854, height = 480):
        self.__instance = tkCanvas(window, width = width, height = height)
        self.__width = width
        self.__height = height
        self.__parent = window

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getParent(self):
        return self.__parent

    def pack(self):
        self.__instance.pack()

    def deleteElement(self, element):
        self.__instance.delete(element)

    def drawOval(self, x1, y1, x2, y2, color = '#000000', outline = '#000000'):
        return self.__instance.create_oval(x1, y1, x2, y2, fill = color,
                                          outline = outline)

    def drawLine(self, x1, y1, x2, y2, arrow = False, color = '#000000',
                 width = 1):
        return self.__instance.create_line(x1, y1, x2, y2, arrow = arrow,
                                          fill = color, width = width)
    def drawText(self, x, y, text):
        return self.__instance.create_text(x, y, text = text)

    def setClickEvent(self, action):
        self.__instance.bind('<Button-1>', action)

    def setMouseMoveEvent(self, action):
        self.__instance.bind('<B1-Motion>', action)

    def setClickReleaseEvent(self, action):
        self.__instance.bind('<ButtonRelease-1>', action)
