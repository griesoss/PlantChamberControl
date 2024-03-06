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
        self.frame = QFrame(self.tab_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame)

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
        self.createSimpleControl()
        
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
    
    
    
    def createSimpleControl(self):
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
            self.SetupFrameDict[key].lineEdit_temperature_adress.setPlaceholderText("0x40-0x4F")
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
    # retranslateUi 
    
    
    def updateLEDList(self, MainWindow):
        """
        Update the LEDList and the Simple Control Tab with the new values from the Setup Tab.
        :param MainWindow: The main window of the application
        """
        #iterate over self.SetupFrameDict and create a new LED object for each entry and update the LEDList
        self.LEDList = []
        for key in self.SetupFrameDict:            
            #create a new LED object for each entry in the dictionary if the str of one of these values is "" do not create an LED object
            if self.SetupFrameDict[key].lineEdit_led_name.text() != "" and self.SetupFrameDict[key].lineEdit_pin_number.text() != "" and self.SetupFrameDict[key].lineEdit_mA_value.text() != "":
                self.LEDList.append(LED(self.SetupFrameDict[key].lineEdit_led_name.text(), False, int(self.SetupFrameDict[key].lineEdit_pin_number.text()), int(self.SetupFrameDict[key].lineEdit_mA_value.text()), self.SetupFrameDict[key].lineEdit_temperature_adress.text()))
        self.createSimpleControl()
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
            