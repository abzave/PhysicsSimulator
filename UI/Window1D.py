from UI.SpaceWindow import SpaceWindow
from Space.Axis import Axis

class Window1D(SpaceWindow):
    
    def __init__(self):
        SpaceWindow.__init__(self, 'Una dimensión')
        self.__axis = Axis(self._canvas, 'x')
        self._execWindow()

    def _onClick(self, event):
        super()._onClick(event)

    def _onClickRelease(self, event):
        super()._onClickRelease(event)
        displacement = self._log.getDisplacement()
        if self._clickedPoint and displacement:
            velocity = displacement / self._log.getDuration()
            self._clickedPoint = None
        
