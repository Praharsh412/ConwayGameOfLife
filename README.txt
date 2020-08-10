Done by--
      EID - H402752
      NAME - Mamidala Sai Praharsh
      Institute - IIT Hyderabad

There are 4 files present namely --- main.py, game_class.py, cell_class.py, button_class.py

---------------------------------------Instructions to RUN the program:-----------------------------------


python version required: python 3.6+ or 3.8

This program uses 'pygame' library (python opensource package) for diplaying the interface of the grid.

To intall pygame the following instructions can be followed:

$pip install pygame OR 
$python3 -m pip install pygame OR 
$python -m pip install pygame   

Navigate to the folder where the files are present , and in the terminal or command prompt execute 'main.py'

$python3 main.py OR $python main.py   (BASED ON THE PATH VARIABLE SET FOR THE PYTHON 3.x version)

Now the pygame window will be up with the white grid with cells adn two buttons 'RUN' and 'RESET' on the top.

To run the evolution game, select the cells to be alive initially with mouse (input), the cells selected will be black in colour to represent that they are alive 

Now, Click on 'RUN' button at the top to view the evolution of the alive cells.

Now the evolution animation will be shown with 'PAUSE' button at the top , now you can select additional cells by clicking pause which pauses the animation
and select additional cells to be alive and click on 'RESUME' button to resume the animation with newly selected cells.

The 'RESET' button is to clear the screen, by clicking on this, all the animation happening will reset and the grid is reset to initial 
position of all white cells

The grid is circularly connected, i.e the neighbour of the last cell in a rows is inturn the first cell in the row, 
similarly neighbours of corner elements are other corner elements, the advantage of this is we will our animation or the evolution of 
alive cells always on the screen (such as 'glider')


------------------------------------------------------------------------------------------------------------


main.py contains the driver code for calling the functions of all other python files

game_class.py contains the class Game_window which contains the functions for creating the game screen for storing the grid
and to add cells

cell_class.py contains class for each cell, and its position in the grid or the screen based on the position accordingly and 
also for to get the neighbours of a cell.

button_class.py contains class for each button(template), and functions for update and draw() to be displayed on the screen.




