import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Widget")
        self.setGeometry(350,150, 600, 600)
        self.UI()

    def UI(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        code = menubar.addMenu("Code")
        helpMenu = menubar.addMenu("Help")

        new = QAction("New Project", self)
        new.setShortcut("Ctrl+O")
        file.addAction(new)
        open=QAction("Open", self)
        file.addAction(open)
        exit=QAction("Exit", self)
        exit.setIcon((QIcon("images/images.jpg")))
        exit.triggered.connect(self.exitFunc)
        file.addAction(exit)
        #### Toolbar
        tb = self.addToolBar("My Toolbar")
        tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        newTb=QAction(QIcon('images/folder.png'), "New", self)
        tb.addAction(newTb)
        openTb = QAction(QIcon('images/empty.png'), "Open", self)
        tb.addAction(openTb)
        saveTb = QAction(QIcon("images/save.png"), "Save", self)
        tb.addAction(saveTb)
        exitTb = QAction(QIcon("images/exit.png"), "Exit", self)
        exitTb.triggered.connect(self.exitFunc)
        tb.addAction(exitTb)
        tb.actionTriggered.connect(self.btnFunc)
        self.combo = QComboBox()
        self.combo.addItems(["Spiderman", "Superman", "Batman"])
        tb.addWidget(self.combo)
        self.show()

    def exitFunc(self):
        print("Hello")
        mbox = QMessageBox.information(self, "Warning", "Are you sure to exit?", QMessageBox.Yes | QMessageBox.No)
        if mbox==QMessageBox.Yes:
            sys.exit()

    def btnFunc(self, btn):
        if btn.text()=="New":
            print("You clicked new button")
        elif btn.text() == "Open":
            print("You clicked open button")
        else:
            print("You clicked save button")


def main():
    App=QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()