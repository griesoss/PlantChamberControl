
from ArduinoCommunication import *
#from PySide6.QtCore import *

class Measurement:
    def __init__(self, arduino_communication):
        """
        Initialize the Measurement object.
        """
        self.ArduinoCommunication = arduino_communication
        
    def start_measurement(self, LEDList):
        """
        Start the measurement.
        """
        # Start Temperautre Recording
        self.record_temp_lambda = lambda: self.record_temp()
        #self.ArduinoCommunication.temp_changed.connect(self.record_temp_lambda)
        
        # Turn on the LEDs one after another and take a picture
        for led in LEDList:
            if led.measurement:
                self.ArduinoCommunication.update_LED(led.pin_num, led.mA_val*led.dimming_val)
                time.sleep(led.duration)
                #QTimer.singleShot(led.duration*1000, lambda: self.ArduinoCommunication.turn_off_LED(led.pin_num))
                self.ArduinoCommunication.turn_off_LED(led.pin_num)
            
            #Take a picture
            #Save the picture
            #Save the data
                #time.sleep(2)
            
        #self.ArduinoCommunication.temp_changed.disconnect(self.record_temp_lambda)
            
    def record_temp(self):
        """
        Start the temperature recording.
        """
        test= self.ArduinoCommunication.temp_data   
        test = 0
            
        
        
        
 