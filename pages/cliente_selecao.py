# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cliente_selecaoXLpabp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *



class Ui_Janela_Cliente_Selecao(object):
    def setupUi(self, Janela_Cliente_Selecao):
        if not Janela_Cliente_Selecao.objectName():
            Janela_Cliente_Selecao.setObjectName(u"Janela_Cliente_Selecao")
        Janela_Cliente_Selecao.setWindowModality(Qt.ApplicationModal)
        Janela_Cliente_Selecao.resize(560, 530)
        Janela_Cliente_Selecao.setMinimumSize(QSize(560, 530))
        Janela_Cliente_Selecao.setMaximumSize(QSize(560, 530))
        self.centralwidget = QWidget(Janela_Cliente_Selecao)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 40))
        self.frame_7.setMaximumSize(QSize(16777215, 40))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"\n"
"QLabel{\n"
"	font: 87 12pt \"Arial Black\";\n"
"	color: #4f5368;\n"
"	\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_7)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setEnabled(True)
        self.frame_5.setStyleSheet(u"QLineEdit{\n"
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
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_5)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(15)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.buscar_cliente = QLineEdit(self.frame_5)
        self.buscar_cliente.setObjectName(u"buscar_cliente")
        self.buscar_cliente.setMinimumSize(QSize(250, 25))
        self.buscar_cliente.setMaximumSize(QSize(250, 25))
        self.buscar_cliente.setClearButtonEnabled(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.buscar_cliente)

        self.tabela_cliente = QTableWidget(self.frame_5)
        if (self.tabela_cliente.columnCount() < 4):
            self.tabela_cliente.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabela_cliente.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabela_cliente.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabela_cliente.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabela_cliente.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabela_cliente.setObjectName(u"tabela_cliente")
        self.tabela_cliente.setAutoFillBackground(False)
        self.tabela_cliente.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.tabela_cliente.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela_cliente.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabela_cliente.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela_cliente.setShowGrid(True)
        self.tabela_cliente.setWordWrap(False)
        self.tabela_cliente.horizontalHeader().setCascadingSectionResizes(True)
        self.tabela_cliente.horizontalHeader().setDefaultSectionSize(160)
        self.tabela_cliente.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabela_cliente.horizontalHeader().setStretchLastSection(True)
        self.tabela_cliente.verticalHeader().setVisible(False)
        self.tabela_cliente.verticalHeader().setCascadingSectionResizes(False)

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.tabela_cliente)

        self.frame_21 = QFrame(self.frame_5)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(50, 50))
        self.frame_21.setStyleSheet(u"QPushButton{\n"
"	font: 9pt \"MS Shell Dlg 2\";\n"
"\n"
"}")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_17)

        self.botao_anterior = QPushButton(self.frame_21)
        self.botao_anterior.setObjectName(u"botao_anterior")
        self.botao_anterior.setEnabled(True)
        self.botao_anterior.setMinimumSize(QSize(100, 25))
        self.botao_anterior.setMaximumSize(QSize(100, 25))
        self.botao_anterior.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_18.addWidget(self.botao_anterior)

        self.botao_proximo = QPushButton(self.frame_21)
        self.botao_proximo.setObjectName(u"botao_proximo")
        self.botao_proximo.setEnabled(True)
        self.botao_proximo.setMinimumSize(QSize(100, 25))
        self.botao_proximo.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_18.addWidget(self.botao_proximo)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_16)


        self.formLayout_2.setWidget(2, QFormLayout.SpanningRole, self.frame_21)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 50))
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color: #d3d3d3;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.adicionar = QPushButton(self.frame_6)
        self.adicionar.setObjectName(u"adicionar")
        self.adicionar.setEnabled(True)
        self.adicionar.setMinimumSize(QSize(100, 30))
        self.adicionar.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_4.addWidget(self.adicionar)

        self.cancelar = QPushButton(self.frame_6)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setMinimumSize(QSize(100, 30))
        self.cancelar.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_4.addWidget(self.cancelar)


        self.verticalLayout.addWidget(self.frame_6)

        Janela_Cliente_Selecao.setCentralWidget(self.centralwidget)

        self.retranslateUi(Janela_Cliente_Selecao)

        QMetaObject.connectSlotsByName(Janela_Cliente_Selecao)
    # setupUi

    def retranslateUi(self, Janela_Cliente_Selecao):
        Janela_Cliente_Selecao.setWindowTitle(QCoreApplication.translate("Janela_Cliente_Selecao", u"MainWindow", None))
        self.label_7.setText(QCoreApplication.translate("Janela_Cliente_Selecao", u"Escolher Cliente", None))
        self.label_5.setText(QCoreApplication.translate("Janela_Cliente_Selecao", u"Nome do Cliente", None))
        ___qtablewidgetitem = self.tabela_cliente.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Janela_Cliente_Selecao", u"ID", None));
        ___qtablewidgetitem1 = self.tabela_cliente.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Janela_Cliente_Selecao", u"Nome ", None));
        ___qtablewidgetitem2 = self.tabela_cliente.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Janela_Cliente_Selecao", u"CPF", None));
        ___qtablewidgetitem3 = self.tabela_cliente.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Janela_Cliente_Selecao", u"Celular", None));
        self.botao_anterior.setText(QCoreApplication.translate("Janela_Cliente_Selecao", u"ANTERIOR", None))
        self.botao_proximo.setText(QCoreApplication.translate("Janela_Cliente_Selecao", u"PR\u00d3XIMO", None))
        self.adicionar.setText(QCoreApplication.translate("Janela_Cliente_Selecao", u"ADICIONAR", None))
        self.cancelar.setText(QCoreApplication.translate("Janela_Cliente_Selecao", u"CANCELAR", None))
    # retranslateUi

