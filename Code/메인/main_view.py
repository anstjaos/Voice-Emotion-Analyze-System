# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog

class MainView(object):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 598)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)

        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)

        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)

        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)

        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)

        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)

        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)

        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)

        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)

        MainWindow.setPalette(palette)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loadFileBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loadFileBtn.setGeometry(QtCore.QRect(82, 520, 131, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.loadFileBtn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        ### 파일 불러오기
        self.loadFileBtn.setFont(font)
        self.loadFileBtn.setStyleSheet("background-color:rgb(52, 152, 219);\n"
"font: 75 10pt \"맑은 고딕\";")
        self.loadFileBtn.setObjectName("loadFileBtn")
        #self.loadFileBtn.clicked.connect(self.controller.loadFile)
        ### 스피커
        self.speakerLabel = QtWidgets.QLabel(self.centralwidget)
        self.speakerLabel.setGeometry(QtCore.QRect(100, 100, 91, 111))
        self.speakerLabel.setText("")
        self.speakerLabel.setPixmap(QtGui.QPixmap("D://asdf/imgsrc/music64.png"))
        self.speakerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.speakerLabel.setObjectName("speakerLabel")
        ### 녹음
        self.recordLabel = QtWidgets.QLabel(self.centralwidget)
        self.recordLabel.setGeometry(QtCore.QRect(120, 290, 51, 91))
        self.recordLabel.setText("")
        self.recordLabel.setPixmap(QtGui.QPixmap("D://asdf/imgsrc/sound64.png"))
        self.recordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.recordLabel.setObjectName("recordLabel")
        ### 재생 버튼
        self.playBtn = QtWidgets.QPushButton(self.centralwidget)
        self.playBtn.setGeometry(QtCore.QRect(210, 130, 51, 51))
        self.playBtn.setAutoFillBackground(False)
        #self.playBtn.setStyleSheet("Image-background:url(:/newPrefix/player64.png);")
        self.playBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D://asdf/imgsrc/player64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playBtn.setIcon(icon)
        self.playBtn.setIconSize(QtCore.QSize(40, 40))
        self.playBtn.setObjectName("playBtn")
        ### 정지 버튼
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setGeometry(QtCore.QRect(280, 130, 51, 51))
        #self.stopBtn.setStyleSheet("Image-background:url(:/newPrefix/pause64.png)")
        self.stopBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D://asdf/imgsrc/pause64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopBtn.setIcon(icon1)
        self.stopBtn.setIconSize(QtCore.QSize(40, 40))
        self.stopBtn.setObjectName("stopBtn")
        ### 녹음 버튼
        self.recordBtn = QtWidgets.QPushButton(self.centralwidget)
        self.recordBtn.setGeometry(QtCore.QRect(304, 520, 131, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.recordBtn.setPalette(palette)
        self.recordBtn.setStyleSheet("background-color:rgb(52, 152, 219);\n"
"font: 75 10pt \"맑은 고딕\";")
        self.recordBtn.setObjectName("recordBtn")
        ### 감정 분석 버튼
        self.emotionAnalyzeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.emotionAnalyzeBtn.setGeometry(QtCore.QRect(527, 520, 131, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 152, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.emotionAnalyzeBtn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.emotionAnalyzeBtn.setFont(font)
        self.emotionAnalyzeBtn.setStyleSheet("background-color:rgb(52, 152, 219);\n"
"font: 75 10pt \"맑은 고딕\";")
        self.emotionAnalyzeBtn.setObjectName("emotionAnalyzeBtn")
        ### 사운드 프로그래스 바
        self.soundPgBar = QtWidgets.QProgressBar(self.centralwidget)
        self.soundPgBar.setGeometry(QtCore.QRect(350, 140, 311, 41))
        self.soundPgBar.setProperty("value", 0)
        self.soundPgBar.setObjectName("soundPgBar")
        ### 볼륨 조절 슬라이더
        self.volumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.volumeSlider.setGeometry(QtCore.QRect(680, 100, 16, 101))
        self.volumeSlider.setOrientation(QtCore.Qt.Vertical)
        self.volumeSlider.setObjectName("volumeSlider")
        self.volumeSlider.setValue(100)
        self.recordTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.recordTimeLabel.setGeometry(QtCore.QRect(210, 310, 401, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.recordTimeLabel.setFont(font)
        self.recordTimeLabel.setObjectName("recordLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadFileBtn.setText(_translate("MainWindow", "파일 불러오기"))
        self.recordBtn.setText(_translate("MainWindow", "음성 녹음"))
        self.emotionAnalyzeBtn.setText(_translate("MainWindow", "감정 분석"))
        self.recordTimeLabel.setText(_translate("MainWindow", "Current Time"))

    def updateSoundPgrBar(self, value):
        self.soundPgBar.setValue(value)

    def updateRecordBtnText(self, txt):
        self.recordBtn.setText(txt)

    def updateRecordTimeLabelText(self, txt):
        self.recordTimeLabel.setText(txt)

    def showMessage(self, txt):
        root = Tk()
        root.withdraw()
        messagebox.showinfo("알림", txt)
        root.destroy()

    def loadFile(self):
        root = Tk()
        root.filename = filedialog.askopenfilename(initialdir="D:\\asdf", title="choose your file",
                                                   filetypes=[("mp3 files", "*.mp3"), ("wav files", "*.wav"),
                                                              ("all files", "*.*")])

        fn = root.filename.split('/')
        fn.reverse()

        parentDir = ""
        fileName = fn[0]
        for i in range(len(fn) - 1, 0, -1):
            parentDir += fn[i]
            if i != 1:
                parentDir += "/"

        root.destroy()
        return parentDir, fileName

