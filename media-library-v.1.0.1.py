# Author: Jiri Svab
# screen resolution needed: width=3440, height=1440
# dependencies: Python3, PyAutogui
# notes: Taking the tasks "Move To" from HOME (alt+h) menu
# notes: Browser zoom level needs to be 150%
# notes: PyAutogui doesnt support dual monitors currently (21/10/19). 
# notes: Nevertheless it is recommended to launch this programm in separate screen.


import pyautogui, sys

run = pyautogui.prompt("How many times do you want to run this program? (Use numbers)")
path = pyautogui.prompt("Move to path:")

for x in range(int(run)): # run through this program x times
	pyautogui.PAUSE = 1.45 # make a pause between each instruction
	pyautogui.click( x=165, y=770, clicks=2, interval=3, button='left') # starting location of mouse
	pyautogui.hotkey('alt', 'h') # opens HOME menu
	pyautogui.moveTo(809, 478, 1, pyautogui.easeInOutQuad) # move mouse over "Move To" in HOME menu
	pyautogui.click(button='left') # click mouse on "Move To" in HOME menu
	pyautogui.moveTo(370, 1154, 1, pyautogui.easeInOutQuad) # move mouse to "Path:"
	pyautogui.click(button='left') # click on "Path:"
	pyautogui.hotkey('ctrl', 'a') # select all
	pyautogui.typewrite(str(path)) # Write the path of uncategorized folder
	pyautogui.moveTo(1339, 1269, 1, pyautogui.easeInOutQuad) # move mouse over button "Move"
	pyautogui.click(button='left') # click on "Move"


pyautogui.alert(f"Done {run} times")
