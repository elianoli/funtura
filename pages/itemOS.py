# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'itemOSibGUeT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *



class Ui_Janela_ItemOS(object):
    def setupUi(self, Janela_ItemOS):
        if not Janela_ItemOS.objectName():
            Janela_ItemOS.setObjectName(u"Janela_ItemOS")
        Janela_ItemOS.setWindowModality(Qt.ApplicationModal)
        Janela_ItemOS.resize(550, 550)
        Janela_ItemOS.setMinimumSize(QSize(550, 550))
        Janela_ItemOS.setMaximumSize(QSize(550, 550))
        self.centralwidget = QWidget(Janela_ItemOS)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 55))
        self.frame.setMaximumSize(QSize(16777215, 55))
        self.frame.setStyleSheet(u"background-color: rgb(75, 117, 132);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.tabWidget_itemOS = QTabWidget(self.centralwidget)
        self.tabWidget_itemOS.setObjectName(u"tabWidget_itemOS")
        self.tabWidget_itemOS.setMouseTracking(False)
        self.tabWidget_itemOS.setStyleSheet(u"font: 10pt \"Arial\";")
        self.tabWidget_itemOS.setTabShape(QTabWidget.Rounded)
        self.tab_funcionario = QWidget()
        self.tab_funcionario.setObjectName(u"tab_funcionario")
        self.verticalLayout_2 = QVBoxLayout(self.tab_funcionario)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.tab_funcionario)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"\n"
"QLabel{\n"
"	font: 87 12pt \"Arial Black\";\n"
"	color: #4f5368;\n"
"	\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.tab_funcionario)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setStyleSheet(u"QLineEdit{\n"
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
"}\n"
"\n"
"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setContentsMargins(-1, 15, -1, -1)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.buscar_funcionario = QLineEdit(self.frame_2)
        self.buscar_funcionario.setObjectName(u"buscar_funcionario")
        self.buscar_funcionario.setMinimumSize(QSize(250, 25))
        self.buscar_funcionario.setMaximumSize(QSize(250, 25))
        self.buscar_funcionario.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.buscar_funcionario)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.printar_funcionario = QLineEdit(self.frame_2)
        self.printar_funcionario.setObjectName(u"printar_funcionario")
        self.printar_funcionario.setEnabled(False)
        self.printar_funcionario.setMinimumSize(QSize(300, 25))
        self.printar_funcionario.setMaximumSize(QSize(300, 25))
        self.printar_funcionario.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.printar_funcionario)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(2, QFormLayout.LabelRole, self.verticalSpacer_3)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.tab_funcionario)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.f_cadastrar = QPushButton(self.frame_4)
        self.f_cadastrar.setObjectName(u"f_cadastrar")
        self.f_cadastrar.setMinimumSize(QSize(100, 30))
        self.f_cadastrar.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_2.addWidget(self.f_cadastrar)

        self.f_vizualizar = QPushButton(self.frame_4)
        self.f_vizualizar.setObjectName(u"f_vizualizar")
        self.f_vizualizar.setMinimumSize(QSize(100, 30))
        self.f_vizualizar.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_2.addWidget(self.f_vizualizar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.f_adicionar = QPushButton(self.frame_4)
        self.f_adicionar.setObjectName(u"f_adicionar")
        self.f_adicionar.setMinimumSize(QSize(100, 30))
        self.f_adicionar.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_2.addWidget(self.f_adicionar)

        self.f_remover = QPushButton(self.frame_4)
        self.f_remover.setObjectName(u"f_remover")
        self.f_remover.setMinimumSize(QSize(100, 30))
        self.f_remover.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_2.addWidget(self.f_remover)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.tabWidget_itemOS.addTab(self.tab_funcionario, "")
        self.tab_servico = QWidget()
        self.tab_servico.setObjectName(u"tab_servico")
        self.verticalLayout_3 = QVBoxLayout(self.tab_servico)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.tab_servico)
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


        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_5 = QFrame(self.tab_servico)
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
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.buscar_servico = QLineEdit(self.frame_5)
        self.buscar_servico.setObjectName(u"buscar_servico")
        self.buscar_servico.setMinimumSize(QSize(250, 25))
        self.buscar_servico.setMaximumSize(QSize(250, 25))
        self.buscar_servico.setClearButtonEnabled(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.buscar_servico)

        self.tabela_servico = QTableWidget(self.frame_5)
        if (self.tabela_servico.columnCount() < 4):
            self.tabela_servico.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabela_servico.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabela_servico.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabela_servico.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabela_servico.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabela_servico.setObjectName(u"tabela_servico")
        self.tabela_servico.setAutoFillBackground(False)
        self.tabela_servico.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela_servico.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabela_servico.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela_servico.setShowGrid(True)
        self.tabela_servico.setWordWrap(False)
        self.tabela_servico.horizontalHeader().setCascadingSectionResizes(True)
        self.tabela_servico.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabela_servico.verticalHeader().setVisible(False)
        self.tabela_servico.verticalHeader().setCascadingSectionResizes(False)

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.tabela_servico)

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

        self.botao_s_anterior = QPushButton(self.frame_21)
        self.botao_s_anterior.setObjectName(u"botao_s_anterior")
        self.botao_s_anterior.setEnabled(True)
        self.botao_s_anterior.setMinimumSize(QSize(100, 25))
        self.botao_s_anterior.setMaximumSize(QSize(100, 25))
        self.botao_s_anterior.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_18.addWidget(self.botao_s_anterior)

        self.botao_s_proximo = QPushButton(self.frame_21)
        self.botao_s_proximo.setObjectName(u"botao_s_proximo")
        self.botao_s_proximo.setEnabled(True)
        self.botao_s_proximo.setMinimumSize(QSize(100, 25))
        self.botao_s_proximo.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_18.addWidget(self.botao_s_proximo)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_16)


        self.formLayout_2.setWidget(2, QFormLayout.SpanningRole, self.frame_21)

        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_10)

        self.printar_servico = QLineEdit(self.frame_5)
        self.printar_servico.setObjectName(u"printar_servico")
        self.printar_servico.setEnabled(False)
        self.printar_servico.setMinimumSize(QSize(380, 25))
        self.printar_servico.setMaximumSize(QSize(380, 25))
        self.printar_servico.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.printar_servico)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.tab_servico)
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
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.s_cadastrar = QPushButton(self.frame_6)
        self.s_cadastrar.setObjectName(u"s_cadastrar")
        self.s_cadastrar.setMinimumSize(QSize(100, 30))
        self.s_cadastrar.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_4.addWidget(self.s_cadastrar)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.s_adicionar = QPushButton(self.frame_6)
        self.s_adicionar.setObjectName(u"s_adicionar")
        self.s_adicionar.setMinimumSize(QSize(100, 30))
        self.s_adicionar.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_4.addWidget(self.s_adicionar)

        self.s_remover = QPushButton(self.frame_6)
        self.s_remover.setObjectName(u"s_remover")
        self.s_remover.setMinimumSize(QSize(100, 30))
        self.s_remover.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_4.addWidget(self.s_remover)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.tabWidget_itemOS.addTab(self.tab_servico, "")
        self.tab_produto = QWidget()
        self.tab_produto.setObjectName(u"tab_produto")
        self.verticalLayout_4 = QVBoxLayout(self.tab_produto)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.tab_produto)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 40))
        self.frame_11.setMaximumSize(QSize(16777215, 40))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"\n"
