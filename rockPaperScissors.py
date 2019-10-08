import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Rock Paper Scissors")
        self.setGeometry(250, 150, 500, 500)
        self.UI()

    def UI(self):
        self.leftImage = QLabel(self)
        self.leftImage.setPixmap(QPixmap('images/rock.jpg'))
        self.leftImage.move(50, 150)
        self.rightImage = QLabel(self)
        self.rightImage.setPixmap(QPixmap('images/rock.jpg'))
        self.rightImage.move(300, 150)
        self.middleText = QLabel("VS", self)
        self.middleText.move(250,225)
        self.leftScoreText = QLabel("Player 1:  ", self)
        self.leftScoreText.move(20, 50)
        self.rightScoreText = QLabel("Player 2:  ", self)
        self.rightScoreText.move(420, 50)
        self.startButton = QPushButton("Start", self)
        self.startButton.move(120, 400)
        self.stopButton = QPushButton("Stop", self)
        self.stopButton.move(330, 400)
        self.startButton.clicked.connect(self.startGame)
        self.stopButton.clicked.connect(self.stopGame)
        self.timer=QTimer()
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.changeSigns)

        self.show()

    def startGame(self):
        print("start")
        self.timer.start()

    def stopGame(self):
        print("Stop")
        self.timer.stop()

    def changeSigns(self):
        print("testing")
        # 1 is paper, 2 is scissors, 3 is rock
        playerOneSign = random.randint(1,3)
        print(playerOneSign)
        playerTwoSign = random.randint(1,3)
        print(playerTwoSign)
        if (playerOneSign == 1):
            self.leftImage.setPixmap(QPixmap('images/paper.jpg'))
        elif (playerOneSign == 2):
            self.leftImage.setPixmap(QPixmap('images/scissors.jpg'))
        else:
            self.leftImage.setPixmap(QPixmap('images/paper.jpg'))
        if (playerTwoSign == 1):
            self.rightImage.setPixmap(QPixmap('images/paper.jpg'))
        elif (playerTwoSign == 2):
            self.rightImage.setPixmap(QPixmap('images/scissors.jpg'))
        else:
            self.rightImage.setPixmap(QPixmap('images/paper.jpg'))


def main():
    App = QApplication(sys.argv)
    window = Window()
    #window.start() # this is used to have the timer start immediately upon opening
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
