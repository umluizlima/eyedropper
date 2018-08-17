import pyautogui
import pyperclip


def run():
    img = pyautogui.screenshot()
    color = img.getpixel(pyautogui.position())
    pyperclip.copy('#{0:02x}{1:02x}{2:02x}'.format(*color))


if __name__ == "__main__":
    run()
