'''
FCFS Disk Scheduling Simulator
By :
    Abhi Patel (IU1941230097)
    Pavan Patel (IU1941230112)
    Saurav Panchal (IU1941230093)
Class :
    CSE - B
Subject :
    Operating System
Faculty :
    Khushbu Maurya
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pyqtgraph import *
import pyqtgraph as pg
import webbrowser
import random
import sys
import os

class Ui_MainWindow():
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1101, 772)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        MainWindow.setCentralWidget(self.centralwidget)
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 521, 251))
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.raise_()

        
        self.setting = QtWidgets.QWidget()
        self.setting.setObjectName("setting")
        self.tabWidget.addTab(self.setting, "")


        # Disk Requests
        self.label_1 = QtWidgets.QLabel(self.setting)
        self.label_1.setGeometry(QtCore.QRect(10, 0, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")

        # Fill Random
        self.pushButton_1 = QtWidgets.QPushButton(self.setting)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 40, 111, 28))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(lambda: self.random_fill())

        # Edit
        self.pushButton_2 = QtWidgets.QPushButton(self.setting)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 80, 111, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.edit_button())

        # Clear
        self.pushButton_3 = QtWidgets.QPushButton(self.setting)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 120, 111, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.clear_button())

        # Enter Disk Requests Here ...
        self.lineEdit = QtWidgets.QLineEdit(self.setting, placeholderText = "Enter Disk Requests Here ...")
        self.lineEdit.setGeometry(QtCore.QRect(133, 10, 371, 100))
        self.lineEdit.setFont(QtGui.QFont("Arial",20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(lambda: self.clicked())
        self.validator()

        # *Separate requests by comma
        self.label_2 = QtWidgets.QLabel(self.setting)
        self.label_2.setGeometry(QtCore.QRect(130, 121, 371, 27))
        self.label_2.setFont(QtGui.QFont("",7))
        self.label_2.setObjectName("label_2")


        self.control = QtWidgets.QWidget()
        self.control.setObjectName("control")
        self.tabWidget.addTab(self.control, "")
        

        # Initital Head Position
        self.label_3 = QtWidgets.QLabel(self.control)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        
        self.spinBox = QtWidgets.QSpinBox(self.control)
        self.spinBox.setGeometry(QtCore.QRect(180, 10, 61, 31))
        self.min_value = 0
        self.max_value = 200
        self.spinBox.setRange(self.min_value, self.max_value)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.raise_()

        # Widget 1 (Minimum Cylinder, HSlider1, Label)
        self.widget_1 = QtWidgets.QWidget(self.control)
        self.widget_1.setGeometry(QtCore.QRect(10, 60, 241, 81))
        self.widget_1.setObjectName("widget_1")
        self.widget_1.raise_()
        
        # Minimum Cyclinder
        self.label_4 = QtWidgets.QLabel(self.widget_1)
        self.label_4.setGeometry(QtCore.QRect(60, 0, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.horizontalSlider_1 = QtWidgets.QSlider(self.widget_1)
        self.horizontalSlider_1.setGeometry(QtCore.QRect(10, 40, 211, 31))
        self.horizontalSlider_1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_1.setMinimum(0)
        self.horizontalSlider_1.setValue(0)
        self.horizontalSlider_1.setMaximum(20)
        self.horizontalSlider_1.setTickInterval(5)
        self.horizontalSlider_1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_1.setObjectName("horizontalSlider_1")
        self.horizontalSlider_1.valueChanged.connect(self.changedValue)

        # HSlider-1 Values Display
        self.label_5 = QtWidgets.QLabel(self.control)
        self.label_5.setGeometry(QtCore.QRect(110, 140, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()

        # Widget 2 (Maximum Cyclinders, HSlider, Label)
        self.widget_2 = QtWidgets.QWidget(self.control)
        self.widget_2.setGeometry(QtCore.QRect(260, 60, 241, 81))
        self.widget_2.setObjectName("widget_2")
        self.widget_2.raise_()

        # Maximum Cyclinder
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(60, 0, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.horizontalSlider_2 = QtWidgets.QSlider(self.widget_2)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(10, 40, 211, 31))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setMinimum(10)
        self.horizontalSlider_2.setValue(0)
        self.horizontalSlider_2.setMaximum(250)
        self.horizontalSlider_2.setTickInterval(15)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.valueChanged.connect(self.changedValue)

        # HSlider-2 Values Display
        self.label_7 = QtWidgets.QLabel(self.control)
        self.label_7.setGeometry(QtCore.QRect(370, 140, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()


        # Report GroupBox
        self.groupBox_1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_1.setGeometry(QtCore.QRect(540, 30, 551, 171))
        self.groupBox_1.setFlat(False)
        self.groupBox_1.setObjectName("groupBox_1")
        self.groupBox_1.raise_()

        # Seek Count
        self.label_8 = QtWidgets.QLabel(self.groupBox_1)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        # Seek Count Display
        self.plainTextEdit_1 = QtWidgets.QPlainTextEdit(self.groupBox_1, readOnly = True)
        self.plainTextEdit_1.setGeometry(QtCore.QRect(110, 20, 431, 51))
        self.plainTextEdit_1.setObjectName("plainTextEdit_1")

        # Avg Seek Count
        self.label_9 = QtWidgets.QLabel(self.groupBox_1)
        self.label_9.setGeometry(QtCore.QRect(10, 80, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        # Avg Seek Count Display
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.groupBox_1, readOnly = True)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(110, 80, 100, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")

        # Horizontal Line Separator
        self.line_1 = QtWidgets.QFrame(self.groupBox_1)
        self.line_1.setGeometry(QtCore.QRect(37, 110, 481, 20))
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
      
        # Re-Draw Graph
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_1)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 130, 151, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.redraw_graph())


        # Answer
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(550, 220, 160, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda: self.clicked())
        self.pushButton_5.raise_()

        # Reset
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(718, 220, 160, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda: self.reset_button())

        # Vertical Line Separator
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(800, 220, 200, 28))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        # New
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(920, 220, 161, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda: self.reset_button())
        self.pushButton_7.raise_()


        # Graph GroupBox
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 270, 1081, 451))
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.raise_()

        self.graphWidget = pg.PlotWidget(self.groupBox_2)
        self.graphWidget.setGeometry(QtCore.QRect(10, 20, 1061, 421))
        self.graphWidget.setLabels(title = 'FCFS Disk Scheduling')
        self.graphWidget.showGrid(True)
        self.graphWidget.setObjectName("graphWidget")
        self.x = []
        self.y = []
        if(self.x == [] and self.y == []):
            self.pushButton_4.hide()
            self.graphWidget.hide()
        
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1101, 26))
        self.menubar.setObjectName("menubar")
        
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        

        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.triggered.connect(lambda: self.reset_button())

        self.actionExit = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionExit.setFont(font)
        self.actionExit.setShortcut("Ctrl+Q")
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(QtWidgets.QApplication.quit)

        
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionReset.triggered.connect(lambda: self.reset_button())
        
        self.actionRedraw_Graph = QtWidgets.QAction(MainWindow)
        self.actionRedraw_Graph.setObjectName("actionRedraw_Graph")
        self.actionRedraw_Graph.triggered.connect(lambda: self.redraw_graph())
        
        
        self.actionFCFS_Disk_Scheduling = QtWidgets.QAction(MainWindow)
        self.actionFCFS_Disk_Scheduling.setObjectName("actionFCFS_Disk_Scheduling")
        self.actionFCFS_Disk_Scheduling.triggered.connect(lambda: webbrowser.open_new_tab('https://www.javatpoint.com/os-fcfs-scheduling-algorithm'))
        
        
        self.menuFile.addAction(self.actionNew)
        
        self.menuFile.addSeparator()
        
        self.menuFile.addAction(self.actionExit)

        
        self.menuEdit.addAction(self.actionReset)
        
        self.menuEdit.addSeparator()
        
        self.menuEdit.addAction(self.actionRedraw_Graph)

        
        self.menuInfo.addAction(self.actionFCFS_Disk_Scheduling)
        

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())        
        self.menubar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        
        MainWindow.setWindowTitle(_translate("MainWindow", "First Come First Serve Disk Scheduling - Simulator"))
        
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setting), _translate("MainWindow", "Setting"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.control), _translate("MainWindow", "Control"))
        self.label_1.setText(_translate("MainWindow", "Disk Requests :"))
        self.pushButton_1.setText(_translate("MainWindow", "Fill Random"))
        self.pushButton_2.setText(_translate("MainWindow", "Edit"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.label_2.setText(_translate("MainWindow", "<font color = 'red'>*Separate requests by comma \",\"</font>"))
        self.label_3.setText(_translate("MainWindow", "Initial Head Position :"))
        self.label_4.setText(_translate("MainWindow", "Minimum Cylinder :"))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "Maximum Cylinder :"))
        self.label_7.setText(_translate("MainWindow", "0"))        
        

        self.groupBox_1.setTitle(_translate("MainWindow", "Report"))

        self.label_8.setText(_translate("MainWindow", "Seek Count :"))
        self.label_9.setText(_translate("MainWindow", "Avg Seek Count :"))


        self.groupBox_2.setTitle(_translate("MainWindow", "Graph"))

        self.pushButton_4.setText(_translate("MainWindow", "Re-Draw Graph"))
        

        self.pushButton_5.setText(_translate("MainWindow", "Answer"))
        self.pushButton_6.setText(_translate("MainWindow", "Reset"))
        self.pushButton_7.setText(_translate("MainWindow", "New"))
        

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuInfo.setTitle(_translate("MainWindow", "About"))
        

        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create New Simulation"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit Application"))


        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionReset.setStatusTip(_translate("MainWindow", "Reset Simulator"))
        self.actionReset.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionRedraw_Graph.setText(_translate("MainWindow", "Redraw Graph"))
        self.actionRedraw_Graph.setShortcut(_translate("MainWindow", "Ctrl+G"))
        
        
        self.actionFCFS_Disk_Scheduling.setText(_translate("MainWindow", "FCFS Disk Scheduling"))

    def FCFS(self,arr, head):
        seek_count = 0
        distance, cur_track = 0, 0
        string_list = []
        for i in range(self.size):
            cur_track = int(arr[i])
            distance = abs(cur_track - head)
            seek_count += distance
            head = cur_track
        self.plainTextEdit_1.setPlainText(str(seek_count))
        avg = round(seek_count/len(self.my_request), 2)
        self.plainTextEdit_2.setPlainText(str(avg))

    def changedValue(self):
        slider_value_1 = self.horizontalSlider_1.value()
        self.label_5.setText(str(slider_value_1))
        self.label_5.adjustSize()

        slider_value_2 = self.horizontalSlider_2.value()
        self.label_7.setText(str(slider_value_2))
        self.label_7.adjustSize()

    def clear_button(self):
        if(self.lineEdit.text() != ""):
            self.lineEdit.clear()

        else:
            self.show_popup()

    def edit_button(self):
        if(self.lineEdit.text() != ""):
            self.lineEdit.selectAll()
        else:
            self.show_popup()

    def reset_button(self):
        if(self.lineEdit.text() != ""):
            self.lineEdit.clear()
            self.plainTextEdit_1.clear()
            self.plainTextEdit_2.clear()
            self.spinBox.setValue(0)
            self.horizontalSlider_1.setValue(0)
            self.horizontalSlider_2.setValue(0)
            self.x = []
            self.y = []
            self.pushButton_4.hide()
            self.graphWidget.clear()
            self.graphWidget.hide()
        else:
            self.show_popup()        

    def draw_graph(self):
        self.data = self.lineEdit.text()
        self.my_request = self.data.strip()
        self.my_request = self.my_request.split(",")
        self.size = len(self.my_request)
        self.head = self.spinBox.value()
        self.FCFS(self.my_request,self.head)

        self.x.clear()
        self.y.clear()
        self.graphWidget.clear()

        self.x.append(self.head)
        self.y.append(0)
        self.i = 0
        self.num = 0

        self.graphWidget.show()
        self.pushButton_4.show()

        self.graphWidget.plot(self.x, self.y, symbol = 'o')
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.update())
        self.timer.start(350)

    def update(self):
        if(self.i <= len(self.my_request)):
            try:
                self.x.append(int(self.my_request[self.i]))
                self.y.append(self.num)
            except:
                print("Graph Printed !")
            self.i = self.i + 1
            self.num = self.num + 0.5
            self.graphWidget.plot(self.x, self.y, symbol = 'o')
        QtWidgets.QApplication.processEvents()

    def redraw_graph(self):
        print("Printing Graph Again !")
        self.clicked()
        self.x = []
        self.y = []
        self.graphWidget.clear()
        self.draw_graph()
        
    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('icon.png'))
        msg.setWindowTitle("Error 404 [FCFS Disk Scheduling Simulator]")
        msg.setText("Empty Requests Found !")

        msg.setIcon(QMessageBox.Critical)

        x = msg.exec_()

    def show_popup_for_cylinder(self):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('icon.png'))
        msg.setWindowTitle("Cylinder Aspect Mismatch ! [FCFS Disk Scheduling Simulator]")
        msg.setText("Minimum Cylinders >= Maximize Cylinders")
        msg.setDetailedText("Here you have set invalid pairs of minimum & maximum cyclinders !")
        msg.setIcon(QMessageBox.Warning)

        x = msg.exec_()

    def validator(self):
        reg_exp = QRegExp("^[0-9,]+$")
        input_validator = QRegExpValidator(reg_exp, self.lineEdit)
        self.lineEdit.setValidator(input_validator)

    def random_fill(self):
        self.head = self.spinBox.setValue(random.randint(self.min_value, self.max_value))
        self.horizontalSlider_1.setValue(0)
        self.horizontalSlider_2.setValue(199)
        self.random_list = []
        for number in range(0,10):
            n = str(random.randint(self.horizontalSlider_1.value(), self.horizontalSlider_2.value()))
            self.random_list.append(n)
        self.my_random_text = ", ".join(self.random_list)
        self.lineEdit.setText(self.my_random_text)
        self.data = self.lineEdit.text() 
  
    def clicked(self):
        if(self.lineEdit.text() != "" and self.horizontalSlider_1.value() < self.horizontalSlider_2.value()):
            self.data = self.lineEdit.text()
            self.my_request = self.data.strip()
            self.my_request = self.my_request.split(",")
            self.size = len(self.my_request)
            self.head = self.spinBox.value()
            self.FCFS(self.my_request,self.head)
            self.draw_graph()
        elif(self.lineEdit.text() == ""):
            self.show_popup()
        elif(self.horizontalSlider_1.value() >= self.horizontalSlider_2.value()):
            self.show_popup_for_cylinder()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())