import sys
import threading
from PySide6 import *

from ui_controlcenter import *

#from LED import *

class MainWindow(QMainWindow):
    
    def __init__(self, led_list, arduino_communication):
        """
        Initialize the main window.
        :param led_list: List of LED objects
        """
        #super().__init__()
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self,led_list, arduino_communication)
        arduino_communication.connection_error.connect(self.handle_connection_error)
        self.show()
        
        
    def handle_connection_error(self):
        """
        Handle the connection error.
        """
        connection_dialog = ConnectionDialog()
        arduino_communication.dialog_opened = True
        connection_dialog.exec()
        arduino_communication.dialog_opened = False
        
        
if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)
    
    # Initialize the LED objects
    led_list = initialize_leds()      
    
    # Establishing Connection with the Arduino
    arduino_communication = ArduinoCommunication()    
        
    # Create a thread for listening to the serial port
    serial_thread = threading.Thread(target= arduino_communication.listen_serial)
    serial_thread.daemon = True # Daemonize the thread so it automatically closes when the main program exits
    serial_thread.start()
    #arduino_communication.temp_changed.connect(lambda: print("test")) # Connect the signal to the slot
    
    # Create the main window    
    window = MainWindow(led_list, arduino_communication)
    
    # Execute the application
    sys.exit(app.exec())
    
