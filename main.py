from numpy import tri
import pyautogui
from PIL import Image, ImageGrab
# from numpy import asarray
import time

def hit(key):
    pyautogui.press(key)

def isCollide(data):
    for i in range(240,350): #350 Changes the width
        for j in range(270,410):
            if data[i,j] < 100:
                hit('down')
                return True

    for i in range(300,400):
        for j in range(430,475):
            if data[i,j] < 100:
                hit('up')
                return True
    return False

if __name__ == "__main__":
    print("About to Start")
    time.sleep(2)
    hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()

        isCollide(data)

        if isCollide(data):
            hit('up')

        # print(asarray(image))

        # Draw rectangle for cactus    
    # image = ImageGrab.grab().convert('L')
    # data = image.load()
    # # for i in range(250,350): #350 Changes the width
    # for i in range(300,400): #350 Changes the width
    #     for j in range(430,475):
    #         data[i,j] = 0
    # image.show()

        # Draw rectangle for bird    
    # image = ImageGrab.grab().convert('L')
    # data = image.load()
    # for i in range(240,350): #350 Changes the width
    #     for j in range(270,410):
    #         data[i,j] = 171
    # image.show()

        # pyautogui.mouseInfo()