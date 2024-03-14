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
from matplotlib.backends.backend_qtagg  import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

#from LED import *
from ArduinoCommunication import *
from measurement import *
import numpy as np

class MpltCanvas(FigureCanvas):
    """
    Matplotlib canvas to display the plots.
    """
    def __init__(self, parent=None):
        """
        Initialize the Matplotlib canvas.
        :param parent: Parent widget
        """
        fig = Figure()
        self.axes = fig.add_subplot(111)
        super(MpltCanvas, self).__init__(fig)
        self.setParent(parent)

    def redraw(self):
        """
        Redraw the plot.
        """
        self.draw() 
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow, led_list, arduino_communication):   
        self.ArduinoCommunication = arduino_communication
        self.Measurement = Measurement(self.ArduinoCommunication)
               
            
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1365, 899)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        
        self.LEDList = led_list
        
        self.build_tab_setup(MainWindow)
        self.build_tab_calibration_measurement(MainWindow)
        self.build_tab_simplecontrol(MainWindow)
        
        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
        
        # Load the LED List after Setup to the Arduino
        self.ArduinoCommunication.setup_LEDs(self.LEDList)
        # setupUi 
    
    def build_tab_setup(self, MainWindow):
        self.tab_setup = QWidget()
        self.tab_setup.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab_setup)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.tab_setup)
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
        
        #build a matrix of x
        for x in range(0, 10):
                self.create_new_led_frame_setup(MainWindow, self.LEDList[x])
        
        self.verticalLayout_6.addWidget(self.frame_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        # Add LED Button
        self.pushButton_add_LED = QPushButton(self.tab_setup)
        self.pushButton_add_LED.setObjectName(u"pushButton_add_LED")        
        self.pushButton_add_LED.clicked.connect(lambda: self.create_new_led_frame_setup(MainWindow,-1))
        self.pushButton_add_LED.clicked.connect(lambda: self.retranslateUi(MainWindow))
        self.verticalLayout_3.addWidget(self.pushButton_add_LED)

        # Setup Button
        self.pushButton_setup = QPushButton(self.tab_setup)
        self.pushButton_setup.setObjectName(u"pushButton_setup")
        self.pushButton_setup.setMinimumSize(QSize(0, 80))
        self.pushButton_setup.clicked.connect(lambda: self.setup_button_clicked(MainWindow))
        self.verticalLayout_3.addWidget(self.pushButton_setup)

        self.tabWidget.addTab(self.tab_setup, "")
        
    def build_tab_calibration_measurement(self, MainWindow):
        self.tab_cal_measure = QWidget()
        self.tab_cal_measure.setObjectName(u"tab_3")
        self.verticalLayout_2 = QVBoxLayout(self.tab_cal_measure)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea_4 = QScrollArea(self.tab_cal_measure)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1711, 1137))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        font = QFont()
        font.setPointSize(9)
        font.setBold(True)        
        
        self.frame_6 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        
        # Create the LED specific frames for the Measurement Tab
        self.createMeasurementFrames() 
        
        self.verticalLayout_8.addWidget(self.frame_6)
        
        self.frame_heading = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_heading.setObjectName(u"frame_heading")
        self.frame_heading.setFrameShape(QFrame.StyledPanel)
        self.frame_heading.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QVBoxLayout(self.frame_heading)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        # Measurement Settings Header Label
        self.label_measure_settings = QLabel(self.frame_heading)
        self.label_measure_settings.setObjectName(u"label_1")
        self.label_measure_settings.setFont(font)        
        self.horizontalLayout_9.addWidget(self.label_measure_settings)
        self.verticalLayout_8.addWidget(self.frame_heading)
        
        # Load Data from the JSON File for the measurement setup for hyperspectral camera and spectrometer
        with open("measurement_specific_setup_data.json", 'r') as json_file:
            data = json.load(json_file)
            
        # Frame for the Spectrometer Settings
        self.frame_spectrometer_val = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_spectrometer_val.setObjectName(u"frame_spectrometer_val")
        self.frame_spectrometer_val.setFrameShape(QFrame.StyledPanel)
        self.frame_spectrometer_val.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_spectrometer_val)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        
        # Label - Spectrometer Values
        self.label_spectrometer_vals = QLabel(self.frame_spectrometer_val)
        self.label_spectrometer_vals.setObjectName(u"label_spectrometer_vals")
        self.label_spectrometer_vals.setMinimumSize(QSize(180, 0))
        self.gridLayout_6.addWidget(self.label_spectrometer_vals, 0, 0, 1, 1)
        
        # Line
        self.line_2 = QFrame(self.frame_spectrometer_val)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.gridLayout_6.addWidget(self.line_2, 0, 1, 1, 1)
        
        # Label - Value 1
        self.label_placeholder1 = QLabel(self.frame_spectrometer_val)
        self.label_placeholder1.setObjectName(u"label_placeholder1")
        self.gridLayout_6.addWidget(self.label_placeholder1, 0, 2, 1, 1)
        
        # Line Edit - Value 1
        self.lineEdit_placeholder1 = QLineEdit(self.frame_spectrometer_val)
        self.lineEdit_placeholder1.setObjectName(u"lineEdit_placeholder1")
        self.lineEdit_placeholder1.setText(str(data['spectrometer']['value1']))
        self.gridLayout_6.addWidget(self.lineEdit_placeholder1, 0, 3, 1, 1)  
      
        # Label - Value 2
        self.label_placeholder2 = QLabel(self.frame_spectrometer_val)
        self.label_placeholder2.setObjectName(u"label_placeholder2")
        self.gridLayout_6.addWidget(self.label_placeholder2, 0, 4, 1, 1)
        
        # Line Edit - Value 2
        self.lineEdit_placeholder2 = QLineEdit(self.frame_spectrometer_val)
        self.lineEdit_placeholder2.setObjectName(u"lineEdit_placeholder2")
        self.lineEdit_placeholder2.setText(str(data['spectrometer']['value2']))
        self.gridLayout_6.addWidget(self.lineEdit_placeholder2, 0, 5, 1, 1)
        
        self.verticalLayout_8.addWidget(self.frame_spectrometer_val)

        # Frame for the Hyperspectral Camera values
        self.frame_hypercam_val = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_hypercam_val.setObjectName(u"frame_hypercam_val")
        self.frame_hypercam_val.setFrameShape(QFrame.StyledPanel)
        self.frame_hypercam_val.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_hypercam_val)
        self.gridLayout_5.setObjectName(u"gridLayout_5")

        # Label - Hyperspectral Camera Values
        self.label_hypercam_vals = QLabel(self.frame_hypercam_val)
        self.label_hypercam_vals.setObjectName(u"label_hypercam_vals")
        self.label_hypercam_vals.setMinimumSize(QSize(180, 0))
        self.gridLayout_5.addWidget(self.label_hypercam_vals, 1, 0, 1, 1)

        # Line
        self.line_3 = QFrame(self.frame_hypercam_val)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.gridLayout_5.addWidget(self.line_3, 1, 2, 1, 1)

        # Label - Value 3
        self.label_placeholder3 = QLabel(self.frame_hypercam_val)
        self.label_placeholder3.setObjectName(u"label_placeholder3")
        self.gridLayout_5.addWidget(self.label_placeholder3, 1, 3, 1, 1)
        
        # Line Edit - Value 3
        self.lineEdit_placeholder3 = QLineEdit(self.frame_hypercam_val)
        self.lineEdit_placeholder3.setObjectName(u"lineEdit_placeholder3")
        self.lineEdit_placeholder3.setText(str(data['hyperspectral_camera']['value']))
        self.gridLayout_5.addWidget(self.lineEdit_placeholder3, 1, 4, 1, 1)
        
        self.verticalLayout_8.addWidget(self.frame_hypercam_val)
        
        # Frame for the Measurement Settings
        self.frame_18 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_18)
        self.gridLayout_7.setObjectName(u"gridLayout_7")

        # Label - Plant ID
        self.label_plant_id = QLabel(self.frame_18)
        self.label_plant_id.setObjectName(u"label_21")
        self.gridLayout_7.addWidget(self.label_plant_id, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_7.addItem(self.horizontalSpacer_3, 0, 4, 1, 1)

        # Line Edit - Plant ID
        self.lineEdit_8 = QLineEdit(self.frame_18)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMaximumSize(QSize(200, 16777215))
        self.gridLayout_7.addWidget(self.lineEdit_8, 0, 1, 1, 1)
        
        # Label - Measurement Type
        self.label_measurement_type = QLabel(self.frame_18)
        self.label_measurement_type.setObjectName(u"label_22")
        self.gridLayout_7.addWidget(self.label_measurement_type, 0, 2, 1, 1)

        # Combo Box - Measurement Type
        self.comboBox = QComboBox(self.frame_18)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.addItem("Zero Level - Mounted")
        self.comboBox.addItem("Zero Level - Unmounted")
        self.comboBox.addItem("In Vivo")
        self.comboBox.currentIndexChanged.connect(print())
        self.gridLayout_7.addWidget(self.comboBox, 0, 3, 1, 1)

        self.verticalLayout_8.addWidget(self.frame_18)

        # Start Calibration Button
        self.pushButton_calibration = QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton_calibration.setObjectName(u"pushButton_calibration")
        self.verticalLayout_8.addWidget(self.pushButton_calibration)

        # Start Measurement Button
        self.pushButton_measurement = QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton_measurement.setObjectName(u"pushButton_measurement")
        self.pushButton_measurement.clicked.connect(lambda: self.measurement_button_clicked())
        self.verticalLayout_8.addWidget(self.pushButton_measurement)

        # Line
        self.line = QFrame(self.scrollAreaWidgetContents_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_8.addWidget(self.line)

        # Frame for the Plots and Images
        self.frame_8 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_8)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        
        # Frame for the Temperature Plot
        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        
        # Plot for the Temperature        
        self.temperaturePlot = MpltCanvas(self.frame_7)
        self.temperaturePlot.setObjectName(u"temperaturePlot")
        self.temperaturePlot.setMinimumSize(0, 400)  # Set minimum size
        self.temperaturePlot.axes.set_xlabel('Time (s)')
        self.temperaturePlot.axes.set_ylabel('Temperature (°C)')
        x_data = [1, 2, 3, 4, 5]
        y_data = [20.5, 22.5, 25.2, 27.4, 28]        
        self.temperaturePlot.axes.plot(x_data, y_data, label='Example')
        self.temperaturePlot.axes.legend()
        self.temperaturePlot.axes.set_ylim(0, 30)
        self.temperaturePlot.redraw()
        self.verticalLayout_10.addWidget(self.temperaturePlot)
        
        # Label - Temperature Plot
        self.label_temp_plot = QLabel(self.frame_7)
        self.label_temp_plot.setObjectName(u"label_7")
        self.label_temp_plot.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_temp_plot)

        self.gridLayout_3.addWidget(self.frame_7, 0, 0, 1, 1)

        # Frame for the Spectrometer Plot
        self.frame = QFrame(self.frame_8)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        
        # Plot for the Spectrometer
        self.spectrometerPlot = MpltCanvas(self.frame)
        self.spectrometerPlot.setObjectName(u"spectrometerPlot")
        self.spectrometerPlot.setMinimumSize(0, 400)  # Set minimum size
        self.spectrometerPlot.axes.set_xlabel('Wavelength (nm)')
        self.spectrometerPlot.axes.set_ylabel('Intensity (%)')
        
        # Example data for V(lambda) curve
        wavelengths = np.arange(350, 1001)  # Wavelengths from 380 nm to 780 nm
        v_lambda = np.array([0.066862395,	0.063576466,	0.063821432,	0.064829878,	0.063598104,	0.061928648,	0.061115604,	0.06122432,	0.061627118,	0.062118068,	0.061692267,	0.060769137,	0.061853237,	0.061646365,	0.060514302,	0.059808391,	0.060742206,	0.061734719,	0.061881735,	0.06097579,	0.060195791,	0.060327137,	0.061098418,	0.060489714,	0.060077486,	0.05981584,	0.059323628,	0.059086345,	0.059262334,	0.059754614,	0.06022724,	0.059818673,	0.059285865,	0.059215404,	0.059160746,	0.059844019,	0.060269873,	0.05936608,	0.059298335,	0.05970933,	0.060042004,	0.059764017,	0.059696085,	0.059913004,	0.06029117,	0.060673927,	0.060858364,	0.06100586,	0.061385036,	0.061574045,	0.062049881,	0.062780199,	0.062982154,	0.063421432,	0.063873185,	0.06410523,	0.064779004,	0.064977648,	0.064916793,	0.065488698,	0.066348179,	0.067101972,	0.067640779,	0.068356474,	0.069063455,	0.069774194,	0.070551289,	0.07141962,	0.072318117,	0.073145055,	0.073775857,	0.074266924,	0.074949739,	0.075974019,	0.076978618,	0.077704494,	0.078297449,	0.079040891,	0.079575873,	0.08015251,	0.080879236,	0.081601125,	0.082364164,	0.082980217,	0.083328569,	0.083719105,	0.084186677,	0.084757072,	0.085438009,	0.086066283,	0.0866307,	0.087152632,	0.087654132,	0.088173697,	0.088677647,	0.089112309,	0.089484106,	0.089999848,	0.09062621,	0.091042121,	0.091439413,	0.091836279,	0.092211346,	0.092541591,	0.092866934,	0.093173371,	0.093418793,	0.093648457,	0.093907666,	0.094161448,	0.094220337,	0.094317639,	0.094456058,	0.094582713,	0.0948195,	0.094954606,	0.094955486,	0.094987014,	0.095120204,	0.095218497,	0.09520895,	0.095343019,	0.095385568,	0.095325513,	0.095283282,	0.09536712,	0.095464934,	0.095545685,	0.095757504,	0.095798634,	0.095815083,	0.096002874,	0.096131585,	0.096202736,	0.096258504,	0.096368739,	0.096566824,	0.096730025,	0.096812376,	0.097021937,	0.097336001,	0.097686133,	0.097995814,	0.098357748,	0.098779734,	0.099235482,	0.099657753,	0.100253637,	0.100907878,	0.101494523,	0.102244613,	0.103032487,	0.1038613,	0.104837384,	0.105850473,	0.106922258,	0.108080148,	0.109300527,	0.110648674,	0.11211434,	0.113663662,	0.115366065,	0.117139568,	0.118963521,	0.120911979,	0.122863635,	0.124919749,	0.12717242,	0.129468796,	0.131759444,	0.134049656,	0.136384319,	0.13868549,	0.140910787,	0.143068049,	0.145269022,	0.147304229,	0.149163453,	0.15091927,	0.15260225,	0.154147676,	0.155525771,	0.15676332,	0.157935129,	0.15900282,	0.159932553,	0.160825122,	0.161650159,	0.162388775,	0.16303481,	0.163599509,	0.164107681,	0.164594123,	0.165115726,	0.165643369,	0.166154186,	0.166636123,	0.167139792,	0.167623793,	0.168053069,	0.168417355,	0.168650964,	0.168785607,	0.168849166,	0.168775827,	0.168500805,	0.16806968,	0.167592605,	0.166925783,	0.166129377,	0.165267146,	0.164345603,	0.163352389,	0.162313012,	0.161254225,	0.160116753,	0.158916219,	0.157653425,	0.156299577,	0.154899533,	0.153485661,	0.152091057,	0.150774265,	0.149504935,	0.148274222,	0.147087427,	0.145971106,	0.144916257,	0.14390978,	0.142948307,	0.142070174,	0.141271032,	0.140530814,	0.139862444,	0.13918517,	0.138485424,	0.137829393,	0.137220143,	0.136640885,	0.136091556,	0.13564541,	0.135267919,	0.134926219,	0.134596995,	0.134317979,	0.134060668,	0.133804013,	0.133553155,	0.133270793,	0.132977735,	0.13269311,	0.132329238,	0.131997057,	0.131669836,	0.131192038,	0.130666542,	0.13011404,	0.129531727,	0.128893267,	0.128221593,	0.127515731,	0.126774246,	0.126040585,	0.125321706,	0.124615346,	0.123900794,	0.123257249,	0.122618369,	0.121936344,	0.12139591,	0.120919623,	0.120476349,	0.120077402,	0.119737265,	0.119471389,	0.119278474,	0.119130015,	0.118979762,	0.118837989,	0.11873322,	0.118643684,	0.118547558,	0.118420485,	0.118235371,	0.117944435,	0.117532174,	0.117002138,	0.116384015,	0.115667775,	0.114876621,	0.114050334,	0.113182972,	0.112274226,	0.111326907,	0.110345805,	0.109367372,	0.10843925,	0.107594614,	0.106790737,	0.106079101,	0.105485425,	0.105002817,	0.104547096,	0.104143351,	0.103791207,	0.103401636,	0.10293319,	0.102386201,	0.101781846,	0.101111154,	0.100362963,	0.099563823,	0.098772699,	0.098003806,	0.097255285,	0.096536696,	0.095909736,	0.095363383,	0.094887514,	0.094477292,	0.094168991,	0.093930107,	0.093752417,	0.093670434,	0.093621509,	0.093609532,	0.093661581,	0.093816751,	0.094024667,	0.094286887,	0.094645074,	0.095141382,	0.095823958,	0.096712757,	0.097777067,	0.099117072,	0.100788684,	0.102838163,	0.105334601,	0.108278294,	0.111748148,	0.11587667,	0.120609884,	0.125945701,	0.131882591,	0.138396259,	0.14547164,	0.153046125,	0.1610417,	0.169415145,	0.178106696,	0.187028121,	0.196068333,	0.205191287,	0.214358467,	0.223525715,	0.232671789,	0.241874838,	0.251112127,	0.260362481,	0.269652837,	0.279030294,	0.288518991,	0.298101552,	0.307732509,	0.317463229,	0.327312032,	0.337257995,	0.347266932,	0.357310286,	0.367379071,	0.377490923,	0.387616866,	0.397707406,	0.407688023,	0.417591989,	0.427326235,	0.436843468,	0.446228248,	0.455374722,	0.464265966,	0.472902702,	0.481217961,	0.489251148,	0.497009113,	0.504480886,	0.511635667,	0.518474428,	0.524984574,	0.531126201,	0.536945871,	0.542487677,	0.547766818,	0.552652522,	0.557220314,	0.561515565,	0.56553085,	0.569264094,	0.572719649,	0.575915512,	0.57891415,	0.581670466,	0.584182481,	0.586480575,	0.588597595,	0.5905674,	0.592392487,	0.59404961,	0.595545024,	0.596922682,	0.598209991,	0.599397389,	0.600485799,	0.601506742,	0.602472962,	0.603293989,	0.604059106,	0.604789621,	0.605462962,	0.606100773,	0.606701253,	0.607270876,	0.607826532,	0.608329503,	0.608830346,	0.609351982,	0.609774723,	0.61017415,	0.61058693,	0.611020121,	0.611426886,	0.61181655,	0.61217442,	0.612465555,	0.612810088,	0.61317298,	0.613516575,	0.613861447,	0.614220671,	0.614523712,	0.61472098,	0.61496511,	0.615253645,	0.615550463,	0.615802007,	0.616005448,	0.616227001,	0.616470909,	0.616646863,	0.61686404,	0.617090782,	0.617270786,	0.617365486,	0.61752244,	0.617747971,	0.617969477,	0.618080247,	0.618169309,	0.618258324,	0.618307888,	0.618379036,	0.618488159,	0.618613378,	0.618686731,	0.618700998,	0.61873856,	0.618860357,	0.618990537,	0.619089585,	0.619150004,	0.619182964,	0.619174398,	0.619251624,	0.619385349,	0.619414347,	0.61945173,	0.619446141,	0.619396296,	0.619415748,	0.61938845,	0.619351532,	0.619352775,	0.619348229,	0.61935609,	0.619387955,	0.619452361,	0.619560647,	0.619661662,	0.619754425,	0.619868349,	0.619880476,	0.619916827,	0.620044551,	0.620203038,	0.620321193,	0.620446157,	0.62061768,	0.620790198,	0.620912948,	0.621053079,	0.621268493,	0.621397227,	0.621505221,	0.621645506,	0.621841848,	0.622013254,	0.62213316,	0.622233958,	0.622391011,	0.622513499,	0.622643884,	0.62280289,	0.622941484,	0.623100136,	0.623273824,	0.623427798,	0.623471417,	0.623566252,	0.623694109,	0.623788635,	0.623891797,	0.624033941,	0.624205862,	0.624368803,	0.624470181,	0.624575392,	0.624713269,	0.624861341,	0.624957252,	0.625047164,	0.625133895,	0.625141285,	0.625273689,	0.62541884,	0.625482119,	0.625569236,	0.625593535,	0.625581367,	0.62559343,	0.625685087,	0.625741571,	0.625781884,	0.625857298,	0.625853586,	0.625893882,	0.625935224,	0.625858916,	0.625855359,	0.625902585,	0.625948841,	0.625938911,	0.625871188,	0.625868433,	0.625933991,	0.625902409,	0.625829079,	0.625772641,	0.625758917,	0.625750385,	0.625746722,	0.625699105,	0.625603733,	0.625596604,	0.625537521,	0.625502085,	0.625556326,	0.62548825,	0.625403324,	0.625285811,	0.625115879,	0.625105509,	0.625000444,	0.624753991,	0.624473552,	0.624292365,	0.624151721,	0.623946417,	0.623579351,	0.623158933,	0.622788651,	0.622446161,	0.62200934,	0.621611811,	0.621101401,	0.620490511,	0.619991951,	0.619279346,	0.618656213,	0.618192819,	0.617495845,	0.616802568,	0.61613089,	0.615379834,	0.614336958,	0.613335469,	0.61241513,	0.611447656,	0.610137972,	0.608908088,	0.607636655,	0.606161841,	0.604610706,	0.602816424,	0.600998784,	0.599387394,	0.597918184,	0.596255711,	0.594606088,	0.593193417,	0.591627876,	0.590188321,	0.588983434,	0.587999679,	0.587062878,	0.586212888,	0.585368171,	0.584501645,	0.583970622,	0.583472346,	0.582945156,	0.582455274,	0.582074903,	0.581575927,	0.581050357,	0.580710402,	0.580542049,	0.580362474,	0.580142754,	0.579953109,	0.579871076,	0.579840575,	0.579841,	0.579870453,	0.579902305,	0.58002297,	0.580169356,	0.580268783,	0.580581972,	0.580924828,	0.581291929,	0.581736785,	0.582084171,	0.582985339,	0.583886508,	0.584787677,	0.585688846,	0.586590015,	0.587491184,	0.588392353,	0.589293521,	0.59019469,])  # Example values of V(lambda) at each wavelength

        self.spectrometerPlot.axes.plot(wavelengths, v_lambda, label='Example')
        self.spectrometerPlot.axes.legend()
        self.spectrometerPlot.axes.set_ylim(0, 1)
        self.spectrometerPlot.redraw()
        self.verticalLayout_9.addWidget(self.spectrometerPlot)

        # Label - Spectrometer Plot
        self.label_spec_plot = QLabel(self.frame)
        self.label_spec_plot.setObjectName(u"label_6")
        self.label_spec_plot.setAlignment(Qt.AlignCenter)
        self.verticalLayout_9.addWidget(self.label_spec_plot)

        self.gridLayout_3.addWidget(self.frame, 0, 1, 1, 1)

        # Frame for the Hyperspectral Camera Image
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        
        # Image for the Hyperspectral Camera	
        self.graphicsView_3 = QGraphicsView(self.frame_9)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        self.verticalLayout_11.addWidget(self.graphicsView_3)

        # Label - Hyperspectral Camera Image
        self.label_hyperspec_img = QLabel(self.frame_9)
        self.label_hyperspec_img.setObjectName(u"label_8")
        self.label_hyperspec_img.setAlignment(Qt.AlignCenter)
        self.verticalLayout_11.addWidget(self.label_hyperspec_img)

        self.gridLayout_3.addWidget(self.frame_9, 1, 0, 1, 1)

        # Frame for the Camera Image
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        
        # Image for the Camera
        self.graphicsView_4 = QGraphicsView(self.frame_10)
        self.graphicsView_4.setObjectName(u"graphicsView_4")
        self.verticalLayout_12.addWidget(self.graphicsView_4)

        # Label - Camera Image
        self.label_cam_img = QLabel(self.frame_10)
        self.label_cam_img.setObjectName(u"label_9")
        self.label_cam_img.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_cam_img)

        self.gridLayout_3.addWidget(self.frame_10, 1, 1, 1, 1)

        self.verticalLayout_8.addWidget(self.frame_8)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_2.addWidget(self.scrollArea_4)

        self.tabWidget.addTab(self.tab_cal_measure, "")
        
    def build_tab_simplecontrol(self, MainWindow):
        self.tab_simpl_ctrl = QWidget()
        self.tab_simpl_ctrl.setObjectName(u"tab_4")
        self.verticalLayout_5 = QVBoxLayout(self.tab_simpl_ctrl)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea_2 = QScrollArea(self.tab_simpl_ctrl)
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

        self.tabWidget.addTab(self.tab_simpl_ctrl, "")
            
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
    
    def create_new_led_frame_measurement(self, index):     
        """
        Create a new frame for the Measurement Tab.
        :param index: Index of the LED in the LEDList
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
        
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)

        self.label_led_name = QLabel(self.frame_general)
        self.label_led_name.setObjectName(u"label_led_name")
        self.label_led_name.setMinimumSize(QSize(180, 0))
        
        self.line_56 = QFrame(self.frame_general)
        self.line_56.setObjectName(u"line_56")
        self.line_56.setFrameShape(QFrame.VLine)
        self.line_56.setFrameShadow(QFrame.Sunken)
        
        self.label_usage = QLabel(self.frame_general)
        self.label_usage.setObjectName(u"label_usage")
        self.label_usage.setMinimumSize(QSize(30, 0))
        
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
        
        self.label_dimmer_val = QLabel(self.frame_led_val)
        self.label_dimmer_val.setObjectName(u"label_dimmer_val")
        
        self.verticalLayout_14.addWidget(self.frame_led_val)
        
        # Frame for the Camera values
        self.frame_cam_val = QFrame(self.frame_measurement)
        self.frame_cam_val.setObjectName(u"frame_cam_val")
        self.frame_cam_val.setFrameShape(QFrame.StyledPanel)
        self.frame_cam_val.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_cam_val)
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        self.label_cam_vals = QLabel(self.frame_cam_val)
        self.label_cam_vals.setObjectName(u"label_cam_vals")
        self.label_cam_vals.setMinimumSize(QSize(180, 0))
        
        self.line_4 = QFrame(self.frame_cam_val)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.gridLayout_4.addWidget(self.line_4, 0, 1, 1, 1)
        
        self.label_iso = QLabel(self.frame_cam_val)
        self.label_iso.setObjectName(u"label_iso")

        self.lineEdit_iso = QLineEdit(self.frame_cam_val)
        self.lineEdit_iso.setObjectName(u"lineEdit_iso")
        
        self.label_aperture = QLabel(self.frame_cam_val)
        self.label_aperture.setObjectName(u"label_aperture")

        self.lineEdit_aperture = QLineEdit(self.frame_cam_val)
        self.lineEdit_aperture.setObjectName(u"lineEdit_aperture")
        
        self.label_shutter_speed = QLabel(self.frame_cam_val)
        self.label_shutter_speed.setObjectName(u"label_shutter_speed")

        self.lineEdit_shutter_speed = QLineEdit(self.frame_cam_val)
        self.lineEdit_shutter_speed.setObjectName(u"lineEdit_shutter_speed")
        
        self.verticalLayout_14.addWidget(self.frame_cam_val)
        
        # Create a new SimpleControlFrame object and append it to the MeasurementFrameList
        self.MeasurementFrameList.append(MeasurementFrame(self.label_led_name, self.label_usage, self.checkBox_calibrate, self.checkBox_measurement, self.label_led_vals, self.lineEdit_dimmer_val, self.label_dimmer_val, self.label_duration, self.lineEdit_duration, self.label_cam_vals, self.label_iso, self.lineEdit_iso, self.label_aperture, self.lineEdit_aperture, self.label_shutter_speed, self.lineEdit_shutter_speed))
        
        # General Information  
        self.horizontalLayout_2.addWidget(self.MeasurementFrameList[index].label_led_name)
        self.horizontalLayout_2.addWidget(self.line_56)
        self.horizontalLayout_2.addWidget(self.MeasurementFrameList[index].label_usage)
        self.horizontalLayout_2.addWidget(self.MeasurementFrameList[index].checkBox_calibrate)
        self.horizontalLayout_2.addWidget(self.MeasurementFrameList[index].checkBox_measurement)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)
        
        self.MeasurementFrameList[index].label_led_name.setText(self.LEDList[index].name + " LED")  
        self.MeasurementFrameList[index].label_led_name.setFont(font)
        self.checkBox_calibrate.setChecked(self.LEDList[index].calibration)
        self.checkBox_measurement.setChecked(self.LEDList[index].measurement)
        
        # LED specific Values
        self.gridLayout_2.addWidget(self.MeasurementFrameList[index].label_led_vals, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.MeasurementFrameList[index].label_duration, 2, 2, 1, 1)
        self.gridLayout_2.addWidget(self.MeasurementFrameList[index].lineEdit_duration, 2, 4, 1, 1)
        self.gridLayout_2.addWidget(self.MeasurementFrameList[index].label_dimmer_val, 2, 5, 1, 1)
        self.gridLayout_2.addWidget(self.MeasurementFrameList[index].lineEdit_dimmer_val, 2, 6, 1, 1)
        
        self.MeasurementFrameList[index].lineEdit_dimmer_val.setText(str(self.LEDList[index].dimming_val))
        self.MeasurementFrameList[index].lineEdit_duration.setText(str(self.LEDList[index].duration))
        
        # Camera specific Values      
        self.gridLayout_4.addWidget(self.MeasurementFrameList[index].label_cam_vals, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.MeasurementFrameList[index].label_iso, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.MeasurementFrameList[index].lineEdit_iso, 0, 3, 1, 1) 
        self.gridLayout_4.addWidget(self.MeasurementFrameList[index].label_aperture, 0, 4, 1, 1)
        self.gridLayout_4.addWidget(self.MeasurementFrameList[index].lineEdit_aperture, 0, 5, 1, 1) 
        self.gridLayout_4.addWidget(self.MeasurementFrameList[index].label_shutter_speed, 0, 6, 1, 1)
        self.gridLayout_4.addWidget(self.MeasurementFrameList[index].lineEdit_shutter_speed, 0, 7, 1, 1) 
        
        self.lineEdit_iso.setText(str(self.LEDList[index].camera_settings.iso))
        self.lineEdit_aperture.setText(str(self.LEDList[index].camera_settings.aperture))
        self.lineEdit_shutter_speed.setText(str(self.LEDList[index].camera_settings.shutter_speed))
        
        # Horizontal Line
        self.line_6 = QFrame(self.frame_measurement)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_14.addWidget(self.line_6)
        
        self.verticalLayout_13.addWidget(self.frame_measurement)
    
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
        self.SimpleControlFrameList[index].lineEdit_duration.setText(str(self.LEDList[index].duration))    
        
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
    
    def setup_button_clicked(self, MainWindow):
        """
        Handle the setup button click event.
        :param MainWindow: The main window of the application
        
        self.pushButton_setup.clicked.connect(lambda: self.updateLEDList(MainWindow))
        self.pushButton_setup.clicked.connect(lambda: self.ArduinoCommunication.setup_LEDs(self.LEDList))
        """
        self.updateLEDList(MainWindow)
        self.ArduinoCommunication.setup_LEDs(self.LEDList)
      
    def measurement_button_clicked(self):
        """
        Handle the measurement button click event.
        :param MainWindow: The main window of the application
        """
        self.tabWidget.setDisabled(True)
        self.ArduinoCommunication.turn_off_all_LEDs(self.LEDList)
        
        for led in self.LEDList:
            for test in self.MeasurementFrameList:
                if led.name == test.label_led_name.text()[:-4]:
                    led.set_dimming_val(int(test.lineEdit_dimmer_val.text()))
                    led.set_duration(int(test.lineEdit_duration.text()))
                    led.set_measurement(test.checkBox_measurement.isChecked())
                    led.set_calibration(test.checkBox_calibrate.isChecked())
                    
        self.Measurement.start_measurement(self.LEDList, self.temperaturePlot)
        
        self.tabWidget.setEnabled(True)
        
    def calibrate_button_clicked(self):
        """
        Handle the calibration button click event.
        :param MainWindow: The main window of the application
        """
        self.tabWidget.setDisabled(True)
        self.ArduinoCommunication.turn_off_all_LEDs(self.LEDList)
        
        for led in self.LEDList:
            for test in self.MeasurementFrameList:
                if led.name == test.label_led_name.text()[:-4]:
                    led.set_dimming_val(int(test.lineEdit_dimmer_val.text()))
                    led.set_duration(int(test.lineEdit_duration.text()))
                    led.set_measurement(test.checkBox_measurement.isChecked())
                    led.set_calibration(test.checkBox_calibrate.isChecked())
                    
        self.Measurement.start_calibration(self.LEDList)
        self.tabWidget.setEnabled(True)
    
    def updateLEDList(self, MainWindow):
        """
        Update the LEDList, the Measurement Tab and the Simple Control Tab with the new values from the Setup Tab.
        :param MainWindow: The main window of the application
        """
        # Turn off all LEDs
        self.ArduinoCommunication.turn_off_all_LEDs(self.LEDList)
        #time.sleep(5)
        
        # Iterate over self.SetupFrameDict and create a new LED object for each entry and update the LEDList
        
        # Remove all LEDs from the LEDList that are not in the SetupFrameDict
        for led in self.LEDList:
            hit = False
            for key in self.SetupFrameDict:
                if led.name == self.SetupFrameDict[key].lineEdit_led_name.text():
                    hit = True
            if not hit:
                self.LEDList.remove(led)
         
        # Update the LEDList with the new LEDs from the SetupFrameDict
        for key in self.SetupFrameDict:
            hit = False            
            # Create a new LED object for each entry in the dictionary if the str of one of these values is "" do not create an LED object
            if self.SetupFrameDict[key].lineEdit_led_name.text() != "" and self.SetupFrameDict[key].lineEdit_pin_number.text() != "" and self.SetupFrameDict[key].lineEdit_mA_value.text() != "":
                for led in self.LEDList:
                    if led.name == self.SetupFrameDict[key].lineEdit_led_name.text():
                        hit = True
            
            if not hit:
                new_led = LED(self.SetupFrameDict[key].lineEdit_led_name.text(), False, int(self.SetupFrameDict[key].lineEdit_pin_number.text()), int(self.SetupFrameDict[key].lineEdit_mA_value.text()), int(self.SetupFrameDict[key].lineEdit_temperature_adress.text()[2:],16))
                self.LEDList.append(new_led)        
                
        self.createSimpleControlFrames()
        self.createMeasurementFrames()
        
        self.retranslateUi(MainWindow)
        # updateLEDList
       
    def activate_func(self, index):
        """
		Activate the LED with the given pin number, PWM value for a given duration.
		:param index: Index of the LED in the LEDList
		"""
		# Turn on the LED
        self.SimpleControlFrameList[index].pushButton_ON.clicked.emit()
		# Wait for the duration
        duration = float(self.SimpleControlFrameList[index].lineEdit_duration.text())
		# Turn off after duration the LED        
        QTimer.singleShot(duration*1000, lambda: self.SimpleControlFrameList[index].pushButton_OFF.clicked.emit())    

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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_setup), QCoreApplication.translate("MainWindow", u"LED Setup", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cal_measure), QCoreApplication.translate("MainWindow", u"Calibration && Measurement", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_simpl_ctrl), QCoreApplication.translate("MainWindow", u"Simple LED Control", None))
        self.label_measurement_type.setText(QCoreApplication.translate("MainWindow", u"Measurement Type", None))
        self.label_plant_id.setText(QCoreApplication.translate("MainWindow", u"Plant ID", None))
        self.pushButton_calibration.setText(QCoreApplication.translate("MainWindow", u"Start Calibration", None))
        
        self.label_placeholder2.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_spectrometer_vals.setText(QCoreApplication.translate("MainWindow", u"Spectrometer Values", None))
        self.label_placeholder1.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_hypercam_vals.setText(QCoreApplication.translate("MainWindow", u"Hyperspectral Camera Values", None))
        self.label_placeholder3.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_measure_settings.setText(QCoreApplication.translate("MainWindow", u"Measurement Settings", None))
        
        # Iterate over self.MeasurementFrameList
        for index in range(0, len(self.MeasurementFrameList)):
            self.MeasurementFrameList[index].label_usage.setText(QCoreApplication.translate("MainWindow", u"Use in ", None))
            self.MeasurementFrameList[index].checkBox_calibrate.setText(QCoreApplication.translate("MainWindow", u" Calibration", None))
            self.MeasurementFrameList[index].checkBox_measurement.setText(QCoreApplication.translate("MainWindow", u" Measurement", None))
            self.MeasurementFrameList[index].label_duration.setText(QCoreApplication.translate("MainWindow", u"Duration", None))
            self.MeasurementFrameList[index].label_led_vals.setText(QCoreApplication.translate("MainWindow", u"LED Values", None))
            self.MeasurementFrameList[index].label_dimmer_val.setText(QCoreApplication.translate("MainWindow", u"Dimmer-Value", None))
            self.MeasurementFrameList[index].label_cam_vals.setText(QCoreApplication.translate("MainWindow", u"Camera Values", None))
            self.MeasurementFrameList[index].label_iso.setText(QCoreApplication.translate("MainWindow", u"ISO", None))
            self.MeasurementFrameList[index].label_aperture.setText(QCoreApplication.translate("MainWindow", u"Aperture", None))
            self.MeasurementFrameList[index].label_shutter_speed.setText(QCoreApplication.translate("MainWindow", u"Shutter Speed", None))
                   
        
        self.pushButton_measurement.setText(QCoreApplication.translate("MainWindow", u"Start Measurement", None))
        self.label_temp_plot.setText(QCoreApplication.translate("MainWindow", u"Temperature Data", None))
        self.label_spec_plot.setText(QCoreApplication.translate("MainWindow", u"Spectrometer Data", None))
        self.label_hyperspec_img.setText(QCoreApplication.translate("MainWindow", u"Hyperspectral Data", None))
        self.label_cam_img.setText(QCoreApplication.translate("MainWindow", u"Camera Data", None))        

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
            :param lineEdit_temperature_adress: The line edit for the Temperature Adress
            :param label_temperature_adress: The label for the Temperature Adress
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
        def __init__(self, label_led_name, label_usage, checkBox_calibrate, checkBox_measurement, label_led_vals, lineEdit_dimmer_val, label_dimmer_val, label_duration, lineEdit_duration, label_cam_vals, label_iso, lineEdit_iso, label_aperture, lineEdit_aperture, label_shutter_speed, lineEdit_shutter_speed):
            """
            Create a new MeasurementFrame object.
            :param label_led_name: The label for the LED Name
            :param label_usage: The label for the Usage
            :param checkBox_calibrate: The check box for the Calibration
            :param checkBox_measurement: The check box for the Measurement
            :param label_led_vals: The label for the LED Values
            :param lineEdit_dimmer_val: The line edit for the Dimmer Value
            :param label_dimmer_val: The label for the Dimmer Value
            :param label_duration: The label for the Duration
            :param lineEdit_duration: The line edit for the Duration
            :param label_cam_vals: The label for the Camera Values
            :param label_iso: The label for the ISO
            :param lineEdit_iso: The line edit for the ISO
            :param label_aperture: The label for the Aperture
            :param lineEdit_aperture: The line edit for the Aperture
            :param label_shutter_speed: The label for the Shutter Speed
            :param lineEdit_shutter_speed: The line edit for the Shutter Speed
            """
            self.label_led_name = label_led_name
            self.label_usage = label_usage
            self.checkBox_calibrate = checkBox_calibrate
            self.checkBox_measurement = checkBox_measurement
            self.label_led_vals = label_led_vals
            self.lineEdit_dimmer_val = lineEdit_dimmer_val
            self.label_dimmer_val = label_dimmer_val
            self.label_duration = label_duration
            self.lineEdit_duration = lineEdit_duration
            self.label_cam_vals = label_cam_vals
            self.label_iso = label_iso
            self.lineEdit_iso = lineEdit_iso
            self.label_aperture = label_aperture
            self.lineEdit_aperture = lineEdit_aperture
            self.label_shutter_speed = label_shutter_speed
            self.lineEdit_shutter_speed = lineEdit_shutter_speed    
            
            
            
            