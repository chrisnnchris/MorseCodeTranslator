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
        self.playerOneScore = 0
        self.playerTwoScore = 0
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
        self.playerOneSign = 0
        self.playerTwoSign = 0
        self.gameResult()
        self.show()

    def startGame(self):
        print("start")
        self.timer.start()

    def stopGame(self):
        print("Stop")
        self.timer.stop()
        self.gameResult()
        self.messageBox()

    def gameResult(self):
        #print("hello")

        if (self.playerOneSign == 1):
            if (self.playerTwoSign == 2):
                self.playerTwoScore = self.playerTwoScore + 1
            else:
                self.playerOneScore = self.playerOneScore + 1
        if (self.playerOneSign == 2):
            if (self.playerTwoSign == 1):
                self.playerTwoScore = self.playerTwoScore + 1
            else:
                self.playerOneScore = self.playerOneScore + 1
        if (self.playerOneSign == 3):
            if (self.playerTwoSign == 1):
                self.playerTwoScore = self.playerTwoScore + 1
            elif (self.playerTwoSign == 2):
                self.playerOneScore = self.playerOneScore + 1


        print("Stop numbers. Player One: " + str(self.playerOneSign) + " Player Two: " + str(self.playerTwoSign))
        print("Scores. Player One: " + str(self.playerOneScore) + " Player Two: " + str(self.playerTwoScore))
        self.leftScoreText.setText("Player 1: " + str(self.playerOneScore))
        self.rightScoreText.setText("Player 2: " + str(self.playerTwoScore))

    def messageBox(self):
        if (self.playerOneScore == 5 or self.playerTwoScore == 5):
            resultMessage = ""
            if (self.playerOneScore > self.playerTwoScore):
                resultMessage = "Player One Wins"
            else:
                resultMessage = "Player Two Wins"
            mbox=QMessageBox.information(self,"Game Result", resultMessage)
            sys.exit()


    def changeSigns(self):
        print("testing")
        # 1 is paper, 2 is scissors, 3 is rock
        self.playerOneSign = random.randint(1,3)
        print(self.playerOneSign)
        self.playerTwoSign = random.randint(1,3)
        print(self.playerTwoSign)
        if (self.playerOneSign == 1):
            self.leftImage.setPixmap(QPixmap('images/paper.jpg'))
        elif (self.playerOneSign == 2):
            self.leftImage.setPixmap(QPixmap('images/scissors.jpg'))
        else:
            self.leftImage.setPixmap(QPixmap('images/paper.jpg'))
        if (self.playerTwoSign == 1):
            self.rightImage.setPixmap(QPixmap('images/paper.jpg'))
        elif (self.playerTwoSign == 2):
            self.rightImage.setPixmap(QPixmap('images/scissors.jpg'))
        else:
            self.rightImage.setPixmap(QPixmap('images/rock.jpg'))


def main():
    App = QApplication(sys.argv)
    window = Window()
    #window.start() # this is used to have the timer start immediately upon opening
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
