import pyautogui
import time

# Open Paint (you can replace this with the path to your desired application)
pyautogui.hotkey('win', 'r')
pyautogui.write('mspaint')
pyautogui.press('enter')

# Wait for Paint to open
time.sleep(2)

# Set the drawing location
x, y = 200, 200
pyautogui.click(x, y)

# Draw a simple pattern
pyautogui.moveTo(x + 50, y, duration=0.5)  # Move right
pyautogui.moveTo(x, y + 50, duration=0.5)  # Move down
pyautogui.moveTo(x - 50, y, duration=0.5)  # Move left
pyautogui.moveTo(x, y - 50, duration=0.5)  # Move up

# Close Paint
pyautogui.hotkey('alt', 'f4')

# You can replace the above steps with your desired pattern or actions.
