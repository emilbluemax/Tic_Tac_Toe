# Tic Tac Toe

<span style="color:blue">A simple tic tac toe game built using **python-tkinter**</span>

---
tkinter is used to build the GUI part of the project

Game for **2 players**.<br>
Where when each player registers one's name they are assigned with a playing token (X,O).
The game does not begin until the players register their names and are assigned a token.
On registering the button states become active/normal.

Once the player registers their name, they cant change their name again <br>
Prompts to the users are made using the **message box** module of tkinter

A global counter is maintained for tracking which player plays.

The tic tac toe **grid is made up of buttons** (b1-b9) <br>
Initial button values are all empty and their states are disabled. <br>
Each button has a unique callback function on button click to assign X, O button text based on the user who clicks <br>
The buttons color changes on click based on the user for a better representation <br>
Once a button is clicked, the button gets disabled preventing any further clicks on it. <br>

After every button click a check function is invoked to check if any user has won the game or not

The winning positions are hard coded using if statments since there are only a limited number of winning sequences<br>
Once a player wins, a victory message is displayed and the game-window is terminated.

---

For running the program: 
+ Clone/Download the program
+ Double click to run

