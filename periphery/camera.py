class Camera ():
    """
    Creates an Camera object with the given parameters and provides methods to get and set the parameters of the camera.
    
    Methods:
        __init__: Initialize the Camera object with the given parameters
        get_iso: Get the ISO value of the camera
        get_aperture: Get the aperture value of the camera
        get_shutter_speed: Get the shutter speed value of the camera
        set_iso: Set the ISO value of the camera
        set_aperture: Set the aperture value of the camera
        set_shutter_speed: Set the shutter speed value of the camera
    
    """
    def __init__(self, iso = 100, aperture = "F/4", shutter_speed = 1/100):
        """
        Initialize the camera object with the given parameters. 
        Use default values if no parameters are given.
        :param iso: ISO value
        :param aperture: Aperture value
        :param shutter_speed: Shutter speed value
        """
        self.iso = iso
        self.aperture = aperture
        self.shutter_speed = shutter_speed
        
    def get_iso(self):
        """
        Get the ISO value of the camera.
        :return: ISO value
        """
        return self.iso
    
    def get_aperture(self):
        """
        Get the aperture value of the camera.
        :return: Aperture value
        """
        return self.aperture
    
    def get_shutter_speed(self):
        """
        Get the shutter speed value of the camera.
        :return: Shutter speed value
        """
        return self.shutter_speed
    
    def set_iso(self, iso):
        """
        Set the ISO value of the camera.
        :param iso: ISO value
        """
        self.iso = iso
    
    def set_aperture(self, aperture):
        """
        Set the aperture value of the camera.
        :param aperture: Aperture value
        """
        self.aperture = aperture
    
    def set_shutter_speed(self, shutter_speed):
        """
        Set the shutter speed value of the camera.
        :param shutter_speed: Shutter speed value
        """
        self.shutter_speed = shutter_speed        