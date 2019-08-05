
class ObjectManager:

    def __init__(self):
        self.__objects = []

    def addObject(self, newObject):
        self.__objects.append(newObject)

    def getClickedObject(self, x, y):
        for currentObject in self.__objects:
            if currentObject.isClicked(x, y):
                return currentObject
        return None

    def moveObject1D(self, objectToMove, velocity):
        y = objectToMove.getY()
        x = objectToMove.getX()
        initialX = x
        time = 0
        while 10 < x < 825 and objectToMove.getThread() == thread:
            x = initialX + velocity * time
            objectToMove.move(x, y)
            time += 0.05

    def moveObject2D(self, objectToMove, velocityX, velocityY):
        y = objectToMove.getY()
        x = objectToMove.getX()
        initialX = x
        initialY = y
        time = 0
        while 10 < x < 825 and 5 < y < 470 \
              and objectToMove.getThread() == thread:
            x = initialX + velocityX * time
            y = initialY + velocityY * time - 9.8 * (time ** 2)
            objectToMove.move(x, y)
            time += 0.05

