import numpy as np  
import win32gui, win32ui, win32con
from PIL import Image
import pyautogui,time
import cv2 as cv

class WindowCapture:

    hwnd = None

    def __init__(self,option,name=None,left=None,top=None,width=None,height=None):

        if option == 'Desktop':
            self.hwnd = win32gui.GetDesktopWindow()
            window_rect = win32gui.GetWindowRect(self.hwnd)
            self.width = window_rect[2] - window_rect[0]
            self.height = window_rect[3] - window_rect[1]
            self.left = 0
            self.top = 0

        elif option == 'winname':
            self.hwnd = win32gui.FindWindow(None, name)
            window_rect = win32gui.GetWindowRect(self.hwnd)
            self.width = window_rect[2] - window_rect[0]
            self.height = window_rect[3] - window_rect[1]
            self.left = 0
            self.top = 0

        elif option == 'region':
            self.hwnd = win32gui.GetDesktopWindow()
            self.left = left
            self.top = top
            self.width = width
            self.height = height

    
    def get_screenshot(self):
        #https://learncodebygaming.com/blog/fast-window-capture

        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.width, self.height)
        cDC.SelectObject(dataBitMap)
        
        cDC.BitBlt((0, 0), (self.width, self.height), dcObj, (self.left, self.top), win32con.SRCCOPY)

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.frombuffer(signedIntsArray, dtype='uint8')

        # opencv now understands
        img.shape = (self.height, self.width, 4)

        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        #REMOVING ALPHA CHANEEL 
        img = img[...,:3]
        img = np.ascontiguousarray(img) 
        return img







