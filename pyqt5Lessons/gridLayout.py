import sys
import PyQt5.QtWidgets


class Window(PyQt5.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout")
        self.setGeometry(50, 50, 600, 600)
        self.UI()

    def UI(self):
        self.gridLayout = PyQt5.QtWidgets.QGridLayout()
        self.setLayout(self.gridLayout)
        '''
        btn1= PyQt5.QtWidgets.QPushButton("Button1")
        btn2= PyQt5.QtWidgets.QPushButton("Button2")
        btn3= PyQt5.QtWidgets.QPushButton("Button3")
        btn4= PyQt5.QtWidgets.QPushButton("Button4")
        self.gridLayout.addWidget(btn1, 0, 0)
        self.gridLayout.addWidget(btn2, 0, 1)
        self.gridLayout.addWidget(btn3, 1, 0)
        self.gridLayout.addWidget(btn4, 1, 1)
        '''
        for i in range(0,3):
            for j in range(0,3):
                btn=PyQt5.QtWidgets.QPushButton("Button{}{}".format(i,j))
                self.gridLayout.addWidget(btn, i, j)
                btn.clicked.connect(self.clickMe)
        #self.gridLayout.setColumnStretch(1, 1)
        self.show()
    def clickMe(self):
        buttonID = self.sender().text()
        if (buttonID == "Button00"):
            print("Button1 was clicked")
        elif (buttonID == "Button01"):
            print("Button2 was clicked")
        elif (buttonID == "Button02"):
            print("Button3 was clicked")

def main():
    App = PyQt5.QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
