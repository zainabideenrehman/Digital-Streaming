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

        Camera_File = open(str(self.folder_path) + "./Files/Camera_IPs.txt", "r+")

        Camera_File.seek(0)

        lines = Camera_File.readlines()

        self.cam1_url = lines[0].strip()
        self.cam1_url = self.cam1_url.split(" ")
        self.cam1_url = self.cam1_url[1]

        self.cam2_url = lines[1].strip()
        self.cam2_url = self.cam2_url.split(" ")
        self.cam2_url = self.cam2_url[1]

        self.cam3_url = lines[2].strip()
        self.cam3_url = self.cam3_url.split(" ")
        self.cam3_url = self.cam3_url[1]

        self.cam4_url = lines[3].strip()
        self.cam4_url = self.cam4_url.split(" ")
        self.cam4_url = self.cam4_url[1]

        self.cam5_url = lines[4].strip()
        self.cam5_url = self.cam5_url.split(" ")
        self.cam5_url = self.cam5_url[1]

        self.cam6_url = lines[5].strip()
        self.cam6_url = self.cam6_url.split(" ")
        self.cam6_url = self.cam6_url[1]

        self.cam7_url = lines[6].strip()
        self.cam7_url = self.cam7_url.split(" ")
        self.cam7_url = self.cam7_url[1]

        self.cam8_url = lines[7].strip()
        self.cam8_url = self.cam8_url.split(" ")
        self.cam8_url = self.cam8_url[1]

        self.cam9_url = lines[8].strip()
        self.cam9_url = self.cam9_url.split(" ")
        self.cam9_url = self.cam9_url[1]

        self.Cam1_ID = QLabel("Camera 1")
        self.Cam1_ID.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.Cam1_ID.setAlignment(Qt.AlignLeft)
        self.Cam1_ID.setStyleSheet("QLabel{color:black; font-size:17px; font-weight:bold;}")

        self.Cam2_ID = QLabel("Camera 2")
        self.Cam2_ID.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.Cam2_ID.setAlignment(Qt.AlignLeft)
        self.Cam2_ID.setStyleSheet("QLabel{color:black; font-size:17px; font-weight:bold;}")

        self.Cam3_ID = QLabel("Camera 3")
        self.Cam3_ID.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.Cam3_ID.setAlignment(Qt.AlignLeft)
        self.Cam3_ID.setStyleSheet("QLabel{color:black; font-size:17px; font-weight:bold;}")

        self.Cam4_ID = QLabel("Camera 4")
        self.Cam4_ID.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.Cam4_ID.setAlignment(Qt.AlignLeft)
        self.Cam4_ID.setStyleSheet("QLabel{color:black; font-size:17px; font-weight:bold;}")

        self.Cam5_ID = QLabel("Camera 5")
        self.Cam5_ID.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.Cam5_ID.setAlignment(Qt.AlignLeft)
        self.Cam5_ID.setStyleSheet("QLabel{color:black; font-size:17px; font-weight:bold;}")

        self.Cam6_ID = QLabel("Camera 6")
        self.Cam6_ID.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.Cam6_ID.setAlignment(Qt.AlignLeft)
        self.Cam6_ID.setStyleSheet("QLabel{color:black; font-size:17px; font-weight:bold;}")

        self.Cam7_ID = QLabel("Camera 7")
        self.Cam7_ID.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.Cam7_ID.setAlignment(Qt.AlignLeft)
        self.Cam7_ID.setStyleSheet("QLabel{color:black; font-size:17px; font-weight:bold;}")

        self.Cam8_ID = QLabel("Camera 8")
        self.Cam8_ID.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.Cam8_ID.setAlignment(Qt.AlignLeft)
        self.Cam8_ID.setStyleSheet("QLabel{color:black; font-size:17px; font-weight:bold;}")

        self.Cam9_ID = QLabel("Camera 9")
        self.Cam9_ID.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.Cam9_ID.setAlignment(Qt.AlignLeft)
        self.Cam9_ID.setStyleSheet("QLabel{color:black; font-size:17px; font-weight:bold;}")

        self.linedit1 = QLineEdit()
        self.linedit1.setFixedSize(int(width / 3), int(height / 36.0))
        self.linedit1.setAlignment(Qt.AlignCenter)
        self.linedit1.setPlaceholderText("Camera 1 ip")
        self.linedit1.setStyleSheet("QLineEdit{color:#000e14; font-size:15px; font-weight:light; border-radius:5px; border:2px solid black;}")

        self.linedit2 = QLineEdit()
        self.linedit2.setFixedSize(int(width / 3), int(height / 36.0))
        self.linedit2.setAlignment(Qt.AlignCenter)
        self.linedit2.setPlaceholderText("Camera 2 ip")
        #self.linedit2.setEchoMode(QLineEdit.Password)
        self.linedit2.setStyleSheet("QLineEdit{color:#000e14; font-size:15px; font-weight:light; border-radius:5px; border:2px solid black;}")

        self.linedit3 = QLineEdit()
        self.linedit3.setFixedSize(int(width / 3), int(height / 36.0))
        self.linedit3.setAlignment(Qt.AlignCenter)
        self.linedit3.setPlaceholderText("Camera 3 ip")
        self.linedit3.setStyleSheet("QLineEdit{color:#000e14; font-size:15px; font-weight:light; border-radius:5px; border:2px solid black;}")

        self.linedit4 = QLineEdit()
        self.linedit4.setFixedSize(int(width / 3), int(height / 36.0))
        self.linedit4.setAlignment(Qt.AlignCenter)
        self.linedit4.setPlaceholderText("Camera 4 ip")
        #self.linedit4.setEchoMode(QLineEdit.Password)
        self.linedit4.setStyleSheet("QLineEdit{color:#000e14; font-size:15px; font-weight:light; border-radius:5px; border:2px solid black;}")

        self.linedit5 = QLineEdit()
        self.linedit5.setFixedSize(int(width / 3), int(height / 36.0))
        self.linedit5.setAlignment(Qt.AlignCenter)
        self.linedit5.setPlaceholderText("Camera 5 ip")
        self.linedit5.setStyleSheet("QLineEdit{color:#000e14; font-size:15px; font-weight:light; border-radius:5px; border:2px solid black;}")

        self.linedit6 = QLineEdit()
        self.linedit6.setFixedSize(int(width / 3), int(height / 36.0))
        self.linedit6.setAlignment(Qt.AlignCenter)
        self.linedit6.setPlaceholderText("Camera 6 ip")
        #self.linedit6.setEchoMode(QLineEdit.Password)
        self.linedit6.setStyleSheet("QLineEdit{color:#000e14; font-size:15px; font-weight:light; border-radius:5px; border:2px solid black;}")

        self.linedit7 = QLineEdit()
        self.linedit7.setFixedSize(int(width / 3), int(height / 36.0))
        self.linedit7.setAlignment(Qt.AlignCenter)
        self.linedit7.setPlaceholderText("Camera 7 ip")
        self.linedit7.setStyleSheet("QLineEdit{color:#000e14; font-size:15px; font-weight:light; border-radius:5px; border:2px solid black;}")

        self.linedit8 = QLineEdit()
        self.linedit8.setFixedSize(int(width / 3), int(height / 36.0))
        self.linedit8.setAlignment(Qt.AlignCenter)
        self.linedit8.setPlaceholderText("Camera 8 ip")
        #self.linedit8.setEchoMode(QLineEdit.Password)
        self.linedit8.setStyleSheet("QLineEdit{color:#000e14; font-size:15px; font-weight:light; border-radius:5px; border:2px solid black;}")

        self.linedit9 = QLineEdit()
        self.linedit9.setFixedSize(int(width / 3), int(height / 36.0))
        self.linedit9.setAlignment(Qt.AlignCenter)
        self.linedit9.setPlaceholderText("Camera 9 ip")
        self.linedit9.setStyleSheet("QLineEdit{color:#000e14; font-size:15px; font-weight:light; border-radius:5px; border:2px solid black;}")

        self.linedit1.setText(self.cam1_url)
        self.linedit2.setText(self.cam2_url)
        self.linedit3.setText(self.cam3_url)
        self.linedit4.setText(self.cam4_url)
        self.linedit5.setText(self.cam5_url)
        self.linedit6.setText(self.cam6_url)
        self.linedit7.setText(self.cam7_url)
        self.linedit8.setText(self.cam8_url)
        self.linedit9.setText(self.cam9_url)


        self.Cam1_Layout = QHBoxLayout()
        self.Cam1_Layout.addStretch(0)
        self.Cam1_Layout.addWidget(self.Cam1_ID)
        self.Cam1_Layout.addWidget(self.linedit1)
        self.Cam1_Layout.addSpacing(1000)
        self.Cam1_Widget = QWidget()
        self.Cam1_Widget.setLayout(self.Cam1_Layout)

        self.Cam2_Layout = QHBoxLayout()
        self.Cam2_Layout.addStretch(0)
        self.Cam2_Layout.addWidget(self.Cam2_ID)
        self.Cam2_Layout.addWidget(self.linedit2)
        self.Cam2_Layout.addSpacing(1000)
        self.Cam2_Widget = QWidget()
        self.Cam2_Widget.setLayout(self.Cam2_Layout)

        self.Cam3_Layout = QHBoxLayout()
        self.Cam3_Layout.addStretch(0)
        self.Cam3_Layout.addWidget(self.Cam3_ID)
        self.Cam3_Layout.addWidget(self.linedit3)
        self.Cam3_Layout.addSpacing(1000)
        self.Cam3_Widget = QWidget()
        self.Cam3_Widget.setLayout(self.Cam3_Layout)

        self.Cam4_Layout = QHBoxLayout()
        self.Cam4_Layout.addStretch(0)
        self.Cam4_Layout.addWidget(self.Cam4_ID)
        self.Cam4_Layout.addWidget(self.linedit4)
        self.Cam4_Layout.addSpacing(1000)
        self.Cam4_Widget = QWidget()
        self.Cam4_Widget.setLayout(self.Cam4_Layout)

        self.Cam5_Layout = QHBoxLayout()
        self.Cam5_Layout.addStretch(0)
        self.Cam5_Layout.addWidget(self.Cam5_ID)
        self.Cam5_Layout.addWidget(self.linedit5)
        self.Cam5_Layout.addSpacing(1000)
        self.Cam5_Widget = QWidget()
        self.Cam5_Widget.setLayout(self.Cam5_Layout)

        self.Cam6_Layout = QHBoxLayout()
        self.Cam6_Layout.addStretch(0)
        self.Cam6_Layout.addWidget(self.Cam6_ID)
        self.Cam6_Layout.addWidget(self.linedit6)
        self.Cam6_Layout.addSpacing(1000)
        self.Cam6_Widget = QWidget()
        self.Cam6_Widget.setLayout(self.Cam6_Layout)

        self.Cam7_Layout = QHBoxLayout()
        self.Cam7_Layout.addStretch(0)
        self.Cam7_Layout.addWidget(self.Cam7_ID)
        self.Cam7_Layout.addWidget(self.linedit7)
        self.Cam7_Layout.addSpacing(1000)
        self.Cam7_Widget = QWidget()
        self.Cam7_Widget.setLayout(self.Cam7_Layout)

        self.Cam8_Layout = QHBoxLayout()
        self.Cam8_Layout.addStretch(0)
        self.Cam8_Layout.addWidget(self.Cam8_ID)
        self.Cam8_Layout.addWidget(self.linedit8)
        self.Cam8_Layout.addSpacing(1000)
        self.Cam8_Widget = QWidget()
        self.Cam8_Widget.setLayout(self.Cam8_Layout)

        self.Cam9_Layout = QHBoxLayout()
        self.Cam9_Layout.addStretch(0)
        self.Cam9_Layout.addWidget(self.Cam9_ID)
        self.Cam9_Layout.addWidget(self.linedit9)
        self.Cam9_Layout.addSpacing(1000)
        self.Cam9_Widget = QWidget()
        self.Cam9_Widget.setLayout(self.Cam9_Layout)


        
        self.pathimage = str(self.folder_path + "/imgs/back3.jpg")
        print(self.pathimage)

        self.Status_Bar = QStatusBar()
        self.setStatusBar(self.Status_Bar)

        self.empty = QLabel()
        self.empty.setFixedSize(int(width / 2.5), int(height / 36.0))

        

        self.Save_File_btn = QPushButton("Save")
        self.Save_File_btn.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.Save_File_btn.setStyleSheet("QPushButton{color:white; background-color:#0f4c75; font-size:17px; font-weight:bold; border-radius:5px; border:2px solid black;}\
                                                     QPushButton:hover{background-color:#3282b8;}\
                                                         QPushButton:pressed{font-size:18px;}")
        
        self.close_Btn = QPushButton("Logout")
        self.close_Btn.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.close_Btn.setStyleSheet("QPushButton{color:white; background-color:#0f4c75; font-size:17px; font-weight:bold; border-radius:5px; border:2px solid black;}\
                                                     QPushButton:hover{background-color:#3282b8;}\
                                                         QPushButton:pressed{font-size:18px;}")


        self.close_Btn.clicked.connect(self.exit_trap)
        self.Save_File_btn.clicked.connect(self.pushstring)

        ############################################################################## LAYOUTS ###########################################################################



        self.LoginBtnLayout = QHBoxLayout()
        self.LoginBtnLayout.addStretch(0)
        self.LoginBtnLayout.addWidget(self.Save_File_btn)
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
        self.mainlayout.addSpacing(100)
        self.mainlayout.addWidget(self.Cam1_Widget)
        self.mainlayout.addWidget(self.Cam2_Widget)
        self.mainlayout.addWidget(self.Cam3_Widget)
        self.mainlayout.addWidget(self.Cam4_Widget)
        self.mainlayout.addWidget(self.Cam5_Widget)
        self.mainlayout.addWidget(self.Cam6_Widget)
        self.mainlayout.addWidget(self.Cam7_Widget)
        self.mainlayout.addWidget(self.Cam8_Widget)
        self.mainlayout.addWidget(self.Cam9_Widget)
        self.mainlayout.addSpacing(300)
        self.mainlayout.addWidget(self.LoginBtnWidget)

        
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainlayout)

        self.setCentralWidget(self.mainWidget)

    def pushstring(self):
        Localization_File = open("./Files/Camera_IPs.txt", "w+")
        Localization_File.write("Camera_1" +" " +str(self.linedit1.text()))
        Localization_File.write("\n")
        Localization_File.write("Camera_2" +" " +str(self.linedit2.text()))
        Localization_File.write("\n")
        Localization_File.write("Camera_3" +" " +str(self.linedit3.text()))
        Localization_File.write("\n")
        Localization_File.write("Camera_4" +" " +str(self.linedit4.text()))
        Localization_File.write("\n")
        Localization_File.write("Camera_5" +" " +str(self.linedit5.text()))
        Localization_File.write("\n")
        Localization_File.write("Camera_6" +" " +str(self.linedit6.text()))
        Localization_File.write("\n")
        Localization_File.write("Camera_7" +" " +str(self.linedit7.text()))
        Localization_File.write("\n")
        Localization_File.write("Camera_8" +" " +str(self.linedit8.text()))
        Localization_File.write("\n")
        Localization_File.write("Camera_9" +" " +str(self.linedit9.text()))
        Localization_File.close()

                                
    def exit_trap(self):
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
