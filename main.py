import time
import pyautogui
import pydirectinput


class xController:
    """A class to map the Keyboard Controls to the Xbox equivalent
    """
    X = "u"
    A = "j"
    PAUSE = "tab"
    UP = "w"
    DOWN = "s"
    LEFT = "a"
    RIGHT = "d"
    SELECT = "enter"

CONTROLLER = xController()
DELAY = 5
ZENI_PER_FIGHT = 6029

def fight():
    startTime = time.time()
    for i in range(295):
        pydirectinput.write(CONTROLLER.X)
        time.sleep(0.014)
    executionTime = (time.time() - startTime)
    
    
    for i in range(6):
        time.sleep(2)
        pydirectinput.press(CONTROLLER.SELECT)  
    time.sleep(15)

def enter_map():
    pydirectinput.press(CONTROLLER.LEFT, interval=0.5)
    pydirectinput.press(CONTROLLER.SELECT, interval=0.5)
    pydirectinput.press(CONTROLLER.UP, interval=0.5)
    pydirectinput.press(CONTROLLER.UP, interval=0.5)
    pydirectinput.press(CONTROLLER.SELECT, interval=0.5)
    time.sleep(DELAY)

def exit_map():
    pydirectinput.press(CONTROLLER.PAUSE, interval=0.5)
    pydirectinput.press(CONTROLLER.UP, interval=0.5)
    pydirectinput.press(CONTROLLER.SELECT, interval=0.5)
    pydirectinput.press(CONTROLLER.UP, interval=0.5)
    pydirectinput.press(CONTROLLER.SELECT, interval=0.5)
    time.sleep(DELAY)


def start_battle():
    for i in range(8):
        pydirectinput.press(CONTROLLER.LEFT, interval=0.2)

    pydirectinput.press(CONTROLLER.SELECT)
    time.sleep(1)
    pydirectinput.press(CONTROLLER.SELECT)
    time.sleep(DELAY)


def loop():
        enter_map()
        start_battle()
        fight()
        exit_map()


def main():
    print("Script Started, You have 15 seconds to switch your screen to Dragon Ball FighterZ")
    time.sleep(15)
    print("waiting complete, starting game loop")
    i = 0
    startTime = time.time()
    executionTime = 1
    zeni = 0
    while True:
        i += 1
        print("-----------")
        print(f"Loop {i} \nTotal Execution Time {int(executionTime/60)} minutes\nEarned roughly {zeni} Total Zeni")
        print("-----------")
        loop()
        zeni += ZENI_PER_FIGHT
        time.sleep(10)
        executionTime = (time.time() - startTime)


if __name__ == "__main__":
    main()