"QLabel{\n"
"	font: 87 12pt \"Arial Black\";\n"
"	color: #4f5368;\n"
"	\n"
"}")

        self.horizontalLayout_7.addWidget(self.label_8)


        self.verticalLayout_4.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.tab_produto)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setEnabled(True)
        self.frame_10.setStyleSheet(u"QLineEdit{\n"
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
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.frame_10)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.buscar_produto = QLineEdit(self.frame_10)
        self.buscar_produto.setObjectName(u"buscar_produto")
        self.buscar_produto.setMinimumSize(QSize(250, 25))
        self.buscar_produto.setMaximumSize(QSize(250, 25))
        self.buscar_produto.setClearButtonEnabled(True)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.buscar_produto)

        self.tabela_produto = QTableWidget(self.frame_10)
        if (self.tabela_produto.columnCount() < 4):
            self.tabela_produto.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabela_produto.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabela_produto.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabela_produto.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabela_produto.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.tabela_produto.setObjectName(u"tabela_produto")
        self.tabela_produto.setAutoFillBackground(False)
        self.tabela_produto.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela_produto.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabela_produto.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela_produto.setShowGrid(True)
        self.tabela_produto.setWordWrap(False)
        self.tabela_produto.horizontalHeader().setCascadingSectionResizes(True)
        self.tabela_produto.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabela_produto.verticalHeader().setVisible(False)

        self.formLayout_4.setWidget(1, QFormLayout.SpanningRole, self.tabela_produto)

        self.frame_22 = QFrame(self.frame_10)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(50, 50))
        self.frame_22.setStyleSheet(u"QPushButton{\n"
"	font: 9pt \"MS Shell Dlg 2\";\n"
"\n"
"}")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_18)

        self.botao_p_anterior = QPushButton(self.frame_22)
        self.botao_p_anterior.setObjectName(u"botao_p_anterior")
        self.botao_p_anterior.setEnabled(True)
        self.botao_p_anterior.setMinimumSize(QSize(100, 25))
        self.botao_p_anterior.setMaximumSize(QSize(100, 25))
        self.botao_p_anterior.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_19.addWidget(self.botao_p_anterior)

        self.botao_p_proximo = QPushButton(self.frame_22)
        self.botao_p_proximo.setObjectName(u"botao_p_proximo")
        self.botao_p_proximo.setEnabled(True)
        self.botao_p_proximo.setMinimumSize(QSize(100, 25))
        self.botao_p_proximo.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_19.addWidget(self.botao_p_proximo)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_19)


        self.formLayout_4.setWidget(2, QFormLayout.SpanningRole, self.frame_22)

        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_9)

        self.printar_produto = QLineEdit(self.frame_10)
        self.printar_produto.setObjectName(u"printar_produto")
        self.printar_produto.setEnabled(False)
        self.printar_produto.setMinimumSize(QSize(380, 25))
        self.printar_produto.setMaximumSize(QSize(380, 25))
        self.printar_produto.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.printar_produto)


        self.verticalLayout_4.addWidget(self.frame_10)

        self.frame_12 = QFrame(self.tab_produto)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 50))
        self.frame_12.setMaximumSize(QSize(16777215, 50))
        self.frame_12.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.p_cadastrar = QPushButton(self.frame_12)
        self.p_cadastrar.setObjectName(u"p_cadastrar")
        self.p_cadastrar.setMinimumSize(QSize(100, 30))
        self.p_cadastrar.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_8.addWidget(self.p_cadastrar)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.p_adicionar = QPushButton(self.frame_12)
        self.p_adicionar.setObjectName(u"p_adicionar")
        self.p_adicionar.setMinimumSize(QSize(100, 30))
        self.p_adicionar.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_8.addWidget(self.p_adicionar)

        self.p_remover = QPushButton(self.frame_12)
        self.p_remover.setObjectName(u"p_remover")
        self.p_remover.setMinimumSize(QSize(100, 30))
        self.p_remover.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_8.addWidget(self.p_remover)


        self.verticalLayout_4.addWidget(self.frame_12)

        self.tabWidget_itemOS.addTab(self.tab_produto, "")
        self.tab_concluir = QWidget()
        self.tab_concluir.setObjectName(u"tab_concluir")
        self.verticalLayout_5 = QVBoxLayout(self.tab_concluir)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_8 = QFrame(self.tab_concluir)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 40))
        self.frame_8.setMaximumSize(QSize(16777215, 40))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"\n"
