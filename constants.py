from pyautogui import size

screen_size = size()

SCREEN_WIDTH, SCREEN_HEIGHT = int(screen_size[0] // 1.5), int(screen_size[1] // 1.5)