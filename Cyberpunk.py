#_______________________ Importing Libraries #____________________________
import time
import subprocess
import sys

# Check requirements in code
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import pyautogui
except:
    install('pyautogui')
#_____________________________________________________________________________

#______________________________ Define coordinates of screen_____________________
craft_coords = (1146,878)

# Enter in the game check
pyautogui.click(craft_coords)
#________________________________________________________________________________

#_________________________________ Main function ________________________________
def craft_some_shit(craft_coords =craft_coords):
    pyautogui.click(craft_coords)
    pyautogui.mouseDown(craft_coords,button='left')
    print(craft_coords)
    time.sleep(0.7)
    pyautogui.mouseUp(craft_coords,button='left')
#__________________________________________________________________________________

#________________________________ Round exec ______________________________________
if __name__ == "__main__":
    print(' '*30,'*'*len('CRAFTING FOR LAZY ASS DUDES'),' '*30)
    print(' '*30,'CRAFTING FOR LAZY ASS DUDES',' '*30)
    print(' '*30,'*'*len('CRAFTING FOR LAZY ASS DUDES'),' '*30)

    print()
    
    round_craft = int(input("Insert-number-of-Crafting-Rounds:"))
  
    # Safe block
    max_craft = 500
    if round_craft > max_craft:
        print('Safe block for more than {} runs, please insert a smaller number'.format(max_craft))
        print('Are you sure you want to run ? ', )
        answer = input('press y to run or n ro go back:')
        if answer == 'y':
            for i in range(0, 4)[::-1]:
                time.sleep(1)
                print('Program will start in {} seconds'.format(str(i)))

            c = 0
            for c in range(0, round_craft):
                # time.sleep(0.5)
                craft_some_shit()
                c += 1
        else:
            round_craft = int(input("Insert-number-of-Crafting-Rounds:"))
    # Warm up
    print('Move your mouse in the game window')
    for i in range(0, 5)[::-1]:
        time.sleep(1)
        print('Program will start in {} seconds'.format(str(i)))

    # Execution
    c = 0
    for c in range(0,round_craft):
        #time.sleep(0.5)
        craft_some_shit()
        c+=1
#____________________________________________________________________________________
