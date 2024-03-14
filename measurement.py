
from ArduinoCommunication import *
from PySide6.QtCore import *
from datetime import datetime
import matplotlib.pyplot as plt
import os


class Measurement:
    """
    Measurement class for starting and saving the measurement data.
    
    Attributes:
        ArduinoCommunication: ArduinoCommunication object
    Methods:
        __init__: Initialize the Measurement object
        start_measurement: Start the measurement
        start_calibration: Start the calibration
        save_to_folder: Save the measurement data to a folder
    """
    def __init__(self, arduino_communication):
        """
        Initialize the Measurement object.
        :param arduino_communication: ArduinoCommunication object
        """
        self.ArduinoCommunication = arduino_communication
        
        
    def start_measurement(self, LEDList, temperaturePlot):
        """
        Start the measurement.
        :param LEDList: List of LED objects
        :param temperaturePlot: Temperature plot Canvas
        """              
        
        # Get the current timestamp
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
            
            #Take and save a picture
        
        # Stop Temperature Recording    
        self.ArduinoCommunication.stop_temp_recording()
        
        # Get the saved Data        
        df = process_temp_sets(self.ArduinoCommunication.continuous_temperature_data)
        
        # Plot the temperature data       
        temperaturePlot.axes.clear()  # Clear the existing plot 
        # For every LED that is being measured, plot the temperature data     
        for led in LEDList: 
            if led.measurement:
                temperaturePlot.axes.plot(df['Time'], df[led.name], label=led.name) # Plot the temperature data
        temperaturePlot.axes.set_xlabel('Time') # Set the x-axis label
        temperaturePlot.axes.set_ylabel('Temperature (°C)') # Set the y-axis label 
        temperaturePlot.axes.legend() # Add a legend
        temperaturePlot.axes.set_ylim(0, 30) # Set the y-axis range
        temperaturePlot.draw()  # Redraw the plot
        
        temperaturePlot.figure.savefig('temperature_plot.png') # Save the plot as a .png file
        
        # Save the measurement data to a folder
        self.save_to_folder(df, temperaturePlot, timestamp)
            
        
    def start_calibration(self, LEDList):
        """
        Start the calibration.
        """
        # TODO: Implement the calibration
        
        
    def save_to_folder(self, df, temperaturePlot, timestamp):
        """
        Save the measurement data to a folder.
        :param df: DataFrame with the temperature data
        :param temperaturePlot: Temperature plot Canvas
        :param timestamp: Timestamp of the start of the measurement
        """
        # Get the directory of the main script
        main_dir = os.path.dirname(os.path.realpath(__file__))

        # Specify the parent directory and the new directory name
        parent_dir = os.path.join(main_dir, "measurement_data")
        #timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        dir_name = timestamp

        # Create the full directory path
        dir_path = os.path.join(parent_dir, dir_name)

        # Create the directory
        os.makedirs(dir_path, exist_ok=True)
        
        # Save the temperature data to the directory
        temp_location_str = dir_path + "/" + timestamp + '_temperature_data'  + '.csv'        
        df.to_csv(temp_location_str, index=False)
        
        # Save the temperature plot to the directory
        temp_fig_location_str = dir_path + "/" + timestamp + '_temperature_graph'  + '.png'
        temperaturePlot.figure.savefig(temp_fig_location_str) 