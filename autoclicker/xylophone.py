import pyautogui
import time

def a():
    time.sleep(0.3)
    pyautogui.press('1')
    time.sleep(0.3)
    pyautogui.press('3')
    time.sleep(0.3)
    pyautogui.press('5')
    time.sleep(0.3)
    pyautogui.press('8')
    time.sleep(0.3)
    pyautogui.press('0')
    time.sleep(0.9)


def main():
    for i in range(50):
        a()

main()