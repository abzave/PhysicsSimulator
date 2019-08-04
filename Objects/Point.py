from UI.Canvas import Canvas

class Point:

    def __init__(self, canvas, x, y, color):
        self.__canvas = canvas
        self.__color = color
        self.__x = x
        self.__y = y
        self.__point = self.__draw(x, y, color)

    def __transformCoordinates(self, x, y):
        return self.__transformX(x), self.__transformY(y)

    def __transformX(self, x):
        return x

    def __transformY(self, y):
        return self.__canvas.getHeight() - y - 13

    def __draw(self, x, y, color):
        x, y = self.__transformCoordinates(x, y)
        return self.__canvas.drawOval(x, y, x + 3, y + 3, color, color)

    def delete(self):
        self.__canvas.deleteElement(self._point)
        
    def move(self, x, y, spaceCoordinates = True):
        self.delete()
        if not spaceCoordinates:
            x, y = self.__transformCoordinates(x, y)
        self.__x = x
        self.__y = y
        self.__point = self.__draw(x, y, self.__color)

    def changeColor(self, color):
        self.__color = color
        self.delete()
        self.__point = self._draw(self.__x, self.__y, self.__color)
                
    def isClicked(self, x, y):
        screenX, screenY = self._transformCoordinates(self.__x, self.__y)
        return screenX <= x <= screenX + 3 and screenY <= y <= screenY + 3

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y
