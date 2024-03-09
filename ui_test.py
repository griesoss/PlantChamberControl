# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'controlcenterEUvTcL.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
#(QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt)
from PySide6.QtGui import * 
#(QAction, QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1755, 1204)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1711, 1017))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 5, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 1, 2, 1, 1)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 1, 4, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 1, 3, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 80))

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_2 = QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea_4 = QScrollArea(self.tab_3)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1711, 1137))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_6 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_15 = QFrame(self.frame_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_15)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_38 = QLabel(self.frame_17)
        self.label_38.setObjectName(u"label_38")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_38)

        self.lineEdit_42 = QLineEdit(self.frame_17)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setEnabled(False)
        self.lineEdit_42.setMinimumSize(QSize(200, 0))
        self.lineEdit_42.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_42.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.lineEdit_42)

        self.checkBox_5 = QCheckBox(self.frame_17)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setMinimumSize(QSize(75, 20))

        self.horizontalLayout_2.addWidget(self.checkBox_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_14.addWidget(self.frame_17)

        self.frame_11 = QFrame(self.frame_15)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_5 = QFrame(self.frame_11)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_5, 2, 1, 1, 1)

        self.lineEdit_43 = QLineEdit(self.frame_11)
        self.lineEdit_43.setObjectName(u"lineEdit_43")

        self.gridLayout_2.addWidget(self.lineEdit_43, 2, 6, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_11)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_2.addWidget(self.lineEdit_5, 2, 4, 1, 1)

        self.label_11 = QLabel(self.frame_11)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 2, 2, 1, 1)

        self.label_20 = QLabel(self.frame_11)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(180, 0))
        font1 = QFont()
        font1.setItalic(False)
        self.label_20.setFont(font1)

        self.gridLayout_2.addWidget(self.label_20, 2, 0, 1, 1)

        self.label_10 = QLabel(self.frame_11)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 5, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_11)

        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_16)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_6 = QLineEdit(self.frame_16)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_6.addWidget(self.lineEdit_6, 0, 3, 1, 1)

        self.label_15 = QLabel(self.frame_16)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_6.addWidget(self.label_15, 0, 4, 1, 1)

        self.line_2 = QFrame(self.frame_16)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_2, 0, 1, 1, 1)

        self.label_17 = QLabel(self.frame_16)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(180, 0))
        self.label_17.setFont(font1)

        self.gridLayout_6.addWidget(self.label_17, 0, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.frame_16)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_6.addWidget(self.lineEdit_7, 0, 5, 1, 1)

        self.label_14 = QLabel(self.frame_16)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 0, 2, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_16)

        self.frame_13 = QFrame(self.frame_15)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_13)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineEdit_9 = QLineEdit(self.frame_13)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_5.addWidget(self.lineEdit_9, 1, 4, 1, 1)

        self.label_13 = QLabel(self.frame_13)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(180, 0))

        self.gridLayout_5.addWidget(self.label_13, 1, 0, 1, 1)

        self.line_3 = QFrame(self.frame_13)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_3, 1, 2, 1, 1)

        self.label_18 = QLabel(self.frame_13)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_5.addWidget(self.label_18, 1, 3, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.frame_15)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_12)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_19 = QLabel(self.frame_12)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_4.addWidget(self.label_19, 0, 2, 1, 1)

        self.line_4 = QFrame(self.frame_12)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_4, 0, 1, 1, 1)

        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(180, 0))

        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(self.frame_12)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_4.addWidget(self.lineEdit_10, 0, 3, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_12)

        self.line_6 = QFrame(self.frame_15)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_6)


        self.verticalLayout_13.addWidget(self.frame_15)


        self.verticalLayout_8.addWidget(self.frame_6)

        self.pushButton_5 = QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_8.addWidget(self.pushButton_5)

        self.line = QFrame(self.scrollAreaWidgetContents_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_8)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.graphicsView = QGraphicsView(self.frame_7)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_10.addWidget(self.graphicsView)

        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_7)


        self.gridLayout_3.addWidget(self.frame_7, 0, 0, 1, 1)

        self.frame = QFrame(self.frame_8)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.graphicsView_2 = QGraphicsView(self.frame)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.verticalLayout_9.addWidget(self.graphicsView_2)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_6)


        self.gridLayout_3.addWidget(self.frame, 0, 1, 1, 1)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.graphicsView_3 = QGraphicsView(self.frame_9)
        self.graphicsView_3.setObjectName(u"graphicsView_3")

        self.verticalLayout_11.addWidget(self.graphicsView_3)

        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_8)


        self.gridLayout_3.addWidget(self.frame_9, 1, 0, 1, 1)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.graphicsView_4 = QGraphicsView(self.frame_10)
        self.graphicsView_4.setObjectName(u"graphicsView_4")

        self.verticalLayout_12.addWidget(self.graphicsView_4)

        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_9)


        self.gridLayout_3.addWidget(self.frame_10, 1, 1, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_8)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_2.addWidget(self.scrollArea_4)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_5 = QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea_2 = QScrollArea(self.tab_4)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1711, 1137))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_5 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.pushButton_13 = QPushButton(self.frame_3)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout_11.addWidget(self.pushButton_13, 1, 5, 1, 1)

        self.label_32 = QLabel(self.frame_3)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_11.addWidget(self.label_32, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_11.addWidget(self.pushButton_3, 1, 12, 1, 1)

        self.lineEdit_32 = QLineEdit(self.frame_3)
        self.lineEdit_32.setObjectName(u"lineEdit_32")

        self.gridLayout_11.addWidget(self.lineEdit_32, 1, 8, 1, 1)

        self.frame_14 = QFrame(self.frame_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.gridLayout_11.addWidget(self.frame_14, 1, 7, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer, 1, 13, 1, 1)

        self.pushButton_14 = QPushButton(self.frame_3)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout_11.addWidget(self.pushButton_14, 1, 6, 1, 1)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_11.addWidget(self.label_5, 0, 2, 1, 1)

        self.lineEdit_33 = QLineEdit(self.frame_3)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setEnabled(False)
        self.lineEdit_33.setClearButtonEnabled(False)

        self.gridLayout_11.addWidget(self.lineEdit_33, 1, 0, 1, 1)

        self.frame_39 = QFrame(self.frame_3)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)

        self.gridLayout_11.addWidget(self.frame_39, 1, 9, 1, 1)

        self.label_33 = QLabel(self.frame_3)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_11.addWidget(self.label_33, 0, 8, 1, 1)

        self.frame_30 = QFrame(self.frame_3)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)

        self.gridLayout_11.addWidget(self.frame_30, 1, 4, 1, 1)

        self.horizontalSlider = QSlider(self.frame_3)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(True)
        self.horizontalSlider.setTickPosition(QSlider.NoTicks)

        self.gridLayout_11.addWidget(self.horizontalSlider, 1, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.tab_4, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ControlCenter", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PWM-Value", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pin Number", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"LED Name", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0-13", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"delete", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0x40 - 0x5F", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Temperature Sensor Adress", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add LED", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"SETUP", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Setup", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"LED Name", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u" Activate", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Duration", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Dimmer-Value", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Spectrometer Values", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Hyperspectral Camera Values", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Camera Values", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Start Measurement", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Temperature Plot", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Spectrometer Plot", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Hyperspectral Picture", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Camera Picture", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Measurement", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"LED Name", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Dimmer", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Duration", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Simple Control", None))
    # retranslateUi

