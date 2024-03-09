# Importing Libraries 

from PySide6.QtCore import *
#(QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt)
from PySide6.QtGui import * 
#(QAction, QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *

import serial 
import time 
import json
from enum import Enum
from LED import *
from TemperatureData import *


class ArduinoCommunication(QObject):
	"""
	Establishes a connection with the Arduino and sends data to the Arduino.
	"""
	connection_error = Signal()
	temp_changed = Signal()
 
	def __init__(self):
		"""
		Initialize the ArduinoCommunication object and establish a connection with the Arduino.
		Set the default values for pin_data and toggle_data.
		"""	
		super().__init__()
		self.dialog_opened = False

		# Estalishing Connection with the Arduino
		arduino_communication = None
		while arduino_communication is None:
			try:
				self.arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1) 
				arduino_communication = self.arduino
			except Exception as e:				
				dialog = ConnectionDialog()
				dialog.exec()
				time.sleep(1)
				arduino_communication = None
     					
		
		# Default values for pin_data
		self.pin_data = {
			"type": "Setup",
			"pwm_pin_val": {
				"uv2": 13,
				"uv1": 12,
				"blue": 11,
				"green": 10,
				"lime": 9,
				"orange": 8,
				"red": 7,
				"farred1": 6,
				"farred2": 5,
				"k5000": 4,
				},
			"temp_addr": {
				"uv2": 0x40,
				"uv1": 0x41,
				"blue": 0x42,
				"green": 0x43,	
				"lime": 0x44,	
				"orange": 0x45,		
				"red": 0x46,
				"farred1": 0x47,	
				"farred2": 0x48,	
				"k5000": 0x49,
        		}
		}

		# Default values for toggle_data
		self.toggle_data = {
			"type": "Toggle",
			"pin_num": 0,
			"pwm_val": 250,
		} 

		# Create a global TemperatureData object array
		self.temp_data = []
		
    
	def turn_off_all_LEDs(self, LED_list):
		"""
		Turn off all the LEDs in the LED_list.
		:param LED_list: List of LED objects
		"""
		for led in LED_list:
			self.turn_off_LED(led.pin_num)
			time.sleep(0.1)
   
   
 
	def update_pin_data(self, LED_list):
		"""
		Update the pin_data with the pin numbers of the LED objects.
		:param LED_list: List of LED objects
		"""
		# Clear the entries for pwm_pin_val and temp_addr in pin_data
		self.pin_data = {
			"type": "Setup",
			"pwm_pin_val": {},
			"temp_addr": {}
		}
		# Iterate through the LED_list
		for led in LED_list:
			# Update the pin_data with the new pin_num
			self.pin_data["pwm_pin_val"][led.name] = led.pin_num
   			# Update the pin_data with the temperature sensor addresses of the LED objects.	
			self.pin_data["temp_addr"][led.name] = led.temp_addr
   
	def update_toggle_data(self, on_off, pin_num, pwm_val):
		"""
		Update the toggle_data with the new values.
		:param on_off: "ON" or "OFF"
		:param pin_num: Pin number of the LED
		:param pwm_val: PWM value of the LED
		"""
		self.toggle_data["type"] = on_off
		self.toggle_data["pin_num"] = pin_num
		self.toggle_data["pwm_val"] = pwm_val
  
	def write_read(self, json_data):
		"""
		Write and read the json_data to and from the Arduino.
		:param json_data: Data to be sent to the Arduino
		"""
		self.arduino.write(json_data) 
		#time.sleep(2) 
		""" data = self.arduino.readlines()
		for line in data:
			print(line.decode().strip()) # printing serial data
			print() """
	
	# Turn on the LED
	def update_LED(self, pin_num, pwm_val):
		"""
		Turn on the LED with the given pin number and PWM value.
		:param pin_num: Pin number of the LED
		:param pwm_val: PWM value of the LED
		"""
		# Update the toggle_data
		self.update_toggle_data("ON", pin_num, pwm_val)
  		# Convert the toggle_data to json
		json_toggle_data = json.dumps(self.toggle_data)
		# Write and read the json_toggle_data
		self.write_read(json_toggle_data.encode())
	
	# Turn off the LED
	def turn_off_LED(self, pin_num):
		"""
		Turn off the LED with the given pin number.
		:param pin_num: Pin number of the LED
		"""
		# Update the toggle_data
		self.update_toggle_data("OFF", pin_num, 255)
  		# Convert the toggle_data to json
		json_toggle_data = json.dumps(self.toggle_data)
		# Write and read the json_toggle_data
		self.write_read(json_toggle_data.encode())
  
  	
	def setup_LEDs(self, LED_list):
		"""
		Set up the LEDs with the given pin numbers.
		:param LED_list: List of LED objects
		"""
		# Update the pin_data
		self.update_pin_data(LED_list)
		# Convert the pin_data to json
		json_pin_data = json.dumps(self.pin_data)
		# Reset the Arduino
		self.arduino.setDTR(False)
		time.sleep(1)
		self.arduino.setDTR(True)
		# Write and read the json_pin_data
		time.sleep(1) # waiting for the serial connection to initialize
		self.write_read(json_pin_data.encode())
  
	def listen_serial(self):
		"""
		Listen to the serial data from the Arduino.
		"""
		while True:
			try:
				line = self.arduino.readline().decode(errors='replace').strip()
				if line:					
					if line.startswith('{"type":"Temperature"'):
						temp_data = json.loads(line)
						# TODO: save data to database
						self.save_temp_data(temp_data)
						self.temp_changed.emit()
					else:
						print(line)
			except Exception as e:
				time.sleep(1)
				self.reconnect()
    
	
  
	def reconnect(self):
		"""
		Reconnect to the Arduino.
		"""
		# try to connect arduino
		arduino_communication = None
		while arduino_communication is None:
			try:
				self.arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1) 
				arduino_communication = self.arduino
			except Exception as e:
				if self.dialog_opened == False:
					self.connection_error.emit()
				time.sleep(1)
				arduino_communication = None
    				
	def save_temp_data(self, temp_data):
		"""
		Get the temperature data from the Arduino.
		"""
		# Iterate through the temp_data
		for key, value_layer1 in temp_data.items():
			values = []
			if value_layer1 != "Temperature":
				for value_layer2 in value_layer1.values():
					values.append(value_layer2)
				self.temp_data.append(TemperatureData(key, values))
		return self.temp_data
  

class ConnectionDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Arduino Connection Error")
        self.resize(300, 100)  # Set the size of the dialog

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Create a horizontal layout for the icon and text
        hlayout = QHBoxLayout()
        layout.addLayout(hlayout)
        
        # Add the icon
        icon_label = QLabel()
        
        icon = QApplication.style().standardIcon(QStyle.SP_MessageBoxWarning)
        pixmap = icon.pixmap(40, 40)  # Set the size of the icon
        
        #pixmap = QPixmap("path_to_your_icon.png")  # Replace with the path to your icon
        icon_label.setPixmap(pixmap)
        hlayout.addWidget(icon_label)
        
        # Add the text
        text_label = QLabel("Arduino not found. Please connect the Arduino and try again. \nIf the problem persists, check if the Serial Port is blocked by another Application.")
        hlayout.addWidget(text_label)

        button = QPushButton("OK")
        button.clicked.connect(self.accept)
        layout.addWidget(button)





