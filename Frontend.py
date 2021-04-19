from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import sqlite3
import os
import shutil
from Screen_4 import MainWindow as Screen_4


root = QFileInfo(__file__).absolutePath()

class MainWindow(QMainWindow):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.setWindowTitle("Project")
        self.setGeometry(0, 0, self.width, self.height)
        
        monitor = QDesktopWidget().screenGeometry(1)
        self.move(monitor.left(), monitor.top())


        self.showFullScreen()
        backImage = QImage(root + "/imgs/back35.jpg")
        sImage = backImage.scaled(QSize(self.width,self.height))
        self.palette = QPalette()
        self.palette.setBrush(10, QBrush(sImage))
        self.setPalette(self.palette)
        
        ######################################################## STATUS BAR ##########################################################################
        self.Status_Bar = QStatusBar()
        self.setStatusBar(self.Status_Bar)

        ######################################################### QLABELS ############################################################################
        self.title = QLabel('Digital Streaming\n ')
        self.title.setStyleSheet('font-size:48px; font-weight:bold; text-align: center; color:black; border-style:none;')
        self.title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.title.setFont(QFont("Times"))

        self.title2 = QLabel('Designed By:')
        self.title2.setStyleSheet('font-size:20px; font-weight:bold; text-align: center; color:black; border-style:none;')
        self.title2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.title2.setFont(QFont("Times"))

        self.empty_logo = QLabel()
        self.empty_logo.setFixedSize(200,250)

        
        self.company_logo = QLabel()
        self.company_logo.setFixedSize(250,200)
        self.company_logo_img = QPixmap(root + '/imgs/company-logo.png')
        self.company_logo.setPixmap(self.company_logo_img)
        self.company_logo.setScaledContents(1)

        self.Login_ID = QLabel("User Name")
        self.Login_ID.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.Login_ID.setAlignment(Qt.AlignLeft)
        self.Login_ID.setStyleSheet("QLabel{color:black; font-size:17px; font-weight:bold;}")

        self.Password = QLabel("Password")
        self.Password.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.Password.setAlignment(Qt.AlignLeft)
        self.Password.setStyleSheet("QLabel{color:black; font-size:17px; font-weight:bold;}")

        self.User_Function = QLabel("User Function")
        self.User_Function.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.User_Function.setAlignment(Qt.AlignLeft)
        self.User_Function.setStyleSheet("QLabel{color:black; font-size:17px; font-weight:bold;}")

        ######################################################## QCOMBOBOX(DROP-DOWN) ##########################################################################
        self.Function_Dropbox = QComboBox()
        self.Function_Dropbox.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.Function_Dropboxlist = ["Operations","Administrator"]
        self.Function_Dropbox.addItems(self.Function_Dropboxlist)
        self.Function_Dropbox.setStyleSheet("QComboBox{color:black; font-size:17px; font-weight:light; text-align: center; border-radius:5px; border:2px solid black;}\
                                            QComboBox:on {padding-left: 38px;}\
                                            QComboBox:!on{padding-left: 38px;}")

        ########################################################### QPUSHBUTTON ###############################################################################
        self.Login_Btn = QPushButton("Login")
        self.Login_Btn.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.Login_Btn.setStyleSheet("QPushButton{color:white; background-color:#0f4c75; font-size:17px; font-weight:bold; border-radius:5px; border:2px solid black;}\
                                                     QPushButton:hover{background-color:#3282b8;}\
                                                         QPushButton:pressed{font-size:18px;}")

        self.close_Btn = QPushButton("Close")
        self.close_Btn.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.close_Btn.setStyleSheet("QPushButton{color:white; background-color:#0f4c75; font-size:17px; font-weight:bold; border-radius:5px; border:2px solid black;}\
                                                     QPushButton:hover{background-color:#3282b8;}\
                                                         QPushButton:pressed{font-size:18px;}")



        ############################################################ QLINEDIT #################################################################################
        self.linedit1 = QLineEdit()
        self.linedit1.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.linedit1.setAlignment(Qt.AlignCenter)
        self.linedit1.setPlaceholderText("username")
        self.linedit1.setStyleSheet("QLineEdit{color:#000e14; font-size:15px; font-weight:light; border-radius:5px; border:2px solid black;}")

        self.linedit2 = QLineEdit()
        self.linedit2.setFixedSize(int(width / 9.5), int(height / 36.0))
        self.linedit2.setAlignment(Qt.AlignCenter)
        self.linedit2.setPlaceholderText("password")
        self.linedit2.setEchoMode(QLineEdit.Password)
        self.linedit2.setStyleSheet("QLineEdit{color:#000e14; font-size:15px; font-weight:light; border-radius:5px; border:2px solid black;}")

        self.Login_Btn.clicked.connect(self.Login_Selection)
        self.close_Btn.clicked.connect(self.closefunc)

        self.initUI(self.width, self.height) # Initialize the UI

    def initUI(self, width, height):

        ############################################################# LAYOUTS ################################################################################
        self.MainDetailsLayout = QHBoxLayout()
        self.MainDetailsLayout.addStretch(0)

        self.LoginDetailsLayout = QVBoxLayout()
        self.LoginDetailsLayout.addStretch(0)

        self.emptyLogoLayout = QHBoxLayout()
        self.emptyLogoLayout.addWidget(self.empty_logo)
        self.emptyLogoLayout.addSpacing(140)
        self.emptyLogoWidget = QWidget()
        self.emptyLogoWidget.setLayout(self.emptyLogoLayout)

        self.UsernameLayout = QHBoxLayout()
        self.UsernameLayout.addStretch(0)
        self.UsernameLayout.addWidget(self.Login_ID)
        self.UsernameLayout.addWidget(self.linedit1)
        self.UsernameLayout.addSpacing(200)
        self.UsernameWidget = QWidget()
        self.UsernameWidget.setLayout(self.UsernameLayout)

        self.PasswordLayout = QHBoxLayout()
        self.PasswordLayout.addStretch(0)
        self.PasswordLayout.addWidget(self.Password)
        self.PasswordLayout.addWidget(self.linedit2)
        self.PasswordLayout.addSpacing(200)
        self.PasswordWidget = QWidget()
        self.PasswordWidget.setLayout(self.PasswordLayout)

        self.UserFunctionLayout = QHBoxLayout()
        self.UserFunctionLayout.addStretch(0)
        self.UserFunctionLayout.addWidget(self.User_Function)
        self.UserFunctionLayout.addWidget(self.Function_Dropbox)
        self.UserFunctionLayout.addSpacing(200)
        self.UserFunctionWidget = QWidget()
        self.UserFunctionWidget.setLayout(self.UserFunctionLayout)

        self.LoginBtnLayout = QHBoxLayout()
        self.LoginBtnLayout.addStretch(0)
        self.LoginBtnLayout.addWidget(self.Login_Btn)
        self.LoginBtnLayout.addWidget(self.close_Btn)
        self.LoginBtnLayout.addSpacing(200)
        self.LoginBtnWidget = QWidget()
        self.LoginBtnWidget.setLayout(self.LoginBtnLayout)

        self.LoginDetailsLayout.addWidget(self.emptyLogoWidget)
        self.LoginDetailsLayout.addWidget(self.UsernameWidget)
        self.LoginDetailsLayout.addWidget(self.PasswordWidget)
        self.LoginDetailsLayout.addWidget(self.UserFunctionWidget)
        self.LoginDetailsLayout.addWidget(self.LoginBtnWidget)
        self.LoginDetailsWidget = QWidget()
        self.LoginDetailsWidget.setLayout(self.LoginDetailsLayout)

        self.LogosLayout = QVBoxLayout()
        self.LogosLayout.addStretch(0)

        self.titleLayout1 = QHBoxLayout()
        self.titleLayout1.addWidget(self.title)
        self.titleWidget1 = QWidget()
        self.titleWidget1.setLayout(self.titleLayout1)

        self.titleLayout2 = QHBoxLayout()
        self.titleLayout2.addWidget(self.title2)
        self.titleWidget2 = QWidget()
        self.titleWidget2.setLayout(self.titleLayout2)

        self.companylogolayout = QHBoxLayout()
        self.companylogolayout.addWidget(self.company_logo)
        self.companylogoWidget = QWidget()
        self.companylogoWidget.setLayout(self.companylogolayout)

        self.LogosLayout.addWidget(self.titleWidget1)
        self.LogosLayout.addWidget(self.titleWidget2)
        self.LogosLayout.addWidget(self.companylogoWidget)
        self.LogosWidget = QWidget()
        self.LogosWidget.setLayout(self.LogosLayout)

        self.MainDetailsLayout.addWidget(self.LogosWidget)
        self.MainDetailsLayout.addSpacing(300)
        self.MainDetailsLayout.addWidget(self.LoginDetailsWidget)
        self.MainDetailsWidget = QWidget()
        self.MainDetailsWidget.setLayout(self.MainDetailsLayout)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addSpacing(350)
        self.mainLayout.addWidget(self.MainDetailsWidget)
        self.mainLayout.addStretch(1)
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)

        self.setCentralWidget(self.mainWidget)

    ############################################################# USER LOG-INs & ################################################################################
    #############################################################   PASSWORDS    #############################################################################

    def Login_Selection(self):
        if self.Function_Dropbox.currentIndex() == 0:

            if self.linedit1.text() == "o" and self.linedit2.text() == "o":
                self.Screen_4 = Screen_4(self.width, self.height, self, root)
                self.Screen_4.show()   
                self.close()

            elif self.linedit1.text() != str(self.rows[1]):
                self.Status_Bar.showMessage("Incorrect username! Enter the correct username.")
                self.Status_Bar.setStyleSheet("font-size: 15px; color: white; background-color: red")
            
            elif self.linedit2.text() != str(self.rows[2]):
                self.Status_Bar.showMessage("Incorrect password! Enter the correct password.")
                self.Status_Bar.setStyleSheet("font-size: 15px; color: white; background-color: red")

        elif self.Function_Dropbox.currentIndex() == 1:
            
            if self.linedit1.text() == "a" and self.linedit2.text() == "a":
                self.Full_Screen = Full_Screen(self.width, self.height, self, root)
                self.Full_Screen.show()   
                self.close()

            elif self.linedit1.text() != str(self.rows[3]):
                self.Status_Bar.showMessage("Incorrect username! Enter the correct username.")
                self.Status_Bar.setStyleSheet("font-size: 15px; color: white; background-color: red")
            
            elif self.linedit2.text() != str(self.rows[4]):
                self.Status_Bar.showMessage("Incorrect password! Enter the correct password.")
                self.Status_Bar.setStyleSheet("font-size: 15px; color: white; background-color: red")

    
        
    def closefunc(self):
        self.close  ()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    V = app.desktop().screenGeometry()
    width = V.width()
    height = V.height()

    main = MainWindow(width, height)
    main.show()

    sys.exit(app.exec_())
