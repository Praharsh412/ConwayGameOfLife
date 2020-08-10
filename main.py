"""
EID - H402752
Name - MAMIDALA SAI PRAHARSH
Institue - IIT Hyderabad

Conway's Game of Life
"""
import pygame
import sys
import random
from game_class import *
from button_class import *

# PYGAME module is used for interactive interface of the game
width = 1080
height = 600

# Pygame initialisation with size and clock
pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode((width, height))
clk = pygame.time.Clock()

# Getting instance of the Game_window from game_class
game_window = Game_window(screen, 40, 80)
fps = 60
state = 'idle'


# FUNCTION FOR START GAME, which contains game_window update as well as draw functions for displaying screen
def start_game(state):
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_position):
                click_cell(mouse_position)
            else:
                for button in buttons:
                    button.click()
    game_window.update()
    for button in buttons:
        button.update(mouse_pos, game_state=state)
    if state =='running':  #WHEN STATE IS RUNNING, THE GAME IS EVALUATED.
        if frame_count%(fps//4) == 0:
            game_window.evaluate()
    screen.fill((133,133,133))
    for button in buttons:
        button.draw()
    game_window.draw()

# FUNCTION FOR VALIDATING THE MOUSE CLICK TO BE ALLOWED ONLY ON THE GRID OF CELLS
def mouse_on_grid(pos):
	if pos[0] > 40 and pos[0] < width-40:
		if pos[1] >80 and pos[1] < height - 20:

			return True
	return False

# FUNCTION FOR CLICK CELL, WHERE THE CELL IS TURNED TO ACTIVE STATUS OR INACTIVE ACCORDINGLY


def click_cell(pos):
    grid_pos = [pos[0]-40, pos[1]-80]
    grid_pos[0] = grid_pos[0]//20
    grid_pos[1] = grid_pos[1]//20
    if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = True




# FUNCTION FOR CREATION OF BUTTONS -  RUN, PAUSE, RESET, RESUME
def make_buttons():
	buttons = []
	buttons.append(Button(screen, width//2 - 50, 40, 100, 30, text='RUN',
	                       colour=(45, 138, 82), hover_colour=(255,255,255), bold_text= True, function=run_game, state='idle'))
	buttons.append(Button(screen, width//1.29 - 50, 40, 100, 30, text='RANDOM',
	                       colour=(46, 104, 135), hover_colour=(255,255,255), bold_text= True, function=random_game, state='idle'))
	buttons.append(Button(screen, width//2 - 50, 40, 100, 30, text='PAUSE',
	                       colour=(148, 37, 48), hover_colour=(255,255,255), bold_text= True, function=pause_game, state='running'))
	buttons.append(Button(screen, width//4 - 50, 40, 100, 30, text='RESET',
	                       colour=(166, 71, 7), hover_colour=(255,255,255), bold_text= True, function= reset_grid))
	buttons.append(Button(screen, width//1.29 - 50, 40, 100, 30, text='RESUME',
	                       colour=(45, 138, 82), hover_colour=(255,255,255), bold_text= True, function= run_game, state='paused'))
	return buttons

# FUNCTION CALLED WHEN RUN BUTTON IS CLICKED, STATE CHANGED TO 'RUNNING'
def run_game():
	global state
	state = 'running'

# FUNCTION CALLED WHEN PAUSE BUTTON IS CLICKED
def pause_game():
	global state
	state = 'paused'

# FUNCTION CALLED WHEN RESET BUTTON IS CLICKED, WHICH REFRESHES THE ENTIRE SCREEN
def reset_grid():
	global state
	state = 'idle'
	game_window.reset_grid()

# FUNCTION CALLED WHEN RANDOM BUTTON IS CLICKED 
def random_game():
	for i in range(25):
		for j in range(50):
			game_window.grid[i][j].alive = random.choice([True, False, False])


buttons = make_buttons()
frame_count = 0

run = True
#LOOP TO KEEP THE PYGAME SCREEN RUNNING
while run:
    frame_count += 1
    mouse_pos = pygame.mouse.get_pos()
    start_game(state)
    pygame.display.update()
    clk.tick(fps)
    

pygame.quit()
sys.exit()


