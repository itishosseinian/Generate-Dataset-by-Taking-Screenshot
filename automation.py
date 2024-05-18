import pyautogui, time, os 
from PIL import Image
import cv2 as cv
import win32gui

from Capture import WindowCapture

class Automation:

    def generate_dataset(self,option,name=None,left=None,top=None,width=None,height=None):

        wincap = WindowCapture(option,name,left,top,width,height)

        if not os.path.exists("images"):
            os.mkdir("images")

        while(True):

            img = wincap.get_screenshot()

            im = Image.fromarray(img[..., [2, 1, 0]])

            im.save(f"./images/img_{len(os.listdir('images'))}.jpg")

            time.sleep(0.3)

    @staticmethod
    def get_coordinates(img_path):
        time.sleep(8)

        print(pyautogui.locateOnScreen(img_path, confidence = 0.9))

    @staticmethod
    def list_window_names():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)


if __name__ == "__main__":
    
    bot = Automation()

    bot.generate_dataset(option = 'region',left=580, top=223, width=743, height=558)

    #Automation.list_window_names()

    #Automation.get_coordinates('Capture.png')