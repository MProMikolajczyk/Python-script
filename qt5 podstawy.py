import sys
from PyQt5 import QtWidgets, QtGui

'''utorzenie aplikacji'''
app = QtWidgets.QApplication(sys.argv)

'''zdefionowanie okna i miejsca jego wyswitlania '''
window = QtWidgets.QWidget()
window.setWindowTitle('ddddd')
window.setGeometry(1500, 20, 500, 200)

'''warstwa wyswietlna i jej polożenie '''
lable = QtWidgets.QLabel(window)
lable.setText('Hello World')
lable.move(100,20)

'''umiezczenie obrazka'''
#lable2 = QtWidgets.QLabel(window)
#lable2.setPixmap(QtGui.QPixmap('globe.png'))
#lable2.move(120,90)

'''przycisk + text wyświetlany'''
batton = QtWidgets.QPushButton(window)
lable3 = QtWidgets.QLabel(window)
batton.setText('dalej')
batton.move(100,50)



lable3.setText('patrz')
lable3.move(100,100)


'''wyśiwtlenie okna + konieczna definicja zamknięcia'''
window.show()
sys.exit(app.exec_())

