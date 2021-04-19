from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
from os import path

from CamThread import CamThread
from Full_Screen import MainWindow as Full_Screen

class MainWindow(QMainWindow):
    def __init__(self, width, height,parent, folder_path):
        super().__init__()
        self.setMouseTracking(True)

        self.parent=parent
        self.folder_path = folder_path
        self.b = None
        self.width = width
        self.height = height
        self.screen_size = (self.width, self.height)
        self.setWindowTitle("IESS")
        self.setGeometry(0, 0, self.width, self.height)
        monitor = QDesktopWidget().screenGeometry(1)
        self.move(monitor.left(), monitor.top())
        self.showFullScreen()
        backImage = QImage(self.folder_path + "/imgs/back35.jpg")
        sImage = backImage.scaled(QSize(self.width, self.height))
        self.palette = QPalette()
        self.palette.setBrush(10, QBrush(sImage))
        self.setPalette(self.palette)
        
        ############################################################################## QLABELS ###########################################################################
        self.title = QLabel('Digital Streaming')
        self.title.setStyleSheet('font-size:{0}px; font-weight:bold; text-align: center; color:black; border-style:none;'.format(int(height / 23)))
        self.title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.title.setFont(QFont("Times"))

        self.empty_logo = QLabel()
        self.empty_logo.setFixedSize(int(width / 32), int(height / 16.5))

        self.company_logo = QLabel()
        self.company_logo.setFixedSize(int(width / 22.5), int(height / 15.5))
        self.company_logo_img = QPixmap(self.folder_path + '/imgs/company-logo.png')
        self.company_logo.setPixmap(self.company_logo_img)
        self.company_logo.setScaledContents(1)


        ############################################################################## TABS ###########################################################################

        #self.main_layout = QTabWidget()
        #self.main_layout.setFixedSize(int(self.width/1.01), int(self.height/1.2))

        self.camOne = QLabel()
        self.camOne.setMouseTracking(True)
        self.camOne.mousePressEvent = self.getFullScreen
        self.camOne.setStyleSheet("background-color:black; border-width:3px; border-style:solid; border-color:#0c7b93;")
        self.camOne.setFixedSize((int(self.width/3.1)), int(self.height/3.9))
        self.camOneTitle = QLabel(" Camera 1")
        self.camOneTitle.setStyleSheet("font-size:{0}px; font-weight:bold; color:black;".format(int(height / 56)))
        self.camOneThread = CamThread(width=int(self.width /3.1), height=int(self.height /3.9), cam_name='CamOne')

        self.camTwo = QLabel()
        self.camTwo.setMouseTracking(True)
        self.camTwo.mousePressEvent = self.getFullScreen
        self.camTwo.setStyleSheet("background-color:black; border-width:3px; border-style:solid; border-color:#0c7b93;")
        self.camTwo.setFixedSize((int(self.width/3.1)), int(self.height/3.9))
        self.camTwoTitle = QLabel(" Camera 2")
        self.camTwoTitle.setStyleSheet("font-size:{0}px; font-weight:bold; color:black;".format(int(height / 56)))
        self.camTwoThread = CamThread(width=int(self.width /3.1), height=int(self.height /3.9), cam_name='CamTwo')

        self.camThree = QLabel()
        self.camThree.setMouseTracking(True)
        self.camThree.mousePressEvent = self.getFullScreen
        self.camThree.setStyleSheet("background-color:black; border-width:3px; border-style:solid; border-color:#0c7b93;")
        self.camThree.setFixedSize((int(self.width/3.1)), int(self.height/3.9))
        self.camThreeTitle = QLabel(" Camera 3")
        self.camThreeTitle.setStyleSheet("font-size:{0}px; font-weight:bold; color:black;".format(int(height / 56)))
        self.camThreeThread = CamThread(width=int(self.width /3.1), height=int(self.height /3.9), cam_name='CamThree')

        self.camFour = QLabel()
        self.camFour.setMouseTracking(True)
        self.camFour.mousePressEvent = self.getFullScreen
        self.camFour.setStyleSheet("background-color:black; border-width:3px; border-style:solid; border-color:#0c7b93;")
        self.camFour.setFixedSize((int(self.width/3.1)), int(self.height/3.9))
        self.camFourTitle = QLabel(" Camera 4")
        self.camFourTitle.setStyleSheet("font-size:{0}px; font-weight:bold; color:black;".format(int(height / 56)))
        self.camFourThread = CamThread(width=int(self.width /3.1), height=int(self.height /3.9), cam_name='CamFour')

        self.camFive = QLabel()
        self.camFive.setMouseTracking(True)
        self.camFive.mousePressEvent = self.getFullScreen
        self.camFive.setStyleSheet("background-color:black; border-width:3px; border-style:solid; border-color:#0c7b93;")
        self.camFive.setFixedSize((int(self.width/3.1)), int(self.height/3.9))
        self.camFiveTitle = QLabel(" Camera 5")
        self.camFiveTitle.setStyleSheet("font-size:{0}px; font-weight:bold; color:black;".format(int(height / 56)))
        self.camFiveThread = CamThread(width=int(self.width /3.1), height=int(self.height /3.9), cam_name='CamFive')

        self.camSix = QLabel()
        self.camSix.setMouseTracking(True)
        self.camSix.mousePressEvent = self.getFullScreen
        self.camSix.setStyleSheet("background-color:black; border-width:3px; border-style:solid; border-color:#0c7b93;")
        self.camSix.setFixedSize((int(self.width/3.1)), int(self.height/3.9))
        self.camSixTitle = QLabel(" Camera 6")
        self.camSixTitle.setStyleSheet("font-size:{0}px; font-weight:bold; color:black;".format(int(height / 56)))
        self.camSixThread = CamThread(width=int(self.width /3.1), height=int(self.height /3.9), cam_name='CamSix')

        self.camSeven = QLabel()
        self.camSeven.setMouseTracking(True)
        self.camSeven.mousePressEvent = self.getFullScreen
        self.camSeven.setStyleSheet("background-color:black; border-width:3px; border-style:solid; border-color:#0c7b93;")
        self.camSeven.setFixedSize((int(self.width/3.1)), int(self.height/3.9))
        self.camSevenTitle = QLabel(" Camera 7")
        self.camSevenTitle.setStyleSheet("font-size:{0}px; font-weight:bold; color:black;".format(int(height / 56)))
        self.camSevenThread = CamThread(width=int(self.width /3.1), height=int(self.height /3.9), cam_name='CamSeven')

        self.camEight = QLabel()
        self.camEight.setMouseTracking(True)
        self.camEight.mousePressEvent = self.getFullScreen
        self.camEight.setStyleSheet("background-color:black; border-width:3px; border-style:solid; border-color:#0c7b93;")
        self.camEight.setFixedSize((int(self.width/3.1)), int(self.height/3.9))
        self.camEightTitle = QLabel(" Camera 8")
        self.camEightTitle.setStyleSheet("font-size:{0}px; font-weight:bold; color:black;".format(int(height / 56)))
        self.camEightThread = CamThread(width=int(self.width /3.1), height=int(self.height /3.9), cam_name='CamEight')

        self.camNine = QLabel()
        self.camNine.setMouseTracking(True)
        self.camNine.mousePressEvent = self.getFullScreen
        self.camNine.setStyleSheet("background-color:black; border-width:3px; border-style:solid; border-color:#0c7b93;")
        self.camNine.setFixedSize((int(self.width/3.1)), int(self.height/3.9))
        self.camNineTitle = QLabel(" Camera 9")
        self.camNineTitle.setStyleSheet("font-size:{0}px; font-weight:bold; color:black;".format(int(height / 56)))
        self.camNineThread = CamThread(width=int(self.width /3.1), height=int(self.height /3.9), cam_name='CamNine')

        #self.camWidget = QWidget()
        #self.camWidget.setLayout(self.camOne)

        
        self.pathimage = str(self.folder_path + "/imgs/back3.jpg")
        print(self.pathimage)

        self.Status_Bar = QStatusBar()
        self.setStatusBar(self.Status_Bar)

        self.Four = QPushButton("Four Windows")
        self.Four.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.Four.setStyleSheet("QPushButton{color:white; background-color:#0f4c75; font-size:17px; font-weight:bold; border-radius:5px; border:2px solid black;}\
                                                     QPushButton:hover{background-color:#3282b8;}\
                                                         QPushButton:pressed{font-size:18px;}")

        self.Nine = QPushButton("Nine Windows")
        self.Nine.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.Nine.setStyleSheet("QPushButton{color:white; background-color:#0f4c75; font-size:17px; font-weight:bold; border-radius:5px; border:2px solid black;}\
                                                     QPushButton:hover{background-color:#3282b8;}\
                                                         QPushButton:pressed{font-size:18px;}")

        self.empty = QLabel()
        self.empty.setFixedSize(int(width / 2.5), int(height / 36.0))

        

        self.close_Btn = QPushButton("Logout")
        self.close_Btn.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.close_Btn.setStyleSheet("QPushButton{color:white; background-color:#0f4c75; font-size:17px; font-weight:bold; border-radius:5px; border:2px solid black;}\
                                                     QPushButton:hover{background-color:#3282b8;}\
                                                         QPushButton:pressed{font-size:18px;}")


        self.close_Btn.clicked.connect(self.exit_trap)
        self.Four.clicked.connect(self.goToFour)

        self.Four.setDisabled(True)
        self.Nine.setDisabled(True)
        self.close_Btn.setDisabled(True)
        QTimer.singleShot(15000, self.EnableButton)

        ############################################################################## LAYOUTS ###########################################################################

