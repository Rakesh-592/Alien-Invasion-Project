class Settings:
    """A class to store all setting for alien invasion"""

    def __init__(self):
        """Initialize the game settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_speed = 1.5