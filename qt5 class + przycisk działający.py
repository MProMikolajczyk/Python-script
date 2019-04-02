import sys
from PyQt5 import QtWidgets, QtGui

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.button = QtWidgets.QPushButton('Dalej')
        self.button2 = QtWidgets.QPushButton('sss')
        self.lable = QtWidgets.QLabel('text taki tam')

        '''horyzonatal box rozciągnnie textu potem'''
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.lable)
        h_box.addStretch()

        '''vbox rozciąganie box przycisku'''
        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box) #tu dodaje wartwe w postaci utworzonej przestrzeni
        v_box.addWidget(self.button)
        v_box.addWidget(self.button2)


        self.setLayout(v_box) #gdzię temu działo ten text po rozciągniciu
        self.setWindowTitle('Tytuł')

        self.button.clicked.connect(self.btn_click) #definiowanie gdzie ma przekierować przycisk

        self.show()

    '''zmiana textu z 'text taki tam' na klikniete po nacisnięciu przycisku '''
    def btn_click(self):
        self.lable.setText('klikniete')

app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())




