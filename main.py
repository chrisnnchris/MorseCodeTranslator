import sys
from PyQt5.QtWidgets import *

englishToMorseDict = {
    'a': "*-",
    'b': "-***",
    'c': "-*-*",
    'd': "-**",
    'e': "*",
    'f': "**-*",
    'g': "--*",
    'h': "****",
    'i': "**",
    'j': "*---",
    'k': "-*-",
    'l': "*-**",
    'm': "--",
    'n': "-*",
    'o': "---",
    'p': "*--*",
    'q': "--*-",
    'r': "*-*",
    's': "***",
    't': "-",
    'u': "**-",
    'v': "***-",
    'w': "*--",
    'x': "-**-",
    'y': "-*--",
    'z': "--**",
    '1': "*----",
    '2': "**---",
    '3': "***--",
    '4': "****-",
    '5': "*****",
    '6': "-****",
    '7': "--***",
    '8': "---**",
    '9': "----*",
    '0': "-----"
}


def englishToMorse(stringInput):
    translateString = ""
    print("This is the stringInput: " + stringInput)
    for x in range(0, len(stringInput)):
        print(stringInput[x])
        print("translated")
        print(englishToMorseDict[stringInput[x].lower()])
        translateString += englishToMorseDict[stringInput[x].lower()] + "  "
    return translateString

'''
test = "hello"
translated = englishToMorse(test)
print(translated)
'''

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Morse Code Translator")
        self.setGeometry(250, 150, 500, 500)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.inputText = QTextEdit()
        self.translateButton = QPushButton("English to Morse")
        self.outputText = QTextEdit()

        hbox.addStretch()
        hbox.addWidget(self.translateButton)
        hbox.addStretch()

        vbox.addWidget(self.inputText)
        vbox.addLayout(hbox)
        vbox.addWidget(self.outputText)

        self.translateButton.clicked.connect(self.translate)

        self.setLayout(vbox)
        self.show()

    def translate(self):
        print("Translate is clicked")
        englishString = self.inputText.toPlainText()
        print("English string is " + englishString)
        morseString = englishToMorse(englishString)
        print("Morse string is " + morseString)
        self.outputText.setText(morseString)

def main():
    App = QApplication(sys.argv)
    window = Window()
    # window.start() # this is used to have the timer start immediately upon opening
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
