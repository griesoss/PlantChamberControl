from periphery.camera import *
import json

class led:
    def __init__(self, name , is_on, pin_num, mA_val, temp_addr, dimming_val, duration, calibration, measurement):
        """
        Initialize the LED object.
        :param name: Name of the LED
        :param pin_num: Pin number of the LED
        :param mA_val: Forward current value of the LED
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
        
        self.camera_settings = 0
        
        
        
    def set_status(self, status):
        """
        Set the status of the LED.
        :param status: Status of the LED
        """
        self.is_on = status
        
    def set_mA_val(self, mA_val):
        """
        Set the mA value of the LED.
        :param mA_val: Forward current value
        """
        self.mA_val = mA_val
        
    def set_pin_num(self, pin_num):
        """
        Set the pin number of the LED.
        :param pin_num: Pin number
        """
        self.pin_num = pin_num
        
    def set_duration(self, duration):
        """
        Set the duration of the LED.
        :param duration: Duration of the LED
        """
        self.duration = duration  
    
    def set_temp_addr(self, temp_addr):
        """
        Set the temperature sensor address of the LED.
        :param temp_addr: Temperature sensor address
        """
        self.temp_addr = temp_addr
        
    def set_dimming_val(self, dimming_val):
        """
        Set the dimming value of the LED.
        :param dimming_val: Dimming value
        """
        self.dimming_val = dimming_val
    
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
    Initialize the LED objects and return a list of LED objects.
    :return: LED_list
    """
    
    with open("setup_data.json", 'r') as json_file:
        data = json.load(json_file)
    
    leds_data = data['leds']
    
    LED_list = []
    
    for led_name, led_data in leds_data.items():
        # led_name will be the name of the LED (e.g., "uv2", "uv1", etc.)
        # led_data will be the dictionary containing the data for the LED
        pin_num = led_data['led_data']['pin_num']
        mA_val = led_data['led_data']['mA_val']
        temp_addr = int(led_data['led_data']['temp_addr'],16)
        dimming_val = led_data['led_data']['dimming_val']
        duration = led_data['led_data']['duration']
        
        calibration = led_data['measurement_data']['calibration']
        measurement = led_data['measurement_data']['measurement']
        
        json_led= led(led_name, False , pin_num, mA_val, temp_addr, dimming_val, duration, calibration, measurement)
        json_led.set_camera_settings(100, 2.8, 1/100)
        
        iso = led_data['camera_data']['iso']
        aperture = led_data['camera_data']['aperture']
        shutter_speed = led_data['camera_data']['shutter_speed']
        json_led.set_camera_settings(iso, aperture, shutter_speed)
        
        LED_list.append(json_led)
    
    
    
    """ LED_uv2 = LED("UV2", False , 12, 60, 0x40)  
    LED_uv1 = LED("UV1", False, 11, 100, 0x41)
    LED_blue = LED("Blue", False, 10, 120, 0x42)
    LED_green = LED("Green", False, 9, 120, 0x43)
    LED_lime = LED("Lime", False, 8, 120, 0x44)
    LED_orange = LED("Orange", False, 7, 120, 0x45)
    LED_red = LED("Red", False, 6, 120, 0x46)
    LED_farred1 = LED("Farred1", False, 5, 120, 0x47)
    LED_farred2 = LED("Farred2", False, 4, 140, 0x48) 
    LED_k5000 = LED("5000 K", False, 3, 120, 0x49) """
    
    # Create a list of the LED objects
    #LED_list = [LED_uv2, LED_uv1, LED_blue, LED_green, LED_lime, LED_orange, LED_red, LED_farred1, LED_farred2, LED_k5000]
    return LED_list

    
def convert_mA_into_pwm_val(mA):
    """
    Convert the forward current value into a PWM value.
    :param mA: Forward current value
    :return: The corresponding PWM value
    """
    """ # 250 mA corresponds to 0 PWM, 0 mA corresponds to 255 PWM
    pwm_val = (250-mA) * 255/250  """
    # 250 mA corresponds to 255 PWM, 0 mA corresponds to 0 PWM
    pwm_val = mA * 255/250
    return pwm_val