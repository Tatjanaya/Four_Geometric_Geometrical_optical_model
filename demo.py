# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QFileDialog, QWidget, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
import simuls_fun
import rebind
from second import NewWindow
from fourth import NewWindow3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(902, 701)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 20, 591, 461))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 520, 141, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 520, 141, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 902, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actioneXIT = QtWidgets.QAction(MainWindow)
        self.actioneXIT.setObjectName("actioneXIT")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionInput = QtWidgets.QAction(MainWindow)
        self.actionInput.setObjectName("actionInput")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionInput_2 = QtWidgets.QAction(MainWindow)
        self.actionInput_2.setObjectName("actionInput_2")
        self.actionCI = QtWidgets.QAction(MainWindow)
        self.actionCI.setObjectName("actionCI")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actioneXIT)
        self.menuRun.addAction(self.actionInput_2)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Unified Model(v2.0)"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton_2.setText(_translate("MainWindow", "退出"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actioneXIT.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionInput.setText(_translate("MainWindow", "Input"))
        self.actionInput_2.setText(_translate("MainWindow", "Run"))

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

        self.actioneXIT.triggered.connect(QCoreApplication.instance().quit)
        self.actionAbout.triggered.connect(lambda: self.open_second_ui())
        self.actionOpen.triggered.connect(lambda: self.openFile())
        self.actionSave.triggered.connect(lambda: self.saveFile())
        self.actionNew.triggered.connect(lambda: self.open_fourth_ui())
        self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton.clicked.connect(self.runFile)
        self.actionInput_2.triggered.connect(lambda: self.runFile())

    def getData(self, str):
        self.textBrowser.setText(str)

    def openFile(self):
        datas = []
        filename, ok = QFileDialog.getOpenFileName(self, "选取文件", r"./", "Text Files(*.txt);;All Files(*)")
        if ok:
            with open(filename, 'r') as f:
                for line in f.readlines():
                    curline = line.strip().split()
                    datas.append([*curline])
            datas = sum(datas, [])
            if len(datas) != 24:
                self.textBrowser.append("不是合适的输入文件")
                return
            global str1
            if datas[20] == "2":
                str1 = "制表符间隔：2"
            else:
                str1 = "空格间隔：1"

            self.textBrowser.setText("波段个数：" + datas[0] + "\n" + \
                                     "观测天顶角最小值：" + datas[1] + "\n" + \
                                     "观测天顶角最大值：" + datas[2] + "\n" + \
                                     "观测天顶角间隔：" + datas[3] + "\n" + \
                                     "太阳天顶角最小值：" + datas[4] + "\n" + \
                                     "太阳天顶角最大值：" + datas[5] + "\n" + \
                                     "太阳天顶角间隔：" + datas[6] + "\n" + \
                                     "观测方位角最小值：" + datas[7] + "\n" + \
                                     "观测方位角最大值：" + datas[8] + "\n" + \
                                     "观测方位角间隔：" + datas[9] + "\n" + \
                                     "太阳方位角最小值：" + datas[10] + "\n" + \
                                     "太阳方位角最大值：" + datas[11] + "\n" + \
                                     "太阳方位角间隔：" + datas[12] + "\n" + \
                                     "LAI最小值：" + datas[13] + "\n" + \
                                     "LAI最大值：" + datas[14] + "\n" + \
                                     "LAI间隔：" + datas[15] + "\n" + \
                                     "基底树干高/垄宽：" + datas[16] + "\n" + \
                                     "冠层厚度/垄间宽：" + datas[17] + "\n" + \
                                     "单位面积树密度/垄高：" + datas[18] + "\n" + \
                                     "树冠半径/垄行-1：" + datas[19] + "\n" + \
                                     str1 + "\n" + \
                                     "输入植被反射率（txt）路径：" + datas[21] + "\n" + \
                                     "输入土壤反射率（txt）路径：" + datas[22] + "\n" + \
                                     "输出文件路径：" + datas[23])

    def open_second_ui(self):
        self.second_ui = NewWindow()
        self.second_ui.show()

    def open_fourth_ui(self):
        self.fourth_ui = NewWindow3()
        self.fourth_ui.show()
        self.fourth_ui.parentclicked.connect(self.getData)

    def saveFile(self):
        try:
            contenttext = self.textBrowser.toPlainText()
            # 得到textBrowser里的全部内容
            strtext = str(contenttext)
            f = QFileDialog.getSaveFileName(self, "选取文件", r"./", "Text Files(*.txt);;All Files(*)")
            datas = []
            with open(f[0], 'w') as f:
                for line in strtext.split("\n"):
                    curline = line.strip().split("：")
                    datas.append(curline[-1])
                f.write(datas[0] + "\n" + \
                        datas[1] + " " + datas[2] + " " + datas[3] + "\n" + \
                        datas[4] + " " + datas[5] + " " + datas[6] + "\n" + \
                        datas[7] + " " + datas[8] + " " + datas[9] + "\n" + \
                        datas[10] + " " + datas[11] + " " + datas[12] + "\n" + \
                        datas[13] + " " + datas[14] + " " + datas[15] + "\n" + \
                        datas[16] + " " + datas[17] + "\n" + \
                        datas[18] + " " + datas[19] + "\n" + \
                        datas[20] + "\n" + \
                        datas[21] + "\n" + \
                        datas[22] + "\n" + \
                        datas[23])
        except Exception as e:
            print(e)

    def runFile(self):
        try:
            self.pushButton.setChecked(True)
            self.pushButton.setAutoExclusive(True)
            contenttext = self.textBrowser.toPlainText()
            # 得到textBrowser里的全部内容
            strtext = str(contenttext)
            datas = []
            for line in strtext.split("\n"):
                curline = line.strip().split("：")
                datas.append(curline[-1])
            if datas[20] == 1:
                flag = 0
            else:
                flag = 1

            # print(datas[19])
            Bands = int(datas[0])
            v_angle_min = int(datas[1])
            v_angle_max = int(datas[2])
            v_interval = int(datas[3])
            s_angle_min = int(datas[4])
            s_angle_max = int(datas[5])
            s_interval = int(datas[6])
            vv_min = int(datas[7])
            vv_max = int(datas[8])
            vv_interval = int(datas[9])
            ss_min = int(datas[10])
            ss_max = int(datas[11])
            ss_interval = int(datas[12])
            LAI_min = float(datas[13])
            LAI_max = float(datas[14])
            LAI_interval = float(datas[15])
            Ha = float(datas[16])
            Hb = float(datas[17])
            nsss = float(datas[18])
            Rsss = float(datas[19])
            Leafpath = datas[21]
            Soilpath = datas[22]
            Outpath = datas[23]
            self.th = MyThread(leafpath=Leafpath, solidpath=Soilpath, filenames=Outpath, bands=Bands, v_min=v_angle_min,
                               v_max=v_angle_max, v_interval=v_interval, s_min=s_angle_min, s_max=s_angle_max,
                               s_interval=s_interval, LAI_min=LAI_min, LAI_max=LAI_max, LAI_interval=LAI_interval,
                               ss_min=ss_min, ss_max=ss_max, ss_interval=ss_interval, vv_min=vv_min, vv_max=vv_max,
                               vv_interval=vv_interval, Ha=Ha, Hb=Hb, nsss=nsss, Rsss=Rsss, flag=flag)
            self.th.start()
            # self.testList(Leafpath, Soilpath)
            '''
            simuls_4.simulss(Leafpath, Soilpath, Outpath, Bands, v_angle_min, v_angle_max, v_interval, s_angle_min,
                             s_angle_max, s_interval, LAI_min, LAI_max, LAI_interval, ss_min, ss_max, ss_interval,
                             vv_min, vv_max, vv_interval)
            '''
            # simuls_4.simulss('./leaf_test.txt', './soil_test.txt', './datas/')
        except Exception as e:
            print(e)


