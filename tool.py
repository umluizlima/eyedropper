import pyautogui
import pyperclip

img = pyautogui.screenshot()
color = img.getpixel(pyautogui.position())
pyperclip.copy('#{0:02x}{1:02x}{2:02x}'.format(*color))
