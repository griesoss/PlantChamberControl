# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'controlcenterKRZIXV.ui'
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

#from LED import *
from ArduinoCommunication import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, led_list, arduino_communication):   
        self.ArduinoCommunication = arduino_communication
               
            
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1365, 899)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1321, 712))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        # Create the frames for the Setup Tab  
        self.SetupFrameDict = dict()
        self.LEDList = led_list
        #build a matrix of x
        for x in range(0, 10):
                self.create_new_led_frame_setup(MainWindow, led_list[x])
        
        self.verticalLayout_6.addWidget(self.frame_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        # Add LED Button
        self.pushButton_add_LED = QPushButton(self.tab)
        self.pushButton_add_LED.setObjectName(u"pushButton_add_LED")        
        self.pushButton_add_LED.clicked.connect(lambda: self.create_new_led_frame_setup(MainWindow,-1))
        self.pushButton_add_LED.clicked.connect(lambda: self.retranslateUi(MainWindow))
        self.verticalLayout_3.addWidget(self.pushButton_add_LED)

        # Setup Button
        self.pushButton_setup = QPushButton(self.tab)
        self.pushButton_setup.setObjectName(u"pushButton_setup")
        self.pushButton_setup.setMinimumSize(QSize(0, 80))
        self.pushButton_setup.clicked.connect(lambda: self.updateLEDList(MainWindow))
        self.pushButton_setup.clicked.connect(lambda: self.ArduinoCommunication.setup_LEDs(self.LEDList))
        self.verticalLayout_3.addWidget(self.pushButton_setup)

        self.tabWidget.addTab(self.tab, "")
        
        # Tab 2 ############################################################################################################	
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        
        # Tab 3 ############################################################################################################
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
        
        self.createMeasurementFrames() # Create the frames for the Measurement Tab
        
        
        #########

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
        
        # Tab 4 ############################################################################################################
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_5 = QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea_2 = QScrollArea(self.tab_4)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1323, 842))
        
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_5 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        
        # Create the frames for the Simple Control Tab        
        self.createSimpleControlFrames()
        
        self.verticalLayout_7.addWidget(self.frame_5)
    
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.tab_4, "")
        
        ######################################################################################################################

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
        
        # Load the LED List after Setup to the Arduino
        self.ArduinoCommunication.setup_LEDs(self.LEDList)
    # setupUi 
    
    def createMeasurementFrames(self):
        """
        Create the frames for the Measurement Tab.
        """
        
        # Delete all previous LED frames in Measurement
        for i in reversed(range(self.frame_6.layout().count())): 
            self.frame_6.layout().itemAt(i).widget().setParent(None)
        
        # Iterate over the List of LEDS provided by the Setup and create the new frames for the LEDs
        self.MeasurementFrameList = []
        index = 0
        for i in range(0, len(self.LEDList)):
            self.create_new_led_frame_measurement(index)
            index = index + 1
    
    def createSimpleControlFrames(self):
        """
        Create in Simple Control a frame for the all LEDs.
        """
        
        # Delete all previous LED frames in Simple Control
        for i in reversed(range(self.frame_5.layout().count())): 
            self.frame_5.layout().itemAt(i).widget().setParent(None)            
        
        # Iterate over the List of LEDS provided by the Setup and create the new frames for the LEDs
        self.SimpleControlFrameList = []
        index = 0
        for led in self.LEDList:
            self.create_new_led_frame_simple_control(index)
            index = index + 1
    
    def retranslateUi(self, MainWindow):
        """
        Set the text of the widgets to the translated text.
        :param MainWindow: The main window of the application
        """
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ControlCenter", None))        
        
        index = 1
        #Iterate over self.SetupFrameDict
        for key in self.SetupFrameDict:
            self.SetupFrameDict[key].label_led_name.setText(QCoreApplication.translate("MainWindow", u"LED Name " + str(index), None))
            self.SetupFrameDict[key].label_pin_number.setText(QCoreApplication.translate("MainWindow", u"Pin Number ", None))
            self.SetupFrameDict[key].label_mA_value.setText(QCoreApplication.translate("MainWindow", u"Forward Current (mA) ", None))
            self.SetupFrameDict[key].pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None)) 
            self.SetupFrameDict[key].lineEdit_pin_number.setPlaceholderText("2-13, 44-46")
            self.SetupFrameDict[key].lineEdit_mA_value.setPlaceholderText("0-250mA")
            self.SetupFrameDict[key].label_temperature_adress.setText(QCoreApplication.translate("MainWindow", u"Temperature Sensor Adress", None))
            self.SetupFrameDict[key].lineEdit_temperature_adress.setPlaceholderText("0x40-0x5F")
            index = index + 1
        
        # Iterate over self.SimpleControlFrameList
        for index in range(0, len(self.SimpleControlFrameList)):
            self.SimpleControlFrameList[index].label_led_name.setText(QCoreApplication.translate("MainWindow", u"LED Name " + str(index + 1), None))
            self.SimpleControlFrameList[index].label_duration.setText(QCoreApplication.translate("MainWindow", u"Duration (s)", None))
            self.SimpleControlFrameList[index].pushButton_ON.setText(QCoreApplication.translate("MainWindow", u"ON", None))
            self.SimpleControlFrameList[index].pushButton_activate.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
            self.SimpleControlFrameList[index].pushButton_OFF.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        
        self.pushButton_add_LED.setText(QCoreApplication.translate("MainWindow", u"Add LED", None))
        self.pushButton_setup.setText(QCoreApplication.translate("MainWindow", u"SETUP", None))        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Setup", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Measurement", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Simple Control", None))
        
        # Iterate over self.MeasurementFrameList
        for index in range(0, len(self.MeasurementFrameList)):
            self.MeasurementFrameList[index].label_led_name.setText(QCoreApplication.translate("MainWindow", u"LED Name " + str(index + 1), None))
            self.MeasurementFrameList[index].checkBox_calibrate.setText(QCoreApplication.translate("MainWindow", u" Calibration", None))
            self.MeasurementFrameList[index].checkBox_measurement.setText(QCoreApplication.translate("MainWindow", u" Measurement", None))
            self.MeasurementFrameList[index].label_duration.setText(QCoreApplication.translate("MainWindow", u"Duration", None))
            self.MeasurementFrameList[index].label_led_vals.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
            self.MeasurementFrameList[index].label_dimmer_val.setText(QCoreApplication.translate("MainWindow", u"Dimmer-Value", None))
            self.MeasurementFrameList[index].label_placeholder2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
            self.MeasurementFrameList[index].label_spectrometer_vals.setText(QCoreApplication.translate("MainWindow", u"Spectrometer Values", None))
            self.MeasurementFrameList[index].label_placeholder1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
            self.MeasurementFrameList[index].label_hypercam_vals.setText(QCoreApplication.translate("MainWindow", u"Hyperspectral Camera Values", None))
            self.MeasurementFrameList[index].label_placeholder3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
            self.MeasurementFrameList[index].label_placeholder4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
            self.MeasurementFrameList[index].label_cam_vals.setText(QCoreApplication.translate("MainWindow", u"Camera Values", None))
                   
        
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Start Measurement", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Temperature Plot", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Spectrometer Plot", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Hyperspectral Picture", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Camera Picture", None))
    
    
    def updateLEDList(self, MainWindow):
        """
        Update the LEDList and the Simple Control Tab with the new values from the Setup Tab.
        :param MainWindow: The main window of the application
        """
        # Turn off all LEDs
        self.ArduinoCommunication.turn_off_all_LEDs(self.LEDList)
        #time.sleep(5)
        # Iterate over self.SetupFrameDict and create a new LED object for each entry and update the LEDList
        self.LEDList = []
        for key in self.SetupFrameDict:            
            # Create a new LED object for each entry in the dictionary if the str of one of these values is "" do not create an LED object
            if self.SetupFrameDict[key].lineEdit_led_name.text() != "" and self.SetupFrameDict[key].lineEdit_pin_number.text() != "" and self.SetupFrameDict[key].lineEdit_mA_value.text() != "":
                self.LEDList.append(LED(self.SetupFrameDict[key].lineEdit_led_name.text(), False, int(self.SetupFrameDict[key].lineEdit_pin_number.text()), int(self.SetupFrameDict[key].lineEdit_mA_value.text()), int(self.SetupFrameDict[key].lineEdit_temperature_adress.text()[2:],16)))
        self.createSimpleControlFrames()
        self.retranslateUi(MainWindow)
    # updateLEDList

    def create_new_led_frame_setup(self, MainWindow,led_list):    
        """
        Create a new frame for the Setup Tab.
        :param led_list: The LEDList
        """     
        
        # Create all non interactive widgets for the frame
        self.frame_setup = QFrame(self.frame_4) 
        self.frame_setup.setObjectName(u"frame_setup")
        self.frame_setup.setFrameShape(QFrame.StyledPanel)
        self.frame_setup.setFrameShadow(QFrame.Raised)
        
        self.gridLayout = QGridLayout(self.frame_setup)
        self.gridLayout.setObjectName(u"gridLayout")
        
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 4, 1, 1)
        
        # Create the interactive widgets for the frame
        self.label_led_name = QLabel(self.frame_setup)
        self.lineEdit_led_name = QLineEdit(self.frame_setup)
        self.label_pin_number = QLabel(self.frame_setup)
        self.lineEdit_pin_number = QLineEdit(self.frame_setup)
        self.label_mA_value = QLabel(self.frame_setup)
        self.lineEdit_mA_value = QLineEdit(self.frame_setup)
        self.pushButton_delete = QPushButton(self.frame_setup)
        self.lineEdit_temperature_adress = QLineEdit(self.frame_setup)
        self.label_temperature_adress = QLabel(self.frame_setup)
        
        # Get the key of the last inserted element in the dictionary if the dictionary is empty return 0
        if len(self.SetupFrameDict) == 0:
            current_index = 1
        else:
            current_index = list(self.SetupFrameDict.keys())[-1] + 1
        
        # Create a new SetupFrame object and append it to the SetupFrameDict
        self.SetupFrameDict[current_index] = SetupFrame(self.frame_setup, self.label_led_name, self.lineEdit_led_name, self.label_pin_number, self.lineEdit_pin_number, self.label_mA_value, self.lineEdit_mA_value, self.pushButton_delete, self.lineEdit_temperature_adress, self.label_temperature_adress)
        
        # Set the object name of the widgets        
        self.SetupFrameDict[current_index].label_led_name.setObjectName(u"label_led_name")
        self.SetupFrameDict[current_index].lineEdit_led_name.setObjectName(u"lineEdit_led_name")
        self.SetupFrameDict[current_index].label_pin_number.setObjectName(u"label_pin_number")
        self.SetupFrameDict[current_index].lineEdit_pin_number.setObjectName(u"lineEdit_pin_number")
        self.SetupFrameDict[current_index].label_mA_value.setObjectName(u"label_mA_value")
        self.SetupFrameDict[current_index].lineEdit_mA_value.setObjectName(u"lineEdit_mA_value")
        self.SetupFrameDict[current_index].pushButton_delete.setObjectName(u"deleteButton") 
        self.SetupFrameDict[current_index].lineEdit_temperature_adress.setObjectName(u"lineEdit_temperature_adress")
        self.SetupFrameDict[current_index].label_temperature_adress.setObjectName(u"label_temperature_adress")        
        
        # Set the text of the widgets to the values of the existing LED in LEDList
        if led_list != -1:
            self.SetupFrameDict[current_index].lineEdit_led_name.setText(led_list.name)
            self.SetupFrameDict[current_index].lineEdit_pin_number.setText(str(led_list.pin_num))
            self.SetupFrameDict[current_index].lineEdit_mA_value.setText(str(led_list.mA_val))
            self.SetupFrameDict[current_index].lineEdit_temperature_adress.setText(str(hex(led_list.temp_addr)))        
        
        # Manage the input validation for the line edits
        pin_validator = QRegularExpressionValidator(QRegularExpression("(?:[0-9]|1[0-3]|4[4-6])")) 
        self.SetupFrameDict[current_index].lineEdit_pin_number.setValidator(pin_validator)
        mA_validator = QRegularExpressionValidator(QRegularExpression("(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0])"))
        self.SetupFrameDict[current_index].lineEdit_mA_value.setValidator(mA_validator)    
        temp_addr_validator = QRegularExpressionValidator(QRegularExpression("0[xX][4-5][0-9a-fA-F]|0[xX]40|0[xX]5[0-9a-fA-F]"))
        self.SetupFrameDict[current_index].lineEdit_temperature_adress.setValidator(temp_addr_validator)    
               
        
        # Define the actions for the delete button 
        self.SetupFrameDict[current_index].pushButton_delete.clicked.connect(lambda: self.SetupFrameDict[current_index].frame_setup.deleteLater()) #delete the frame
        self.SetupFrameDict[current_index].pushButton_delete.clicked.connect(lambda: self.SetupFrameDict.pop(current_index)) #delete the entry for the frame in the dictionary
        self.SetupFrameDict[current_index].pushButton_delete.clicked.connect(lambda: self.retranslateUi(MainWindow)) #retranslate the UI
        
        # Add the widgets to the grid layout of the frame
        self.gridLayout.addWidget(self.SetupFrameDict[current_index].label_led_name, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.SetupFrameDict[current_index].lineEdit_led_name, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.SetupFrameDict[current_index].label_pin_number, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.SetupFrameDict[current_index].lineEdit_pin_number, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.SetupFrameDict[current_index].label_mA_value, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.SetupFrameDict[current_index].lineEdit_mA_value, 1, 2, 1, 1)    
        self.gridLayout.addWidget(self.SetupFrameDict[current_index].pushButton_delete, 1, 4, 1, 1)
        self.gridLayout.addWidget(self.SetupFrameDict[current_index].label_temperature_adress, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.SetupFrameDict[current_index].lineEdit_temperature_adress, 1, 3, 1, 1)

        self.verticalLayout.addWidget(self.frame_setup)
    
    def create_new_led_frame_simple_control(self, index):     
        """
        Create a new frame for the Simple Control Tab.
        :param index: Index of the LED in the LEDList
        """  
        # Create all non interactive widgets for the frame
        self.frame_simple_control = QFrame(self.frame_5)
        self.frame_simple_control.setObjectName(u"frame_simple_control")
        self.frame_simple_control.setFrameShape(QFrame.StyledPanel)
        self.frame_simple_control.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_simple_control)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
               
        self.frame_14 = QFrame(self.frame_simple_control)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_11.addWidget(self.frame_14, 1, 5, 1, 1)
        
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_11.addItem(self.horizontalSpacer, 1, 11, 1, 1)
        
        self.frame_30 = QFrame(self.frame_simple_control)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.gridLayout_11.addWidget(self.frame_30, 1, 2, 1, 1)

        self.frame_39 = QFrame(self.frame_simple_control)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.gridLayout_11.addWidget(self.frame_39, 1, 7, 1, 1)
        
        # Create the interactive widgets for the frame
        self.label_duration = QLabel(self.frame_simple_control)
        self.lineEdit_duration = QLineEdit(self.frame_simple_control)
        self.pushButton_ON = QPushButton(self.frame_simple_control)
        self.pushButton_activate = QPushButton(self.frame_simple_control)
        self.pushButton_OFF = QPushButton(self.frame_simple_control)
        self.label_led_name = QLabel(self.frame_simple_control)        
        self.lineEdit_led_name = QLineEdit(self.frame_simple_control)
        self.lineEdit_led_name.setEnabled(False)
        self.lineEdit_led_name.setClearButtonEnabled(False)
        self.horizontalSlider = QSlider(self.frame_simple_control)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        
        
        # Create a new SimpleControlFrame object and append it to the SimpleControlFrameList
        self.SimpleControlFrameList.append(SimpleControlFrame(self.frame_simple_control, self.label_led_name, self.lineEdit_led_name, self.label_duration, self.lineEdit_duration, self.pushButton_ON, self.pushButton_OFF, self.pushButton_activate, self.horizontalSlider))

        # Set the object name of the widgets
        self.SimpleControlFrameList[index].label_led_name.setObjectName(u"label_led_name")
        self.SimpleControlFrameList[index].lineEdit_led_name.setObjectName(u"lineEdit_led_name")
        self.SimpleControlFrameList[index].label_duration.setObjectName(u"label_duration")
        self.SimpleControlFrameList[index].lineEdit_duration.setObjectName(u"lineEdit_duration")
        self.SimpleControlFrameList[index].pushButton_ON.setObjectName(u"pushButton_ON")
        self.SimpleControlFrameList[index].pushButton_activate.setObjectName(u"pushButton_activate")
        self.SimpleControlFrameList[index].pushButton_OFF.setObjectName(u"pushButton_OFF")
        self.SimpleControlFrameList[index].horizontalSlider.setObjectName(u"horizontalSlider")
        
        # Set the maximum value of the slider to the mA value of the LED and the minimum value to 0
        self.SimpleControlFrameList[index].horizontalSlider.setMinimum(0)
        self.SimpleControlFrameList[index].horizontalSlider.setMaximum(self.LEDList[index].mA_val)
        self.SimpleControlFrameList[index].horizontalSlider.setValue(self.SimpleControlFrameList[index].horizontalSlider.maximum())
        
        # Set the name of the LED
        self.SimpleControlFrameList[index].lineEdit_led_name.setText(self.LEDList[index].name)    
        
        # Define the actions for the On, Off and Activate Button
        self.SimpleControlFrameList[index].pushButton_ON.clicked.connect(lambda: self.ArduinoCommunication.update_LED(self.LEDList[index].pin_num, convert_mA_into_pwm_val(self.SimpleControlFrameList[index].horizontalSlider.value())))
        self.SimpleControlFrameList[index].pushButton_ON.clicked.connect(lambda: self.LEDList[index].set_status(True))
        self.SimpleControlFrameList[index].pushButton_ON.clicked.connect(lambda: self.SimpleControlFrameList[index].label_led_name.setText(QCoreApplication.translate("MainWindow", u"LED Name " + str(index + 1) + " 💡", None)))
        self.SimpleControlFrameList[index].pushButton_OFF.clicked.connect(lambda: self.ArduinoCommunication.turn_off_LED(self.LEDList[index].pin_num))
        self.SimpleControlFrameList[index].pushButton_OFF.clicked.connect(lambda: self.LEDList[index].set_status(False))
        self.SimpleControlFrameList[index].pushButton_OFF.clicked.connect(lambda: self.SimpleControlFrameList[index].label_led_name.setText(QCoreApplication.translate("MainWindow", u"LED Name " + str(index + 1), None)))
        self.SimpleControlFrameList[index].pushButton_activate.clicked.connect(lambda: self.activate_func(index))
        self.SimpleControlFrameList[index].horizontalSlider.valueChanged.connect(lambda: self.slider_func(index))
        # Add the widgets to the grid layout of the frame
        self.gridLayout_11.addWidget(self.SimpleControlFrameList[index].lineEdit_led_name, 1, 0, 1, 1)
        self.gridLayout_11.addWidget(self.SimpleControlFrameList[index].label_duration, 0, 6, 1, 1)
        self.gridLayout_11.addWidget(self.SimpleControlFrameList[index].lineEdit_duration, 1, 6, 1, 1)
        self.gridLayout_11.addWidget(self.SimpleControlFrameList[index].pushButton_ON, 1, 3, 1, 1)
        self.gridLayout_11.addWidget(self.SimpleControlFrameList[index].pushButton_activate, 1, 10, 1, 1)
        self.gridLayout_11.addWidget(self.SimpleControlFrameList[index].pushButton_OFF, 1, 2, 1, 1)
        self.gridLayout_11.addWidget(self.SimpleControlFrameList[index].label_led_name, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.SimpleControlFrameList[index].horizontalSlider, 1, 1, 1, 1)
        
        # Add the frame to the vertical layout 
        self.verticalLayout_4.addWidget(self.frame_simple_control)
        
    def slider_func(self, index):
        """
        Set the PWM value of the LED to the value of the slider.
        If the LED is turned on changes will be visible immediately on the LED.
        If the Led is turned off changes will be visible after turning the LED on.
        :param index: Index of the LED in the LEDList
        """
        if self.LEDList[index].is_on == True:
            self.ArduinoCommunication.update_LED(self.LEDList[index].pin_num, convert_mA_into_pwm_val(self.SimpleControlFrameList[index].horizontalSlider.value()))  
            
            # if the slider value is 0 set the label of the LED to the original name
            if self.SimpleControlFrameList[index].horizontalSlider.value() == 0:
                self.SimpleControlFrameList[index].label_led_name.setText(QCoreApplication.translate("MainWindow", u"LED Name " + str(index + 1), None))
            # if the slider value is not 0 set the label of the LED to the original name and add a lightbulb emoji
            else:
                self.SimpleControlFrameList[index].label_led_name.setText(QCoreApplication.translate("MainWindow", u"LED Name " + str(index + 1) + " 💡", None))
        else:
                  
            self.SimpleControlFrameList[index].label_led_name.setText(QCoreApplication.translate("MainWindow", u"LED Name " + str(index + 1), None))
        
    def activate_func(self, index):
        """
		Activate the LED with the given pin number, PWM value for a given duration.
		:param pin_num: Pin number of the LED
		:param pwm_val: PWM value of the LED
		:param duration: Duration of the LED
		"""
		# Turn on the LED
        self.SimpleControlFrameList[index].pushButton_ON.clicked.emit()
		# Wait for the duration
        duration = int(self.SimpleControlFrameList[index].lineEdit_duration.text())
		# Turn off after duration the LED        
        QTimer.singleShot(duration*1000, lambda: self.SimpleControlFrameList[index].pushButton_OFF.clicked.emit())
        
    def create_new_led_frame_measurement(self, index):     
        """
        Create a new frame for the Measurement Tab.
        """  
        self.frame_measurement = QFrame(self.frame_6)
        
        self.frame_measurement.setObjectName(u"frame_measurement")
        self.frame_measurement.setFrameShape(QFrame.StyledPanel)
        self.frame_measurement.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_measurement)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        
        # Frame for the general settings
        self.frame_general = QFrame(self.frame_measurement)
        self.frame_general.setObjectName(u"frame_17")
        self.frame_general.setFrameShape(QFrame.StyledPanel)
        self.frame_general.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_general)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_led_name = QLabel(self.frame_general)
        self.label_led_name.setObjectName(u"label_led_name")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        #font.setWeight(75)
        self.label_led_name.setFont(font)

        

        self.lineEdit_led_name = QLineEdit(self.frame_general)
        self.lineEdit_led_name.setObjectName(u"lineEdit_42")
        self.lineEdit_led_name.setEnabled(False)
        self.lineEdit_led_name.setMinimumSize(QSize(200, 0))
        self.lineEdit_led_name.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_led_name.setClearButtonEnabled(False)

        self.checkBox_calibrate = QCheckBox(self.frame_general)
        self.checkBox_calibrate.setObjectName(u"checkBox_calibrate")
        self.checkBox_calibrate.setMinimumSize(QSize(75, 20))  
        
        self.checkBox_measurement = QCheckBox(self.frame_general)
        self.checkBox_measurement.setObjectName(u"checkBox_measurement")
        self.checkBox_measurement.setMinimumSize(QSize(75, 20))   
        
        self.verticalLayout_14.addWidget(self.frame_general)

        # Frame for the LED values	
        self.frame_led_val = QFrame(self.frame_measurement)
        self.frame_led_val.setObjectName(u"frame_led_val")
        self.frame_led_val.setFrameShape(QFrame.StyledPanel)
        self.frame_led_val.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_led_val)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_5 = QFrame(self.frame_led_val)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_5, 2, 1, 1, 1)

        self.lineEdit_dimmer_val = QLineEdit(self.frame_led_val)
        self.lineEdit_dimmer_val.setObjectName(u"lineEdit_dimmer_val")

    
        self.lineEdit_duration = QLineEdit(self.frame_led_val)
        self.lineEdit_duration.setObjectName(u"lineEdit_duration")

        self.label_duration = QLabel(self.frame_led_val)
        self.label_duration.setObjectName(u"label_duration")

        self.label_led_vals = QLabel(self.frame_led_val)
        self.label_led_vals.setObjectName(u"label_led_vals")
        self.label_led_vals.setMinimumSize(QSize(180, 0))
        font1 = QFont()
        font1.setItalic(False)
        self.label_led_vals.setFont(font1)

        self.label_dimmer_val = QLabel(self.frame_led_val)
        self.label_dimmer_val.setObjectName(u"label_dimmer_val")

        

        self.verticalLayout_14.addWidget(self.frame_led_val)

        # Frame for the Spectrometer values
        self.frame_spectrometer_val = QFrame(self.frame_measurement)
        self.frame_spectrometer_val.setObjectName(u"frame_spectrometer_val")
        self.frame_spectrometer_val.setFrameShape(QFrame.StyledPanel)
        self.frame_spectrometer_val.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_spectrometer_val)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_placeholder1 = QLineEdit(self.frame_spectrometer_val)
        self.lineEdit_placeholder1.setObjectName(u"lineEdit_placeholder1")

        

        self.label_placeholder2 = QLabel(self.frame_spectrometer_val)
        self.label_placeholder2.setObjectName(u"label_placeholder2")

        

        self.line_2 = QFrame(self.frame_spectrometer_val)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_2, 0, 1, 1, 1)

        self.label_spectrometer_vals = QLabel(self.frame_spectrometer_val)
        self.label_spectrometer_vals.setObjectName(u"label_spectrometer_vals")
        self.label_spectrometer_vals.setMinimumSize(QSize(180, 0))
        self.label_spectrometer_vals.setFont(font1)

        self.lineEdit_placeholder2 = QLineEdit(self.frame_spectrometer_val)
        self.lineEdit_placeholder2.setObjectName(u"lineEdit_placeholder2")

        self.label_placeholder1 = QLabel(self.frame_spectrometer_val)
        self.label_placeholder1.setObjectName(u"label_placeholder1")

        
        

        self.verticalLayout_14.addWidget(self.frame_spectrometer_val)

        # Frame for the Hyperspectral Camera values
        self.frame_hypercam_val = QFrame(self.frame_measurement)
        self.frame_hypercam_val.setObjectName(u"frame_hypercam_val")
        self.frame_hypercam_val.setFrameShape(QFrame.StyledPanel)
        self.frame_hypercam_val.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_hypercam_val)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        
        self.lineEdit_placeholder3 = QLineEdit(self.frame_hypercam_val)
        self.lineEdit_placeholder3.setObjectName(u"lineEdit_placeholder3")

        self.label_hypercam_vals = QLabel(self.frame_hypercam_val)
        self.label_hypercam_vals.setObjectName(u"label_hypercam_vals")
        self.label_hypercam_vals.setMinimumSize(QSize(180, 0))

        

        self.line_3 = QFrame(self.frame_hypercam_val)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_3, 1, 2, 1, 1)

        self.label_placeholder3 = QLabel(self.frame_hypercam_val)
        self.label_placeholder3.setObjectName(u"label_placeholder3")


        


        self.verticalLayout_14.addWidget(self.frame_hypercam_val)

        
        # Frame for the Camera values
        self.frame_cam_val = QFrame(self.frame_measurement)
        self.frame_cam_val.setObjectName(u"frame_cam_val")
        self.frame_cam_val.setFrameShape(QFrame.StyledPanel)
        self.frame_cam_val.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_cam_val)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_placeholder4 = QLabel(self.frame_cam_val)
        self.label_placeholder4.setObjectName(u"label_placeholder4")

        self.line_4 = QFrame(self.frame_cam_val)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_4, 0, 1, 1, 1)

        self.label_cam_vals = QLabel(self.frame_cam_val)
        self.label_cam_vals.setObjectName(u"label_cam_vals")
        self.label_cam_vals.setMinimumSize(QSize(180, 0))

        self.lineEdit_placeholder4 = QLineEdit(self.frame_cam_val)
        self.lineEdit_placeholder4.setObjectName(u"lineEdit_placeholder4")
      
        self.verticalLayout_14.addWidget(self.frame_cam_val)

        self.line_6 = QFrame(self.frame_measurement)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_6)
        
         # Create a new SimpleControlFrame object and append it to the MeasurementFrameList
        self.MeasurementFrameList.append(MeasurementFrame(self.label_led_name, self.lineEdit_led_name, self.checkBox_calibrate, self.checkBox_measurement, self.label_led_vals, self.lineEdit_dimmer_val, self.label_dimmer_val, self.label_duration, self.lineEdit_duration, self.label_spectrometer_vals, self.label_placeholder2, self.lineEdit_placeholder2, self.label_placeholder1, self.lineEdit_placeholder1, self.label_hypercam_vals, self.label_placeholder3, self.lineEdit_placeholder3, self.label_cam_vals, self.label_placeholder4, self.lineEdit_placeholder4))
        
        self.horizontalLayout_2.addWidget(self.MeasurementFrameList[index].label_led_name)   
        self.horizontalLayout_2.addWidget(self.MeasurementFrameList[index].lineEdit_led_name)
        self.horizontalLayout_2.addWidget(self.MeasurementFrameList[index].checkBox_calibrate)
        self.horizontalLayout_2.addWidget(self.MeasurementFrameList[index].checkBox_measurement)
        
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)
        
        self.gridLayout_2.addWidget(self.MeasurementFrameList[index].label_led_vals, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.MeasurementFrameList[index].lineEdit_dimmer_val, 2, 6, 1, 1)
        self.gridLayout_2.addWidget(self.MeasurementFrameList[index].label_dimmer_val, 2, 5, 1, 1)
        self.gridLayout_2.addWidget(self.MeasurementFrameList[index].label_duration, 2, 2, 1, 1)
        self.gridLayout_2.addWidget(self.MeasurementFrameList[index].lineEdit_duration, 2, 4, 1, 1)
        
        self.gridLayout_6.addWidget(self.MeasurementFrameList[index].label_spectrometer_vals, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.MeasurementFrameList[index].label_placeholder2, 0, 4, 1, 1)
        self.gridLayout_6.addWidget(self.MeasurementFrameList[index].lineEdit_placeholder2, 0, 5, 1, 1)
        self.gridLayout_6.addWidget(self.MeasurementFrameList[index].label_placeholder1, 0, 2, 1, 1)
        self.gridLayout_6.addWidget(self.MeasurementFrameList[index].lineEdit_placeholder1, 0, 3, 1, 1)
        
        self.gridLayout_5.addWidget(self.MeasurementFrameList[index].label_hypercam_vals, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.MeasurementFrameList[index].lineEdit_placeholder3, 1, 4, 1, 1)
        self.gridLayout_5.addWidget(self.MeasurementFrameList[index].label_placeholder3, 1, 3, 1, 1)
        
        self.gridLayout_4.addWidget(self.MeasurementFrameList[index].label_cam_vals, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.MeasurementFrameList[index].label_placeholder4, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.MeasurementFrameList[index].lineEdit_placeholder4, 0, 3, 1, 1) 
        
        # Set the name of the LED
        self.MeasurementFrameList[index].lineEdit_led_name.setText(self.LEDList[index].name)  
        
        self.verticalLayout_13.addWidget(self.frame_measurement)
        
        
