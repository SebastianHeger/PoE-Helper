import pyautogui
import keyboard
import time

link_coordinates = {"x":665, "y":910}


def link():
    """Activate a fusing orb left clicking on it with a fusing item in the middle of the currency tab"""
    while True:
        shift_pressed = False
        while keyboard.is_pressed('+') and keyboard.is_pressed('strg'):
            if not shift_pressed:
                pyautogui.keyDown("shift")
                shift_pressed = True
            pyautogui.click(link_coordinates["x"], link_coordinates["y"])
        pyautogui.keyUp("shift")

if __name__ == "__main__":
    link()