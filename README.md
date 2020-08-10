# ConwayGameOfLife
The repository contains code for Simulation of Conway's game of life in pygame

# Instructions to run the program:

There are 4 files present namely --- main.py, game_class.py, cell_class.py, button_class.py

python version required: **python 3.6+ or 3.8**

This program uses **'pygame'** library (python opensource package) for diplaying the interface of the grid.

Information about pygame can be found here: https://realpython.com/pygame-a-primer/

To install pygame the following instructions can be followed:
```
$pip install pygame
```
or
```
$python3 -m pip install pygame
```
or
```
$python -m pip install pygame
```
Depending on path variable used for python 3.x version

Navigate to the folder where the files are present , and in the terminal or command prompt execute 'main.py'

```
python3 main.py
```
OR
```
$python main.py
```
(BASED ON THE PATH VARIABLE SET FOR THE PYTHON 3.x version)

Now the pygame window will be up with the white grid with cells and two buttons 'RUN' and 'RESET' and 'RANDOM' on the top.

![alt text](https://github.com/Praharsh412/PraharshConwayGameOfLife/blob/master/Images/StartWIndow.png)

To run the evolution game, select the cells to be alive initially with mouse (input), the cells selected will be black in colour to represent that they are alive.
![alt text](https://github.com/Praharsh412/PraharshConwayGameOfLife/blob/master/Images/SelectWIndow.png)

To create a random set of alive cells, click on 'RANDOM', this will create a random set of cells with black in colour to represent them as alive. 

![alt text](https://github.com/Praharsh412/PraharshConwayGameOfLife/blob/master/Images/SelectRandom.png)

Now, Click on 'RUN' button at the top to view the evolution of the alive cells.

After click on RUN:
![alt text](https://github.com/Praharsh412/PraharshConwayGameOfLife/blob/master/Images/SelectPause.png)

Now the evolution animation will be shown with 'PAUSE' button at the top , now you can select additional cells by clicking pause which pauses the animation
and select additional cells to be alive and click on 'RESUME' button to resume the animation with newly selected cells.

![alt text](https://github.com/Praharsh412/PraharshConwayGameOfLife/blob/master/Images/SelectResume.png)


The 'RESET' button is to clear the screen, by clicking on this, all the animation happening will reset and the grid is reset to initial 
position of all white cells

![alt text](https://github.com/Praharsh412/PraharshConwayGameOfLife/blob/master/Images/SelectReset.png)

The grid is circularly connected, i.e the neighbour of the last cell in a rows is inturn the first cell in the row, 
similarly neighbours of corner elements are other corner elements, the advantage of this is we will our animation or the evolution of 
alive cells always on the screen (such as 'glider')

# Files description:
main.py contains the driver code for calling the functions of all other python files

game_class.py contains the class Game_window which contains the functions for creating the game screen for storing the grid
and to add cells

cell_class.py contains class for each cell, and its position in the grid or the screen based on the position accordingly and 
also for to get the neighbours of a cell.

button_class.py contains class for each button(template), and functions for update and draw() to be displayed on the screen.


