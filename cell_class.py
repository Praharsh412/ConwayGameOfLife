"""
EID - H402752
Name - MAMIDALA SAI PRAHARSH
Institue - IIT Hyderabad

"""


import pygame
import random

# CELL CLASS FOR CREATION OF EACH CELL IN THE GRID
class Cell:
    # FUNCTION FOR INITIALISATION OF THE CELL WITH PIXEL SIZE AND POSITION COORDINATES
	def __init__(self,surface, grid_x, grid_y):
		self.alive = False
		self.surface = surface
		self.grid_x = grid_x
		self.grid_y = grid_y
		self.image = pygame.Surface((20, 20)) #cell pixel size
		self.rect = self.image.get_rect()
		self.neighbours = []
		self.alive_neighbours = 0
		

    # FUNCTION FOR UPDATE OF THE CELL RECTANGLE REFERENCE SETTING 
	def update(self):
		self.rect.topleft = (self.grid_x*20, self.grid_y*20)
		
	# FUNCTION FOR BLITTING THE IMAGE INTO THE SURFACE WHERE THE CELL IS POSITIONED
	def draw(self):
        # CELL ALIVE - COLOR BLACK
		if self.alive:
			self.image.fill((0,0,0))
        # CELL DEAD - COLOR WHITE
		else:
			self.image.fill((0,0,0))
			pygame.draw.rect(self.image, (255,255,255),(1,1,19,19))
		self.surface.blit(self.image, (self.grid_x*20, self.grid_y*20))
	
    # FUNCTION FOR GETTING THE NEIGHBOURS OF A CELL DIAGONAL, AS WELL AS VERTICAL AND HORIZONTAL
	def get_neighbours(self, grid):
		neighbour_list = [[1,1], [-1,-1], [-1,1], [1,-1], [0,-1], [0,1], [1,0], [-1,0]]
		for neighbour in neighbour_list:
			neighbour[0] += self.grid_x
			neighbour[1] += self.grid_y
            # the neighbours of the cells at the boundaries are linked back to the first index like a circular screen  
		for neighbour in neighbour_list:
			if neighbour[0] < 0:
				neighbour[0] += 50
			if neighbour[1] < 0:
				neighbour[1] += 25
			if neighbour[0] > 49:
				neighbour[0] -= 50
			if neighbour[1] > 24:
				neighbour[1] -= 25
		for neighbour in neighbour_list:
			try:
				self.neighbours.append(grid[neighbour[1]][neighbour[0]])

			except:
				print(neighbour)
	
    # FUNCTION FOR GETTING THE COUNT OF THE LIVE NEIGHBOURS OF A CELL
	def live_neighbours(self):
		count = 0
		for neighbour in self.neighbours:
			if neighbour.alive:
				count += 1
		self.alive_neighbours = count





