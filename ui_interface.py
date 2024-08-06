# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceTYOwcG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(777, 456)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #040f13;\n"
"}\n"
"#side_menu{\n"
"	background-color: #071e26;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"	padding: 10px;\n"
"	background-color:rgb(3, 58, 37);\n"
"	border-radius: 5px;\n"
"}\n"
"#main_body{\n"
"	background-color: #071e26;\n"
"	border-radius: 10px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 50))
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.side_menu = QWidget(self.frame_2)
        self.side_menu.setObjectName(u"side_menu")
        self.verticalLayout_2 = QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.side_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(150, 0))
        self.frame_4.setMaximumSize(QSize(150, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.imgDataBtn_video = QPushButton(self.frame_4)
        self.imgDataBtn_video.setObjectName(u"imgDataBtn_video")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setBold(True)
        font1.setWeight(75)
        self.imgDataBtn_video.setFont(font1)
        self.imgDataBtn_video.setStyleSheet(u"color: #FFFFFF;\n"
"")
        icon = QIcon()
        icon.addFile(u"icons/free-icon-film-strip-3410768.png", QSize(), QIcon.Normal, QIcon.Off)
        self.imgDataBtn_video.setIcon(icon)

        self.verticalLayout_3.addWidget(self.imgDataBtn_video)

        self.imgDataBtn_WebCAM = QPushButton(self.frame_4)
        self.imgDataBtn_WebCAM.setObjectName(u"imgDataBtn_WebCAM")
        self.imgDataBtn_WebCAM.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.imgDataBtn_WebCAM.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.imgDataBtn_WebCAM)

        self.imgDataBtn = QPushButton(self.frame_4)
        self.imgDataBtn.setObjectName(u"imgDataBtn")
        self.imgDataBtn.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/alert-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.imgDataBtn.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.imgDataBtn)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.side_menu)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.image_list = QListView(self.frame_5)
        self.image_list.setObjectName(u"image_list")
        self.image_list.setGeometry(QRect(0, 0, 151, 181))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.image_list.sizePolicy().hasHeightForWidth())
        self.image_list.setSizePolicy(sizePolicy1)
        self.image_list.setMinimumSize(QSize(100, 100))
        self.image_list.setMaximumSize(QSize(1000000, 300))
        self.image_list.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"color:white;\n"
"font: 15pt \"Bahnschrift SemiLight\";\n"
"border-radius: 10px;")

        self.verticalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.side_menu)

        self.main_body = QFrame(self.frame_2)
        self.main_body.setObjectName(u"main_body")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy2)
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.main_body)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cam_display = QLabel(self.main_body)
        self.cam_display.setObjectName(u"cam_display")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.cam_display.setFont(font2)
        self.cam_display.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.cam_display)


        self.horizontalLayout.addWidget(self.main_body)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ub3c4\ub85c \ub178\uba74 \ud45c\uc2dc \uac80\ucd9c", None))
        self.imgDataBtn_video.setText(QCoreApplication.translate("MainWindow", u"     VIDEO", None))
        self.imgDataBtn_WebCAM.setText(QCoreApplication.translate("MainWindow", u"        CAM", None))
        self.imgDataBtn.setText(QCoreApplication.translate("MainWindow", u"       INFO.", None))
        self.cam_display.setText("")
    # retranslateUi

