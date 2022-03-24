# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagar_servico.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_servico(object):
    def setupUi(self, servico):
        if not servico.objectName():
            servico.setObjectName(u"servico")
        servico.resize(320, 450)
        servico.setMinimumSize(QSize(320, 450))
        servico.setMaximumSize(QSize(320, 450))
        self.centralwidget = QWidget(servico)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"	background-color: #eaefef;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 1.5px solid #44475a;\n"
"}\n"
"\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}\n"
"QComboBox{\n"
"	font: 9pt \"MS Shell Dlg 2\";\n"
"}\n"
"QDateEdit{\n"
"	font: 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 60))
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.frame.setStyleSheet(u"background-color: rgb(75, 117, 132);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, -1, -1)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(300, 30))
        self.label.setMaximumSize(QSize(300, 30))
        self.label.setStyleSheet(u"font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(120, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.linu_fun = QLineEdit(self.frame_2)
        self.linu_fun.setObjectName(u"linu_fun")
        self.linu_fun.setMinimumSize(QSize(150, 0))
        self.linu_fun.setMaximumSize(QSize(150, 16777215))
        self.linu_fun.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.linu_fun)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.line_cpf = QLineEdit(self.frame_2)
        self.line_cpf.setObjectName(u"line_cpf")
        self.line_cpf.setMaximumSize(QSize(150, 16777215))
        self.line_cpf.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.line_cpf)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.line_ser = QLineEdit(self.frame_2)
        self.line_ser.setObjectName(u"line_ser")
        self.line_ser.setMaximumSize(QSize(150, 16777215))
        self.line_ser.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.line_ser)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.line_val = QLineEdit(self.frame_2)
        self.line_val.setObjectName(u"line_val")
        self.line_val.setMaximumSize(QSize(100, 16777215))
        self.line_val.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.line_val)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_4)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 0))

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.box_com = QComboBox(self.frame_4)
        self.box_com.addItem("")
        self.box_com.addItem("")
        self.box_com.addItem("")
        self.box_com.addItem("")
        self.box_com.addItem("")
        self.box_com.addItem("")
        self.box_com.addItem("")
        self.box_com.addItem("")
        self.box_com.addItem("")
        self.box_com.addItem("")
        self.box_com.setObjectName(u"box_com")
        self.box_com.setMaximumSize(QSize(75, 16777215))
        self.box_com.setStyleSheet(u"QComboBox{\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"	background-color: none;\n"
"}")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.box_com)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.line_val_com = QLineEdit(self.frame_4)
        self.line_val_com.setObjectName(u"line_val_com")
        self.line_val_com.setMaximumSize(QSize(100, 16777215))
        self.line_val_com.setReadOnly(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.line_val_com)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 80))
        self.frame_3.setMaximumSize(QSize(16777215, 80))
        self.frame_3.setStyleSheet(u"background-color: rgb(75, 117, 132);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(25)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 30, -1)
        self.horizontalSpacer = QSpacerItem(276, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_pagar = QPushButton(self.frame_3)
        self.btn_pagar.setObjectName(u"btn_pagar")
        self.btn_pagar.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"	min-width: 88;\n"
"	max-width: 88;\n"
"	min-height: 33;\n"
"	max-height: 33;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_pagar)

        self.btn_cancelar = QPushButton(self.frame_3)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"	min-width: 88;\n"
"	max-width: 88;\n"
"	min-height: 33;\n"
"	max-height: 33;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_cancelar)


        self.verticalLayout.addWidget(self.frame_3)

        servico.setCentralWidget(self.centralwidget)

        self.retranslateUi(servico)

        QMetaObject.connectSlotsByName(servico)
    # setupUi

    def retranslateUi(self, servico):
        servico.setWindowTitle(QCoreApplication.translate("servico", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("servico", u"Servi\u00e7o", None))
        self.label_4.setText(QCoreApplication.translate("servico", u"Funcion\u00e1rio", None))
        self.label_5.setText(QCoreApplication.translate("servico", u"CPF", None))
        self.label_6.setText(QCoreApplication.translate("servico", u"Servi\u00e7o", None))
        self.label_7.setText(QCoreApplication.translate("servico", u"Valor", None))
        self.label_2.setText(QCoreApplication.translate("servico", u"Comiss\u00e3o", None))
        self.box_com.setItemText(0, QCoreApplication.translate("servico", u"20%", None))
        self.box_com.setItemText(1, QCoreApplication.translate("servico", u"25%", None))
        self.box_com.setItemText(2, QCoreApplication.translate("servico", u"33%", None))
        self.box_com.setItemText(3, QCoreApplication.translate("servico", u"40%", None))
        self.box_com.setItemText(4, QCoreApplication.translate("servico", u"50%", None))
        self.box_com.setItemText(5, QCoreApplication.translate("servico", u"60%", None))
        self.box_com.setItemText(6, QCoreApplication.translate("servico", u"67%", None))
        self.box_com.setItemText(7, QCoreApplication.translate("servico", u"75%", None))
        self.box_com.setItemText(8, QCoreApplication.translate("servico", u"80%", None))
        self.box_com.setItemText(9, QCoreApplication.translate("servico", u"100%", None))

        self.label_3.setText(QCoreApplication.translate("servico", u"Valor c/ comiss\u00e3o", None))
        self.btn_pagar.setText(QCoreApplication.translate("servico", u"PAGAR", None))
        self.btn_cancelar.setText(QCoreApplication.translate("servico", u"CANCELAR", None))
    # retranslateUi

