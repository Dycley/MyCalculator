# -*- coding: utf-8 -*-
import datetime

# Form implementation generated from reading ui file 'date.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow


class Ui_Date(QMainWindow):
    def setupUi(self, Date):
        Date.setObjectName("Date")
        Date.resize(600, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("calculator.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Date.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Date)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_3.addWidget(self.dateEdit)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.verticalLayout_3.addWidget(self.dateEdit_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.dateEdit_3 = QtWidgets.QDateEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.dateEdit_3.setFont(font)
        self.dateEdit_3.setCalendarPopup(True)
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.verticalLayout_4.addWidget(self.dateEdit_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spinBox = QtWidgets.QSpinBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.spinBox.setFont(font)
        self.spinBox.setMaximum(999)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.spinBox_2 = QtWidgets.QSpinBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setMaximum(999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_2.addWidget(self.spinBox_2)
        self.spinBox_3 = QtWidgets.QSpinBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setMaximum(999)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_2.addWidget(self.spinBox_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        Date.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Date)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 551, 22))
        self.menubar.setObjectName("menubar")
        Date.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Date)
        self.statusbar.setObjectName("statusbar")
        Date.setStatusBar(self.statusbar)
        self.retranslateUi(Date)

        self.frame_2.hide()
        self.comboBox.currentIndexChanged.connect(self.change)
        self.dateEdit.dateChanged.connect(self.calculate_0)
        self.dateEdit_2.dateChanged.connect(self.calculate_0)
        self.dateEdit_3.dateChanged.connect(self.calculate_1)
        self.radioButton.toggled.connect(self.calculate_1)
        self.spinBox.valueChanged.connect(self.calculate_1)
        self.spinBox_2.valueChanged.connect(self.calculate_1)
        self.spinBox_3.valueChanged.connect(self.calculate_1)
        QtCore.QMetaObject.connectSlotsByName(Date)

    def retranslateUi(self, Date):
        _translate = QtCore.QCoreApplication.translate
        Date.setWindowTitle(_translate("Date", "日期计算"))
        self.comboBox.setItemText(0, _translate("Date", "日期之间的相隔时间"))
        self.comboBox.setItemText(1, _translate("Date", "添加或减去天数"))
        self.label.setText(_translate("Date", "开始日期："))
        self.label_2.setText(_translate("Date", "结束日期："))
        self.label_3.setText(_translate("Date", "差值："))
        self.label_4.setText(_translate("Date", "0天"))
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit_2.setDate(QDate.currentDate())
        self.dateEdit_3.setDate(QDate.currentDate())
        self.label_5.setText(_translate("Date", "开始日期："))
        self.radioButton_2.setText(_translate("Date", "添加"))
        self.radioButton.setText(_translate("Date", "减去"))
        self.label_6.setText(_translate("Date", "年"))
        self.label_7.setText(_translate("Date", "月"))
        self.label_8.setText(_translate("Date", "日"))
        self.label_10.setText(_translate("Date", "日期:"))
        self.label_9.setText(_translate("Date", self.dateEdit_3.text()))

    def change(self):
        if self.comboBox.currentIndex() == 0:
            self.frame_2.hide()
            self.frame.show()
        elif self.comboBox.currentIndex() == 1:
            self.frame.hide()
            self.frame_2.show()

    def calculate_0(self):  # 计算日期之间的相隔时间
        date1 = datetime.datetime.strptime(self.dateEdit.text(), "%Y/%m/%d").date()
        date2 = datetime.datetime.strptime(self.dateEdit_2.text(), "%Y/%m/%d").date()
        days = (date2 - date1).days
        self.label_4.setText(str(abs(days)) + "天")

    def calculate_1(self):  # 计算添加或减去天数
        y, m, d = [int(i) for i in self.dateEdit_3.text().split("/")]
        year_delta = self.spinBox.value()
        month_delta = self.spinBox_2.value()
        day_delta = datetime.timedelta(days=self.spinBox_3.value())
        try:
            month_max = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if self.radioButton_2.isChecked():
                Y = y + year_delta + month_delta // 12
                M = (m + month_delta - 1) % 12 + 1
                if Y % 4 == 0 and Y % 100 != 0 or Y % 400 == 0:
                    month_max[2] = 29
                if d > month_max[M]:
                    d = month_max[M]
                date3 = datetime.datetime(Y, M, d)
                date_value = date3 + day_delta
            elif self.radioButton.isChecked():
                Y = y - year_delta - month_delta // 12
                M = (m - month_delta + 1200 - 1) % 12 + 1
                if m < M:
                    Y -= 1
                if Y % 4 == 0 and Y % 100 != 0 or Y % 400 == 0:
                    month_max[2] = 29
                if d > month_max[M]:
                    d = month_max[M]
                date3 = datetime.datetime(Y, M, d)
                date_value = date3 - day_delta
            self.label_9.setText(str(date_value.date()))
        except:
            self.label_9.setText("超出日期")
