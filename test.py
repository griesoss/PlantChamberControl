import serial
import threading
import queue

# Function to listen to the serial port
def listen_serial():
    while True:
        line = ser.readline().decode().strip()
        if line:
            print(line)
            # Perform desired action

# Function to send data to the Arduino
def send_to_arduino(data):
    #with serial_lock:
        ser.write(data.encode())

# Open serial connection
ser = serial.Serial('COM3', 115200)  # Adjust the port and baud rate as needed

# Create a lock for serial port access
#serial_lock = threading.Lock()

# Create a thread for listening to the serial port

serial_thread = threading.Thread(target=listen_serial)
serial_thread.daemon = True  # Daemonize the thread so it automatically closes when the main program exits
serial_thread.start()

# Main program loop
while True:
    # Get user input
    data_to_send = "Enter data to send to Arduino: "
    
    
    # Send data to Arduino
    send_to_arduino(data_to_send)