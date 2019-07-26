from tkinter import Canvas as tkCanvas

class Canvas:

    def __init__(self, window, width = 854, height = 480):
        self._instance = tkCanvas(window, width = width, height = height)
        self._width = width
        self._height = height
        self._parent = window

    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height

    def getParent(self):
        return self._parent

    def pack(self):
        self._instance.pack()

    def deleteElement(self, element):
        self._instance.delete(element)

    def drawOval(self, x1, y1, x2, y2, color = '#000000', outline = '#000000'):
        return self._instance.create_oval(x1, y1, x2, y2, fill = color,
                                          outline = outline)

    def drawLine(self, x1, y1, x2, y2, arrow = False, color = '#000000',
                 width = 1):
        return self._instance.create_line(x1, y1, x2, y2, arrow = arrow,
                                          fill = color, width = width)
    def drawText(self, x, y, text):
        return self._instance.create_text(x, y, text = text)

    def setClickEvent(self, action):
        self._instance.bind('<Button-1>', action)

    def setMouseMoveEvent(self, action):
        self._instance.bind('<B1-Motion>', action)

    def setClickReleaseEvent(self, action):
        self._instance.bind('<ButtonRelease-1>', action)
