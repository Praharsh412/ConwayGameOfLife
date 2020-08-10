"""
EID - H402752
Name - MAMIDALA SAI PRAHARSH
Institue - IIT Hyderabad

"""

import pygame
import threading
from cell_class import *
import time
vec = pygame.math.Vector2

# GAME_WINDOW CLASS FOR CREATION OF GAME SCREEN FOR GRID AND EVALUATION OF THE ALGORITHM OF GAME OF LIFE
class Game_window:
    # INITIALISATION OF THE GAME SCREEN WITH CELLS BEING CREATED FROM CELL_CLASS AND STORED IN GRID
    def __init__(self, screen, x,y):
        self.screen = screen
        self.pos = vec(x,y)
        self.width = 1000
        self.height = 500
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rows = 25
        self.cols = 50
        # 25 sets of 50 cells created
        self.grid = [[Cell(self.image, xt, yt) for xt in range(self.cols)] for yt in range(self.rows)]
        for row in self.grid:
            for cell in row:
                cell.get_neighbours(self.grid)
    
    # UPDATE FUNCTION FOR SETTING THE POSITION OF THE GAME SCREEN

    def update(self):
        self.rect.topleft = self.pos
        for row in self.grid:
            for cell in row:
                cell.update()
    
    # DRAW FUNCTION FOR BLTTING THE IMAGE OF THE GAME SURFACE TO THE SCREEN
    def draw(self):
        self.image.fill((102,102,102))
        for row in self.grid:
            for cell in row:
                cell.draw()

        self.screen.blit(self.image, (self.pos.x, self.pos.y))

    # RESET FUNCTION FOR REFRESHING THE GIRD FOR NEW INPUT
    def reset_grid(self):
        self.grid = [[Cell(self.image, xt, yt) for xt in range(self.cols)] for yt in range(self.rows)]
        for row in self.grid:
            for cell in row:
                cell.get_neighbours(self.grid)
    
    # EVALUATE FUNCTION FOR ALGORITHM OF GAME OF LIFE FOR THE NEXT STEP IN EVOLUTION
    def evaluate(self):
        #get a copy of the present grid
        new_grid = self.grid.copy()
        
        #get alive neighbours of a cell in the grid
        for row in self.grid:
            for cell in row:
                cell.live_neighbours()
        
        #enumerate on the grid cells and check the conditions on number of neighbours alive for a particular cell and update accordinly
        for yidx, row in enumerate(self.grid):
            #print({"gone":yidx, 'start':start_idx})
            for xidx, cell in enumerate(row):
                if cell.alive:
                    # remains alive and passed on to next generation
                    if cell.alive_neighbours == 2 or cell.alive_neighbours == 3:
                        new_grid[yidx][xidx].alive = True
                    # alive cell with less than 2 alive neighbours dies -- underpopulation
                    if cell.alive_neighbours < 2:
                        new_grid[yidx][xidx].alive = False
                    # alive cell with greater than 3 alive neighbouts dies -- overpopulation
                    if cell.alive_neighbours > 3:
                        new_grid[yidx][xidx].alive = False
                else:
                    # dead cell with exactly 3 alive neighbours becomes alive in the next generation -- reproduction
                    if cell.alive_neighbours == 3:
                        new_grid[yidx][xidx].alive = True

        # grid is updated with the new grid to display in the next generation
        self.grid = new_grid


                    





        