class SetupFrame:
        def __init__(self, frame_setup, label_led_name, lineEdit_led_name, label_pin_number, lineEdit_pin_number, label_mA_value, lineEdit_mA_value, pushButton_delete, lineEdit_temperature_adress, label_temperature_adress):
            """
            Create a new SetupFrame object.
            :param frame_setup: The frame of the setup
            :param label_led_name: The label for the LED Name
            :param lineEdit_led_name: The line edit for the LED Name
            :param label_pin_number: The label for the Pin Number
            :param lineEdit_pin_number: The line edit for the Pin Number
            :param label_mA_value: The label for the mA Value
            :param lineEdit_mA_value: The line edit for the mA Value
            :param pushButton_delete: The push button to delete the frame
            """
            self.frame_setup = frame_setup
            self.label_led_name = label_led_name
            self.lineEdit_led_name = lineEdit_led_name
            self.label_pin_number = label_pin_number
            self.lineEdit_pin_number = lineEdit_pin_number
            self.label_mA_value = label_mA_value
            self.lineEdit_mA_value = lineEdit_mA_value
            self.pushButton_delete = pushButton_delete
            self.lineEdit_temperature_adress = lineEdit_temperature_adress
            self.label_temperature_adress = label_temperature_adress
            
                        
class SimpleControlFrame:
        def __init__(self, frame_3, label_led_name, lineEdit_led_name, label_duration, lineEdit_duration, pushButton_ON, pushButton_OFF, pushButton_activate, horizontalSlider):
            """
            Create a new SimpleControlFrame object.
            :param frame_3: The frame of the simple control
            :param label_led_name: The label for the LED Name
            :param lineEdit_led_name: The line edit for the LED Name
            :param label_duration: The label for the Duration
            :param lineEdit_duration: The line edit for the Duration
            :param pushButton_ON: The push button to turn the LED on
            :param pushButton_OFF: The push button to turn the LED off
            :param pushButton_activate: The push button to activate the LED
            :param horizontalSlider: The slider to set the pwm value
            """
            self.frame_3 = frame_3
            self.label_led_name = label_led_name
            self.lineEdit_led_name = lineEdit_led_name
            self.label_duration = label_duration
            self.lineEdit_duration = lineEdit_duration
            self.pushButton_ON = pushButton_ON
            self.pushButton_OFF = pushButton_OFF
            self.pushButton_activate = pushButton_activate
            self.horizontalSlider = horizontalSlider
            
