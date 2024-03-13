
from ArduinoCommunication import *
from PySide6.QtCore import *
from datetime import datetime
import matplotlib.pyplot as plt


class Measurement:
    
    
    def __init__(self, arduino_communication):
        """
        Initialize the Measurement object.
        """
        self.ArduinoCommunication = arduino_communication
        
        
    def start_measurement(self, LEDList, temperaturePlot):
        """
        Start the measurement.
        """
        
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        print ("Start measurement at: " + timestamp)
        # Start Temperature Recording
        self.ArduinoCommunication.start_temp_recording()
        
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
        
        # Stop Temperature Recording    
        self.ArduinoCommunication.stop_temp_recording()
        
        # Get the saved Data
        
        df = process_temp_sets(self.ArduinoCommunication.continuous_temperature_data)
        location_str = 'measurement_data_' + timestamp + '.csv'
        #df.to_csv(location_str, index=False)
        
        
        # Assuming your DataFrame is named df
        # Convert 'Time' column to datetime if it's not already
        #df['Time'] = pd.to_datetime(df['Time'])
        
        temperaturePlot.axes.clear()  # Clear the existing plot
        
        for led in LEDList:
            if led.measurement:
                temperaturePlot.axes.plot(df['Time'], df[led.name], label=led.name)
        temperaturePlot.axes.set_xlabel('Time')
        temperaturePlot.axes.set_ylabel('Temperature (°C)')
        temperaturePlot.axes.legend()
        temperaturePlot.axes.set_ylim(0, 30)
        temperaturePlot.draw()  # Redraw the plot
            
        
    def start_calibration(self, LEDList):
        """
        Start the calibration.
        """
        
        
        
        
            
        
        
        
 