class MyThread(QThread):
    def __init__(self, leafpath, solidpath, filenames, bands, v_min, v_max, v_interval, s_min, s_max, s_interval,
                 LAI_min, LAI_max, LAI_interval, ss_min, ss_max, ss_interval, vv_min, vv_max, vv_interval, Ha, Hb,
                 nsss, Rsss, flag, parent=None):
        super().__init__(parent=parent)
        self.leafpath = leafpath
        self.solidpath = solidpath
        self.filenames = filenames
        self.bands = bands
        self.v_min = int(v_min)
        self.v_max = int(v_max)
        self.v_interval = int(v_interval)
        self.s_min = int(s_min)
        self.s_max = int(s_max)
        self.s_interval = int(s_interval)
        self.LAI_min = float(LAI_min)
        self.LAI_max = float(LAI_max)
        self.LAI_interval = float(LAI_interval)
        self.ss_min = int(ss_min)
        self.ss_max = int(ss_max)
        self.ss_interval = int(ss_interval)
        self.vv_min = int(vv_min)
        self.vv_max = int(vv_max)
        self.vv_interval = int(vv_interval)
        self.Ha = Ha
        self.Hb = Hb
        self.nsss = nsss
        self.Rsss = Rsss
        self.flag = flag

    def run(self):
        isExists = os.path.exists(self.filenames)
        if not isExists:
            os.mkdir(self.filenames)
        outputs = self.filenames
        flag = 0
        simuls_fun.simulss(self.leafpath, self.solidpath, outputs, self.bands, self.v_min, self.v_max,
                         self.v_interval, self.s_min, self.s_max, self.s_interval,
                         self.LAI_min, self.LAI_max, self.LAI_interval, self.ss_min, self.ss_max, self.ss_interval,
                         self.vv_min, self.vv_max, self.vv_interval, self.Ha, self.Hb, self.nsss, self.Rsss, flag)
        rebind.rebinds(outputs)
        print("Done!")
