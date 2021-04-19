from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
from os import path

from CamThread import CamThread
#from Screen_4 import MainWindow as Screen_4

class MainWindow(QMainWindow):
    def __init__(self, width, height,parent, folder_path, FourOrNine):
        super().__init__()

        self.parent=parent
        self.FourOrNine = FourOrNine
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
        #self.camOne.setMouseTracking(True)
        #self.camOne.mousePressEvent = self.getPos1
        self.camOne.setStyleSheet("background-color:black; border-width:3px; border-style:solid; border-color:#0c7b93;")
        self.camOne.setFixedSize((int(self.width/1.01)), int(self.height/1.2))

        self.camOneTitle = QLabel("                                                                                                                                             Camera 1")
        self.camOneTitle.setStyleSheet("font-size:{0}px; text-align: center; font-weight:bold; color:black;".format(int(height / 56)))

        self.camOneThread = CamThread(width=int(self.width /1.01), height=int(self.height /1.2), cam_name='CamOne')

        #self.camWidget = QWidget()
        #self.camWidget.setLayout(self.camOne)

        
        self.pathimage = str(self.folder_path + "/imgs/back3.jpg")
        print(self.pathimage)

        self.Status_Bar = QStatusBar()
        self.setStatusBar(self.Status_Bar)

##        self.Four = QPushButton("Four Windows")
##        self.Four.setFixedSize(int(width / 9.5), int(height / 36.0))
##        self.Four.setStyleSheet("QPushButton{color:white; background-color:#0f4c75; font-size:17px; font-weight:bold; border-radius:5px; border:2px solid black;}\
##                                                     QPushButton:hover{background-color:#3282b8;}\
##                                                         QPushButton:pressed{font-size:18px;}")
##
##        self.Nine = QPushButton("Nine Windows")
##        self.Nine.setFixedSize(int(width / 9.5), int(height / 36.0))
##        self.Nine.setStyleSheet("QPushButton{color:white; background-color:#0f4c75; font-size:17px; font-weight:bold; border-radius:5px; border:2px solid black;}\
##                                                     QPushButton:hover{background-color:#3282b8;}\
##                                                         QPushButton:pressed{font-size:18px;}")

        self.empty = QLabel()
        self.empty.setFixedSize(int(width / 2.5), int(height / 36.0))

        self.Four = QLabel()
        self.Four.setFixedSize(int(width / 9.5), int(height / 36.0))

        self.Nine = QLabel()
        self.Nine.setFixedSize(int(width / 9.5), int(height / 36.0))

        

        self.close_Btn = QPushButton("Back")
        self.close_Btn.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.close_Btn.setStyleSheet("QPushButton{color:white; background-color:#0f4c75; font-size:17px; font-weight:bold; border-radius:5px; border:2px solid black;}\
                                                     QPushButton:hover{background-color:#3282b8;}\
                                                         QPushButton:pressed{font-size:18px;}")


        self.close_Btn.clicked.connect(self.exit_trap)
        #self.Four.clicked.connect(self.goToFour)
        #self.Nine.clicked.connect(self.goToNine)

        self.close_Btn.setDisabled(True)
        QTimer.singleShot(5000, self.EnableButton)

        ############################################################################## LAYOUTS ###########################################################################

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
        self.mainlayout.addWidget(self.camOneTitle)
        self.mainlayout.addWidget(self.camOne)
        self.mainlayout.addWidget(self.LoginBtnWidget)

        
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainlayout)

        self.setCentralWidget(self.mainWidget)
        self.camOneThread.start()
        self.camOneThread.changePixmap.connect(self.setCamOneImage)

    @pyqtSlot(QImage)
    def setCamOneImage(self, image):
        self.camOne.setPixmap(QPixmap.fromImage(image))

    def goToFour(self):
        #self.Screen_4 = Screen_4(self.width, self.height, self, self.folder_path)
        self.parent.show()   
        self.close()

    def goToNine(self):
        #self.Screen_4 = Screen_4(self.width, self.height, self, self.folder_path)
        self.parent.show()   
        self.close()

    def EnableButton(self):
        self.close_Btn.setDisabled(False)

    def exit_trap(self):
        self.camOneThread.Flag_Cam = True
        self.parent.Four.setDisabled(True)
        self.parent.Nine.setDisabled(True)
        self.parent.close_Btn.setDisabled(True)
        

        if self.FourOrNine == "Four":
            self.parent.camOneThread.start()
            self.parent.camTwoThread.start()
            self.parent.camThreeThread.start()
            self.parent.camFourThread.start()
            QTimer.singleShot(8000, self.parent.EnableButton)
        elif self.FourOrNine == "Nine":
            self.parent.camOneThread.start()
            self.parent.camTwoThread.start()
            self.parent.camThreeThread.start()
            self.parent.camFourThread.start()
            self.parent.camFiveThread.start()
            self.parent.camSixThread.start()
            self.parent.camSevenThread.start()
            self.parent.camEightThread.start()
            self.parent.camNineThread.start()
            QTimer.singleShot(15000, self.parent.EnableButton)
            
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
