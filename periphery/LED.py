from periphery.camera import *
import json

class LED:
    """
    LED class to represent the LED objects. Provides methods to initialize, get and set the values of the LED.
    
    Methods:
        __init__: Initialize the LED object with the given parameters
        set_status: Set the status of the LED
        set_dimming_val: Set the dimming value of the LED
        set_duration: Set the duration of the LED
        set_calibration: Set the calibration status of the LED
        set_measurement: Set the measurement status of the LED
        set_camera_settings: Set the camera settings of the LED
    """
    def __init__(self, name , is_on, pin_num, mA_val, temp_addr, dimming_val = 1, duration = 1, calibration = False, measurement= False):
        """
        Initialize the LED object with the given parameters. For the parameters that are not given, use default values.
        :param name: Name of the LED
        :param pin_num: Pin number of the LED
        :param mA_val: Maximum forward current value of the LED
        :param temp_addr: Address of the temperature sensor of the LED
        :param dimming_val: Dimming value of the LED
        :param duration: Duration of the LED
        :param calibration: Whether the LED is used for calibration
        :param measurement: Whether the LED is used for measurement
        """
        self.name = name
        self.is_on = is_on
        self.pin_num = pin_num
        self.mA_val = mA_val
        self.temp_addr = temp_addr
        self.dimming_val = dimming_val
        self.duration = duration
        self.calibration = calibration
        self.measurement = measurement
        
        self.camera_settings = Camera()
        
    def set_status(self, status):
        """
        Set the status of the LED.
        :param status: Status of the LED
        """
        self.is_on = status
        
    def set_dimming_val(self, dimming_val):
        """
        Set the dimming value of the LED.
        :param dimming_val: Dimming value of the LED
        """
        self.dimming_val = dimming_val
    
    def set_duration(self, duration):
        """
        Set the duration of the LED.
        :param duration: Duration of the LED
        """
        self.duration = duration
    
    def set_calibration(self, calibration):
        """
        Set the calibration status of the LED. If the LED is used for calibration, the calibration status is True.
        :param calibration: Calibration status of the LED
        """
        self.calibration = calibration
    
    def set_measurement(self, measurement):
        """
        Set the measurement status of the LED. If the LED is used for measurement, the measurement status is True.
        :param measurement: Measurement status of the LED
        """
        self.measurement = measurement
        
    def set_camera_settings(self, iso, aperture, shutter_speed):
        """
        Set the camera settings of the LED.
        :param iso: ISO value
        :param aperture: Aperture value
        :param shutter_speed: Shutter speed value
        """
        self.camera_settings = Camera(iso, aperture, shutter_speed)
           
    
def initialize_leds():
    """
    Initialize the LED objects with the data from the setup data JSON file and return a list of LED objects.
    :return: LED_list
    """    
    with open("led_specific_setup_data.json", 'r') as json_file:
        data = json.load(json_file)
    
    # Get the LED data from the JSON file
    leds_data = data['leds']
    
    
    LED_list = []
    
    # For each LED in the JSON file, create a LED object and add it to the LED_list.
    # The LED object is initialized with the led_data, measurement_data and camera_data
    for led_name, led_data in leds_data.items():
        
        # Get the led_data
        pin_num = led_data['led_data']['pin_num']
        mA_val = led_data['led_data']['mA_val']
        temp_addr = int(led_data['led_data']['temp_addr'],16)
        dimming_val = led_data['led_data']['dimming_val']
        duration = led_data['led_data']['duration']
        
        # Get the measurement_data
        calibration = led_data['measurement_data']['calibration']
        measurement = led_data['measurement_data']['measurement']
        
        # Create a LED object with the led_data, measurement_data
        json_led= LED(led_name, False , pin_num, mA_val, temp_addr, dimming_val, duration, calibration, measurement)
        json_led.set_camera_settings(100, 2.8, 1/100)
        
        # Get the camera_data
        iso = led_data['camera_data']['iso']
        aperture = led_data['camera_data']['aperture']
        shutter_speed = led_data['camera_data']['shutter_speed']
        
        # Set the camera settings of the LED
        json_led.set_camera_settings(iso, aperture, shutter_speed)
        
        # Add the LED object to the LED_list
        LED_list.append(json_led)
        
    return LED_list

    
def convert_mA_into_pwm_val(mA):
    """
    Convert the forward current value into a PWM value.
    :param mA: Forward current value
    :return: The corresponding PWM value
    """    
    # 250 mA corresponds to 255 PWM, 0 mA corresponds to 0 PWM
    pwm_val = mA * 255/250
    return pwm_val