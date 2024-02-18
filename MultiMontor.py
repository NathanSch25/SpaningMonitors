'''-----------------------#
Nathan R. Schober         |
02/18/2024 - 02/18/2024   |
Auto display spaning      |
------------------------'''

import pygetwindow as gw
import time
import pyautogui

def moveAndClick(x, y, x1, y1):
    pyautogui.moveTo(x + x1, y + y1)
    pyautogui.click()

x= 1200
y = 50
#opens nvidia control panel
pyautogui.moveTo(x,y)
pyautogui.rightClick()
moveAndClick(x, y, 20, 180)

#provides just enough time for control panel to open
time.sleep(3)

#Saves the tab We will be working with
nvidia = gw.getWindowsWithTitle('NVIDIA Control Panel')[0]
nvidia.resizeTo(700, 700)

#opens the surrond/physics sub menu
x, y = nvidia.topleft
moveAndClick(x, y, 60, 170)

#clicks span display option
moveAndClick(x, y, 335, 260)

#opens the menu for selecting the displays to use
moveAndClick(x, y, 350, 275)
time.sleep(2)

#Saves the Surround tab
setUp = gw.getWindowsWithTitle('NVIDIA Set Up Surround')[0]
x, y = setUp.topleft

#selects both monitors
moveAndClick(x, y, 70, 530)
moveAndClick(x, y, 70, 550)

#clicks the enable button
moveAndClick(x, y, 600, 750)

# Move the window to the new position
time.sleep(5)
setUp.moveTo(x + 1500, y)

#Closes surround
x, y = setUp.topright
moveAndClick(x, y, -20, 10)

#gives time for resolution to refresh
time.sleep(1)

#Closes Control Panel
x, y = nvidia.topright
moveAndClick(x, y, -20, 10)

#clears the on screen prompt
pyautogui.press('enter')
