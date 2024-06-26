# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_emp.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputt = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.inputt.setFont(font)
        self.inputt.setAlignment(QtCore.Qt.AlignCenter)
        self.inputt.setObjectName("inputt")
        self.verticalLayout.addWidget(self.inputt)
        self.neid = QtWidgets.QLabel(self.centralwidget)
        self.neid.setObjectName("neid")
        self.verticalLayout.addWidget(self.neid)
        self.e1 = QtWidgets.QLineEdit(self.centralwidget)
        self.e1.setObjectName("e1")
        self.verticalLayout.addWidget(self.e1)
        self.neproperty = QtWidgets.QLabel(self.centralwidget)
        self.neproperty.setObjectName("neproperty")
        self.verticalLayout.addWidget(self.neproperty)
        self.e2 = QtWidgets.QLineEdit(self.centralwidget)
        self.e2.setObjectName("e2")
        self.verticalLayout.addWidget(self.e2)
        self.nename = QtWidgets.QLabel(self.centralwidget)
        self.nename.setObjectName("nename")
        self.verticalLayout.addWidget(self.nename)
        self.e3 = QtWidgets.QLineEdit(self.centralwidget)
        self.e3.setObjectName("e3")
        self.verticalLayout.addWidget(self.e3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.e4 = QtWidgets.QDateEdit(self.centralwidget)
        self.e4.setObjectName("e4")
        self.verticalLayout.addWidget(self.e4)
        self.newemp = QtWidgets.QPushButton(self.centralwidget)
        self.newemp.setObjectName("newemp")
        self.verticalLayout.addWidget(self.newemp)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inputt.setText(_translate("MainWindow", "輸入資料"))
        self.neid.setText(_translate("MainWindow", "員工編號:"))
        self.neproperty.setText(_translate("MainWindow", "員工性質:"))
        self.nename.setText(_translate("MainWindow", "員工姓名:"))
        self.label.setText(_translate("MainWindow", "入職日期:"))
        self.newemp.setText(_translate("MainWindow", "新增"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
