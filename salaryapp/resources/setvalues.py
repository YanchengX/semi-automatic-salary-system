# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setvalues.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 470)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.l1 = QtWidgets.QLineEdit(self.centralwidget)
        self.l1.setObjectName("l1")
        self.verticalLayout.addWidget(self.l1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.l2 = QtWidgets.QLineEdit(self.centralwidget)
        self.l2.setObjectName("l2")
        self.verticalLayout.addWidget(self.l2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.l3 = QtWidgets.QLineEdit(self.centralwidget)
        self.l3.setObjectName("l3")
        self.verticalLayout.addWidget(self.l3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.l4 = QtWidgets.QLineEdit(self.centralwidget)
        self.l4.setObjectName("l4")
        self.verticalLayout.addWidget(self.l4)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.l5 = QtWidgets.QLineEdit(self.centralwidget)
        self.l5.setObjectName("l5")
        self.verticalLayout.addWidget(self.l5)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.l6 = QtWidgets.QLineEdit(self.centralwidget)
        self.l6.setObjectName("l6")
        self.verticalLayout.addWidget(self.l6)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.l7 = QtWidgets.QLineEdit(self.centralwidget)
        self.l7.setObjectName("l7")
        self.verticalLayout.addWidget(self.l7)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.l8 = QtWidgets.QLineEdit(self.centralwidget)
        self.l8.setObjectName("l8")
        self.verticalLayout.addWidget(self.l8)
        self.setbutton = QtWidgets.QPushButton(self.centralwidget)
        self.setbutton.setObjectName("setbutton")
        self.verticalLayout.addWidget(self.setbutton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "參數設定"))
        self.label_3.setText(_translate("MainWindow", "勞保費計算:"))
        self.label.setText(_translate("MainWindow", "健保費計算:"))
        self.label_4.setText(_translate("MainWindow", "開門獎金:"))
        self.label_2.setText(_translate("MainWindow", "全勤獎金:"))
        self.label_6.setText(_translate("MainWindow", "責任獎金:"))
        self.label_5.setText(_translate("MainWindow", "供餐補貼:"))
        self.label_7.setText(_translate("MainWindow", "加班前兩小:"))
        self.label_9.setText(_translate("MainWindow", "加班兩小後"))
        self.setbutton.setText(_translate("MainWindow", "完成"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())