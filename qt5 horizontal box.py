import sys
from PyQt5 import QtWidgets, QtGui

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
button = QtWidgets.QPushButton('Przycisk')
lable = QtWidgets.QLabel('Patrz')

'''horyzotalny box'''
h_box = QtWidgets.QHBoxLayout()
h_box.addStretch()
h_box.addWidget(lable)
h_box.addStretch()

'''v box ktory uzywa horizontal box '''
v_box = QtWidgets.QVBoxLayout()
v_box.addWidget(button)
v_box.addLayout(h_box)
window.setLayout(v_box)

window.setWindowTitle('tytuł')
window.show()

sys.exit(app.exec_())
