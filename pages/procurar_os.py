# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'procurar_osTosold.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_procurar_os(object):
    def setupUi(self, procurar_os):
        if not procurar_os.objectName():
            procurar_os.setObjectName(u"procurar_os")
        procurar_os.setWindowModality(Qt.ApplicationModal)
        procurar_os.resize(800, 600)
        procurar_os.setMinimumSize(QSize(800, 600))
        procurar_os.setMaximumSize(QSize(800, 600))
        procurar_os.setStyleSheet(u"QLineEdit{\n"
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
        self.centralwidget = QWidget(procurar_os)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
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


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.line_cliente = QLineEdit(self.frame_5)
        self.line_cliente.setObjectName(u"line_cliente")

        self.horizontalLayout_4.addWidget(self.line_cliente)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_5)

        self.tab_os = QTableWidget(self.frame_2)
        if (self.tab_os.columnCount() < 9):
            self.tab_os.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tab_os.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tab_os.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tab_os.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tab_os.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tab_os.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tab_os.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tab_os.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tab_os.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tab_os.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tab_os.setObjectName(u"tab_os")
        self.tab_os.setFocusPolicy(Qt.ClickFocus)
        self.tab_os.setStyleSheet(u"font: 10pt \"Arial\";")
        self.tab_os.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tab_os.setAlternatingRowColors(True)
        self.tab_os.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tab_os.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tab_os.setTextElideMode(Qt.ElideLeft)

        self.verticalLayout.addWidget(self.tab_os)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btn_anterior = QPushButton(self.frame_4)
        self.btn_anterior.setObjectName(u"btn_anterior")

        self.horizontalLayout_3.addWidget(self.btn_anterior)

        self.btn_proximo = QPushButton(self.frame_4)
        self.btn_proximo.setObjectName(u"btn_proximo")

        self.horizontalLayout_3.addWidget(self.btn_proximo)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.frame_2)

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

        self.btn_selecionar = QPushButton(self.frame_3)
        self.btn_selecionar.setObjectName(u"btn_selecionar")
        self.btn_selecionar.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"	min-width: 108;\n"
"	max-width: 108;\n"
"	min-height: 33;\n"
"	max-height: 33;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_selecionar)

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


        self.verticalLayout_2.addWidget(self.frame_3)

        procurar_os.setCentralWidget(self.centralwidget)

        self.retranslateUi(procurar_os)

        QMetaObject.connectSlotsByName(procurar_os)
    # setupUi

    def retranslateUi(self, procurar_os):
        procurar_os.setWindowTitle(QCoreApplication.translate("procurar_os", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("procurar_os", u"Procurar Ordem de Servi\u00e7o", None))
        self.label_2.setText(QCoreApplication.translate("procurar_os", u"Nome do Cliente", None))
        ___qtablewidgetitem = self.tab_os.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("procurar_os", u"idOS", None));
        ___qtablewidgetitem1 = self.tab_os.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("procurar_os", u"Cliente", None));
        ___qtablewidgetitem2 = self.tab_os.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("procurar_os", u"Ve\u00edculo", None));
        ___qtablewidgetitem3 = self.tab_os.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("procurar_os", u"EstadoOS", None));
        ___qtablewidgetitem4 = self.tab_os.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("procurar_os", u"ValorTotal", None));
        ___qtablewidgetitem5 = self.tab_os.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("procurar_os", u"ValorEntrada", None));
        ___qtablewidgetitem6 = self.tab_os.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("procurar_os", u"numParcelas", None));
        ___qtablewidgetitem7 = self.tab_os.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("procurar_os", u"DataAbertura", None));
        ___qtablewidgetitem8 = self.tab_os.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("procurar_os", u"DataFechamento", None));
        self.btn_anterior.setText(QCoreApplication.translate("procurar_os", u"ANTERIOR", None))
        self.btn_proximo.setText(QCoreApplication.translate("procurar_os", u"PR\u00d3XIMO", None))
        self.btn_selecionar.setText(QCoreApplication.translate("procurar_os", u"SELECIONAR", None))
        self.btn_cancelar.setText(QCoreApplication.translate("procurar_os", u"CANCELAR", None))
    # retranslateUi

