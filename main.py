import time
import pyautogui
import pydirectinput
import keyboard

class xController:
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
    print(f"Fight took {int(executionTime)} to finish")
    
    
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
    i = 0
    startTime = time.time()
    executionTime = 1
    zeni = 0
    Looping = True 
    while Looping:
        if keyboard.is_pressed('escape'):
            Looping = False
            continue
        i += 1
        print("-----------")
        print(f"Loop {i} \nTotal Execution Time {int(executionTime/60)} minutes\nEarned roughly {zeni} Total Zeni")
        print("-----------")
        enter_map()
        start_battle()
        fight()
        exit_map()
        zeni += ZENI_PER_FIGHT
        time.sleep(10)
        executionTime = (time.time() - startTime)
    print(f"Looping Done, earned a total of {zeni} Zeni in {executionTime}")


def main():
    print("Script Started, ")
    time.sleep(15) # gives you 
    print("waiting complete")
    loop()

if __name__ == "__main__":
    main()