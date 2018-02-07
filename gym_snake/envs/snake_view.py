"""
 Example program to show using an array to back a grid on-screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame


 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [255, 255]

class SnakeView:
    def __init__(self, tile_width, tile_height, tile_colors):        
        # Initialize pygame
        pygame.init()

        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tile_colors = tile_colors
 

        self.screen = pygame.display.set_mode(WINDOW_SIZE)
 
        # Set title of screen
        pygame.display.set_caption("Array Backed Grid")
    

# # Loop until the user clicks the close button.
# done = False
 
# # Used to manage how fast the screen updates
# clock = pygame.time.Clock()
    def render(self, state):
        # Set the screen background
        self.screen.fill((0,0,0))
    
        # Draw the grid
        for row in range(self.tile_height):
            for column in range(self.tile_width):
                element = state[row][column]
                color = self.tile_colors[element]
                # if grid[row][column] == 1:
                #     color = GREEN
                pygame.draw.rect(self.screen,
                                color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
    def close(self):
        pygame.quit()