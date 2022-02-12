from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt






__version__ = '0.1'
__author__ = 'Mason Grant'

# Create the View for the app
class RPSUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Rock Paper Scissors')
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(30)
        self.display.setAlignment(Qt.AlignCenter)
        self.display.setReadOnly(True)
        self.display.setFont(QFont('Times', 10))
        self.totalsDisplay = QLineEdit()
        self.totalsDisplay.setFixedHeight(30)
        self.totalsDisplay.setAlignment(Qt.AlignCenter)
        self.display.setReadOnly(True)
        self.totalsDisplay.setFont(QFont('Times', 10))
        self.generalLayout.addWidget(self.display)
        self.generalLayout.addWidget(self.totalsDisplay)

    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()

        buttons = {'Rock':     (1,0),
                   'Paper':    (1,1),
                   'Scissors': (1,2),
                  }

        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(100, 100)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Set the display's text"""
        self.display.setText(text)
        self.display.setFocus()
    
    def setTotalsDisplay(self, wins, losses, ties):
        """Set the totals display text"""
        text = "Wins: " + str(wins) + " Losses: " + str(losses) + " Ties: " + str(ties)
        self.totalsDisplay.setText(text)
