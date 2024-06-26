from PyQt5 import QtCore, QtGui, QtWidgets
from new_empy import New_emp
from del_emp import Del_emp
from setvalues import Setvalues
class MainView(QtWidgets.QMainWindow):
    def __init__(self, model, controller):
        super().__init__()
        self.setupUi(self)
        self.model = model
        self.controller = controller
        self.attachcontroller()

        self.show_undoview()
        self.default_set()      #diable all textable
        self.get_date()
        self.sumtotal()
        self.auto_counting_event()
        self.comboshow()
        self.defaultcombox()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1088, 830)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Show = QtWidgets.QWidget(self.centralwidget)
        self.Show.setGeometry(QtCore.QRect(9, 9, 532, 517))
        self.Show.setObjectName("Show")
        self.Totalpay = QtWidgets.QLabel(self.Show)
        self.Totalpay.setGeometry(QtCore.QRect(0, 490, 531, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Totalpay.setFont(font)
        self.Totalpay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Totalpay.setObjectName("Totalpay")
        self.undoview = QtWidgets.QListView(self.Show)
        self.undoview.setGeometry(QtCore.QRect(0, 0, 531, 481))
        self.undoview.setObjectName("undoview")
        self.Basic_set = QtWidgets.QWidget(self.centralwidget)
        self.Basic_set.setGeometry(QtCore.QRect(10, 540, 531, 259))
        self.Basic_set.setObjectName("Basic_set")
        self.spectialdayoff = QtWidgets.QLineEdit(self.Basic_set)
        self.spectialdayoff.setGeometry(QtCore.QRect(370, 60, 154, 21))
        self.spectialdayoff.setText("")
        self.spectialdayoff.setObjectName("spectialdayoff")
        self.ename = QtWidgets.QLineEdit(self.Basic_set)
        self.ename.setGeometry(QtCore.QRect(80, 100, 154, 21))
        self.ename.setText("")
        self.ename.setObjectName("ename")
        self.label = QtWidgets.QLabel(self.Basic_set)
        self.label.setGeometry(QtCore.QRect(10, 20, 58, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Basic_set)
        self.label_2.setGeometry(QtCore.QRect(300, 20, 58, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Basic_set)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 58, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Basic_set)
        self.label_4.setGeometry(QtCore.QRect(300, 60, 58, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.Basic_set)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 58, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.Basic_set)
        self.label_6.setGeometry(QtCore.QRect(300, 100, 58, 16))
        self.label_6.setObjectName("label_6")
        self.seniority = QtWidgets.QLineEdit(self.Basic_set)
        self.seniority.setEnabled(True)
        self.seniority.setGeometry(QtCore.QRect(370, 20, 154, 21))
        self.seniority.setText("")
        self.seniority.setObjectName("seniority")
        self.eid = QtWidgets.QLineEdit(self.Basic_set)
        self.eid.setGeometry(QtCore.QRect(80, 20, 154, 21))
        self.eid.setText("")
        self.eid.setObjectName("eid")
        self.pushButton = QtWidgets.QPushButton(self.Basic_set)
        self.pushButton.setGeometry(QtCore.QRect(330, 180, 93, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Basic_set)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 180, 93, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.basicsalary_2 = QtWidgets.QLineEdit(self.Basic_set)
        self.basicsalary_2.setGeometry(QtCore.QRect(370, 100, 154, 21))
        self.basicsalary_2.setText("")
        self.basicsalary_2.setObjectName("basicsalary_2")
        self.eproperty = QtWidgets.QLineEdit(self.Basic_set)
        self.eproperty.setGeometry(QtCore.QRect(80, 60, 154, 21))
        self.eproperty.setText("")
        self.eproperty.setObjectName("eproperty")
        self.line_2 = QtWidgets.QFrame(self.Basic_set)
        self.line_2.setGeometry(QtCore.QRect(10, 0, 541, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(self.Basic_set)
        self.line_4.setGeometry(QtCore.QRect(0, 10, 16, 221))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_3 = QtWidgets.QFrame(self.Basic_set)
        self.line_3.setGeometry(QtCore.QRect(520, 10, 20, 221))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_5 = QtWidgets.QFrame(self.Basic_set)
        self.line_5.setGeometry(QtCore.QRect(10, 220, 521, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.Account = QtWidgets.QWidget(self.centralwidget)
        self.Account.setGeometry(QtCore.QRect(550, 10, 532, 791))
        self.Account.setObjectName("Account")
        self.month = QtWidgets.QLabel(self.Account)
        self.month.setGeometry(QtCore.QRect(140, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.month.setFont(font)
        self.month.setAlignment(QtCore.Qt.AlignCenter)
        self.month.setObjectName("month")
        self.year = QtWidgets.QLabel(self.Account)
        self.year.setGeometry(QtCore.QRect(10, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.year.setFont(font)
        self.year.setAlignment(QtCore.Qt.AlignCenter)
        self.year.setObjectName("year")
        self.label_9 = QtWidgets.QLabel(self.Account)
        self.label_9.setGeometry(QtCore.QRect(10, 120, 58, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Account)
        self.label_10.setGeometry(QtCore.QRect(10, 150, 61, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Account)
        self.label_11.setGeometry(QtCore.QRect(10, 410, 61, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.Account)
        self.label_12.setGeometry(QtCore.QRect(10, 180, 58, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.Account)
        self.label_13.setGeometry(QtCore.QRect(10, 240, 58, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.Account)
        self.label_14.setGeometry(QtCore.QRect(10, 270, 58, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.Account)
        self.label_15.setGeometry(QtCore.QRect(10, 210, 58, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.Account)
        self.label_16.setGeometry(QtCore.QRect(10, 360, 58, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.Account)
        self.label_17.setGeometry(QtCore.QRect(10, 440, 58, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.Account)
        self.label_18.setGeometry(QtCore.QRect(10, 470, 58, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.Account)
        self.label_19.setGeometry(QtCore.QRect(10, 300, 58, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.Account)
        self.label_20.setGeometry(QtCore.QRect(10, 330, 61, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.Account)
        self.label_21.setGeometry(QtCore.QRect(290, 320, 58, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.Account)
        self.label_22.setGeometry(QtCore.QRect(290, 350, 58, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.Account)
        self.label_23.setGeometry(QtCore.QRect(290, 380, 58, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.Account)
        self.label_24.setGeometry(QtCore.QRect(290, 410, 61, 16))
        self.label_24.setObjectName("label_24")
        self.label_26 = QtWidgets.QLabel(self.Account)
        self.label_26.setGeometry(QtCore.QRect(10, 600, 58, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.Account)
        self.label_27.setGeometry(QtCore.QRect(290, 140, 58, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.Account)
        self.label_28.setGeometry(QtCore.QRect(290, 170, 58, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.Account)
        self.label_29.setGeometry(QtCore.QRect(290, 200, 58, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.Account)
        self.label_30.setGeometry(QtCore.QRect(290, 230, 58, 16))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.Account)
        self.label_31.setGeometry(QtCore.QRect(290, 260, 58, 16))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.Account)
        self.label_32.setGeometry(QtCore.QRect(290, 290, 58, 16))
        self.label_32.setObjectName("label_32")
        self.basicsalary = QtWidgets.QLineEdit(self.Account)
        self.basicsalary.setGeometry(QtCore.QRect(100, 120, 113, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.basicsalary.setFont(font)
        self.basicsalary.setObjectName("basicsalary")
        self.healthfee = QtWidgets.QLineEdit(self.Account)
        self.healthfee.setGeometry(QtCore.QRect(100, 470, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.healthfee.setFont(font)
        self.healthfee.setObjectName("healthfee")
        self.sundayovertime = QtWidgets.QLineEdit(self.Account)
        self.sundayovertime.setGeometry(QtCore.QRect(380, 290, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sundayovertime.setFont(font)
        self.sundayovertime.setObjectName("sundayovertime")
        self.saturdayovertime_meals = QtWidgets.QLineEdit(self.Account)
        self.saturdayovertime_meals.setGeometry(QtCore.QRect(380, 260, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.saturdayovertime_meals.setFont(font)
        self.saturdayovertime_meals.setObjectName("saturdayovertime_meals")
        self.mealcall = QtWidgets.QLineEdit(self.Account)
        self.mealcall.setGeometry(QtCore.QRect(100, 330, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mealcall.setFont(font)
        self.mealcall.setObjectName("mealcall")
        self.otherminus = QtWidgets.QLineEdit(self.Account)
        self.otherminus.setGeometry(QtCore.QRect(100, 360, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.otherminus.setFont(font)
        self.otherminus.setObjectName("otherminus")
        self.borrow = QtWidgets.QLineEdit(self.Account)
        self.borrow.setGeometry(QtCore.QRect(100, 300, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.borrow.setFont(font)
        self.borrow.setObjectName("borrow")
        self.normalfirstovertime = QtWidgets.QLineEdit(self.Account)
        self.normalfirstovertime.setGeometry(QtCore.QRect(380, 140, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.normalfirstovertime.setFont(font)
        self.normalfirstovertime.setObjectName("normalfirstovertime")
        self.saturdayovertime = QtWidgets.QLineEdit(self.Account)
        self.saturdayovertime.setGeometry(QtCore.QRect(380, 230, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.saturdayovertime.setFont(font)
        self.saturdayovertime.setObjectName("saturdayovertime")
        self.laborpension = QtWidgets.QLineEdit(self.Account)
        self.laborpension.setGeometry(QtCore.QRect(100, 600, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.laborpension.setFont(font)
        self.laborpension.setObjectName("laborpension")
        self.workerfee = QtWidgets.QLineEdit(self.Account)
        self.workerfee.setGeometry(QtCore.QRect(100, 440, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.workerfee.setFont(font)
        self.workerfee.setObjectName("workerfee")
        self.responsiblebouns = QtWidgets.QLineEdit(self.Account)
        self.responsiblebouns.setGeometry(QtCore.QRect(100, 210, 113, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.responsiblebouns.setFont(font)
        self.responsiblebouns.setObjectName("responsiblebouns")
        self.otherplus = QtWidgets.QLineEdit(self.Account)
        self.otherplus.setGeometry(QtCore.QRect(100, 240, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.otherplus.setFont(font)
        self.otherplus.setObjectName("otherplus")
        self.dayoff = QtWidgets.QLineEdit(self.Account)
        self.dayoff.setGeometry(QtCore.QRect(100, 270, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dayoff.setFont(font)
        self.dayoff.setObjectName("dayoff")
        self.total_salary = QtWidgets.QLineEdit(self.Account)
        self.total_salary.setGeometry(QtCore.QRect(380, 630, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.total_salary.setFont(font)
        self.total_salary.setObjectName("total_salary")
        self.overtimeother = QtWidgets.QLineEdit(self.Account)
        self.overtimeother.setGeometry(QtCore.QRect(380, 410, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.overtimeother.setFont(font)
        self.overtimeother.setObjectName("overtimeother")
        self.specialovertime = QtWidgets.QLineEdit(self.Account)
        self.specialovertime.setGeometry(QtCore.QRect(380, 350, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.specialovertime.setFont(font)
        self.specialovertime.setObjectName("specialovertime")
        self.sundayfovertime_meals = QtWidgets.QLineEdit(self.Account)
        self.sundayfovertime_meals.setGeometry(QtCore.QRect(380, 320, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sundayfovertime_meals.setFont(font)
        self.sundayfovertime_meals.setObjectName("sundayfovertime_meals")
        self.specialovertime_meals = QtWidgets.QLineEdit(self.Account)
        self.specialovertime_meals.setGeometry(QtCore.QRect(380, 380, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.specialovertime_meals.setFont(font)
        self.specialovertime_meals.setObjectName("specialovertime_meals")
        self.normalovertime_meals = QtWidgets.QLineEdit(self.Account)
        self.normalovertime_meals.setGeometry(QtCore.QRect(380, 200, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.normalovertime_meals.setFont(font)
        self.normalovertime_meals.setObjectName("normalovertime_meals")
        self.allrbouns = QtWidgets.QLineEdit(self.Account)
        self.allrbouns.setGeometry(QtCore.QRect(100, 410, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.allrbouns.setFont(font)
        self.allrbouns.setObjectName("allrbouns")
        self.normalmeals = QtWidgets.QLineEdit(self.Account)
        self.normalmeals.setGeometry(QtCore.QRect(100, 150, 113, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.normalmeals.setFont(font)
        self.normalmeals.setObjectName("normalmeals")
        self.openbouns = QtWidgets.QLineEdit(self.Account)
        self.openbouns.setGeometry(QtCore.QRect(100, 180, 113, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.openbouns.setFont(font)
        self.openbouns.setObjectName("openbouns")
        self.normalsecondovertime = QtWidgets.QLineEdit(self.Account)
        self.normalsecondovertime.setGeometry(QtCore.QRect(380, 170, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.normalsecondovertime.setFont(font)
        self.normalsecondovertime.setObjectName("normalsecondovertime")
        self.pushButton_4 = QtWidgets.QPushButton(self.Account)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 730, 93, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.Account)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 730, 93, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.Account)
        self.pushButton_6.setGeometry(QtCore.QRect(430, 730, 93, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_33 = QtWidgets.QLabel(self.Account)
        self.label_33.setGeometry(QtCore.QRect(290, 630, 58, 16))
        self.label_33.setObjectName("label_33")
        self.pushButton_7 = QtWidgets.QPushButton(self.Account)
        self.pushButton_7.setGeometry(QtCore.QRect(400, 0, 121, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.ename_2 = QtWidgets.QLabel(self.Account)
        self.ename_2.setGeometry(QtCore.QRect(390, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.ename_2.setFont(font)
        self.ename_2.setObjectName("ename_2")
        self.eid_2 = QtWidgets.QLabel(self.Account)
        self.eid_2.setGeometry(QtCore.QRect(300, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.eid_2.setFont(font)
        self.eid_2.setObjectName("eid_2")
        self.label_36 = QtWidgets.QLabel(self.Account)
        self.label_36.setGeometry(QtCore.QRect(100, 90, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.Account)
        self.label_37.setGeometry(QtCore.QRect(380, 110, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.Account)
        self.label_38.setGeometry(QtCore.QRect(10, 530, 61, 16))
        self.label_38.setObjectName("label_38")
        self.normaltotal = QtWidgets.QLineEdit(self.Account)
        self.normaltotal.setGeometry(QtCore.QRect(100, 530, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.normaltotal.setFont(font)
        self.normaltotal.setObjectName("normaltotal")
        self.label_39 = QtWidgets.QLabel(self.Account)
        self.label_39.setGeometry(QtCore.QRect(290, 530, 61, 16))
        self.label_39.setObjectName("label_39")
        self.overtimetotal = QtWidgets.QLineEdit(self.Account)
        self.overtimetotal.setGeometry(QtCore.QRect(380, 530, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.overtimetotal.setFont(font)
        self.overtimetotal.setObjectName("overtimetotal")
        self.label_7 = QtWidgets.QLabel(self.Account)
        self.label_7.setGeometry(QtCore.QRect(220, 120, 58, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.Account)
        self.label_8.setGeometry(QtCore.QRect(220, 150, 58, 21))
        self.label_8.setObjectName("label_8")
        self.label_25 = QtWidgets.QLabel(self.Account)
        self.label_25.setGeometry(QtCore.QRect(220, 180, 58, 21))
        self.label_25.setObjectName("label_25")
        self.label_34 = QtWidgets.QLabel(self.Account)
        self.label_34.setGeometry(QtCore.QRect(220, 210, 58, 21))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.Account)
        self.label_35.setGeometry(QtCore.QRect(220, 240, 58, 21))
        self.label_35.setObjectName("label_35")
        self.label_40 = QtWidgets.QLabel(self.Account)
        self.label_40.setGeometry(QtCore.QRect(220, 360, 58, 21))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.Account)
        self.label_41.setGeometry(QtCore.QRect(220, 300, 58, 21))
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.Account)
        self.label_42.setGeometry(QtCore.QRect(220, 410, 58, 21))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.Account)
        self.label_43.setGeometry(QtCore.QRect(220, 270, 58, 21))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.Account)
        self.label_44.setGeometry(QtCore.QRect(220, 440, 58, 21))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.Account)
        self.label_45.setGeometry(QtCore.QRect(220, 330, 58, 21))
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.Account)
        self.label_46.setGeometry(QtCore.QRect(220, 470, 58, 21))
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.Account)
        self.label_47.setGeometry(QtCore.QRect(220, 530, 58, 21))
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.Account)
        self.label_48.setGeometry(QtCore.QRect(220, 600, 58, 21))
        self.label_48.setObjectName("label_48")
        self.label_51 = QtWidgets.QLabel(self.Account)
        self.label_51.setGeometry(QtCore.QRect(500, 140, 58, 21))
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.Account)
        self.label_52.setGeometry(QtCore.QRect(500, 170, 58, 21))
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.Account)
        self.label_53.setGeometry(QtCore.QRect(500, 200, 58, 21))
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.Account)
        self.label_54.setGeometry(QtCore.QRect(500, 230, 58, 21))
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.Account)
        self.label_55.setGeometry(QtCore.QRect(500, 260, 58, 21))
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.Account)
        self.label_56.setGeometry(QtCore.QRect(500, 290, 58, 21))
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.Account)
        self.label_57.setGeometry(QtCore.QRect(500, 320, 58, 21))
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(self.Account)
        self.label_58.setGeometry(QtCore.QRect(500, 350, 58, 21))
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.Account)
        self.label_59.setGeometry(QtCore.QRect(500, 380, 58, 21))
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.Account)
        self.label_60.setGeometry(QtCore.QRect(500, 410, 58, 21))
        self.label_60.setObjectName("label_60")
        self.label_63 = QtWidgets.QLabel(self.Account)
        self.label_63.setGeometry(QtCore.QRect(500, 530, 58, 21))
        self.label_63.setObjectName("label_63")
        self.label_64 = QtWidgets.QLabel(self.Account)
        self.label_64.setGeometry(QtCore.QRect(500, 630, 58, 21))
        self.label_64.setObjectName("label_64")
        self.label_50 = QtWidgets.QLabel(self.Account)
        self.label_50.setGeometry(QtCore.QRect(90, 50, 58, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.label_61 = QtWidgets.QLabel(self.Account)
        self.label_61.setGeometry(QtCore.QRect(240, 50, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_61.setFont(font)
        self.label_61.setObjectName("label_61")
        self.line = QtWidgets.QFrame(self.Account)
        self.line.setGeometry(QtCore.QRect(0, 70, 531, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.comboBox = QtWidgets.QComboBox(self.Account)
        self.comboBox.setGeometry(QtCore.QRect(0, 0, 161, 22))
        self.comboBox.setObjectName("comboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1088, 25))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionMain = QtWidgets.QAction(MainWindow)
        self.actionMain.setObjectName("actionMain")
        self.actionehistory = QtWidgets.QAction(MainWindow)
        self.actionehistory.setObjectName("actionehistory")
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actiondelete = QtWidgets.QAction(MainWindow)
        self.actiondelete.setObjectName("actiondelete")
        self.actionsetting = QtWidgets.QAction(MainWindow)
        self.actionsetting.setObjectName("actionsetting")
        self.actionchistory = QtWidgets.QAction(MainWindow)
        self.actionchistory.setObjectName("actionchistory")
        self.actionehistory_2 = QtWidgets.QAction(MainWindow)
        self.actionehistory_2.setObjectName("actionehistory_2")
        self.menu.addAction(self.actionnew)
        self.menu.addAction(self.actiondelete)
        self.menu_2.addAction(self.actionsetting)
        self.menu_3.addAction(self.actionchistory)
        self.menu_3.addAction(self.actionehistory_2)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.undoview, self.eid)
        MainWindow.setTabOrder(self.eid, self.seniority)
        MainWindow.setTabOrder(self.seniority, self.eproperty)
        MainWindow.setTabOrder(self.eproperty, self.spectialdayoff)
        MainWindow.setTabOrder(self.spectialdayoff, self.ename)
        MainWindow.setTabOrder(self.ename, self.basicsalary_2)
        MainWindow.setTabOrder(self.basicsalary_2, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.basicsalary)
        MainWindow.setTabOrder(self.basicsalary, self.normalmeals)
        MainWindow.setTabOrder(self.normalmeals, self.openbouns)
        MainWindow.setTabOrder(self.openbouns, self.responsiblebouns)
        MainWindow.setTabOrder(self.responsiblebouns, self.otherplus)
        MainWindow.setTabOrder(self.otherplus, self.dayoff)
        MainWindow.setTabOrder(self.dayoff, self.borrow)
        MainWindow.setTabOrder(self.borrow, self.mealcall)
        MainWindow.setTabOrder(self.mealcall, self.otherminus)
        MainWindow.setTabOrder(self.otherminus, self.allrbouns)
        MainWindow.setTabOrder(self.allrbouns, self.workerfee)
        MainWindow.setTabOrder(self.workerfee, self.healthfee)
        MainWindow.setTabOrder(self.healthfee, self.normalfirstovertime)
        MainWindow.setTabOrder(self.normalfirstovertime, self.normalsecondovertime)
        MainWindow.setTabOrder(self.normalsecondovertime, self.normalovertime_meals)
        MainWindow.setTabOrder(self.normalovertime_meals, self.saturdayovertime)
        MainWindow.setTabOrder(self.saturdayovertime, self.saturdayovertime_meals)
        MainWindow.setTabOrder(self.saturdayovertime_meals, self.sundayovertime)
        MainWindow.setTabOrder(self.sundayovertime, self.sundayfovertime_meals)
        MainWindow.setTabOrder(self.sundayfovertime_meals, self.specialovertime)
        MainWindow.setTabOrder(self.specialovertime, self.specialovertime_meals)
        MainWindow.setTabOrder(self.specialovertime_meals, self.overtimeother)
        MainWindow.setTabOrder(self.overtimeother, self.normaltotal)
        MainWindow.setTabOrder(self.normaltotal, self.overtimetotal)
        MainWindow.setTabOrder(self.overtimetotal, self.laborpension)
        MainWindow.setTabOrder(self.laborpension, self.total_salary)
        MainWindow.setTabOrder(self.total_salary, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.pushButton_6)
        MainWindow.setTabOrder(self.pushButton_6, self.pushButton_7)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Totalpay.setText(_translate("MainWindow", "1,000,000,000"))
        self.label.setText(_translate("MainWindow", "員工編號"))
        self.label_2.setText(_translate("MainWindow", "年資"))
        self.label_3.setText(_translate("MainWindow", "員工性質"))
        self.label_4.setText(_translate("MainWindow", "特休"))
        self.label_5.setText(_translate("MainWindow", "員工姓名"))
        self.label_6.setText(_translate("MainWindow", "基本底薪"))
        self.pushButton.setText(_translate("MainWindow", "修改"))
        self.pushButton_2.setText(_translate("MainWindow", "完成"))
        self.month.setText(_translate("MainWindow", "month"))
        self.year.setText(_translate("MainWindow", "year"))
        self.label_9.setText(_translate("MainWindow", "基本底薪"))
        self.label_10.setText(_translate("MainWindow", "伙食津貼"))
        self.label_11.setText(_translate("MainWindow", "全勤獎金"))
        self.label_12.setText(_translate("MainWindow", "開門津貼"))
        self.label_13.setText(_translate("MainWindow", "其他+"))
        self.label_14.setText(_translate("MainWindow", "請假"))
        self.label_15.setText(_translate("MainWindow", "責任津貼"))
        self.label_16.setText(_translate("MainWindow", "其他-"))
        self.label_17.setText(_translate("MainWindow", "勞保費"))
        self.label_18.setText(_translate("MainWindow", "健保費"))
        self.label_19.setText(_translate("MainWindow", "借支"))
        self.label_20.setText(_translate("MainWindow", "代訂伙食"))
        self.label_21.setText(_translate("MainWindow", "休伙食"))
        self.label_22.setText(_translate("MainWindow", "國定加"))
        self.label_23.setText(_translate("MainWindow", "國定伙食"))
        self.label_24.setText(_translate("MainWindow", "加班其他"))
        self.label_26.setText(_translate("MainWindow", "勞退"))
        self.label_27.setText(_translate("MainWindow", "平加1"))
        self.label_28.setText(_translate("MainWindow", "平加2"))
        self.label_29.setText(_translate("MainWindow", "平加伙"))
        self.label_30.setText(_translate("MainWindow", "例假加"))
        self.label_31.setText(_translate("MainWindow", "例加伙食"))
        self.label_32.setText(_translate("MainWindow", "休加"))
        self.basicsalary.setText(_translate("MainWindow", "0"))
        self.healthfee.setText(_translate("MainWindow", "0"))
        self.sundayovertime.setText(_translate("MainWindow", "0"))
        self.saturdayovertime_meals.setText(_translate("MainWindow", "0"))
        self.mealcall.setText(_translate("MainWindow", "0"))
        self.otherminus.setText(_translate("MainWindow", "0"))
        self.borrow.setText(_translate("MainWindow", "0"))
        self.normalfirstovertime.setText(_translate("MainWindow", "0"))
        self.saturdayovertime.setText(_translate("MainWindow", "0"))
        self.laborpension.setText(_translate("MainWindow", "0"))
        self.workerfee.setText(_translate("MainWindow", "0"))
        self.responsiblebouns.setText(_translate("MainWindow", "0"))
        self.otherplus.setText(_translate("MainWindow", "0"))
        self.dayoff.setText(_translate("MainWindow", "0"))
        self.total_salary.setText(_translate("MainWindow", "0"))
        self.overtimeother.setText(_translate("MainWindow", "0"))
        self.specialovertime.setText(_translate("MainWindow", "0"))
        self.sundayfovertime_meals.setText(_translate("MainWindow", "0"))
        self.specialovertime_meals.setText(_translate("MainWindow", "0"))
        self.normalovertime_meals.setText(_translate("MainWindow", "0"))
        self.allrbouns.setText(_translate("MainWindow", "0"))
        self.normalmeals.setText(_translate("MainWindow", "0"))
        self.openbouns.setText(_translate("MainWindow", "0"))
        self.normalsecondovertime.setText(_translate("MainWindow", "0"))
        self.pushButton_4.setText(_translate("MainWindow", "刪除"))
        self.pushButton_5.setText(_translate("MainWindow", "預覽"))
        self.pushButton_6.setText(_translate("MainWindow", "新增"))
        self.label_33.setText(_translate("MainWindow", "本月薪水"))
        self.pushButton_7.setText(_translate("MainWindow", "本月結算"))
        self.ename_2.setText(_translate("MainWindow", "ename"))
        self.eid_2.setText(_translate("MainWindow", "eid"))
        self.label_36.setText(_translate("MainWindow", "一般項"))
        self.label_37.setText(_translate("MainWindow", "加班項"))
        self.label_38.setText(_translate("MainWindow", "一般總和"))
        self.normaltotal.setText(_translate("MainWindow", "0"))
        self.label_39.setText(_translate("MainWindow", "加班總和"))
        self.overtimetotal.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "元"))
        self.label_8.setText(_translate("MainWindow", "次"))
        self.label_25.setText(_translate("MainWindow", "次"))
        self.label_34.setText(_translate("MainWindow", "元"))
        self.label_35.setText(_translate("MainWindow", "元"))
        self.label_40.setText(_translate("MainWindow", "元"))
        self.label_41.setText(_translate("MainWindow", "元"))
        self.label_42.setText(_translate("MainWindow", "元"))
        self.label_43.setText(_translate("MainWindow", "小時"))
        self.label_44.setText(_translate("MainWindow", "元"))
        self.label_45.setText(_translate("MainWindow", "次"))
        self.label_46.setText(_translate("MainWindow", "元"))
        self.label_47.setText(_translate("MainWindow", "元"))
        self.label_48.setText(_translate("MainWindow", "元"))
        self.label_51.setText(_translate("MainWindow", "小時"))
        self.label_52.setText(_translate("MainWindow", "小時"))
        self.label_53.setText(_translate("MainWindow", "次"))
        self.label_54.setText(_translate("MainWindow", "天"))
        self.label_55.setText(_translate("MainWindow", "次"))
        self.label_56.setText(_translate("MainWindow", "天"))
        self.label_57.setText(_translate("MainWindow", "次"))
        self.label_58.setText(_translate("MainWindow", "天"))
        self.label_59.setText(_translate("MainWindow", "次"))
        self.label_60.setText(_translate("MainWindow", "元"))
        self.label_63.setText(_translate("MainWindow", "元"))
        self.label_64.setText(_translate("MainWindow", "元"))
        self.label_50.setText(_translate("MainWindow", "年"))
        self.label_61.setText(_translate("MainWindow", "月"))
        self.menu.setTitle(_translate("MainWindow", "員工"))
        self.menu_2.setTitle(_translate("MainWindow", "設定"))
        self.menu_3.setTitle(_translate("MainWindow", "資料"))
        self.actionMain.setText(_translate("MainWindow", "setvalue"))
        self.actionehistory.setText(_translate("MainWindow", "ehistory"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actiondelete.setText(_translate("MainWindow", "delete"))
        self.actionsetting.setText(_translate("MainWindow", "setting"))
        self.actionchistory.setText(_translate("MainWindow", "chistory"))
        self.actionehistory_2.setText(_translate("MainWindow", "ehistory"))


    #listview click guide event(prevent)
    def undoclick_setting(self,MainWindow):
        #basic info disable
        self.info_disable()
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(False)        
        #Account-detail
        self.account_able()


    #listview show
    def show_undoview(self):
        #view禁止點擊來編輯
        self.undoview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.undoview.setModel(self.model)
        self.controller.show_undoview()


    #防呆引導insert switch
    def info_able(self):
        self.eproperty.setEnabled(True)
        self.ename.setEnabled(True)
        self.seniority.setEnabled(True)
        self.spectialdayoff.setEnabled(True)
        self.basicsalary_2.setEnabled(True)
    def info_disable(self):
        self.eid.setEnabled(False)
        self.eproperty.setEnabled(False)
        self.ename.setEnabled(False)
        self.seniority.setEnabled(False)
        self.spectialdayoff.setEnabled(False)
        self.basicsalary.setEnabled(False)
        self.basicsalary_2.setEnabled(False)
        self.pushButton.setEnabled(False)
    def account_able(self):
        self.normalmeals.setEnabled(True)
        self.allrbouns.setEnabled(True)
        self.openbouns.setEnabled(True)
        self.responsiblebouns.setEnabled(True)
        self.otherplus.setEnabled(True)
        self.workerfee.setEnabled(True)
        self.healthfee.setEnabled(True)
        self.dayoff.setEnabled(True)
        self.borrow.setEnabled(True)
        self.mealcall.setEnabled(True)
        self.otherminus.setEnabled(True)
        self.normalfirstovertime.setEnabled(True)
        self.normalsecondovertime.setEnabled(True)
        self.saturdayovertime.setEnabled(True)
        self.specialovertime.setEnabled(True)
        self.sundayovertime.setEnabled(True)
        self.normalovertime_meals.setEnabled(True)
        self.saturdayovertime_meals.setEnabled(True)
        self.specialovertime_meals.setEnabled(True)
        self.sundayfovertime_meals.setEnabled(True)
        self.overtimeother.setEnabled(True)
    def account_disable(self):
        self.total_salary.setEnabled(False)
        self.laborpension.setEnabled(False)
        self.normalmeals.setEnabled(False)
        self.allrbouns.setEnabled(False)
        self.openbouns.setEnabled(False)
        self.responsiblebouns.setEnabled(False)
        self.otherplus.setEnabled(False)
        self.workerfee.setEnabled(False)
        self.healthfee.setEnabled(False)
        self.dayoff.setEnabled(False)
        self.borrow.setEnabled(False)
        self.mealcall.setEnabled(False)
        self.otherminus.setEnabled(False)
        self.normaltotal.setEnabled(False)
        self.normalfirstovertime.setEnabled(False)
        self.normalsecondovertime.setEnabled(False)
        self.saturdayovertime.setEnabled(False)
        self.specialovertime.setEnabled(False)
        self.sundayovertime.setEnabled(False)
        self.normalovertime_meals.setEnabled(False)
        self.saturdayovertime_meals.setEnabled(False)
        self.specialovertime_meals.setEnabled(False)
        self.sundayfovertime_meals.setEnabled(False)
        self.overtimeother.setEnabled(False)
        self.overtimetotal.setEnabled(False)
    def account_button_disable(self):
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)


    #default setting when open App
    def default_set(self):
        #info
        self.info_disable()
        self.pushButton_2.setEnabled(False)
        #Account
        self.account_disable()
        self.account_button_disable()


    #listview click
    def undoview_clicked(self, QModelIndex):
        self.model.click_emp.connect(self.info_change)
        self.controller.undoview_clicked(QModelIndex.row())
        self.undoclick_setting(self)
        self.account_guide_checked(QModelIndex.row())
    def info_change(self, dict_empdata):
        #basic_set
        self.eid.setText(dict_empdata['eid'])
        self.eproperty.setText(dict_empdata['eproperty'])
        self.ename.setText(dict_empdata['ename'])
        self.seniority.setText(str(dict_empdata['seniority']))
        self.spectialdayoff.setText(str(dict_empdata['specialdayoff']))
        self.basicsalary.setText(str(dict_empdata['basicsalary']))
        self.basicsalary_2.setText(str(dict_empdata['basicsalary']))
        #Account
        self.eid_2.setText(dict_empdata['eid'])
        self.ename_2.setText(dict_empdata['ename'])    
        #Account-detail
        self.total_salary.setText(str(dict_empdata['total_salary']))
        self.laborpension.setText(str(dict_empdata['laborpension']))
        self.normalmeals.setText(str(dict_empdata['normalmeals']))
        self.allrbouns.setText(str(dict_empdata['allrbouns']))
        self.openbouns.setText(str(dict_empdata['openbouns']))
        self.responsiblebouns.setText(str(dict_empdata['responsiblebouns']))
        self.otherplus.setText(str(dict_empdata['otherplus']))
        self.workerfee.setText(str(dict_empdata['workerfee']))
        self.healthfee.setText(str(dict_empdata['healthfee']))
        self.dayoff.setText(str(dict_empdata['dayoff']))
        self.borrow.setText(str(dict_empdata['borrow']))
        self.mealcall.setText(str(dict_empdata['mealcall']))
        self.otherminus.setText(str(dict_empdata['otherminus']))
        self.normaltotal.setText(str(dict_empdata['normaltotal']))
        self.normalfirstovertime.setText(str(dict_empdata['normalfirstovertime']))
        self.normalsecondovertime.setText(str(dict_empdata['normalsecondovertime']))
        self.saturdayovertime.setText(str(dict_empdata['saturdayovertime']))
        self.specialovertime.setText(str(dict_empdata['specialovertime']))
        self.sundayovertime.setText(str(dict_empdata['sundayovertime']))
        self.normalovertime_meals.setText(str(dict_empdata['normalovertime_meals']))
        self.saturdayovertime_meals.setText(str(dict_empdata['saturdayovertime_meals']))
        self.specialovertime_meals.setText(str(dict_empdata['specialovertime_meals']))
        self.sundayfovertime_meals.setText(str(dict_empdata['sundayfovertime_meals']))
        self.overtimeother.setText(str(dict_empdata['overtimeother']))
        self.overtimetotal.setText(str(dict_empdata['overtimetotal']))


    #一般資訊編輯click
    def infodata_edit_clicked(self):
        self.model.info_edit_click.connect(self.infodata_editable)
        self.controller.infodata_edit_clicked()
    def infodata_editable(self):
        self.info_able()
        self.pushButton_2.setEnabled(True)
        self.account_disable()


    
    def infodata_done_clicked(self):
        '''一般資訊完成click'''
        try:
            self.model.info_done_click.connect(self.update_infodata)
            self.tmp = [
                self.eid.text(),
                self.eproperty.text(),
                self.ename.text(),
                int(self.seniority.text()),
                int(self.spectialdayoff.text()),
                int(self.basicsalary_2.text())
            ]
            self.controller.infodata_done_clicked(self.tmp)
        except:
            QtWidgets.QMessageBox.information(self, '發生錯誤', '檢查是否已點擊員工或輸入錯誤')
        finally:
            self.model.info_done_click.disconnect(self.update_infodata)
            self.account_disable()
    def update_infodata(self, eid_data):
        #不用messagebox, 用label顯示 尚未處理
        QtWidgets.QMessageBox.information(self, '修改成功', '%s 已更新資料'%eid_data)
        self.basicsalary.setText(self.basicsalary_2.text())
        self.controller.show_undoview()
        self.undoclick_setting(self)


    #試算表引導button event
    def account_guide_checked(self, Index):
        self.model.account_guide_signal.connect(self.button_guide)
        self.controller.account_guide_checked(Index)
        self.model.account_guide_signal.disconnect(self.button_guide)
    def button_guide(self,salaryischecked):
        if salaryischecked == '0':
            self.account_able()
            #4,5,6 delete,preview,update/create
            self.pushButton_4.setEnabled(False)
            self.pushButton_5.setEnabled(False)
            self.pushButton_6.setEnabled(True)
        if salaryischecked == '1':
            self.pushButton_4.setEnabled(True)
            self.pushButton_5.setEnabled(True)
            self.pushButton_6.setEnabled(True)


    #新增更新create/update試算表click
    def create_account_clicked(self):
        self.model.create_click.connect(self.addtodoneview)
        self.data = {
            'eid'         :self.eid.text(),
            'year'        :self.year.text(),
            'month'       :self.month.text(),
            #-------------
            'basicsalary': int(self.basicsalary.text()),
            'normalmeals': int(self.normalmeals.text()),
            'openbouns':    int(self.openbouns.text()),
            'responsiblebouns':int(self.responsiblebouns.text()),
            'otherplus':    int(self.otherplus.text()),
            'dayoff':       int(self.dayoff.text()),
            'borrow':       int(self.borrow.text()),
            'mealcall':     int(self.mealcall.text()),
            'otherminus':   int(self.otherminus.text()), 
            #-------normal
            'normalfirstovertime' :int(self.normalfirstovertime.text()),
            'normalsecondovertime':int(self.normalsecondovertime.text()),
            'normalovertime_meals':int(self.normalovertime_meals.text()),
            'saturdayovertime'    :int(self.saturdayovertime.text()),
            'saturdayovertime_meals':int(self.saturdayovertime_meals.text()),
            'sundayovertime'      :int(self.sundayovertime.text()),
            'sundayfovertime_meals':int(self.sundayfovertime_meals.text()),
            'specialovertime'     :int(self.specialovertime.text()),
            'specialovertime_meals':int(self.specialovertime_meals.text()),
            'overtimeother'       :int(self.overtimeother.text()),
            #-------ovetime
            'allrbouns':int(self.allrbouns.text()),
            'workerfee':int(self.workerfee.text()),
            'healthfee':int(self.healthfee.text()),
            'normaltotal':int(self.normaltotal.text()),
            'overtimetotal':int(self.overtimetotal.text()),
            'laborpension':int(self.laborpension.text()),
            'total_salary':int(self.total_salary.text()),
            #-------autoItem  
        }
        
        self.controller.create_account_clicked(self.data)
        self.controller.show_undoview()
        self.model.create_click.disconnect(self.addtodoneview)
        
        self.account_guide_checked(1)
        self.default_set()
        self.sumtotal()
    def addtodoneview(self,strdata):
        self.controller.show_undoview()
        if '###' in strdata:
            QtWidgets.QMessageBox.information(self, '更新成功', '%s之薪水已更新'%strdata.replace("###",""))
        else:
            QtWidgets.QMessageBox.information(self, '新增成功', '%s之薪水已新增'%strdata)
    
    
    #刪除試算表click
    def delete_account_clicked(self):
        self.model.delete_click.connect(self.delete_info)
        self.data = {
            'eid' : self.eid.text(),
            'year': str(self.year.text()),
            'month': str(self.month.text())
        }
        self.controller.delete_account_clicked(self.data)
        self.controller.show_undoview()
        self.model.delete_click.disconnect(self.delete_info)
        self.account_guide_checked(0)
        self.default_set()
        self.sumtotal()
    def delete_info(self,eid):
        self.info = '%s 資料已經被刪除'%eid
        QtWidgets.QMessageBox.information(self, '刪除成功', self.info)
        #account-detail item refresh
        self.total_salary.setText('0')
        self.laborpension.setText('0')
        self.normalmeals.setText('0')
        self.allrbouns.setText('0')
        self.openbouns.setText('0')
        self.responsiblebouns.setText('0')
        self.otherplus.setText('0')
        self.workerfee.setText('0')
        self.healthfee.setText('0')
        self.dayoff.setText('0')
        self.borrow.setText('0')
        self.mealcall.setText('0')
        self.otherminus.setText('0')
        self.normaltotal.setText('0')
        self.normalfirstovertime.setText('0')
        self.normalsecondovertime.setText('0')
        self.saturdayovertime.setText('0')
        self.specialovertime.setText('0')
        self.sundayovertime.setText('0')
        self.normalovertime_meals.setText('0')
        self.saturdayovertime_meals.setText('0')
        self.specialovertime_meals.setText('0')
        self.sundayfovertime_meals.setText('0')
        self.overtimeother.setText('0')
        self.overtimetotal.setText('0')


    #word預覽click
    def preview_word(self):
        self.model.preview_click.connect(self.wordshow)
        self.controller.preview_clicked(self.eid.text())
        self.model.preview_click.disconnect(self.wordshow)
    def wordshow(self, emp_info):
        pass


    #總薪資in label
    def sumtotal(self):
        self.model.sumtotalsignal.connect(self.sum_refresh)
        self.controller.sumtotal()
        self.model.sumtotalsignal.disconnect(self.sum_refresh)
    def sum_refresh(self,sum_salary):
        self.Totalpay.setText(sum_salary)


    #日期
    def get_date(self):
        self.model.date_signal.connect(self.getdate)
        self.controller.get_date()
    def getdate(self,yandm):
        self.year.setText(str(yandm[0]))
        self.month.setText(str(yandm[1]))
    

    #line-edit連結textchange event
    def auto_counting_event(self):
        #normal
        self.normalmeals.textEdited.connect(self.sumhandle)
        self.openbouns.textEdited.connect(self.sumhandle)
        self.responsiblebouns.textChanged.connect(self.sumhandle)
        self.otherplus.textChanged.connect(self.sumhandle)
        self.dayoff.textChanged.connect(self.sumhandle)
        self.borrow.textChanged.connect(self.sumhandle)
        self.mealcall.textChanged.connect(self.sumhandle)
        self.otherminus.textChanged.connect(self.sumhandle)
        
        #overtime
        self.normalfirstovertime.textChanged.connect(self.sumhandle)
        self.normalsecondovertime.textChanged.connect(self.sumhandle)
        self.normalovertime_meals.textChanged.connect(self.sumhandle)
        self.saturdayovertime.textChanged.connect(self.sumhandle)
        self.saturdayovertime_meals.textChanged.connect(self.sumhandle)
        self.sundayovertime.textChanged.connect(self.sumhandle)
        self.sundayfovertime_meals.textChanged.connect(self.sumhandle)
        self.specialovertime.textChanged.connect(self.sumhandle)
        self.specialovertime_meals.textChanged.connect(self.sumhandle)        
        self.overtimeother.textChanged.connect(self.sumhandle)
        
        #auto-count-item
        self.allrbouns.textChanged.connect(self.sumhandle)
        self.workerfee.textChanged.connect(self.sumhandle)
        self.healthfee.textChanged.connect(self.sumhandle)
        self.normaltotal.textChanged.connect(self.sumhandle)
        self.overtimetotal.textChanged.connect(self.sumhandle)
        self.laborpension.textChanged.connect(self.sumhandle)
        self.total_salary.textChanged.connect(self.sumhandle)
    #連結event 做dict丟入model計算
    def sumhandle(self):
        data = {
            'basicsalary': int(self.basicsalary.text()),
            'normalmeals': int(self.normalmeals.text()),
            'openbouns':    int(self.openbouns.text()),
            'responsiblebouns':int(self.responsiblebouns.text()),
            'otherplus':    int(self.otherplus.text()),
            'dayoff':       int(self.dayoff.text()),
            'borrow':       int(self.borrow.text()),
            'mealcall':     int(self.mealcall.text()),
            'otherminus':   int(self.otherminus.text()), 
            #-------normal
            'normalfirstovertime' :int(self.normalfirstovertime.text()),
            'normalsecondovertime':int(self.normalsecondovertime.text()),
            'normalovertime_meals':int(self.normalovertime_meals.text()),
            'saturdayovertime'    :int(self.saturdayovertime.text()),
            'saturdayovertime_meals':int(self.saturdayovertime_meals.text()),
            'sundayovertime'      :int(self.sundayovertime.text()),
            'sundayfovertime_meals':int(self.sundayfovertime_meals.text()),
            'specialovertime'     :int(self.specialovertime.text()),
            'specialovertime_meals':int(self.specialovertime_meals.text()),
            'overtimeother'       :int(self.overtimeother.text()),
            #-------ovetime
            'allrbouns':int(self.allrbouns.text()),
            'workerfee':int(self.workerfee.text()),
            'healthfee':int(self.healthfee.text()),
            'normaltotal':int(self.normaltotal.text()),
            'overtimetotal':int(self.overtimetotal.text()),
            'laborpension':int(self.laborpension.text()),
            'total_salary':int(self.total_salary.text()),
            #-------autoItem  
        }
        self.model.auto_count_value.connect(self.sum_change)
        self.controller.autocount(data)
        self.model.auto_count_value.disconnect(self.sum_change)
    #model計算回來emit total值
    def sum_change(self, auto_data):
        self.allrbouns.setText(auto_data['all'])
        self.workerfee.setText(auto_data['worker'])
        self.healthfee.setText(auto_data['health'])
        self.normaltotal.setText(auto_data['normalt'])
        self.overtimetotal.setText(auto_data['overt'])
        self.laborpension.setText(auto_data['labor'])
        self.total_salary.setText(auto_data['total'])


    
    def close_account(self):
        '''當月結算'''
        self.model.closeAccount.connect(self.change)
        self.controller.close_account()
        self.model.closeAccount.disconnect(self.change)
    def change(self,s):
        #讓combobox處在latest月and refresh combobox
        self.comboshow()
        self.defaultcombox()

    
    def comboshow(self):
        '''日期combobox_event'''
        self.model.comboevent.connect(self.showdate)
        self.controller.comboshow()
        self.model.comboevent.disconnect(self.showdate)
    def showdate(self, alldate):
        self.comboBox.clear()
        self.comboBox.addItems(alldate)


    def defaultcombox(self):
        self.model.defcom.connect(self.d_com_show)
        self.controller.dcs()
        self.model.defcom.disconnect(self.d_com_show)
    def d_com_show(self, date):
        self.comboBox.setCurrentText(str(date[0] + '-' + date[1]))
        print(str(date[0] + '-' + date[1]))
    
    def selectdate(self):
        '''date select event'''
        self.model.dateselectsignal.connect(self.dateback)
        self.controller.selectdate(self.comboBox.currentText())
        self.model.dateselectsignal.disconnect(self.dateback)
    def dateback(self, ym):
        #refresh year, month ,listview, sumtotal, information(更月提示)
        self.show_undoview()
        self.sumtotal()
        self.year.setText(ym[0])
        self.month.setText(ym[1])
        self.islatest()
        #+刻意等待時間

    def islatest(self):
        '''是否為最後登記月'''
        self.model.latesignal.connect(self.closelimit)
        self.controller.islatest(self.year, self.month)
        self.model.latesignal.disconnect(self.closelimit)
    def closelimit(self, bool):
        self.pushButton_7.setEnabled(bool)


#-----------------------------------------------------
#sub view init
    
    def newemp(self):
        self.new_emp_window = New_emp()
        self.new_emp_window.show()
        self.new_emp_window.newemp.clicked.connect(self.new_emp_e) 


    def delemp(self):
        self.del_emp_window = Del_emp()
        self.del_emp_window.show()
        self.del_emp_window.delbutton.clicked.connect(self.del_emp_e) 

        self.model.initdel.connect(self.del_init)
        self.controller.delshow()
        self.model.initdel.disconnect(self.del_init)
    def del_init(self, iddata):
        '''combobox init顯示'''
        self.del_emp_window.dcomboBox.addItems(iddata)
        

    def valueset(self):
        '''參數設定窗顯示以及預設原始資料from DB-> setvalues'''
        self.svs_window = Setvalues()
        self.svs_window.show()
        self.svs_window.setbutton.clicked.connect(self.setvalues_e) 

        self.model.initset.connect(self.setview_init)
        self.controller.showset()
        self.model.initset.disconnect(self.setview_init)
    def setview_init(self, data):
        '''初始化資料顯示'''
        self.svs_window.l1.setText(str(data[0]))
        self.svs_window.l2.setText(str(data[1]))
        self.svs_window.l3.setText(str(data[2]))
        self.svs_window.l4.setText(str(data[3]))
        self.svs_window.l5.setText(str(data[4]))
        self.svs_window.l6.setText(str(data[5]))
        self.svs_window.l7.setText(str(data[6]))
        self.svs_window.l8.setText(str(data[7]))


    def data_his(self):
        pass

#-----------------------------------------------------
#sub-view event

    def new_emp_e(self):
        '''新增員工button事件'''
        self.model.newemp.connect(self.new_emp_refresh)
        dic = {
            'eid' : self.new_emp_window.e1.text(),
            'eproperty' : self.new_emp_window.e2.text(),
            'ename' : self.new_emp_window.e3.text(),
            'date' : self.new_emp_window.e4.text()
        }
        self.controller.new_emp(dic)
        self.model.newemp.disconnect(self.new_emp_refresh)
    def new_emp_refresh(self):
        self.show_undoview()   
        self.new_emp_window.close()


    def del_emp_e(self):
        '''del emp combobox event'''
        self.model.delemp.connect(self.refreshview)
        self.controller.del_emp_e(self.del_emp_window.dcomboBox.currentText())
        self.model.delemp.disconnect(self.refreshview)      
    def del_emp_refresh(self):
        self.show_undoview()   
        self.del_emp_window.close()        


    def setvalues_e(self):
        '''set values button clicked event'''
        self.model.valuesetting.connect(self.setdone)
        dic = {
            'workerfee':self.svs_window.l1.text(),
            'healthfee':self.svs_window.l2.text(),
            'openb':self.svs_window.l3.text(),
            'allb':self.svs_window.l4.text(),
            'respb':self.svs_window.l5.text(),
            'meal':self.svs_window.l6.text(),
            'over1':self.svs_window.l7.text(),
            'over2':self.svs_window.l8.text()            
        }
        self.controller.setvalues_e(dic)
        self.model.valuesetting.disconnect(self.setdone)
    def setdone(self):
        QtWidgets.QMessageBox.information(self, '參數設定', '設定成功')
        self.svs_window.close()


    def refreshview(self,id):
        print(id)
        self.show_undoview()        


    #依照該button對應event進行connect (各事件再處理與controller的互動，這邊只是連接畫面跟事件觸及)
    def attachcontroller(self):
        #listview activate
        self.undoview.clicked.connect(self.undoview_clicked)
        self.undoview.activated.connect(self.undoview_clicked)
        
        #infodata page
        self.pushButton.clicked.connect(self.infodata_edit_clicked)
        self.pushButton_2.clicked.connect(self.infodata_done_clicked)        
        
        #account page
        #self.pushButton_3.clicked.connect(self.accountdata_clicked)
        self.pushButton_4.clicked.connect(self.delete_account_clicked)
        self.pushButton_5.clicked.connect(self.preview_word)
        self.pushButton_6.clicked.connect(self.create_account_clicked)
        
        #close-account
        self.pushButton_7.clicked.connect(self.close_account)

        #dateselect
        self.comboBox.currentIndexChanged.connect(self.selectdate)

        "-------Subclass-------"

        #emp page
        self.actionnew.triggered.connect(self.newemp)
        self.actiondelete.triggered.connect(self.delemp)
        #setting page
        self.actionsetting.triggered.connect(self.valueset)
        # history

