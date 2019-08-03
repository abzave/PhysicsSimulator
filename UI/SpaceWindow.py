from UI.Window import Window
from UI.EventLog import EventLog
from Objects.Point import Point
from Objects.ObjectManager import ObjectManager

class SpaceWindow:

    def __init__(self, name):
        self.__window = Window(name)
        self._canvas = self.__window.createCanvas()
        self._log = EventLog()
        self._clickedPoint = None
        self.__bindActions()
        self.__addButtons()

    def __bindActions(self):
        self._canvas.setClickEvent(self._onClick)
        self._canvas.setMouseMoveEvent(self._onClickMove)
        self._canvas.setClickReleaseEvent(self._onClickRelease)

    def __addButtons(self):
        self.__window.createButton(744, 10, 100, 20, 'Agregar punto',
                                  self.__addPoint)

    def __configureWindow(self):
        self.__window.setResizable(False, False)

    def _execWindow(self):
        self.__window.exec()

    def __addPoint(self):
        point = Point(self._canvas, 10, 5, '#000000')

    def _onClick(self, event):
        self._log.setEventX(event.x)
        if self._clickedPoint:
            self._log.setStartTime()

    def _onClickMove(self, event):
        if self._clickedPoint:
            self._clickedPoint.move(event.x, event.y, False)

    def _onClickRelease(self, event):
        self._log.setEndXPosition(event.x)
        self._log.setEndTime()
