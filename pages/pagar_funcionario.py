# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagar_funcionarioSIxMRm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_pagar_funcionario(object):
    def setupUi(self, pagar_funcionario):
        if not pagar_funcionario.objectName():
            pagar_funcionario.setObjectName(u"pagar_funcionario")
        pagar_funcionario.setWindowModality(Qt.ApplicationModal)
        pagar_funcionario.resize(800, 600)
        pagar_funcionario.setMinimumSize(QSize(800, 600))
        pagar_funcionario.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(pagar_funcionario)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"	background-color: #DAEFF0;\n"
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
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
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


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.line_funcionario = QLineEdit(self.frame_4)
        self.line_funcionario.setObjectName(u"line_funcionario")

        self.horizontalLayout_3.addWidget(self.line_funcionario)

        self.horizontalSpacer_2 = QSpacerItem(333, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.tab_servicos_prestados = QTableWidget(self.frame_5)
        if (self.tab_servicos_prestados.columnCount() < 5):
            self.tab_servicos_prestados.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tab_servicos_prestados.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tab_servicos_prestados.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tab_servicos_prestados.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tab_servicos_prestados.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tab_servicos_prestados.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tab_servicos_prestados.setObjectName(u"tab_servicos_prestados")
        self.tab_servicos_prestados.setFocusPolicy(Qt.ClickFocus)
        self.tab_servicos_prestados.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tab_servicos_prestados.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tab_servicos_prestados.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.tab_servicos_prestados)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(293, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.btn_anterior = QPushButton(self.frame_6)
        self.btn_anterior.setObjectName(u"btn_anterior")

        self.horizontalLayout_4.addWidget(self.btn_anterior)

        self.btn_proximo = QPushButton(self.frame_6)
        self.btn_proximo.setObjectName(u"btn_proximo")

        self.horizontalLayout_4.addWidget(self.btn_proximo)

        self.horizontalSpacer_4 = QSpacerItem(293, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.verticalLayout_3.addWidget(self.frame_2)

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


        self.verticalLayout_3.addWidget(self.frame_3)

        pagar_funcionario.setCentralWidget(self.centralwidget)

        self.retranslateUi(pagar_funcionario)

        QMetaObject.connectSlotsByName(pagar_funcionario)
    # setupUi

    def retranslateUi(self, pagar_funcionario):
        pagar_funcionario.setWindowTitle(QCoreApplication.translate("pagar_funcionario", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("pagar_funcionario", u"Pagar Funcion\u00e1rio", None))
        self.label_2.setText(QCoreApplication.translate("pagar_funcionario", u"Funcion\u00e1rio", None))
        self.label_3.setText(QCoreApplication.translate("pagar_funcionario", u"Servi\u00e7os Prestados", None))
        ___qtablewidgetitem = self.tab_servicos_prestados.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("pagar_funcionario", u"Funcion\u00e1rio", None));
        ___qtablewidgetitem1 = self.tab_servicos_prestados.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("pagar_funcionario", u"CPF", None));
        ___qtablewidgetitem2 = self.tab_servicos_prestados.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("pagar_funcionario", u"Servi\u00e7o", None));
        ___qtablewidgetitem3 = self.tab_servicos_prestados.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("pagar_funcionario", u"Valor", None));
        ___qtablewidgetitem4 = self.tab_servicos_prestados.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("pagar_funcionario", u"Descri\u00e7\u00e3o", None));
        self.btn_anterior.setText(QCoreApplication.translate("pagar_funcionario", u"ANTERIOR", None))
        self.btn_proximo.setText(QCoreApplication.translate("pagar_funcionario", u"PROXIMO", None))
        self.btn_pagar.setText(QCoreApplication.translate("pagar_funcionario", u"PAGAR", None))
        self.btn_cancelar.setText(QCoreApplication.translate("pagar_funcionario", u"CANCELAR", None))
    # retranslateUi

