#importing sys and pygame modules
import sys
import pygame

#using settings
from settings import Settings
#using the ship
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """initialize and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height)) #tuple that draws game dimension windows
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        #set a background color(by default it gives black)
        self.bg_color = (230,230,230) #(R,G,B)

    def run_game(self):
        """start the main loop for the game"""
        while True:
            self._check_events() #_check_events() is a helper
            self.ship.update() 
            self._update_screen()
            
    def _check_events(self):
        #watch for keyboard and mouse events.
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()     
                #elif for movement to the right
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
            
            
    def _update_screen(self):
        #redraw the screen to fill the size
        """update images on the screen, and flip the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

         #make the most recently drawn screen visible
        pygame.display.flip()

#main class
if __name__ == '__main__':
    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()

