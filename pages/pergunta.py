# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'perguntaAquNIV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

class Ui_Janela_Pergunta(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
                    
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(520, 230)
        MainWindow.setMinimumSize(QSize(520, 230))
        MainWindow.setMaximumSize(QSize(520, 230))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 20))
        self.frame_3.setMaximumSize(QSize(16777215, 20))
        self.frame_3.setStyleSheet(u"background-color: rgb(75, 117, 132);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_3)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.texto = QLabel(self.frame)
        self.texto.setObjectName(u"texto")
        self.texto.setStyleSheet(u"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}")
        self.texto.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.texto)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 70))
        self.frame_2.setMaximumSize(QSize(16777215, 70))
        self.frame_2.setStyleSheet(u"background-color: rgb(75, 117, 132);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.botao_sim = QPushButton(self.frame_2)
        self.botao_sim.setObjectName(u"botao_sim")
        self.botao_sim.setMinimumSize(QSize(90, 35))
        self.botao_sim.setMaximumSize(QSize(90, 35))
        self.botao_sim.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}")

        self.horizontalLayout.addWidget(self.botao_sim)

        self.botao_nao = QPushButton(self.frame_2)
        self.botao_nao.setObjectName(u"botao_nao")
        self.botao_nao.setMinimumSize(QSize(90, 35))
        self.botao_nao.setMaximumSize(QSize(90, 35))
        self.botao_nao.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}")

        self.horizontalLayout.addWidget(self.botao_nao)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.texto.setText("")
        self.botao_sim.setText(QCoreApplication.translate("MainWindow", u"SIM", None))
        self.botao_nao.setText(QCoreApplication.translate("MainWindow", u"N\u00c3O", None))
    # retranslateUi

   