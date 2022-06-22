# cse210-05
Polymorphism: Teach One Another. Cycle Game 

# Overview
Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.

# Rules
Cycle is played according to the following rules. The players can move up, down, left and right where player one uses the W, S, A and D keys and player two uses the I, K, J and L keys. Each player's trails grows as they move. Players try to maneuver so the opponent collides with their trail. If a player collides with their opponemts's trail; a "game over" message is displayed in the middle of the screen. the cycles turn white and players keep moving and turning but don't run into each other.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```
python Cycle

# Requirements
The program must also meet the following requirements.

The program must include a README file.
The program must include class and method comments.
The program must have at least 16 classes.
The program must remain true to game play described in the overview.
To run the project
Go to the __main__.py file and execute the following command: python3 __main_.py



## Project Structure
---
The project files and folders are organized as follows:
```
root                   	                                  
  +--README.md			                    
  +--constants.py                       
  +--game
      +--actor.py                       
      +--cast.py                        
      +--food.py                        
      +--score.py                       
      +--cycle.py                       
      +--director.py          
      +--action.py                  
      +--control_actors_action.py   
      +--draw_actors_action.py      
      +--handle_collisions_action.py 
      +--move_actors-action.py       
      +--script.py                   
      +--keyboard-services.py            
      +--video-service.py           
      +--color.py            
      +--point.py 
  +--__main__.py            
```
## Required Software
--
* Python 3.8.0 
* Raylib Python CFFI 3.7
--


## *Authors & Contributions*
Arnold Sujan Katru (kat21015@byui.edu)- Scoring
Sandra Asamoah Adeleye (ade21006@byui.edu)- Collision Detection
Marcus Blanc (bla21011@byui.edu)- Game Over Messages
Karrass Phiri (phi21020@byui.edu)-Duplicate Player And Wall



