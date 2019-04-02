import sys
from PyQt5 import QtWidgets, QtGui

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.le = QtWidgets.QLineEdit()
        self.b1 =QtWidgets.QPushButton('Clear')
        self.b2 = QtWidgets.QPushButton('Print')

        '''vboxy'''
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)

        '''okreslenie wartwy wyśiwtlanej'''
        self.setLayout((v_box))
        self.setWindowTitle('Tytuł')

        '''co się dzieje po kliknięciu przycisku'''
        self.b1.clicked.connect(self.btm_click)
        self.b2.clicked.connect(self.btm_click)

        self.show()

    '''funkcja sender określenie wszytkich przyciaków w jednej funkcji'''
    def btm_click(self):
        sender = self.sender()
        if sender.text() == 'Print':
            print(self.le.text())
        else:
            self.le.clear()

app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())




