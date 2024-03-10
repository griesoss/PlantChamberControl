class Camera ():
    def __init__(self, iso, aperture, shutter_speed):
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