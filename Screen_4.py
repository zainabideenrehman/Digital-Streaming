from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
from os import path

from CamThread import CamThread
from Full_Screen import MainWindow as Full_Screen
from Screen_9 import MainWindow as Screen_9

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
        self.camOne.setFixedSize((int(self.width/2.5)), int(self.height/2.7))
        self.camOneTitle = QLabel(" Camera 1")
        self.camOneTitle.setStyleSheet("font-size:{0}px; font-weight:bold; color:black;".format(int(height / 56)))
        self.camOneThread = CamThread(width=int(self.width /2.5), height=int(self.height /2.7), cam_name='CamOne')

        self.camTwo = QLabel()
        self.camTwo.setMouseTracking(True)
        self.camTwo.mousePressEvent = self.getFullScreen
        self.camTwo.setStyleSheet("background-color:black; border-width:3px; border-style:solid; border-color:#0c7b93;")
        self.camTwo.setFixedSize((int(self.width/2.5)), int(self.height/2.7))
        self.camTwoTitle = QLabel(" Camera 2")
        self.camTwoTitle.setStyleSheet("font-size:{0}px; font-weight:bold; color:black;".format(int(height / 56)))
        self.camTwoThread = CamThread(width=int(self.width /2.5), height=int(self.height /2.7), cam_name='CamOne')

        self.camThree = QLabel()
        self.camThree.setMouseTracking(True)
        self.camThree.mousePressEvent = self.getFullScreen
        self.camThree.setStyleSheet("background-color:black; border-width:3px; border-style:solid; border-color:#0c7b93;")
        self.camThree.setFixedSize((int(self.width/2.5)), int(self.height/2.7))
        self.camThreeTitle = QLabel(" Camera 3")
        self.camThreeTitle.setStyleSheet("font-size:{0}px; font-weight:bold; color:black;".format(int(height / 56)))
        self.camThreeThread = CamThread(width=int(self.width /2.5), height=int(self.height /2.7), cam_name='CamOne')

        self.camFour = QLabel()
        self.camFour.setMouseTracking(True)
        self.camFour.mousePressEvent = self.getFullScreen
        self.camFour.setStyleSheet("background-color:black; border-width:3px; border-style:solid; border-color:#0c7b93;")
        self.camFour.setFixedSize((int(self.width/2.5)), int(self.height/2.7))
        self.camFourTitle = QLabel(" Camera 4")
        self.camFourTitle.setStyleSheet("font-size:{0}px; font-weight:bold; color:black;".format(int(height / 56)))
        self.camFourThread = CamThread(width=int(self.width /2.5), height=int(self.height /2.7), cam_name='CamOne')

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
        self.Nine.clicked.connect(self.goToNine)


        self.Four.setDisabled(True)
        self.Nine.setDisabled(True)
        self.close_Btn.setDisabled(True)
        QTimer.singleShot(8000, self.EnableButton)

        ############################################################################## LAYOUTS ###########################################################################

        self.Camera12Layout = QHBoxLayout()
        self.Camera12Layout.addStretch(0)
        self.Camera12Layout.addWidget(self.camOneTitle)
        self.Camera12Layout.addSpacing(700)
        self.Camera12Layout.addWidget(self.camTwoTitle)
        self.Camera12Layout.addSpacing(500)
        self.Camera12Widget = QWidget()
        self.Camera12Widget.setLayout(self.Camera12Layout)

        self.Camera34Layout = QHBoxLayout()
        self.Camera34Layout.addStretch(0)
        self.Camera34Layout.addWidget(self.camThreeTitle)
        self.Camera34Layout.addSpacing(700)
        self.Camera34Layout.addWidget(self.camFourTitle)
        self.Camera34Layout.addSpacing(500)
        self.Camera34Widget = QWidget()
        self.Camera34Widget.setLayout(self.Camera34Layout)

        self.Cam12Layout = QHBoxLayout()
        self.Cam12Layout.addStretch(0)
        self.Cam12Layout.addWidget(self.camOne)
        self.Cam12Layout.addWidget(self.camTwo)
        self.Cam12Layout.addSpacing(200)
        self.Cam12Widget = QWidget()
        self.Cam12Widget.setLayout(self.Cam12Layout)

        self.Cam34Layout = QHBoxLayout()
        self.Cam34Layout.addStretch(0)
        self.Cam34Layout.addWidget(self.camThree)
        self.Cam34Layout.addWidget(self.camFour)
        self.Cam34Layout.addSpacing(200)
        self.Cam34Widget = QWidget()
        self.Cam34Widget.setLayout(self.Cam34Layout)



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
        self.mainlayout.addWidget(self.Camera12Widget)
        self.mainlayout.addWidget(self.Cam12Widget)
        self.mainlayout.addWidget(self.Camera34Widget)
        self.mainlayout.addWidget(self.Cam34Widget)
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

    def EnableButton(self):
        self.Nine.setDisabled(False)
        self.close_Btn.setDisabled(False)
        

    def getFullScreen(self,event):
        self.camOneThread.Flag_Cam = True
        self.camTwoThread.Flag_Cam = True
        self.camThreeThread.Flag_Cam = True
        self.camFourThread.Flag_Cam = True
        self.Full_Screen = Full_Screen(self.width, self.height, self, self.folder_path, "Four")
        self.Full_Screen.show()   
        self.close()

    def goToNine(self):
        self.camOneThread.Flag_Cam = True
        self.camTwoThread.Flag_Cam = True
        self.camThreeThread.Flag_Cam = True
        self.camFourThread.Flag_Cam = True
        self.Screen_9 = Screen_9(self.width, self.height, self, self.folder_path)
        self.Screen_9.show()   
        self.close()


    def exit_trap(self):
        self.camOneThread.Flag_Cam = True
        self.camTwoThread.Flag_Cam = True
        self.camThreeThread.Flag_Cam = True
        self.camFourThread.Flag_Cam = True
        
        self.parent.show()
        self.close()

    

if __name__ == '__main__':
    app = QApplication(sys.argv)

    V = app.desktop().screenGeometry()
    width = V.width()
    height = V.height()
    main = MainWindow(width, height)
    main.show()

    sys.exit(app.exec_())
