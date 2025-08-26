from UI.Window import Window

class MainWindow(Window):

    def __init__(self):
        Window.__init__(self, 'Simulador de fisica', 205, 115)
        self.__createButtons()
        self.__configureWindow()        

    def __createButtons(self):
        self.createButton(50, 10, 100, 25, '1 Dimensión', self.__button1DAction)
        self.createButton(50, 45, 100, 25, '2 Dimensiones',
                          self.__button2DAction)
        self.createButton(50, 80, 100, 25, '3 Dimensiones',
                          self.__button3DAction)
    
    def __configureWindow(self):
        self.setResizable(False, False)
        self.exec()

    def __button1DAction(self):
        self.close()

    def __button2DAction(self):
        self.close()

    def __button3DAction(self):
        self.close()
