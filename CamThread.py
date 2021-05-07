from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import cv2
import time
from os.path import isfile, join
import os
import numpy as np
from datetime import datetime
from datetime import timedelta
import re
import os.path
from os import path
import pafy

class CamThread(QThread):
    changePixmap = pyqtSignal(QImage)

    def __init__(self,width, height, cam_name, url):
        super().__init__()
        self.cam_name = cam_name
        self.url = url
        self.width = width
        self.height = height
        self.Flag_Cam = False
        self.Flag_cap = False


    def run(self):

        self.Flag_Cam = False
        self.Flag_cap = False
        
        while True:
            self.frame_rate=8
            self.Flag_cap = False

            while True:
                if self.Flag_Cam == True:
                    self.frame_reset = np.zeros((self.height, self.width, 3))
                    p = self.convertToQtImage(self.frame_reset, self.width, self.height)
                    self.changePixmap.emit(p)
                    return
                try:
                    url = self.url
                    video = pafy.new(url)
                    best = video.getbest(preftype="mp4")
                    cap = cv2.VideoCapture(best.url)
                    time.sleep(0.01)
                except:
                    continue

                if (cap.isOpened()):

                    ret, img_input = cap.read()
                    if ret == False:
                        cap.release()
                        time.sleep(0.5)
                        continue

                    self.Flag_cap = True
                    break
                else:
                    print("cap is closed")
                

            
            while(cap.isOpened()):             
                self.Flag_cap = True
                
                if self.Flag_Cam == True:
                    self.frame_reset = np.zeros((self.height, self.width, 3))
                    p = self.convertToQtImage(self.frame_reset, self.width, self.height)
                    self.changePixmap.emit(p)
                    return
                time.sleep(0.01)

                try:
                    ret, img_input = cap.read()
                except Exception as e:
                    print(e)

                if ret == False:
                    cap.release()
                    self.frame_reset = np.zeros((self.height, self.width, 3))
                    p = self.convertToQtImage(self.frame_reset, self.width, self.height)
                    self.changePixmap.emit(p)
                    break
                else:
                    img_input = cv2.cvtColor(img_input, cv2.COLOR_BGR2RGB)
                    p = self.convertToQtImage(img_input, self.width, self.height)
                    self.changePixmap.emit(p)
                    time.sleep(0.02)


    def convertToQtImage(self, frame, width, height):
        h, w, ch = frame.shape
        bytesPerLine = ch * w
        convertToQtFormat = QImage(frame.data, w, h, bytesPerLine, QImage.Format_RGB888)
        p = convertToQtFormat.scaled(self.width, self.height)
        return p
