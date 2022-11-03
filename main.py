import sqlite3
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(643, 550)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 621, 521))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('coffee.db')
        self.write()

    def write(self):
        cur = self.con.cursor()
        request = f"""SELECT name, roasting, groundoringrains, taste, price, volume FROM Coffee"""
        result = cur.execute(request).fetchall()
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setHorizontalHeaderLabels(['Название сорта', 'Степень обжарки',
                                                    'Молотый/в зернах', 'описание вкуса',
                                                    'Цена', 'Объём упаковки'])
        for i, elem in enumerate(result):
            for j, value in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = MyWidget()
    db.show()
    sys.exit(app.exec())