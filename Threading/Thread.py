from time import sleep
import threading

class Thread:

    def __init__(self, function, *args):
        self._instance = threading.Thread(target = function, args = args)
        self._functionArgs = args
        self._function = function

    def start(self):
        self._instance.start()

    def join(self):
        self._instance.join()

    def changeArguments(self, *args):
        self._instance = threading.Thread(target = self._function, args = args)

    @staticmethod
    def sleep(seconds):
        sleep(seconds)
