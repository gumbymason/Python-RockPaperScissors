import sys
from PyQt5.QtWidgets import *
import View
import Controller
import Model




__version__ = '0.1'
__author__ = 'Mason Grant'


def main():
    RPS = QApplication(sys.argv)
    view = View.RPSUi()
    view.show()

    model = Model.Choice
    Controller.RPSCtrl(model = model, view = view)
    sys.exit(RPS.exec_())

if __name__ == '__main__':
    main()