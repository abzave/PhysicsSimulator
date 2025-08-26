import time

class EventLog:

    def __init__(self):
        self.__startTime = None
        self.__endTime = None
        self.__startX = None
        self.__endX = None

    def setStartTime(self):
        self.__startTime = time.time()

    def getStartTime(self):
        return self.__startTime

    def setEndTime(self):
        self.__endTime = time.time()

    def getEndTime(self):
        return self.__endTime

    def getDuration(self):
        return self.__endTime - self._startTime

    def setEventX(self, x):
        self.__startX = x

    def getEventX(self):
        return self.__startX

    def setEndXPosition(self, x):
        self.__endX = x

    def getEndXPosition(self):
        return self.__endX

    def getDisplacement(self):
        return self.__endX - self.__startX