class MeasurementFrame:
        def __init__(self, label_led_name, lineEdit_led_name, checkBox_calibrate, checkBox_measurement, label_led_vals, lineEdit_dimmer_val, label_dimmer_val, label_duration, lineEdit_duration, label_spectrometer_vals, label_placeholder2, lineEdit_placeholder2, label_placeholder1, lineEdit_placeholder1, label_hypercam_vals, label_placeholder3, lineEdit_placeholder3, label_cam_vals, label_placeholder4, lineEdit_placeholder4):
            """
            Create a new MeasurementFrame object.
            :param label_led_name: The label for the LED Name
            :param lineEdit_led_name: The line edit for the LED Name
            :param checkBox_calibrate: The check box to activate the LED
            :param checkBox_measurement: The check box to activate the Measurement
            :param label_led_vals: The label for the LED Values
            :param lineEdit_dimmer_val: The line edit for the Dimmer Value
            :param label_dimmer_val: The label for the Dimmer Value
            :param label_duration: The label for the Duration
            :param lineEdit_duration: The line edit for the Duration
            :param label_spectrometer_vals: The label for the Spectrometer Values
            :param label_placeholder2: The label for the Spectrometer Values
            :param lineEdit_placeholder2: The line edit for the Spectrometer Values
            :param label_placeholder1: The label for the Spectrometer Values
            :param lineEdit_placeholder1: The line edit for the Spectrometer Values
            :param label_hypercam_vals: The label for the Hyperspectral Camera Values
            :param label_placeholder3: The label for the Hyperspectral Camera Values
            :param lineEdit_placeholder3: The line edit for the Hyperspectral Camera Values
            :param label_cam_vals: The label for the Camera Values
            :param label_placeholder4: The label for the Camera Values
            :param lineEdit_placeholder4: The line edit for the Camera Values
            """
            self.label_led_name = label_led_name
            self.lineEdit_led_name = lineEdit_led_name
            self.checkBox_calibrate = checkBox_calibrate
            self.checkBox_measurement = checkBox_measurement
            self.label_led_vals = label_led_vals
            self.lineEdit_dimmer_val = lineEdit_dimmer_val
            self.label_dimmer_val = label_dimmer_val
            self.label_duration = label_duration
            self.lineEdit_duration = lineEdit_duration
            self.label_spectrometer_vals = label_spectrometer_vals
            self.label_placeholder2 = label_placeholder2
            self.lineEdit_placeholder2 = lineEdit_placeholder2
            self.label_placeholder1 = label_placeholder1
            self.lineEdit_placeholder1 = lineEdit_placeholder1
            self.label_hypercam_vals = label_hypercam_vals
            self.label_placeholder3 = label_placeholder3
            self.lineEdit_placeholder3 = lineEdit_placeholder3
            self.label_cam_vals = label_cam_vals
            self.label_placeholder4 = label_placeholder4
            self.lineEdit_placeholder4 = lineEdit_placeholder4
            
            
            