import sys
from PyQt5.QtWidgets import (QLabel,QCheckBox,QPushButton,QVBoxLayout,QApplication,QWidget)
from PyQt5.QtCore import Qt

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.lbl = QLabel()
        self.chx =QCheckBox("dododododododo?")
        self.btn = QPushButton('dalej')

        loyout = QVBoxLayout ()
        loyout.addWidget(self.lbl)
        loyout.addWidget(self.chx)
        loyout.addWidget(self.btn)

        self.setLayout(loyout)

        self.btn.clicked.connect(lambda: self.btn_click(self.chx.isChecked(),self.lbl))

        self.show()

    def btn_click(self,chk,lbl):
        if chk:
            lbl.setText('sasasasasasasa')
        else:
            lbl.setText('gogogogoog')

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())




