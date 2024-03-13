class Camera ():
    def __init__(self, iso = 100, aperture = "F/4", shutter_speed = 1/100):
        self.iso = iso
        self.aperture = aperture
        self.shutter_speed = shutter_speed
        
    def get_iso(self):
        """
        Get the ISO value of the camera.
        """
        return self.iso
    
    def get_aperture(self):
        """
        Get the aperture value of the camera.
        """
        return self.aperture
    
    def get_shutter_speed(self):
        """
        Get the shutter speed value of the camera.
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
        