import sys
from PyQt5.QtWidgets import (QLineEdit,QSlider,QPushButton,QVBoxLayout,QApplication,QWidget)
from PyQt5.QtCore import Qt

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.le = QLineEdit()
        self.b1 =QPushButton('Clear')
        self.b2 = QPushButton('Print')
        self.s1 = QSlider(Qt.Horizontal)
        self.s1.setMinimum(1)
        self.s1.setMaximum(99)
        self.s1.setValue(25)
        self.s1.setTickInterval(10)
        self.s1.setTickPosition(QSlider.TicksBelow)

        '''vboxy'''
        v_box = QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)
        v_box.addWidget(self.s1)

        '''okreslenie wartwy wyśiwtlanej'''
        self.setLayout((v_box))
        self.setWindowTitle('Tytuł')

        '''co się dzieje po kliknięciu przycisku'''
        self.b1.clicked.connect(self.btm_click)
        self.b2.clicked.connect(self.btm_click)
        self.s1.valueChanged.connect(self.v_change)



        self.show()

    '''funkcja sender określenie wszytkich przyciaków w jednej funkcji'''
    def btm_click(self):
        sender = self.sender()
        if sender.text() == 'Print':
            print(self.le.text())
        else:
            self.le.clear()
    '''drukowanie wartości z slaidera '''
    def v_change(self):
        my_value = str(self.s1.value())
        self.le.setText(my_value)

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())