##        self.Camera12Layout = QHBoxLayout()
##        self.Camera12Layout.addStretch(0)
##        self.Camera12Layout.addWidget(self.camOneTitle)
##        self.Camera12Layout.addSpacing(700)
##        self.Camera12Layout.addWidget(self.camTwoTitle)
##        self.Camera12Layout.addSpacing(500)
##        self.Camera12Widget = QWidget()
##        self.Camera12Widget.setLayout(self.Camera12Layout)
##
##        self.Camera34Layout = QHBoxLayout()
##        self.Camera34Layout.addStretch(0)
##        self.Camera34Layout.addWidget(self.camThreeTitle)
##        self.Camera34Layout.addSpacing(700)
##        self.Camera34Layout.addWidget(self.camFourTitle)
##        self.Camera34Layout.addSpacing(500)
##        self.Camera34Widget = QWidget()
##        self.Camera34Widget.setLayout(self.Camera34Layout)

        self.Cam123Layout = QHBoxLayout()
        self.Cam123Layout.addStretch(0)
        self.Cam123Layout.addWidget(self.camOne)
        self.Cam123Layout.addWidget(self.camTwo)
        self.Cam123Layout.addWidget(self.camThree)
        #self.Cam123Layout.addSpacing(200)
        self.Cam123Widget = QWidget()
        self.Cam123Widget.setLayout(self.Cam123Layout)

        self.Cam456Layout = QHBoxLayout()
        self.Cam456Layout.addStretch(0)
        self.Cam456Layout.addWidget(self.camFour)
        self.Cam456Layout.addWidget(self.camFive)
        self.Cam456Layout.addWidget(self.camSix)
        #self.Cam456Layout.addSpacing(200)
        self.Cam456Widget = QWidget()
        self.Cam456Widget.setLayout(self.Cam456Layout)

        self.Cam789Layout = QHBoxLayout()
        self.Cam789Layout.addStretch(0)
        self.Cam789Layout.addWidget(self.camSeven)
        self.Cam789Layout.addWidget(self.camEight)
        self.Cam789Layout.addWidget(self.camNine)
        #self.Cam789Layout.addSpacing(200)
        self.Cam789Widget = QWidget()
        self.Cam789Widget.setLayout(self.Cam789Layout)



        self.LoginBtnLayout = QHBoxLayout()
        self.LoginBtnLayout.addStretch(0)
        self.LoginBtnLayout.addWidget(self.Four)
        self.LoginBtnLayout.addWidget(self.Nine)
        self.LoginBtnLayout.addWidget(self.empty)
        self.LoginBtnLayout.addWidget(self.close_Btn)
        self.LoginBtnLayout.addSpacing(200)
        self.LoginBtnWidget = QWidget()
        self.LoginBtnWidget.setLayout(self.LoginBtnLayout)

        
        self.titleLayout = QHBoxLayout()
        self.titleLayout.addWidget(self.empty_logo)
        self.titleLayout.addWidget(self.title)
        self.titleLayout.addWidget(self.company_logo)
        self.titleLayout.setAlignment(self.company_logo, Qt.AlignVCenter)
        self.titleWidget = QWidget()
        self.titleWidget.setLayout(self.titleLayout)
        self.titleWidget.setPalette(self.palette)
        self.titleWidget.setStyleSheet('border-style:None; border-radius:12px;')
        self.titleWidget.setFixedSize(width - int(width / 95), int(height / 13.5))

        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.titleWidget)
        self.mainlayout.addWidget(self.Cam123Widget)
        self.mainlayout.addWidget(self.Cam456Widget)
        self.mainlayout.addWidget(self.Cam789Widget)
        self.mainlayout.addWidget(self.LoginBtnWidget)

        
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainlayout)

        self.setCentralWidget(self.mainWidget)
        
        self.camOneThread.start()
        self.camOneThread.changePixmap.connect(self.setCamOneImage)

        self.camTwoThread.start()
        self.camTwoThread.changePixmap.connect(self.setCamTwoImage)

        self.camThreeThread.start()
        self.camThreeThread.changePixmap.connect(self.setCamThreeImage)

        self.camFourThread.start()
        self.camFourThread.changePixmap.connect(self.setCamFourImage)

        self.camFiveThread.start()
        self.camFiveThread.changePixmap.connect(self.setCamFiveImage)

        self.camSixThread.start()
        self.camSixThread.changePixmap.connect(self.setCamSixImage)

        self.camSevenThread.start()
        self.camSevenThread.changePixmap.connect(self.setCamSevenImage)

        self.camEightThread.start()
        self.camEightThread.changePixmap.connect(self.setCamEightImage)

        self.camNineThread.start()
        self.camNineThread.changePixmap.connect(self.setCamNineImage)

    @pyqtSlot(QImage)
    def setCamOneImage(self, image):
        self.camOne.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(QImage)
    def setCamTwoImage(self, image):
        self.camTwo.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(QImage)
    def setCamThreeImage(self, image):
        self.camThree.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(QImage)
    def setCamFourImage(self, image):
        self.camFour.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(QImage)
    def setCamFiveImage(self, image):
        self.camFive.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(QImage)
    def setCamSixImage(self, image):
        self.camSix.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(QImage)
    def setCamSevenImage(self, image):
        self.camSeven.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(QImage)
    def setCamEightImage(self, image):
        self.camEight.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(QImage)
    def setCamNineImage(self, image):
        self.camNine.setPixmap(QPixmap.fromImage(image))

    def EnableButton(self):
        self.Four.setDisabled(False)
        self.close_Btn.setDisabled(False)

    def getFullScreen(self,event):
        self.camOneThread.Flag_Cam = True
        self.camTwoThread.Flag_Cam = True
        self.camThreeThread.Flag_Cam = True
        self.camFourThread.Flag_Cam = True
        self.camFiveThread.Flag_Cam = True
        self.camSixThread.Flag_Cam = True
        self.camSevenThread.Flag_Cam = True
        self.camEightThread.Flag_Cam = True
        self.camNineThread.Flag_Cam = True
        
        self.Full_Screen = Full_Screen(self.width, self.height, self, self.folder_path, "Nine")
        self.Full_Screen.show()   
        self.close()

    def goToFour(self):
        #self.Screen_9 = Screen_9(self.width, self.height, self, self.folder_path)

        self.camOneThread.Flag_Cam = True
        self.camTwoThread.Flag_Cam = True
        self.camThreeThread.Flag_Cam = True
        self.camFourThread.Flag_Cam = True
        self.camFiveThread.Flag_Cam = True
        self.camSixThread.Flag_Cam = True
        self.camSevenThread.Flag_Cam = True
        self.camEightThread.Flag_Cam = True
        self.camNineThread.Flag_Cam = True

        self.parent.Four.setDisabled(True)
        self.parent.Nine.setDisabled(True)
        self.parent.close_Btn.setDisabled(True)
        QTimer.singleShot(8000, self.parent.EnableButton)

        self.parent.camOneThread.start()
        self.parent.camTwoThread.start()
        self.parent.camThreeThread.start()
        self.parent.camFourThread.start()

        #print(self.parent.camOneThread.Flag_cap)

        
        self.parent.show()   
        self.close()


    def exit_trap(self):
        self.camOneThread.Flag_Cam = True
        self.camTwoThread.Flag_Cam = True
        self.camThreeThread.Flag_Cam = True
        self.camFourThread.Flag_Cam = True
        self.camFiveThread.Flag_Cam = True
        self.camSixThread.Flag_Cam = True
        self.camSevenThread.Flag_Cam = True
        self.camEightThread.Flag_Cam = True
        self.camNineThread.Flag_Cam = True
        
        self.parent.parent.show()
        self.close()

    

if __name__ == '__main__':
    app = QApplication(sys.argv)

    V = app.desktop().screenGeometry()
    width = V.width()
    height = V.height()
    main = MainWindow(width, height)
    main.show()

    sys.exit(app.exec_())
