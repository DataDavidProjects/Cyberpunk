# Cyberpunk

Play Cyberpunk with Python.
**A non official version of python to speed up the crafting system of Cyberpunk 2077.**

This is just a system to simulate a click and hold in the crafting session ,if you have any issues or bugs in the game remind they won't be caused by this simple script.

##  CRAFTING IN CYBERPUNK For NON Python users:

  * Install Python >3 
  
      * link to download python in official webpage : https://www.python.org/downloads/release/python-385/
      
      * Link to download Python 3.8.5 For windows10 64bit users ( good for most windows users) : https://www.python.org/ftp/python/3.8.5/python-3.8.5-amd64.exe
      
      
      * Click and follow the installation, if you have problems check some tutorial on youtube like this one: https://www.youtube.com/watch?v=UvcQlPZ8ecA
  
  * Download from this repo the file "Cyberpunk.py"
  
  * Enter in Cyberpunk 2077 
  
  * Press the windows logo in the keyboard and go in the folder where you have the file "Cyberpunk.py" ( most of you will have it in the Downloads folder")
  
  * Double-click on the Python file "Cyberpunk.py" in your computer ( the python lunch icon will appear in your taskbar, click on it)
  
  * You might see some line of codes going on , don't worry they are just installing the requirements
  
  * Python will ask you to "Insert-number-of-Crafting-Rounds" , it is the number of items you wish to craft
  
  * Write a number like 5 or more and press "Enter" in the keyboard
  
  * The Program will start the countdown
  
  * Mouve your mouse in the game window just to ensure you are in the game and wait for the execution of the script
  
  * The mouse will click and craft for you ;) 
  
  * GIG closed
  
 IMPORTANT NOTE: DURING THE EXECUTION YOUR MOUSE WILL BE BLOCKED BE SURE TO INSERT A SMALL NUMBER <500 OTHERWISE YOU HAVE TO WAIT A LOT
 
  
## More Details

This script is just a set of rules based on the following python libraries:

* PyAutoGUI: https://pypi.org/project/PyAutoGUI/

Given a 1920x1080 there are standard coordinates in order to click and craft, if you have some experience feel free to change them in the code.

### Modify coordinates :

standard
* craft_coords = (1146,878)

custom
* craft_coords = (modify here,modify here)

There is a safe system to warn users that if they run more than 500 rounds they will be blocked for 0.7 * number of craftinhg seconds.