"QLabel{\n"
"	font: 87 12pt \"Arial Black\";\n"
"	color: #4f5368;\n"
"	\n"
"}")

        self.horizontalLayout_6.addWidget(self.label_11)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.tab_concluir)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"	background-color: #FFFFFF;\n"
"}\n"
"\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame_9)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(6)
        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(90, 0))
        self.label_12.setMaximumSize(QSize(90, 16777215))
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.funcionario = QLineEdit(self.frame_9)
        self.funcionario.setObjectName(u"funcionario")
        self.funcionario.setEnabled(False)
        self.funcionario.setMinimumSize(QSize(250, 25))
        self.funcionario.setMaximumSize(QSize(250, 25))

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.funcionario)

        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(90, 0))
        self.label_13.setMaximumSize(QSize(90, 16777215))
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.servico = QLineEdit(self.frame_9)
        self.servico.setObjectName(u"servico")
        self.servico.setEnabled(False)
        self.servico.setMinimumSize(QSize(380, 25))
        self.servico.setMaximumSize(QSize(380, 25))

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.servico)

        self.label_14 = QLabel(self.frame_9)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(80, 0))
        self.label_14.setMaximumSize(QSize(80, 16777215))
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_14)

        self.produto = QLineEdit(self.frame_9)
        self.produto.setObjectName(u"produto")
        self.produto.setEnabled(False)
        self.produto.setMinimumSize(QSize(380, 25))
        self.produto.setMaximumSize(QSize(380, 25))

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.produto)

        self.label_15 = QLabel(self.frame_9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(80, 0))
        self.label_15.setMaximumSize(QSize(80, 16777215))
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_15)

        self.subtotal = QLineEdit(self.frame_9)
        self.subtotal.setObjectName(u"subtotal")
        self.subtotal.setEnabled(False)
        self.subtotal.setMinimumSize(QSize(100, 0))
        self.subtotal.setMaximumSize(QSize(100, 16777215))

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.subtotal)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_3.setItem(4, QFormLayout.LabelRole, self.verticalSpacer_2)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.frame_14 = QFrame(self.tab_concluir)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 40))
        self.frame_14.setMaximumSize(QSize(16777215, 40))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_16 = QLabel(self.frame_14)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_10.addWidget(self.label_16)


        self.verticalLayout_5.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.tab_concluir)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 30))
        self.frame_13.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.salvar = QPushButton(self.frame_13)
        self.salvar.setObjectName(u"salvar")
        self.salvar.setMinimumSize(QSize(100, 30))
        self.salvar.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_9.addWidget(self.salvar)

        self.cancelar = QPushButton(self.frame_13)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setMinimumSize(QSize(100, 30))
        self.cancelar.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_9.addWidget(self.cancelar)


        self.verticalLayout_5.addWidget(self.frame_13)

        self.tabWidget_itemOS.addTab(self.tab_concluir, "")

        self.verticalLayout.addWidget(self.tabWidget_itemOS)

        Janela_ItemOS.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.tabWidget_itemOS, self.buscar_funcionario)
        QWidget.setTabOrder(self.buscar_funcionario, self.f_adicionar)
        QWidget.setTabOrder(self.f_adicionar, self.f_remover)
        QWidget.setTabOrder(self.f_remover, self.f_cadastrar)
        QWidget.setTabOrder(self.f_cadastrar, self.f_vizualizar)
        QWidget.setTabOrder(self.f_vizualizar, self.buscar_servico)
        QWidget.setTabOrder(self.buscar_servico, self.s_adicionar)
        QWidget.setTabOrder(self.s_adicionar, self.s_remover)
        QWidget.setTabOrder(self.s_remover, self.s_cadastrar)
        QWidget.setTabOrder(self.s_cadastrar, self.buscar_produto)
        QWidget.setTabOrder(self.buscar_produto, self.p_adicionar)
        QWidget.setTabOrder(self.p_adicionar, self.p_remover)
        QWidget.setTabOrder(self.p_remover, self.p_cadastrar)
        QWidget.setTabOrder(self.p_cadastrar, self.salvar)
        QWidget.setTabOrder(self.salvar, self.cancelar)
        QWidget.setTabOrder(self.cancelar, self.produto)
        QWidget.setTabOrder(self.produto, self.tabela_servico)
        QWidget.setTabOrder(self.tabela_servico, self.servico)
        QWidget.setTabOrder(self.servico, self.printar_funcionario)
        QWidget.setTabOrder(self.printar_funcionario, self.subtotal)
        QWidget.setTabOrder(self.subtotal, self.printar_servico)
        QWidget.setTabOrder(self.printar_servico, self.printar_produto)
        QWidget.setTabOrder(self.printar_produto, self.tabela_produto)
        QWidget.setTabOrder(self.tabela_produto, self.funcionario)

        self.retranslateUi(Janela_ItemOS)

        self.tabWidget_itemOS.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Janela_ItemOS)
    # setupUi

    def retranslateUi(self, Janela_ItemOS):
        Janela_ItemOS.setWindowTitle(QCoreApplication.translate("Janela_ItemOS", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Janela_ItemOS", u"Itens da Ordem de Servi\u00e7o", None))
        self.label_3.setText(QCoreApplication.translate("Janela_ItemOS", u"Escolher Funcion\u00e1rio", None))
        self.label_2.setText(QCoreApplication.translate("Janela_ItemOS", u"Nome do Funcion\u00e1rio", None))
        self.label_4.setText(QCoreApplication.translate("Janela_ItemOS", u"Funcion\u00e1rio Escolhido", None))
        self.f_cadastrar.setText(QCoreApplication.translate("Janela_ItemOS", u"CADASTRAR", None))
        self.f_vizualizar.setText(QCoreApplication.translate("Janela_ItemOS", u"VISUALIZAR", None))
        self.f_adicionar.setText(QCoreApplication.translate("Janela_ItemOS", u"ADICIONAR", None))
        self.f_remover.setText(QCoreApplication.translate("Janela_ItemOS", u"REMOVER", None))
        self.tabWidget_itemOS.setTabText(self.tabWidget_itemOS.indexOf(self.tab_funcionario), QCoreApplication.translate("Janela_ItemOS", u"Funcion\u00e1rio", None))
        self.label_7.setText(QCoreApplication.translate("Janela_ItemOS", u"Escolher Servi\u00e7o", None))
        self.label_5.setText(QCoreApplication.translate("Janela_ItemOS", u"Nome do Servi\u00e7o", None))
        ___qtablewidgetitem = self.tabela_servico.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Janela_ItemOS", u"ID", None));
        ___qtablewidgetitem1 = self.tabela_servico.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Janela_ItemOS", u"Nome ", None));
        ___qtablewidgetitem2 = self.tabela_servico.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Janela_ItemOS", u"Valor", None));
        ___qtablewidgetitem3 = self.tabela_servico.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Janela_ItemOS", u"Descri\u00e7\u00e3o", None));
        self.botao_s_anterior.setText(QCoreApplication.translate("Janela_ItemOS", u"ANTERIOR", None))
        self.botao_s_proximo.setText(QCoreApplication.translate("Janela_ItemOS", u"PR\u00d3XIMO", None))
        self.label_10.setText(QCoreApplication.translate("Janela_ItemOS", u"Servi\u00e7o Escolhido", None))
        self.s_cadastrar.setText(QCoreApplication.translate("Janela_ItemOS", u"CADASTRAR", None))
        self.s_adicionar.setText(QCoreApplication.translate("Janela_ItemOS", u"ADICIONAR", None))
        self.s_remover.setText(QCoreApplication.translate("Janela_ItemOS", u"REMOVER", None))
        self.tabWidget_itemOS.setTabText(self.tabWidget_itemOS.indexOf(self.tab_servico), QCoreApplication.translate("Janela_ItemOS", u"Servi\u00e7o", None))
        self.label_8.setText(QCoreApplication.translate("Janela_ItemOS", u"Escolher Produto", None))
        self.label_6.setText(QCoreApplication.translate("Janela_ItemOS", u"Nome do Produto", None))
        ___qtablewidgetitem4 = self.tabela_produto.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Janela_ItemOS", u"ID", None));
        ___qtablewidgetitem5 = self.tabela_produto.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Janela_ItemOS", u"Nome ", None));
        ___qtablewidgetitem6 = self.tabela_produto.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Janela_ItemOS", u"Valor", None));
        ___qtablewidgetitem7 = self.tabela_produto.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Janela_ItemOS", u"Descri\u00e7\u00e3o", None));
        self.botao_p_anterior.setText(QCoreApplication.translate("Janela_ItemOS", u"ANTERIOR", None))
        self.botao_p_proximo.setText(QCoreApplication.translate("Janela_ItemOS", u"PR\u00d3XIMO", None))
        self.label_9.setText(QCoreApplication.translate("Janela_ItemOS", u"Produto Escolhido", None))
        self.p_cadastrar.setText(QCoreApplication.translate("Janela_ItemOS", u"CADASTRAR", None))
        self.p_adicionar.setText(QCoreApplication.translate("Janela_ItemOS", u"ADICIONAR", None))
        self.p_remover.setText(QCoreApplication.translate("Janela_ItemOS", u"REMOVER", None))
        self.tabWidget_itemOS.setTabText(self.tabWidget_itemOS.indexOf(self.tab_produto), QCoreApplication.translate("Janela_ItemOS", u"Produto", None))
        self.label_11.setText(QCoreApplication.translate("Janela_ItemOS", u"Concluir Item da Ordem de Servi\u00e7o", None))
        self.label_12.setText(QCoreApplication.translate("Janela_ItemOS", u"Funcion\u00e1rio *", None))
        self.label_13.setText(QCoreApplication.translate("Janela_ItemOS", u"Servi\u00e7o *", None))
        self.label_14.setText(QCoreApplication.translate("Janela_ItemOS", u"Produto", None))
        self.label_15.setText(QCoreApplication.translate("Janela_ItemOS", u"Subtotal", None))
        self.label_16.setText(QCoreApplication.translate("Janela_ItemOS", u"* Campos Obrigat\u00f3rios", None))
        self.salvar.setText(QCoreApplication.translate("Janela_ItemOS", u"SALVAR", None))
        self.cancelar.setText(QCoreApplication.translate("Janela_ItemOS", u"CANCELAR", None))
        self.tabWidget_itemOS.setTabText(self.tabWidget_itemOS.indexOf(self.tab_concluir), QCoreApplication.translate("Janela_ItemOS", u"Concluir", None))
    # retranslateUi

