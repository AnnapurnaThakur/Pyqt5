# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkbox.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 357)
        MainWindow.setStyleSheet("background-color: rgb(111, 200, 129);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


#######################################################################################################
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(40, 67, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        #self.checkBox.stateChanged.connect(self.check1)
        

#########################################################################################################
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(40, 130, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        #self.checkBox_2.stateChanged.connect(self.check2)


############################################################################################################
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(40, 100, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        #self.checkBox_3.stateChanged.connect(self.check3)



##############################################################################################################
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(108, 255, 214);\n"
"color:rgb(0, 0, 0);\n"
" border-radius:10px;}\n"
"\n"
"QPushButton::hover{\n"
"background-color:rgb(73, 57, 255);\n"
"color:rgb(255, 255, 0);\n"
" border-radius:10px;}\n"
"\n"
"\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.button)

############################################################################################################
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 230, 241, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")


###############################################################################################################
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

###############################################################################################################
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

##################################################################################################################
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
###########################################################################################################

      
    def button(self):
        a=0
        b=0
        c=0
        tot=0
        test1=int(self.checkBox.checkState())
        test2=int(self.checkBox_3.checkState())
        test3=int(self.checkBox_2.checkState())
        if test1==2:
            print("1st amount ")
            a=230
        if test2==2:
            print("2nd amount ")
            b=100

        if test3==2:
            print("3nd amount ")
            c=80

        tot=str(a+b+c)
        print("Total", tot)

        self.lineEdit.setText(tot)

########################################################################################3

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "Rs. 230 rice"))
        self.checkBox_2.setText(_translate("MainWindow", "Rs. 80 Aata "))
        self.checkBox_3.setText(_translate("MainWindow", "Rs. 100 Daal"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.label.setText(_translate("MainWindow", "Total           "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
