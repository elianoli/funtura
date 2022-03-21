# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesuHEAMV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(1209, 799)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StackedWidget.sizePolicy().hasHeightForWidth())
        StackedWidget.setSizePolicy(sizePolicy)
        StackedWidget.setToolTipDuration(1)
        StackedWidget.setStyleSheet(u"QLineEdit:focus{\n"
"	border: 1.5px solid #44475a;\n"
"}")
        self.os_page = QWidget()
        self.os_page.setObjectName(u"os_page")
        self.os_page.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.os_page)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.os_tab = QTabWidget(self.os_page)
        self.os_tab.setObjectName(u"os_tab")
        self.os_tab.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.view_os = QWidget()
        self.view_os.setObjectName(u"view_os")
        self.verticalLayout_14 = QVBoxLayout(self.view_os)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.view_os)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setEnabled(True)
        self.frame_47.setMinimumSize(QSize(0, 180))
        self.frame_47.setMaximumSize(QSize(16777214, 180))
        self.frame_47.setStyleSheet(u"\n"
"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"	background-color: #DAEFF0;\n"
"	\n"
"}\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 1.5px solid #44475a;\n"
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
"QPushButton:disabled{\n"
"	background-color: #d3d3d3;\n"
"}\n"
"\n"
"QCheckBox{\n"
"	font: 11pt \"MS Shell Dlg 2\";\n"
"	background-color: #DAEFF0;\n"
"}\n"
"QDateEdit{\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"	background-color: none;\n"
"}\n"
"")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.frame_47)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setVerticalSpacing(10)
        self.formLayout_4.setContentsMargins(9, 0, 0, 0)
        self.checkbox_filtro = QCheckBox(self.frame_47)
        self.checkbox_filtro.setObjectName(u"checkbox_filtro")
        self.checkbox_filtro.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.checkbox_filtro)

        self.frame_filtro = QFrame(self.frame_47)
        self.frame_filtro.setObjectName(u"frame_filtro")
        self.frame_filtro.setMinimumSize(QSize(1150, 100))
        self.frame_filtro.setStyleSheet(u"QFrame{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	background-color: #DAEFF0;\n"
"}\n"
"QLabel{\n"
"	border: none;\n"
"}")
        self.frame_filtro.setFrameShape(QFrame.StyledPanel)
        self.frame_filtro.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_filtro)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(7)
        self.gridLayout_12.setVerticalSpacing(10)
        self.checkbox_ano = QCheckBox(self.frame_filtro)
        self.checkbox_ano.setObjectName(u"checkbox_ano")
        self.checkbox_ano.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.checkbox_ano, 2, 9, 1, 1)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_34, 1, 3, 1, 1)

        self.data_os = QDateEdit(self.frame_filtro)
        self.data_os.setObjectName(u"data_os")
        self.data_os.setMinimumSize(QSize(100, 25))
        self.data_os.setMaximumSize(QSize(100, 25))
        self.data_os.setStyleSheet(u"background-color: none;")
        self.data_os.setMinimumDate(QDate(2022, 3, 15))
        self.data_os.setCalendarPopup(True)

        self.gridLayout_12.addWidget(self.data_os, 2, 7, 1, 1)

        self.mes_os = QComboBox(self.frame_filtro)
        self.mes_os.addItem("")
        self.mes_os.addItem("")
        self.mes_os.addItem("")
        self.mes_os.addItem("")
        self.mes_os.addItem("")
        self.mes_os.addItem("")
        self.mes_os.addItem("")
        self.mes_os.addItem("")
        self.mes_os.addItem("")
        self.mes_os.addItem("")
        self.mes_os.addItem("")
        self.mes_os.addItem("")
        self.mes_os.setObjectName(u"mes_os")
        self.mes_os.setMinimumSize(QSize(110, 25))
        self.mes_os.setMaximumSize(QSize(110, 25))
        self.mes_os.setStyleSheet(u"QComboBox{\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"	background-color: none;\n"
"}")
        self.mes_os.setMaxVisibleItems(12)

        self.gridLayout_12.addWidget(self.mes_os, 1, 10, 1, 1)

        self.checkbox_mes = QCheckBox(self.frame_filtro)
        self.checkbox_mes.setObjectName(u"checkbox_mes")
        self.checkbox_mes.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.checkbox_mes, 1, 9, 1, 1)

        self.ano_os = QSpinBox(self.frame_filtro)
        self.ano_os.setObjectName(u"ano_os")
        self.ano_os.setMinimumSize(QSize(80, 25))
        self.ano_os.setMaximumSize(QSize(80, 25))
        self.ano_os.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")
        self.ano_os.setMinimum(2022)
        self.ano_os.setMaximum(3000)
        self.ano_os.setSingleStep(1)
        self.ano_os.setDisplayIntegerBase(10)

        self.gridLayout_12.addWidget(self.ano_os, 2, 10, 1, 1)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_35, 1, 11, 1, 1)

        self.label_37 = QLabel(self.frame_filtro)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_37, 2, 0, 1, 1)

        self.checkbox_periodo = QCheckBox(self.frame_filtro)
        self.checkbox_periodo.setObjectName(u"checkbox_periodo")
        self.checkbox_periodo.setCheckable(True)
        self.checkbox_periodo.setChecked(False)
        self.checkbox_periodo.setAutoRepeat(False)
        self.checkbox_periodo.setAutoExclusive(True)
        self.checkbox_periodo.setTristate(False)

        self.gridLayout_12.addWidget(self.checkbox_periodo, 1, 5, 1, 1)

        self.estado_os_filtro = QComboBox(self.frame_filtro)
        self.estado_os_filtro.addItem("")
        self.estado_os_filtro.addItem("")
        self.estado_os_filtro.addItem("")
        self.estado_os_filtro.setObjectName(u"estado_os_filtro")
        self.estado_os_filtro.setMinimumSize(QSize(120, 25))
        self.estado_os_filtro.setMaximumSize(QSize(120, 25))
        self.estado_os_filtro.setStyleSheet(u"QComboBox{\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"	background-color: none;\n"
"}")

        self.gridLayout_12.addWidget(self.estado_os_filtro, 2, 1, 1, 1)

        self.checkbox_data = QCheckBox(self.frame_filtro)
        self.checkbox_data.setObjectName(u"checkbox_data")
        self.checkbox_data.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.checkbox_data, 2, 5, 1, 1)

        self.frame_49 = QFrame(self.frame_filtro)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"}")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.frame_49)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_27.addWidget(self.label_39)

        self.data_de = QDateEdit(self.frame_49)
        self.data_de.setObjectName(u"data_de")
        self.data_de.setMinimumSize(QSize(100, 25))
        self.data_de.setStyleSheet(u"background-color: none;")
        self.data_de.setMinimumDate(QDate(2022, 3, 15))
        self.data_de.setCalendarPopup(True)

        self.horizontalLayout_27.addWidget(self.data_de)

        self.label_38 = QLabel(self.frame_49)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_27.addWidget(self.label_38)

        self.data_ate = QDateEdit(self.frame_49)
        self.data_ate.setObjectName(u"data_ate")
        self.data_ate.setMinimumSize(QSize(100, 25))
        self.data_ate.setStyleSheet(u"background-color: none;")
        self.data_ate.setMinimumDate(QDate(2022, 3, 15))
        self.data_ate.setCalendarPopup(True)

        self.horizontalLayout_27.addWidget(self.data_ate)


        self.gridLayout_12.addWidget(self.frame_49, 1, 7, 1, 1)

        self.checkbox_nome = QCheckBox(self.frame_filtro)
        self.checkbox_nome.setObjectName(u"checkbox_nome")

        self.gridLayout_12.addWidget(self.checkbox_nome, 1, 0, 1, 1)

        self.horizontalSpacer_36 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_36, 1, 8, 1, 1)

        self.checkbox_nenhum = QCheckBox(self.frame_filtro)
        self.checkbox_nenhum.setObjectName(u"checkbox_nenhum")
        self.checkbox_nenhum.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.checkbox_nenhum, 1, 4, 1, 1)

        self.nome_cliente_filtro = QLineEdit(self.frame_filtro)
        self.nome_cliente_filtro.setObjectName(u"nome_cliente_filtro")
        self.nome_cliente_filtro.setMinimumSize(QSize(240, 25))
        self.nome_cliente_filtro.setMaximumSize(QSize(240, 25))
        self.nome_cliente_filtro.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.nome_cliente_filtro.setReadOnly(True)
        self.nome_cliente_filtro.setClearButtonEnabled(False)

        self.gridLayout_12.addWidget(self.nome_cliente_filtro, 1, 1, 1, 1)

        self.adicionar_c_filtro = QPushButton(self.frame_filtro)
        self.adicionar_c_filtro.setObjectName(u"adicionar_c_filtro")
        self.adicionar_c_filtro.setEnabled(True)
        self.adicionar_c_filtro.setMinimumSize(QSize(100, 25))
        self.adicionar_c_filtro.setMaximumSize(QSize(100, 25))

        self.gridLayout_12.addWidget(self.adicionar_c_filtro, 1, 2, 1, 1)


        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.frame_filtro)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout_4.setItem(1, QFormLayout.FieldRole, self.horizontalSpacer_37)

        self.buscar_os = QPushButton(self.frame_47)
        self.buscar_os.setObjectName(u"buscar_os")
        self.buscar_os.setEnabled(True)
        self.buscar_os.setMinimumSize(QSize(100, 25))
        self.buscar_os.setMaximumSize(QSize(100, 25))

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.buscar_os)


        self.verticalLayout_14.addWidget(self.frame_47)

        self.frame_52 = QFrame(self.view_os)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(0, 35))
        self.frame_52.setMaximumSize(QSize(16777215, 35))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_52)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(9, 0, 0, 0)
        self.label_46 = QLabel(self.frame_52)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"\n"
"QLabel{\n"
"	font: 87 12pt \"Arial Black\";\n"
"	color: #4f5368;\n"
"}")

        self.verticalLayout_19.addWidget(self.label_46)


        self.verticalLayout_14.addWidget(self.frame_52)

        self.frame_45 = QFrame(self.view_os)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setStyleSheet(u"")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_45)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setVerticalSpacing(15)
        self.tabela_ordem_servico = QTableWidget(self.frame_45)
        if (self.tabela_ordem_servico.columnCount() < 8):
            self.tabela_ordem_servico.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabela_ordem_servico.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabela_ordem_servico.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabela_ordem_servico.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabela_ordem_servico.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabela_ordem_servico.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabela_ordem_servico.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabela_ordem_servico.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabela_ordem_servico.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tabela_ordem_servico.setObjectName(u"tabela_ordem_servico")
        self.tabela_ordem_servico.setStyleSheet(u"font: 10pt \"Arial\";")
        self.tabela_ordem_servico.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.tabela_ordem_servico.setProperty("showDropIndicator", True)
        self.tabela_ordem_servico.setDragEnabled(False)
        self.tabela_ordem_servico.setAlternatingRowColors(True)
        self.tabela_ordem_servico.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabela_ordem_servico.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela_ordem_servico.setTextElideMode(Qt.ElideMiddle)
        self.tabela_ordem_servico.setShowGrid(True)
        self.tabela_ordem_servico.setGridStyle(Qt.SolidLine)
        self.tabela_ordem_servico.setWordWrap(True)
        self.tabela_ordem_servico.setCornerButtonEnabled(True)
        self.tabela_ordem_servico.horizontalHeader().setCascadingSectionResizes(True)
        self.tabela_ordem_servico.horizontalHeader().setMinimumSectionSize(160)
        self.tabela_ordem_servico.horizontalHeader().setStretchLastSection(True)
        self.tabela_ordem_servico.verticalHeader().setVisible(False)

        self.gridLayout_13.addWidget(self.tabela_ordem_servico, 1, 0, 1, 3)


        self.verticalLayout_14.addWidget(self.frame_45)

        self.frame_53 = QFrame(self.view_os)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalSpacer_31 = QSpacerItem(472, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_31)

        self.botao_os_anterior = QPushButton(self.frame_53)
        self.botao_os_anterior.setObjectName(u"botao_os_anterior")
        self.botao_os_anterior.setEnabled(True)
        self.botao_os_anterior.setMinimumSize(QSize(100, 25))
        self.botao_os_anterior.setMaximumSize(QSize(100, 25))
        self.botao_os_anterior.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_26.addWidget(self.botao_os_anterior)

        self.botao_os_proximo = QPushButton(self.frame_53)
        self.botao_os_proximo.setObjectName(u"botao_os_proximo")
        self.botao_os_proximo.setEnabled(True)
        self.botao_os_proximo.setMinimumSize(QSize(100, 25))
        self.botao_os_proximo.setMaximumSize(QSize(100, 25))
        self.botao_os_proximo.setStyleSheet(u"font: 8pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_26.addWidget(self.botao_os_proximo)

        self.horizontalSpacer_32 = QSpacerItem(472, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_32)


        self.verticalLayout_14.addWidget(self.frame_53)

        self.frame_46 = QFrame(self.view_os)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setEnabled(True)
        self.frame_46.setMinimumSize(QSize(0, 50))
        self.frame_46.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color: #d3d3d3;\n"
"}")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 15, 0)
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_33)

        self.gerenciar_os = QPushButton(self.frame_46)
        self.gerenciar_os.setObjectName(u"gerenciar_os")
        self.gerenciar_os.setEnabled(True)
        self.gerenciar_os.setMinimumSize(QSize(120, 30))
        self.gerenciar_os.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_8.addWidget(self.gerenciar_os)


        self.verticalLayout_14.addWidget(self.frame_46)

        self.os_tab.addTab(self.view_os, "")
        self.frame_45.raise_()
        self.frame_53.raise_()
        self.frame_47.raise_()
        self.frame_52.raise_()
        self.frame_46.raise_()
        self.reg_os = QWidget()
        self.reg_os.setObjectName(u"reg_os")
        self.verticalLayout_4 = QVBoxLayout(self.reg_os)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.reg_os)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 40))
        self.frame_12.setMaximumSize(QSize(16777215, 40))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setStyleSheet(u"\n"
"QLabel{\n"
"	font: 87 12pt \"Arial Black\";\n"
"	color: #4f5368;\n"
"	\n"
"}")

        self.horizontalLayout_12.addWidget(self.label_9)


        self.verticalLayout_4.addWidget(self.frame_12)

        self.frame_9 = QFrame(self.reg_os)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setEnabled(True)
        self.frame_9.setMinimumSize(QSize(0, 80))
        self.frame_9.setMaximumSize(QSize(16777215, 80))
        self.frame_9.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"	background-color: #DAEFF0;\n"
"}\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 1.5px solid #44475a;\n"
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
"QPushButton:disabled{\n"
"	background-color: #d3d3d3;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(-1, 0, 6, 0)
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.buscar_c_os = QLineEdit(self.frame_9)
        self.buscar_c_os.setObjectName(u"buscar_c_os")
        self.buscar_c_os.setMinimumSize(QSize(250, 25))
        self.buscar_c_os.setMaximumSize(QSize(250, 25))
        self.buscar_c_os.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.buscar_c_os, 0, 1, 1, 1)

        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)

        self.cadastrar_c_os = QPushButton(self.frame_9)
        self.cadastrar_c_os.setObjectName(u"cadastrar_c_os")
        self.cadastrar_c_os.setEnabled(True)
        self.cadastrar_c_os.setMinimumSize(QSize(100, 30))
        self.cadastrar_c_os.setMaximumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.cadastrar_c_os, 0, 3, 1, 1)

        self.buscar_v_os = QLineEdit(self.frame_9)
        self.buscar_v_os.setObjectName(u"buscar_v_os")
        self.buscar_v_os.setMinimumSize(QSize(200, 25))
        self.buscar_v_os.setMaximumSize(QSize(200, 25))
        self.buscar_v_os.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.buscar_v_os, 1, 1, 1, 1)

        self.visualizar_c_os = QPushButton(self.frame_9)
        self.visualizar_c_os.setObjectName(u"visualizar_c_os")
        self.visualizar_c_os.setEnabled(True)
        self.visualizar_c_os.setMinimumSize(QSize(100, 30))
        self.visualizar_c_os.setMaximumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.visualizar_c_os, 0, 4, 1, 1)

        self.cadastrar_v_os = QPushButton(self.frame_9)
        self.cadastrar_v_os.setObjectName(u"cadastrar_v_os")
        self.cadastrar_v_os.setMinimumSize(QSize(100, 30))
        self.cadastrar_v_os.setMaximumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.cadastrar_v_os, 1, 3, 1, 1)

        self.pushButton_4 = QPushButton(self.frame_9)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setMinimumSize(QSize(100, 30))
        self.pushButton_4.setMaximumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.pushButton_4, 1, 4, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 0, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 0, 5, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 1, 5, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_9)

        self.frame_18 = QFrame(self.reg_os)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 40))
        self.frame_18.setMaximumSize(QSize(16777215, 40))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_13 = QLabel(self.frame_18)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 30))
        self.label_13.setMaximumSize(QSize(150, 30))
        self.label_13.setStyleSheet(u"\n"
"QLabel{\n"
"	font: 87 11pt \"Arial Black\";\n"
"	color: #4f5368;\n"
"}")

        self.horizontalLayout_16.addWidget(self.label_13)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_10)


        self.verticalLayout_4.addWidget(self.frame_18)

        self.frame_11 = QFrame(self.reg_os)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 250))
        self.frame_11.setMaximumSize(QSize(16777215, 500))
        self.frame_11.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color: #d3d3d3;\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(15)
        self.gridLayout_2.setVerticalSpacing(9)
        self.horizontalSpacer_13 = QSpacerItem(120, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_13, 0, 5, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_12, 0, 3, 1, 1)

        self.tabela_itens = QTableWidget(self.frame_11)
        if (self.tabela_itens.columnCount() < 3):
            self.tabela_itens.setColumnCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabela_itens.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabela_itens.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabela_itens.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        self.tabela_itens.setObjectName(u"tabela_itens")
        self.tabela_itens.setMinimumSize(QSize(600, 230))
        self.tabela_itens.setMaximumSize(QSize(800, 230))
        self.tabela_itens.setStyleSheet(u"font: 10pt \"Arial\";")
        self.tabela_itens.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela_itens.setAlternatingRowColors(True)
        self.tabela_itens.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabela_itens.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela_itens.setShowGrid(True)
        self.tabela_itens.setGridStyle(Qt.SolidLine)
        self.tabela_itens.horizontalHeader().setCascadingSectionResizes(False)
        self.tabela_itens.horizontalHeader().setMinimumSectionSize(100)
        self.tabela_itens.horizontalHeader().setDefaultSectionSize(200)
        self.tabela_itens.horizontalHeader().setStretchLastSection(True)
        self.tabela_itens.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.tabela_itens, 0, 0, 1, 3)

        self.frame_19 = QFrame(self.frame_11)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(350, 16777215))
        self.frame_19.setStyleSheet(u"\n"
"QFrame{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	background-color: #DAEFF0;\n"
"}\n"
"QRadioButton{\n"
"	background-color: #DAEFF0;\n"
"	\n"
"}\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"	border: none;\n"
"}")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.formLayout_8 = QFormLayout(self.frame_19)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setVerticalSpacing(12)
        self.formLayout_8.setContentsMargins(-1, -1, 0, -1)
        self.label_14 = QLabel(self.frame_19)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"\n"
"QLabel{\n"
"	font: 87 11pt \"Arial Black\";\n"
"	color: #4f5368;\n"
"}")
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_8.setWidget(0, QFormLayout.SpanningRole, self.label_14)

        self.vista = QRadioButton(self.frame_19)
        self.vista.setObjectName(u"vista")
        self.vista.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.formLayout_8.setWidget(1, QFormLayout.SpanningRole, self.vista)

        self.parcelado = QRadioButton(self.frame_19)
        self.parcelado.setObjectName(u"parcelado")
        self.parcelado.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.formLayout_8.setWidget(2, QFormLayout.SpanningRole, self.parcelado)

        self.label_19 = QLabel(self.frame_19)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_8.setWidget(3, QFormLayout.LabelRole, self.label_19)

        self.valor_entrada = QLineEdit(self.frame_19)
        self.valor_entrada.setObjectName(u"valor_entrada")
        self.valor_entrada.setMinimumSize(QSize(100, 25))
        self.valor_entrada.setMaximumSize(QSize(100, 25))
        self.valor_entrada.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"}")

        self.formLayout_8.setWidget(3, QFormLayout.FieldRole, self.valor_entrada)

        self.label_20 = QLabel(self.frame_19)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_8.setWidget(4, QFormLayout.LabelRole, self.label_20)

        self.num_parcelas = QSpinBox(self.frame_19)
        self.num_parcelas.setObjectName(u"num_parcelas")
        self.num_parcelas.setMinimumSize(QSize(55, 25))
        self.num_parcelas.setMaximumSize(QSize(55, 25))
        self.num_parcelas.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")
        self.num_parcelas.setAlignment(Qt.AlignCenter)
        self.num_parcelas.setMinimum(2)

        self.formLayout_8.setWidget(4, QFormLayout.FieldRole, self.num_parcelas)


        self.gridLayout_2.addWidget(self.frame_19, 0, 4, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_14, 2, 3, 1, 3)

        self.frame_20 = QFrame(self.frame_11)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_17.setSpacing(15)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 9, 0, -1)
        self.inserir_item = QPushButton(self.frame_20)
        self.inserir_item.setObjectName(u"inserir_item")
        self.inserir_item.setMinimumSize(QSize(130, 30))
        self.inserir_item.setMaximumSize(QSize(130, 30))

        self.horizontalLayout_17.addWidget(self.inserir_item)

        self.remover_item = QPushButton(self.frame_20)
        self.remover_item.setObjectName(u"remover_item")
        self.remover_item.setEnabled(True)
        self.remover_item.setMinimumSize(QSize(130, 30))
        self.remover_item.setMaximumSize(QSize(130, 30))

        self.horizontalLayout_17.addWidget(self.remover_item)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_15)

        self.label_21 = QLabel(self.frame_20)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"QLabel{\n"
"	font: 87 11pt \"Arial Black\";\n"
"	color: #4f5368;\n"
"}")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_21)

        self.total = QLineEdit(self.frame_20)
        self.total.setObjectName(u"total")
        self.total.setEnabled(False)
        self.total.setMinimumSize(QSize(120, 25))
        self.total.setMaximumSize(QSize(120, 25))
        self.total.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"}")

        self.horizontalLayout_17.addWidget(self.total)


        self.gridLayout_2.addWidget(self.frame_20, 2, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.reg_os)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 50))
        self.frame_10.setMaximumSize(QSize(16777215, 50))
        self.frame_10.setStyleSheet(u"\n"
"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color: #d3d3d3;\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_11 = QSpacerItem(643, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_11)

        self.salvar_os = QPushButton(self.frame_10)
        self.salvar_os.setObjectName(u"salvar_os")
        self.salvar_os.setMinimumSize(QSize(130, 30))
        self.salvar_os.setMaximumSize(QSize(130, 30))

        self.horizontalLayout_13.addWidget(self.salvar_os)

        self.cancelar_os = QPushButton(self.frame_10)
        self.cancelar_os.setObjectName(u"cancelar_os")
        self.cancelar_os.setMinimumSize(QSize(130, 30))
        self.cancelar_os.setMaximumSize(QSize(130, 30))

        self.horizontalLayout_13.addWidget(self.cancelar_os)


        self.verticalLayout_4.addWidget(self.frame_10)

        self.os_tab.addTab(self.reg_os, "")

        self.horizontalLayout.addWidget(self.os_tab)

        StackedWidget.addWidget(self.os_page)
        self.client_page = QWidget()
        self.client_page.setObjectName(u"client_page")
        self.verticalLayout = QVBoxLayout(self.client_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_23 = QFrame(self.client_page)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 50))
        self.frame_23.setMaximumSize(QSize(16777215, 50))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_c = QLabel(self.frame_23)
        self.label_c.setObjectName(u"label_c")
        sizePolicy.setHeightForWidth(self.label_c.sizePolicy().hasHeightForWidth())
        self.label_c.setSizePolicy(sizePolicy)
        self.label_c.setMinimumSize(QSize(600, 30))
        self.label_c.setMaximumSize(QSize(1300, 30))
        self.label_c.setStyleSheet(u"\n"
"QLabel{\n"
"	font: 87 12pt \"Arial Black\";\n"
"	color: #4f5368;\n"
"	\n"
"}")
        self.label_c.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_c)


        self.verticalLayout.addWidget(self.frame_23)

        self.frame_13 = QFrame(self.client_page)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"	background-color: #DAEFF0;\n"
"}\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 1.5px solid #44475a;\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.formLayout_7 = QFormLayout(self.frame_13)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setVerticalSpacing(15)
        self.label_5 = QLabel(self.frame_13)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.buscar_cliente = QLineEdit(self.frame_13)
        self.buscar_cliente.setObjectName(u"buscar_cliente")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buscar_cliente.sizePolicy().hasHeightForWidth())
        self.buscar_cliente.setSizePolicy(sizePolicy1)
        self.buscar_cliente.setMinimumSize(QSize(250, 25))
        self.buscar_cliente.setMaximumSize(QSize(250, 25))
        self.buscar_cliente.setClearButtonEnabled(True)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.buscar_cliente)

        self.tabela_clientes = QTableWidget(self.frame_13)
        if (self.tabela_clientes.columnCount() < 11):
            self.tabela_clientes.setColumnCount(11)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabela_clientes.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabela_clientes.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabela_clientes.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabela_clientes.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabela_clientes.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabela_clientes.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabela_clientes.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tabela_clientes.setHorizontalHeaderItem(7, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tabela_clientes.setHorizontalHeaderItem(8, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tabela_clientes.setHorizontalHeaderItem(9, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tabela_clientes.setHorizontalHeaderItem(10, __qtablewidgetitem21)
        self.tabela_clientes.setObjectName(u"tabela_clientes")
        self.tabela_clientes.setFocusPolicy(Qt.ClickFocus)
        self.tabela_clientes.setStyleSheet(u"font: 10pt \"Arial\";")
        self.tabela_clientes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela_clientes.setAlternatingRowColors(True)
        self.tabela_clientes.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabela_clientes.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela_clientes.setTextElideMode(Qt.ElideLeft)
        self.tabela_clientes.horizontalHeader().setStretchLastSection(True)
        self.tabela_clientes.verticalHeader().setVisible(False)

        self.formLayout_7.setWidget(1, QFormLayout.SpanningRole, self.tabela_clientes)

        self.frame_21 = QFrame(self.frame_13)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(50, 50))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_17)

        self.botao_c_anterior = QPushButton(self.frame_21)
        self.botao_c_anterior.setObjectName(u"botao_c_anterior")
        self.botao_c_anterior.setEnabled(True)
        self.botao_c_anterior.setMinimumSize(QSize(100, 25))
        self.botao_c_anterior.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_18.addWidget(self.botao_c_anterior)

        self.botao_c_proximo = QPushButton(self.frame_21)
        self.botao_c_proximo.setObjectName(u"botao_c_proximo")
        self.botao_c_proximo.setEnabled(True)
        self.botao_c_proximo.setMinimumSize(QSize(100, 25))
        self.botao_c_proximo.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_18.addWidget(self.botao_c_proximo)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_16)


        self.formLayout_7.setWidget(2, QFormLayout.SpanningRole, self.frame_21)


        self.verticalLayout.addWidget(self.frame_13)

        self.frame_botoes = QFrame(self.client_page)
        self.frame_botoes.setObjectName(u"frame_botoes")
        self.frame_botoes.setMinimumSize(QSize(0, 50))
        self.frame_botoes.setMaximumSize(QSize(16777215, 50))
        self.frame_botoes.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color: #d3d3d3;\n"
"}")
        self.frame_botoes.setFrameShape(QFrame.StyledPanel)
        self.frame_botoes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_botoes)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, -1, 15, -1)
        self.c_botao_editar = QPushButton(self.frame_botoes)
        self.c_botao_editar.setObjectName(u"c_botao_editar")
        self.c_botao_editar.setMinimumSize(QSize(80, 30))
        self.c_botao_editar.setMaximumSize(QSize(80, 30))
        self.c_botao_editar.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.c_botao_editar)

        self.c_botao_remover = QPushButton(self.frame_botoes)
        self.c_botao_remover.setObjectName(u"c_botao_remover")
        self.c_botao_remover.setMinimumSize(QSize(80, 30))
        self.c_botao_remover.setMaximumSize(QSize(80, 30))
        self.c_botao_remover.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.c_botao_remover)

        self.horizontalSpacer = QSpacerItem(486, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.c_botao_cadastrar = QPushButton(self.frame_botoes)
        self.c_botao_cadastrar.setObjectName(u"c_botao_cadastrar")
        self.c_botao_cadastrar.setMinimumSize(QSize(100, 30))
        self.c_botao_cadastrar.setMaximumSize(QSize(100, 30))
        self.c_botao_cadastrar.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.c_botao_cadastrar)


        self.verticalLayout.addWidget(self.frame_botoes)

        StackedWidget.addWidget(self.client_page)
        self.worker_page = QWidget()
        self.worker_page.setObjectName(u"worker_page")
        self.verticalLayout_5 = QVBoxLayout(self.worker_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_22 = QFrame(self.worker_page)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 50))
        self.frame_22.setMaximumSize(QSize(16777215, 50))
        self.frame_22.setStyleSheet(u"\n"
"\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_23 = QLabel(self.frame_22)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"QLabel{\n"
"	font: 87 12pt \"Arial Black\";\n"
"	color: #4f5368;\n"
"}")
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_23)


        self.verticalLayout_5.addWidget(self.frame_22)

        self.frame_15 = QFrame(self.worker_page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"	background-color: #DAEFF0;\n"
"}\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 1.5px solid #44475a;\n"
"}")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.formLayout_6 = QFormLayout(self.frame_15)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setVerticalSpacing(15)
        self.label_6 = QLabel(self.frame_15)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.buscar_funcionario = QLineEdit(self.frame_15)
        self.buscar_funcionario.setObjectName(u"buscar_funcionario")
        self.buscar_funcionario.setMinimumSize(QSize(250, 25))
        self.buscar_funcionario.setMaximumSize(QSize(250, 25))
        self.buscar_funcionario.setClearButtonEnabled(True)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.buscar_funcionario)

        self.tabela_funcionarios = QTableWidget(self.frame_15)
        if (self.tabela_funcionarios.columnCount() < 11):
            self.tabela_funcionarios.setColumnCount(11)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tabela_funcionarios.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tabela_funcionarios.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tabela_funcionarios.setHorizontalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tabela_funcionarios.setHorizontalHeaderItem(3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tabela_funcionarios.setHorizontalHeaderItem(4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tabela_funcionarios.setHorizontalHeaderItem(5, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tabela_funcionarios.setHorizontalHeaderItem(6, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tabela_funcionarios.setHorizontalHeaderItem(7, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tabela_funcionarios.setHorizontalHeaderItem(8, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tabela_funcionarios.setHorizontalHeaderItem(9, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tabela_funcionarios.setHorizontalHeaderItem(10, __qtablewidgetitem32)
        self.tabela_funcionarios.setObjectName(u"tabela_funcionarios")
        self.tabela_funcionarios.setFocusPolicy(Qt.ClickFocus)
        self.tabela_funcionarios.setStyleSheet(u"font: 10pt \"Arial\";")
        self.tabela_funcionarios.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela_funcionarios.setAlternatingRowColors(True)
        self.tabela_funcionarios.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabela_funcionarios.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela_funcionarios.horizontalHeader().setStretchLastSection(True)
        self.tabela_funcionarios.verticalHeader().setVisible(False)

        self.formLayout_6.setWidget(1, QFormLayout.SpanningRole, self.tabela_funcionarios)

        self.frame_24 = QFrame(self.frame_15)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(50, 50))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_18)

        self.botao_f_anterior = QPushButton(self.frame_24)
        self.botao_f_anterior.setObjectName(u"botao_f_anterior")
        self.botao_f_anterior.setEnabled(True)
        self.botao_f_anterior.setMinimumSize(QSize(100, 25))
        self.botao_f_anterior.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_19.addWidget(self.botao_f_anterior)

        self.botao_f_proximo = QPushButton(self.frame_24)
        self.botao_f_proximo.setObjectName(u"botao_f_proximo")
        self.botao_f_proximo.setEnabled(True)
        self.botao_f_proximo.setMinimumSize(QSize(100, 25))
        self.botao_f_proximo.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_19.addWidget(self.botao_f_proximo)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_19)


        self.formLayout_6.setWidget(2, QFormLayout.SpanningRole, self.frame_24)


        self.verticalLayout_5.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.worker_page)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 50))
        self.frame_16.setMaximumSize(QSize(16777215, 50))
        self.frame_16.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color: #d3d3d3;\n"
"}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, -1, 15, -1)
        self.f_botao_editar = QPushButton(self.frame_16)
        self.f_botao_editar.setObjectName(u"f_botao_editar")
        self.f_botao_editar.setMinimumSize(QSize(80, 30))
        self.f_botao_editar.setMaximumSize(QSize(80, 30))
        self.f_botao_editar.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.f_botao_editar)

        self.f_botao_remover = QPushButton(self.frame_16)
        self.f_botao_remover.setObjectName(u"f_botao_remover")
        self.f_botao_remover.setMinimumSize(QSize(80, 30))
        self.f_botao_remover.setMaximumSize(QSize(80, 30))
        self.f_botao_remover.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.f_botao_remover)

        self.horizontalSpacer_2 = QSpacerItem(525, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.f_botao_cadastrar = QPushButton(self.frame_16)
        self.f_botao_cadastrar.setObjectName(u"f_botao_cadastrar")
        self.f_botao_cadastrar.setMinimumSize(QSize(100, 30))
        self.f_botao_cadastrar.setMaximumSize(QSize(100, 30))
        self.f_botao_cadastrar.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.f_botao_cadastrar)


        self.verticalLayout_5.addWidget(self.frame_16)

        StackedWidget.addWidget(self.worker_page)
        self.car_page = QWidget()
        self.car_page.setObjectName(u"car_page")
        self.verticalLayout_2 = QVBoxLayout(self.car_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_14 = QFrame(self.car_page)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 50))
        self.frame_14.setMaximumSize(QSize(16777215, 50))
        self.frame_14.setStyleSheet(u"\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label = QLabel(self.frame_14)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"	font: 87 12pt \"Arial Black\";\n"
"	color: #4f5368;\n"
"}")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_14)

        self.frame_17 = QFrame(self.car_page)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"	background-color: #DAEFF0;\n"
"}\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 1.5px solid #44475a;\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_17)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(15)
        self.label_2 = QLabel(self.frame_17)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.buscar_veiculo = QLineEdit(self.frame_17)
        self.buscar_veiculo.setObjectName(u"buscar_veiculo")
        self.buscar_veiculo.setMinimumSize(QSize(150, 25))
        self.buscar_veiculo.setMaximumSize(QSize(150, 25))
        self.buscar_veiculo.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.buscar_veiculo)

        self.tabela_veiculos = QTableWidget(self.frame_17)
        if (self.tabela_veiculos.columnCount() < 6):
            self.tabela_veiculos.setColumnCount(6)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tabela_veiculos.setHorizontalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tabela_veiculos.setHorizontalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tabela_veiculos.setHorizontalHeaderItem(2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tabela_veiculos.setHorizontalHeaderItem(3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tabela_veiculos.setHorizontalHeaderItem(4, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tabela_veiculos.setHorizontalHeaderItem(5, __qtablewidgetitem38)
        self.tabela_veiculos.setObjectName(u"tabela_veiculos")
        self.tabela_veiculos.setFocusPolicy(Qt.ClickFocus)
        self.tabela_veiculos.setStyleSheet(u"font: 10pt \"Arial\";")
        self.tabela_veiculos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela_veiculos.setAlternatingRowColors(True)
        self.tabela_veiculos.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabela_veiculos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela_veiculos.horizontalHeader().setStretchLastSection(True)
        self.tabela_veiculos.verticalHeader().setVisible(False)
        self.tabela_veiculos.verticalHeader().setHighlightSections(True)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.tabela_veiculos)

        self.frame_26 = QFrame(self.frame_17)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(50, 50))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_20)

        self.botao_v_anterior = QPushButton(self.frame_26)
        self.botao_v_anterior.setObjectName(u"botao_v_anterior")
        self.botao_v_anterior.setEnabled(True)
        self.botao_v_anterior.setMinimumSize(QSize(100, 25))
        self.botao_v_anterior.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_20.addWidget(self.botao_v_anterior)

        self.botao_v_proximo = QPushButton(self.frame_26)
        self.botao_v_proximo.setObjectName(u"botao_v_proximo")
        self.botao_v_proximo.setEnabled(True)
        self.botao_v_proximo.setMinimumSize(QSize(100, 25))
        self.botao_v_proximo.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_20.addWidget(self.botao_v_proximo)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_21)


        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.frame_26)


        self.verticalLayout_2.addWidget(self.frame_17)

        self.frame_25 = QFrame(self.car_page)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 50))
        self.frame_25.setMaximumSize(QSize(16777215, 50))
        self.frame_25.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color: #d3d3d3;\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(15, -1, 15, -1)
        self.v_botao_editar = QPushButton(self.frame_25)
        self.v_botao_editar.setObjectName(u"v_botao_editar")
        self.v_botao_editar.setMinimumSize(QSize(80, 30))
        self.v_botao_editar.setMaximumSize(QSize(80, 30))
        self.v_botao_editar.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.v_botao_editar)

        self.v_botao_remover = QPushButton(self.frame_25)
        self.v_botao_remover.setObjectName(u"v_botao_remover")
        self.v_botao_remover.setMinimumSize(QSize(80, 30))
        self.v_botao_remover.setMaximumSize(QSize(80, 30))
        self.v_botao_remover.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.v_botao_remover)

        self.horizontalSpacer_3 = QSpacerItem(525, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.v_botao_cadastrar = QPushButton(self.frame_25)
        self.v_botao_cadastrar.setObjectName(u"v_botao_cadastrar")
        self.v_botao_cadastrar.setMinimumSize(QSize(100, 30))
        self.v_botao_cadastrar.setMaximumSize(QSize(100, 30))
        self.v_botao_cadastrar.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.v_botao_cadastrar)


        self.verticalLayout_2.addWidget(self.frame_25)

        StackedWidget.addWidget(self.car_page)
        self.product_page = QWidget()
        self.product_page.setObjectName(u"product_page")
        self.verticalLayout_3 = QVBoxLayout(self.product_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.product_page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel{\n"
"	font: 87 12pt \"Arial Black\";\n"
"	color: #4f5368;\n"
"}")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_8)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.product_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"	background-color: #DAEFF0;\n"
"}\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 1.5px solid #44475a;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setVerticalSpacing(15)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.buscar_produto = QLineEdit(self.frame_2)
        self.buscar_produto.setObjectName(u"buscar_produto")
        self.buscar_produto.setMinimumSize(QSize(200, 25))
        self.buscar_produto.setMaximumSize(QSize(200, 25))
        self.buscar_produto.setClearButtonEnabled(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.buscar_produto)

        self.tabela_produtos = QTableWidget(self.frame_2)
        if (self.tabela_produtos.columnCount() < 4):
            self.tabela_produtos.setColumnCount(4)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tabela_produtos.setHorizontalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tabela_produtos.setHorizontalHeaderItem(1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tabela_produtos.setHorizontalHeaderItem(2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tabela_produtos.setHorizontalHeaderItem(3, __qtablewidgetitem42)
        self.tabela_produtos.setObjectName(u"tabela_produtos")
        self.tabela_produtos.setFocusPolicy(Qt.ClickFocus)
        self.tabela_produtos.setStyleSheet(u"font: 10pt \"Arial\";")
        self.tabela_produtos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela_produtos.setAlternatingRowColors(True)
        self.tabela_produtos.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabela_produtos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela_produtos.horizontalHeader().setStretchLastSection(True)
        self.tabela_produtos.verticalHeader().setVisible(False)

        self.formLayout_3.setWidget(1, QFormLayout.SpanningRole, self.tabela_produtos)

        self.frame_27 = QFrame(self.frame_2)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(50, 50))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_22)

        self.botao_p_anterior = QPushButton(self.frame_27)
        self.botao_p_anterior.setObjectName(u"botao_p_anterior")
        self.botao_p_anterior.setEnabled(True)
        self.botao_p_anterior.setMinimumSize(QSize(100, 25))
        self.botao_p_anterior.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_21.addWidget(self.botao_p_anterior)

        self.botao_p_proximo = QPushButton(self.frame_27)
        self.botao_p_proximo.setObjectName(u"botao_p_proximo")
        self.botao_p_proximo.setEnabled(True)
        self.botao_p_proximo.setMinimumSize(QSize(100, 25))
        self.botao_p_proximo.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_21.addWidget(self.botao_p_proximo)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_23)


        self.formLayout_3.setWidget(2, QFormLayout.SpanningRole, self.frame_27)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_botoes_2 = QFrame(self.product_page)
        self.frame_botoes_2.setObjectName(u"frame_botoes_2")
        self.frame_botoes_2.setMinimumSize(QSize(0, 50))
        self.frame_botoes_2.setMaximumSize(QSize(16777215, 50))
        self.frame_botoes_2.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color: #d3d3d3;\n"
"}")
        self.frame_botoes_2.setFrameShape(QFrame.StyledPanel)
        self.frame_botoes_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_botoes_2)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(15, -1, 15, -1)
        self.p_botao_editar = QPushButton(self.frame_botoes_2)
        self.p_botao_editar.setObjectName(u"p_botao_editar")
        self.p_botao_editar.setMinimumSize(QSize(80, 30))
        self.p_botao_editar.setMaximumSize(QSize(80, 30))
        self.p_botao_editar.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.p_botao_editar)

        self.p_botao_remover = QPushButton(self.frame_botoes_2)
        self.p_botao_remover.setObjectName(u"p_botao_remover")
        self.p_botao_remover.setMinimumSize(QSize(80, 30))
        self.p_botao_remover.setMaximumSize(QSize(80, 30))
        self.p_botao_remover.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.p_botao_remover)

        self.horizontalSpacer_4 = QSpacerItem(486, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.p_botao_cadastrar = QPushButton(self.frame_botoes_2)
        self.p_botao_cadastrar.setObjectName(u"p_botao_cadastrar")
        self.p_botao_cadastrar.setMinimumSize(QSize(100, 30))
        self.p_botao_cadastrar.setMaximumSize(QSize(100, 30))
        self.p_botao_cadastrar.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.p_botao_cadastrar)


        self.verticalLayout_3.addWidget(self.frame_botoes_2)

        StackedWidget.addWidget(self.product_page)
        self.service_page = QWidget()
        self.service_page.setObjectName(u"service_page")
        self.verticalLayout_7 = QVBoxLayout(self.service_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_3 = QFrame(self.service_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setStyleSheet(u"\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel{\n"
"	font: 87 12pt \"Arial Black\";\n"
"	color: #4f5368;\n"
"}")

        self.horizontalLayout_14.addWidget(self.label_3)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.service_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"	background-color: #DAEFF0;\n"
"}\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 1.5px solid #44475a;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_4)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(15)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.buscar_servico = QLineEdit(self.frame_4)
        self.buscar_servico.setObjectName(u"buscar_servico")
        self.buscar_servico.setMinimumSize(QSize(200, 25))
        self.buscar_servico.setMaximumSize(QSize(200, 25))
        self.buscar_servico.setClearButtonEnabled(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.buscar_servico)

        self.tabela_servicos = QTableWidget(self.frame_4)
        if (self.tabela_servicos.columnCount() < 4):
            self.tabela_servicos.setColumnCount(4)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tabela_servicos.setHorizontalHeaderItem(0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tabela_servicos.setHorizontalHeaderItem(1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tabela_servicos.setHorizontalHeaderItem(2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tabela_servicos.setHorizontalHeaderItem(3, __qtablewidgetitem46)
        self.tabela_servicos.setObjectName(u"tabela_servicos")
        self.tabela_servicos.setFocusPolicy(Qt.ClickFocus)
        self.tabela_servicos.setStyleSheet(u"font: 10pt \"Arial\";")
        self.tabela_servicos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela_servicos.setAlternatingRowColors(True)
        self.tabela_servicos.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabela_servicos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela_servicos.horizontalHeader().setStretchLastSection(True)
        self.tabela_servicos.verticalHeader().setVisible(False)

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.tabela_servicos)

        self.frame_28 = QFrame(self.frame_4)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(50, 50))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_24)

        self.botao_s_anterior = QPushButton(self.frame_28)
        self.botao_s_anterior.setObjectName(u"botao_s_anterior")
        self.botao_s_anterior.setEnabled(True)
        self.botao_s_anterior.setMinimumSize(QSize(100, 25))
        self.botao_s_anterior.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_22.addWidget(self.botao_s_anterior)

        self.botao_s_proximo = QPushButton(self.frame_28)
        self.botao_s_proximo.setObjectName(u"botao_s_proximo")
        self.botao_s_proximo.setEnabled(True)
        self.botao_s_proximo.setMinimumSize(QSize(100, 25))
        self.botao_s_proximo.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_22.addWidget(self.botao_s_proximo)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_25)


        self.formLayout_2.setWidget(2, QFormLayout.SpanningRole, self.frame_28)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.frame_botoes_3 = QFrame(self.service_page)
        self.frame_botoes_3.setObjectName(u"frame_botoes_3")
        self.frame_botoes_3.setMinimumSize(QSize(0, 50))
        self.frame_botoes_3.setMaximumSize(QSize(16777215, 50))
        self.frame_botoes_3.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color: #d3d3d3;\n"
"}")
        self.frame_botoes_3.setFrameShape(QFrame.StyledPanel)
        self.frame_botoes_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_botoes_3)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(15, -1, 15, -1)
        self.s_botao_editar = QPushButton(self.frame_botoes_3)
        self.s_botao_editar.setObjectName(u"s_botao_editar")
        self.s_botao_editar.setMinimumSize(QSize(80, 30))
        self.s_botao_editar.setMaximumSize(QSize(80, 30))
        self.s_botao_editar.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.s_botao_editar)

        self.s_botao_remover = QPushButton(self.frame_botoes_3)
        self.s_botao_remover.setObjectName(u"s_botao_remover")
        self.s_botao_remover.setMinimumSize(QSize(80, 30))
        self.s_botao_remover.setMaximumSize(QSize(80, 30))
        self.s_botao_remover.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.s_botao_remover)

        self.horizontalSpacer_5 = QSpacerItem(486, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.s_botao_cadastrar = QPushButton(self.frame_botoes_3)
        self.s_botao_cadastrar.setObjectName(u"s_botao_cadastrar")
        self.s_botao_cadastrar.setMinimumSize(QSize(100, 30))
        self.s_botao_cadastrar.setMaximumSize(QSize(100, 30))
        self.s_botao_cadastrar.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.s_botao_cadastrar)


        self.verticalLayout_7.addWidget(self.frame_botoes_3)

        StackedWidget.addWidget(self.service_page)
        self.report_page = QWidget()
        self.report_page.setObjectName(u"report_page")
        self.verticalLayout_6 = QVBoxLayout(self.report_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_29 = QFrame(self.report_page)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_29)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 50))
        self.frame_30.setMaximumSize(QSize(16777215, 50))
        self.frame_30.setStyleSheet(u"QLabel{\n"
"	font: 87 12pt \"Arial Black\";\n"
"	color: #4f5368;\n"
"}")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_30)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_22 = QLabel(self.frame_30)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_8.addWidget(self.label_22)


        self.gridLayout_7.addWidget(self.frame_30, 0, 0, 1, 1)

        self.frame_39 = QFrame(self.frame_29)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"	background-color: #DAEFF0;\n"
"}\n"
"\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_39)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.re_liquido = QLineEdit(self.frame_39)
        self.re_liquido.setObjectName(u"re_liquido")
        self.re_liquido.setEnabled(False)
        self.re_liquido.setMinimumSize(QSize(120, 25))
        self.re_liquido.setMaximumSize(QSize(120, 25))
        self.re_liquido.setReadOnly(True)

        self.gridLayout_6.addWidget(self.re_liquido, 1, 2, 1, 1)

        self.label_36 = QLabel(self.frame_39)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_6.addWidget(self.label_36, 0, 2, 1, 1)

        self.label_32 = QLabel(self.frame_39)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_6.addWidget(self.label_32, 0, 0, 1, 1)

        self.re_retirado = QLineEdit(self.frame_39)
        self.re_retirado.setObjectName(u"re_retirado")
        self.re_retirado.setEnabled(False)
        self.re_retirado.setMinimumSize(QSize(120, 25))
        self.re_retirado.setMaximumSize(QSize(120, 25))
        self.re_retirado.setReadOnly(True)

        self.gridLayout_6.addWidget(self.re_retirado, 1, 1, 1, 1)

        self.label_33 = QLabel(self.frame_39)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_6.addWidget(self.label_33, 0, 1, 1, 1)

        self.re_receber = QLineEdit(self.frame_39)
        self.re_receber.setObjectName(u"re_receber")
        self.re_receber.setEnabled(False)
        self.re_receber.setMinimumSize(QSize(120, 25))
        self.re_receber.setMaximumSize(QSize(120, 25))
        self.re_receber.setReadOnly(True)

        self.gridLayout_6.addWidget(self.re_receber, 1, 3, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_28, 1, 4, 1, 1)

        self.label_34 = QLabel(self.frame_39)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_6.addWidget(self.label_34, 0, 3, 1, 1)

        self.re_recebido = QLineEdit(self.frame_39)
        self.re_recebido.setObjectName(u"re_recebido")
        self.re_recebido.setEnabled(False)
        self.re_recebido.setMinimumSize(QSize(120, 25))
        self.re_recebido.setMaximumSize(QSize(120, 25))
        self.re_recebido.setReadOnly(True)

        self.gridLayout_6.addWidget(self.re_recebido, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_39, 0, 1, 2, 1)

        self.frame_32 = QFrame(self.frame_29)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(350, 0))
        self.frame_32.setMaximumSize(QSize(350, 16777215))
        self.frame_32.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"	background-color: #DAEFF0;\n"
"}\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 1.5px solid #44475a;\n"
"}")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_32)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 80))
        self.frame_33.setMaximumSize(QSize(16777215, 80))
        self.frame_33.setStyleSheet(u"QLineEdit{\n"
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
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.formLayout_9 = QFormLayout(self.frame_33)
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.label_29 = QLabel(self.frame_33)
        self.label_29.setObjectName(u"label_29")

        self.formLayout_9.setWidget(2, QFormLayout.LabelRole, self.label_29)

        self.label_24 = QLabel(self.frame_33)
        self.label_24.setObjectName(u"label_24")

        self.formLayout_9.setWidget(1, QFormLayout.LabelRole, self.label_24)

        self.re_nome = QLineEdit(self.frame_33)
        self.re_nome.setObjectName(u"re_nome")
        self.re_nome.setMinimumSize(QSize(200, 25))
        self.re_nome.setMaximumSize(QSize(200, 25))

        self.formLayout_9.setWidget(1, QFormLayout.FieldRole, self.re_nome)

        self.re_placa = QLineEdit(self.frame_33)
        self.re_placa.setObjectName(u"re_placa")
        self.re_placa.setMinimumSize(QSize(120, 25))
        self.re_placa.setMaximumSize(QSize(120, 25))

        self.formLayout_9.setWidget(2, QFormLayout.FieldRole, self.re_placa)


        self.verticalLayout_9.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_32)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 0))
        self.frame_34.setMaximumSize(QSize(16777215, 16777215))
        self.frame_34.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"	background-color: #DAEFF0;\n"
"}\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_34)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.label_25 = QLabel(self.frame_34)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 40))
        self.label_25.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_4.addWidget(self.label_25, 1, 0, 1, 1)

        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 0))
        self.frame_35.setMaximumSize(QSize(16777215, 16777215))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_35)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(18)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.label_27 = QLabel(self.frame_35)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 40))
        self.label_27.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_3.addWidget(self.label_27, 0, 3, 1, 1)

        self.re_data_f = QDateEdit(self.frame_35)
        self.re_data_f.setObjectName(u"re_data_f")
        self.re_data_f.setMinimumSize(QSize(80, 25))
        self.re_data_f.setMaximumSize(QSize(80, 25))

        self.gridLayout_3.addWidget(self.re_data_f, 1, 3, 1, 1)

        self.label_26 = QLabel(self.frame_35)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 40))
        self.label_26.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_3.addWidget(self.label_26, 0, 0, 1, 1)

        self.re_data_i = QDateEdit(self.frame_35)
        self.re_data_i.setObjectName(u"re_data_i")
        self.re_data_i.setMinimumSize(QSize(80, 25))
        self.re_data_i.setMaximumSize(QSize(80, 25))
        self.re_data_i.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.re_data_i.setLayoutDirection(Qt.LeftToRight)
        self.re_data_i.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.re_data_i.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)

        self.gridLayout_3.addWidget(self.re_data_i, 1, 0, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_26, 0, 4, 1, 1)


        self.gridLayout_4.addWidget(self.frame_35, 2, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_34)

        self.frame_37 = QFrame(self.frame_32)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_37)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(0)
        self.gridLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.label_35 = QLabel(self.frame_37)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_10.addWidget(self.label_35, 0, 0, 1, 1)

        self.frame_36 = QFrame(self.frame_37)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(0, 80))
        self.frame_36.setMaximumSize(QSize(16777215, 80))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.formLayout_10 = QFormLayout(self.frame_36)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.formLayout_10.setHorizontalSpacing(18)
        self.label_28 = QLabel(self.frame_36)
        self.label_28.setObjectName(u"label_28")

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.label_28)

        self.re_estado_os = QComboBox(self.frame_36)
        self.re_estado_os.addItem("")
        self.re_estado_os.addItem("")
        self.re_estado_os.addItem("")
        self.re_estado_os.addItem("")
        self.re_estado_os.setObjectName(u"re_estado_os")
        self.re_estado_os.setMinimumSize(QSize(100, 25))
        self.re_estado_os.setMaximumSize(QSize(100, 25))

        self.formLayout_10.setWidget(0, QFormLayout.FieldRole, self.re_estado_os)

        self.label_30 = QLabel(self.frame_36)
        self.label_30.setObjectName(u"label_30")

        self.formLayout_10.setWidget(1, QFormLayout.LabelRole, self.label_30)

        self.re_estado_p = QComboBox(self.frame_36)
        self.re_estado_p.addItem("")
        self.re_estado_p.addItem("")
        self.re_estado_p.addItem("")
        self.re_estado_p.setObjectName(u"re_estado_p")
        self.re_estado_p.setMinimumSize(QSize(100, 25))
        self.re_estado_p.setMaximumSize(QSize(100, 25))

        self.formLayout_10.setWidget(1, QFormLayout.FieldRole, self.re_estado_p)


        self.gridLayout_10.addWidget(self.frame_36, 1, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_37)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)


        self.gridLayout_7.addWidget(self.frame_32, 1, 0, 2, 1)

        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_31)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.re_tabela = QTableWidget(self.frame_31)
        if (self.re_tabela.columnCount() < 6):
            self.re_tabela.setColumnCount(6)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.re_tabela.setHorizontalHeaderItem(0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.re_tabela.setHorizontalHeaderItem(1, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.re_tabela.setHorizontalHeaderItem(2, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.re_tabela.setHorizontalHeaderItem(3, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.re_tabela.setHorizontalHeaderItem(4, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.re_tabela.setHorizontalHeaderItem(5, __qtablewidgetitem52)
        self.re_tabela.setObjectName(u"re_tabela")
        self.re_tabela.setEnabled(True)
        self.re_tabela.setStyleSheet(u"font: 10pt \"Arial\";")
        self.re_tabela.setSelectionMode(QAbstractItemView.SingleSelection)
        self.re_tabela.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.re_tabela.setShowGrid(False)
        self.re_tabela.setGridStyle(Qt.SolidLine)

        self.gridLayout_5.addWidget(self.re_tabela, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_31, 2, 1, 1, 1)

        self.frame_38 = QFrame(self.frame_29)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(0, 50))
        self.frame_38.setMaximumSize(QSize(16777215, 50))
        self.frame_38.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_27)

        self.re_visualizar = QPushButton(self.frame_38)
        self.re_visualizar.setObjectName(u"re_visualizar")
        self.re_visualizar.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"	min-width: 98;\n"
"	max-width: 98;\n"
"	min-height: 28;\n"
"	max-height: 28;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}")

        self.horizontalLayout_23.addWidget(self.re_visualizar)

        self.re_imprimir = QPushButton(self.frame_38)
        self.re_imprimir.setObjectName(u"re_imprimir")
        self.re_imprimir.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"	min-width: 98;\n"
"	max-width: 98;\n"
"	min-height: 28;\n"
"	max-height: 28;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}")

        self.horizontalLayout_23.addWidget(self.re_imprimir)


        self.gridLayout_7.addWidget(self.frame_38, 3, 0, 1, 2)


        self.verticalLayout_6.addWidget(self.frame_29)

        StackedWidget.addWidget(self.report_page)
        self.finance_page = QWidget()
        self.finance_page.setObjectName(u"finance_page")
        self.finance_page.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"	background-color: #DAEFF0;\n"
"}\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.finance_page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_5 = QFrame(self.finance_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QTextEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"	background-color: #DAEFF0;\n"
"}\n"
"QLabel{\n"
"	font: 75 9pt \"Arial\";\n"
"}\n"
"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"	background-color: #DAEFF0;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_42 = QFrame(self.frame_6)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_42)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_40 = QLabel(self.frame_42)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}")

        self.verticalLayout_13.addWidget(self.label_40)

        self.ca_tabela = QTableWidget(self.frame_42)
        if (self.ca_tabela.columnCount() < 5):
            self.ca_tabela.setColumnCount(5)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.ca_tabela.setHorizontalHeaderItem(0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.ca_tabela.setHorizontalHeaderItem(1, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.ca_tabela.setHorizontalHeaderItem(2, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.ca_tabela.setHorizontalHeaderItem(3, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.ca_tabela.setHorizontalHeaderItem(4, __qtablewidgetitem57)
        self.ca_tabela.setObjectName(u"ca_tabela")
        self.ca_tabela.setFocusPolicy(Qt.ClickFocus)
        self.ca_tabela.setStyleSheet(u"font: 10pt \"Arial\";")
        self.ca_tabela.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ca_tabela.setAlternatingRowColors(True)
        self.ca_tabela.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ca_tabela.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ca_tabela.setTextElideMode(Qt.ElideLeft)

        self.verticalLayout_13.addWidget(self.ca_tabela)

        self.frame_51 = QFrame(self.frame_42)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_41)

        self.btn_anterior = QPushButton(self.frame_51)
        self.btn_anterior.setObjectName(u"btn_anterior")

        self.horizontalLayout_30.addWidget(self.btn_anterior)

        self.btn_proximo = QPushButton(self.frame_51)
        self.btn_proximo.setObjectName(u"btn_proximo")

        self.horizontalLayout_30.addWidget(self.btn_proximo)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_42)


        self.verticalLayout_13.addWidget(self.frame_51)

        self.frame_54 = QFrame(self.frame_42)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalSpacer_43 = QSpacerItem(443, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_43)

        self.desfazer_mov = QPushButton(self.frame_54)
        self.desfazer_mov.setObjectName(u"desfazer_mov")
        self.desfazer_mov.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"	min-width: 198;\n"
"	max-width: 198;\n"
"	min-height: 33;\n"
"	max-height: 33;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}")

        self.horizontalLayout_31.addWidget(self.desfazer_mov)


        self.verticalLayout_13.addWidget(self.frame_54)


        self.gridLayout_9.addWidget(self.frame_42, 0, 1, 3, 1)

        self.frame_40 = QFrame(self.frame_6)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_40)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_10 = QLabel(self.frame_40)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 30))
        self.label_10.setMaximumSize(QSize(16777215, 30))
        self.label_10.setStyleSheet(u"\n"
"QLabel{\n"
"	font: 87 12pt \"Arial Black\";\n"
"	color: #4f5368;\n"
"	\n"
"}")

        self.verticalLayout_11.addWidget(self.label_10)


        self.gridLayout_9.addWidget(self.frame_40, 0, 0, 1, 1)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QSize(300, 50))
        self.frame_8.setMaximumSize(QSize(300, 50))
        self.frame_8.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"	background-color: #DAEFF0;\n"
"}\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 1.5px solid #44475a;\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(2, 0, 0, 0)
        self.ca_saldo = QLineEdit(self.frame_8)
        self.ca_saldo.setObjectName(u"ca_saldo")
        self.ca_saldo.setMinimumSize(QSize(80, 25))
        self.ca_saldo.setMaximumSize(QSize(80, 25))
        self.ca_saldo.setLayoutDirection(Qt.LeftToRight)
        self.ca_saldo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ca_saldo.setReadOnly(True)

        self.gridLayout_8.addWidget(self.ca_saldo, 0, 1, 1, 1)

        self.label_15 = QLabel(self.frame_8)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_8.addWidget(self.label_15, 0, 0, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_29, 0, 2, 1, 1)


        self.gridLayout_9.addWidget(self.frame_8, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.frame_6)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(300, 0))
        self.groupBox_3.setMaximumSize(QSize(300, 16777215))
        self.groupBox_3.setStyleSheet(u"font: 75 9pt \"Arial\";")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_7 = QFrame(self.groupBox_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(170, 0))
        self.frame_7.setMaximumSize(QSize(170, 16777215))
        self.frame_7.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"	background-color: #DAEFF0;\n"
"}\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(45, 0))
        self.label_18.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout_24.addWidget(self.label_18)

        self.ca_valor = QLineEdit(self.frame_7)
        self.ca_valor.setObjectName(u"ca_valor")
        self.ca_valor.setMinimumSize(QSize(100, 25))
        self.ca_valor.setMaximumSize(QSize(100, 25))
        self.ca_valor.setAlignment(Qt.AlignCenter)
        self.ca_valor.setReadOnly(False)
        self.ca_valor.setClearButtonEnabled(True)

        self.horizontalLayout_24.addWidget(self.ca_valor)


        self.verticalLayout_12.addWidget(self.frame_7)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_12.addWidget(self.label_16)

        self.ca_aporte = QRadioButton(self.groupBox_3)
        self.ca_aporte.setObjectName(u"ca_aporte")

        self.verticalLayout_12.addWidget(self.ca_aporte)

        self.ca_saque = QRadioButton(self.groupBox_3)
        self.ca_saque.setObjectName(u"ca_saque")

        self.verticalLayout_12.addWidget(self.ca_saque)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_12.addWidget(self.label_17)

        self.ca_desc = QTextEdit(self.groupBox_3)
        self.ca_desc.setObjectName(u"ca_desc")
        self.ca_desc.setMinimumSize(QSize(250, 100))
        self.ca_desc.setMaximumSize(QSize(250, 100))

        self.verticalLayout_12.addWidget(self.ca_desc)

        self.frame_41 = QFrame(self.groupBox_3)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_30)

        self.ca_botao_efetuar = QPushButton(self.frame_41)
        self.ca_botao_efetuar.setObjectName(u"ca_botao_efetuar")
        self.ca_botao_efetuar.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"	min-width: 98;\n"
"	max-width: 98;\n"
"	min-height: 28;\n"
"	max-height: 28;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}")

        self.horizontalLayout_25.addWidget(self.ca_botao_efetuar)


        self.verticalLayout_12.addWidget(self.frame_41)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)


        self.gridLayout_9.addWidget(self.groupBox_3, 2, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_6, 0, 0, 1, 1)

        self.frame_44 = QFrame(self.frame_5)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(0, 50))
        self.frame_44.setMaximumSize(QSize(16777215, 50))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.ca_receber_p = QPushButton(self.frame_44)
        self.ca_receber_p.setObjectName(u"ca_receber_p")
        self.ca_receber_p.setMinimumSize(QSize(150, 30))
        self.ca_receber_p.setMaximumSize(QSize(150, 30))
        self.ca_receber_p.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"	min-width: 148;\n"
"	max-width: 148;\n"
"	min-height: 28;\n"
"	max-height: 28;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}")

        self.horizontalLayout_7.addWidget(self.ca_receber_p)

        self.ca_pagar_f = QPushButton(self.frame_44)
        self.ca_pagar_f.setObjectName(u"ca_pagar_f")
        self.ca_pagar_f.setMinimumSize(QSize(150, 30))
        self.ca_pagar_f.setMaximumSize(QSize(150, 30))
        self.ca_pagar_f.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"	min-width: 148;\n"
"	max-width: 148;\n"
"	min-height: 28;\n"
"	max-height: 28;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}")

        self.horizontalLayout_7.addWidget(self.ca_pagar_f)

        self.horizontalSpacer_6 = QSpacerItem(535, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.gridLayout_11.addWidget(self.frame_44, 1, 0, 1, 1)


        self.verticalLayout_15.addWidget(self.frame_5)

        StackedWidget.addWidget(self.finance_page)

        self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex(7)
        self.os_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.checkbox_filtro.setText(QCoreApplication.translate("StackedWidget", u"Aplicar Filtro", None))
        self.checkbox_ano.setText(QCoreApplication.translate("StackedWidget", u"Ano", None))
        self.mes_os.setItemText(0, QCoreApplication.translate("StackedWidget", u"JANEIRO", None))
        self.mes_os.setItemText(1, QCoreApplication.translate("StackedWidget", u"FEVEREIRO", None))
        self.mes_os.setItemText(2, QCoreApplication.translate("StackedWidget", u"MAR\u00c7O", None))
        self.mes_os.setItemText(3, QCoreApplication.translate("StackedWidget", u"ABRIL", None))
        self.mes_os.setItemText(4, QCoreApplication.translate("StackedWidget", u"MAIO", None))
        self.mes_os.setItemText(5, QCoreApplication.translate("StackedWidget", u"JUNHO", None))
        self.mes_os.setItemText(6, QCoreApplication.translate("StackedWidget", u"JULHO", None))
        self.mes_os.setItemText(7, QCoreApplication.translate("StackedWidget", u"AGOSTO", None))
        self.mes_os.setItemText(8, QCoreApplication.translate("StackedWidget", u"SETEMBRO", None))
        self.mes_os.setItemText(9, QCoreApplication.translate("StackedWidget", u"OUTUBRO", None))
        self.mes_os.setItemText(10, QCoreApplication.translate("StackedWidget", u"NOVEMBRO", None))
        self.mes_os.setItemText(11, QCoreApplication.translate("StackedWidget", u"DEZEMBRO", None))

        self.checkbox_mes.setText(QCoreApplication.translate("StackedWidget", u"M\u00eas", None))
        self.ano_os.setSuffix("")
        self.ano_os.setPrefix("")
        self.label_37.setText(QCoreApplication.translate("StackedWidget", u"Estado", None))
        self.checkbox_periodo.setText(QCoreApplication.translate("StackedWidget", u"Per\u00edodo", None))
        self.estado_os_filtro.setItemText(0, QCoreApplication.translate("StackedWidget", u"ABERTA", None))
        self.estado_os_filtro.setItemText(1, QCoreApplication.translate("StackedWidget", u"FINALIZADA", None))
        self.estado_os_filtro.setItemText(2, QCoreApplication.translate("StackedWidget", u"CANCELADA", None))

        self.checkbox_data.setText(QCoreApplication.translate("StackedWidget", u"Data", None))
        self.label_39.setText(QCoreApplication.translate("StackedWidget", u"De", None))
        self.label_38.setText(QCoreApplication.translate("StackedWidget", u"At\u00e9", None))
        self.checkbox_nome.setText(QCoreApplication.translate("StackedWidget", u"Cliente", None))
        self.checkbox_nenhum.setText(QCoreApplication.translate("StackedWidget", u"Nenhum", None))
        self.adicionar_c_filtro.setText(QCoreApplication.translate("StackedWidget", u"ADICIONAR", None))
        self.buscar_os.setText(QCoreApplication.translate("StackedWidget", u"BUSCAR OS", None))
        self.label_46.setText(QCoreApplication.translate("StackedWidget", u"Ordens de Servi\u00e7o", None))
        ___qtablewidgetitem = self.tabela_ordem_servico.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("StackedWidget", u"Cliente", None));
        ___qtablewidgetitem1 = self.tabela_ordem_servico.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("StackedWidget", u"ID ", None));
        ___qtablewidgetitem2 = self.tabela_ordem_servico.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("StackedWidget", u"Data-Hora Abertura", None));
        ___qtablewidgetitem3 = self.tabela_ordem_servico.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("StackedWidget", u"Data-Hora Fechamento", None));
        ___qtablewidgetitem4 = self.tabela_ordem_servico.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("StackedWidget", u"Estado", None));
        ___qtablewidgetitem5 = self.tabela_ordem_servico.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("StackedWidget", u"Valor Total", None));
        ___qtablewidgetitem6 = self.tabela_ordem_servico.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("StackedWidget", u"Valor Entrada", None));
        ___qtablewidgetitem7 = self.tabela_ordem_servico.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("StackedWidget", u"Num. Parcelas", None));
        self.botao_os_anterior.setText(QCoreApplication.translate("StackedWidget", u"ANTERIOR", None))
        self.botao_os_proximo.setText(QCoreApplication.translate("StackedWidget", u"PR\u00d3XIMO", None))
        self.gerenciar_os.setText(QCoreApplication.translate("StackedWidget", u"GERENCIAR OS", None))
        self.os_tab.setTabText(self.os_tab.indexOf(self.view_os), QCoreApplication.translate("StackedWidget", u"Visualizar", None))
        self.label_9.setText(QCoreApplication.translate("StackedWidget", u"Cadastro de Ordens de Servi\u00e7o", None))
        self.label_11.setText(QCoreApplication.translate("StackedWidget", u"Nome do Cliente * ", None))
        self.label_12.setText(QCoreApplication.translate("StackedWidget", u"Placa do Ve\u00edculo *", None))
#if QT_CONFIG(tooltip)
        self.cadastrar_c_os.setToolTip(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p>Cadastrar Cliente</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cadastrar_c_os.setText(QCoreApplication.translate("StackedWidget", u"CADASTRAR", None))
#if QT_CONFIG(tooltip)
        self.visualizar_c_os.setToolTip(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p>Visualizar Cliente</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.visualizar_c_os.setText(QCoreApplication.translate("StackedWidget", u"VISUALIZAR", None))
#if QT_CONFIG(tooltip)
        self.cadastrar_v_os.setToolTip(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p>Cadastrar Ve\u00edculo</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cadastrar_v_os.setText(QCoreApplication.translate("StackedWidget", u"CADASTRAR", None))
#if QT_CONFIG(tooltip)
        self.pushButton_4.setToolTip(QCoreApplication.translate("StackedWidget", u"<html><head/><body><p>Visualizar Ve\u00edculo</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_4.setText(QCoreApplication.translate("StackedWidget", u"VISUALIZAR", None))
        self.label_13.setText(QCoreApplication.translate("StackedWidget", u"Tabela de Itens", None))
        ___qtablewidgetitem8 = self.tabela_itens.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("StackedWidget", u"Funcion\u00e1rio", None));
        ___qtablewidgetitem9 = self.tabela_itens.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("StackedWidget", u"Servi\u00e7o", None));
        ___qtablewidgetitem10 = self.tabela_itens.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("StackedWidget", u"Produto", None));
        self.label_14.setText(QCoreApplication.translate("StackedWidget", u"Forma de Pagamento", None))
        self.vista.setText(QCoreApplication.translate("StackedWidget", u"A vista", None))
        self.parcelado.setText(QCoreApplication.translate("StackedWidget", u"Parcelado", None))
        self.label_19.setText(QCoreApplication.translate("StackedWidget", u"Valor de Entrada ", None))
        self.label_20.setText(QCoreApplication.translate("StackedWidget", u"N\u00famero Parcelas", None))
        self.inserir_item.setText(QCoreApplication.translate("StackedWidget", u"INSERIR ITEM", None))
        self.remover_item.setText(QCoreApplication.translate("StackedWidget", u"REMOVER ITEM", None))
        self.label_21.setText(QCoreApplication.translate("StackedWidget", u"TOTAL", None))
        self.salvar_os.setText(QCoreApplication.translate("StackedWidget", u"SALVAR OS", None))
        self.cancelar_os.setText(QCoreApplication.translate("StackedWidget", u"CANCELAR OS", None))
        self.os_tab.setTabText(self.os_tab.indexOf(self.reg_os), QCoreApplication.translate("StackedWidget", u"Cadastrar", None))
        self.label_c.setText(QCoreApplication.translate("StackedWidget", u"Clientes", None))
        self.label_5.setText(QCoreApplication.translate("StackedWidget", u"Nome", None))
        ___qtablewidgetitem11 = self.tabela_clientes.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("StackedWidget", u"ID", None));
        ___qtablewidgetitem12 = self.tabela_clientes.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("StackedWidget", u"Nome ", None));
        ___qtablewidgetitem13 = self.tabela_clientes.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("StackedWidget", u"CPF", None));
        ___qtablewidgetitem14 = self.tabela_clientes.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("StackedWidget", u"Sexo", None));
        ___qtablewidgetitem15 = self.tabela_clientes.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("StackedWidget", u"Data Nasc.", None));
        ___qtablewidgetitem16 = self.tabela_clientes.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("StackedWidget", u"Celular", None));
        ___qtablewidgetitem17 = self.tabela_clientes.horizontalHeaderItem(6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("StackedWidget", u"E-mail", None));
        ___qtablewidgetitem18 = self.tabela_clientes.horizontalHeaderItem(7)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("StackedWidget", u"Logradouro", None));
        ___qtablewidgetitem19 = self.tabela_clientes.horizontalHeaderItem(8)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("StackedWidget", u"Cidade", None));
        ___qtablewidgetitem20 = self.tabela_clientes.horizontalHeaderItem(9)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("StackedWidget", u"Bairro", None));
        ___qtablewidgetitem21 = self.tabela_clientes.horizontalHeaderItem(10)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("StackedWidget", u"N\u00famero", None));
        self.botao_c_anterior.setText(QCoreApplication.translate("StackedWidget", u"ANTERIOR", None))
        self.botao_c_proximo.setText(QCoreApplication.translate("StackedWidget", u"PR\u00d3XIMO", None))
        self.c_botao_editar.setText(QCoreApplication.translate("StackedWidget", u"EDITAR", None))
        self.c_botao_remover.setText(QCoreApplication.translate("StackedWidget", u"REMOVER", None))
        self.c_botao_cadastrar.setText(QCoreApplication.translate("StackedWidget", u"CADASTRAR", None))
        self.label_23.setText(QCoreApplication.translate("StackedWidget", u"Funcion\u00e1rios", None))
        self.label_6.setText(QCoreApplication.translate("StackedWidget", u"Nome", None))
        ___qtablewidgetitem22 = self.tabela_funcionarios.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("StackedWidget", u"ID", None));
        ___qtablewidgetitem23 = self.tabela_funcionarios.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("StackedWidget", u"Nome", None));
        ___qtablewidgetitem24 = self.tabela_funcionarios.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("StackedWidget", u"CPF", None));
        ___qtablewidgetitem25 = self.tabela_funcionarios.horizontalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("StackedWidget", u"Sexo", None));
        ___qtablewidgetitem26 = self.tabela_funcionarios.horizontalHeaderItem(4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("StackedWidget", u"Data Nasc.", None));
        ___qtablewidgetitem27 = self.tabela_funcionarios.horizontalHeaderItem(5)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("StackedWidget", u"Celular", None));
        ___qtablewidgetitem28 = self.tabela_funcionarios.horizontalHeaderItem(6)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("StackedWidget", u"E-mail", None));
        ___qtablewidgetitem29 = self.tabela_funcionarios.horizontalHeaderItem(7)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("StackedWidget", u"Logradouro", None));
        ___qtablewidgetitem30 = self.tabela_funcionarios.horizontalHeaderItem(8)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("StackedWidget", u"Cidade", None));
        ___qtablewidgetitem31 = self.tabela_funcionarios.horizontalHeaderItem(9)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("StackedWidget", u"Bairro", None));
        ___qtablewidgetitem32 = self.tabela_funcionarios.horizontalHeaderItem(10)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("StackedWidget", u"N\u00famero", None));
        self.botao_f_anterior.setText(QCoreApplication.translate("StackedWidget", u"ANTERIOR", None))
        self.botao_f_proximo.setText(QCoreApplication.translate("StackedWidget", u"PR\u00d3XIMO", None))
        self.f_botao_editar.setText(QCoreApplication.translate("StackedWidget", u"EDITAR", None))
        self.f_botao_remover.setText(QCoreApplication.translate("StackedWidget", u"REMOVER", None))
        self.f_botao_cadastrar.setText(QCoreApplication.translate("StackedWidget", u"CADASTRAR", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"Ve\u00edculos", None))
        self.label_2.setText(QCoreApplication.translate("StackedWidget", u"Placa", None))
        ___qtablewidgetitem33 = self.tabela_veiculos.horizontalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("StackedWidget", u"ID", None));
        ___qtablewidgetitem34 = self.tabela_veiculos.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("StackedWidget", u"Placa", None));
        ___qtablewidgetitem35 = self.tabela_veiculos.horizontalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("StackedWidget", u"Ano Fab.", None));
        ___qtablewidgetitem36 = self.tabela_veiculos.horizontalHeaderItem(3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("StackedWidget", u"Cor", None));
        ___qtablewidgetitem37 = self.tabela_veiculos.horizontalHeaderItem(4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("StackedWidget", u"Marca", None));
        ___qtablewidgetitem38 = self.tabela_veiculos.horizontalHeaderItem(5)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("StackedWidget", u"Descri\u00e7\u00e3o", None));
        self.botao_v_anterior.setText(QCoreApplication.translate("StackedWidget", u"ANTERIOR", None))
        self.botao_v_proximo.setText(QCoreApplication.translate("StackedWidget", u"PR\u00d3XIMO", None))
        self.v_botao_editar.setText(QCoreApplication.translate("StackedWidget", u"EDITAR", None))
        self.v_botao_remover.setText(QCoreApplication.translate("StackedWidget", u"REMOVER", None))
        self.v_botao_cadastrar.setText(QCoreApplication.translate("StackedWidget", u"CADASTRAR", None))
        self.label_8.setText(QCoreApplication.translate("StackedWidget", u"Produtos", None))
        self.label_7.setText(QCoreApplication.translate("StackedWidget", u"Nome do produto", None))
        ___qtablewidgetitem39 = self.tabela_produtos.horizontalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("StackedWidget", u"ID", None));
        ___qtablewidgetitem40 = self.tabela_produtos.horizontalHeaderItem(1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("StackedWidget", u"Nome", None));
        ___qtablewidgetitem41 = self.tabela_produtos.horizontalHeaderItem(2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("StackedWidget", u"Valor", None));
        ___qtablewidgetitem42 = self.tabela_produtos.horizontalHeaderItem(3)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("StackedWidget", u"Descri\u00e7\u00e3o", None));
        self.botao_p_anterior.setText(QCoreApplication.translate("StackedWidget", u"ANTERIOR", None))
        self.botao_p_proximo.setText(QCoreApplication.translate("StackedWidget", u"PR\u00d3XIMO", None))
        self.p_botao_editar.setText(QCoreApplication.translate("StackedWidget", u"EDITAR", None))
        self.p_botao_remover.setText(QCoreApplication.translate("StackedWidget", u"REMOVER", None))
        self.p_botao_cadastrar.setText(QCoreApplication.translate("StackedWidget", u"CADASTRAR", None))
        self.label_3.setText(QCoreApplication.translate("StackedWidget", u"Servi\u00e7os", None))
        self.label_4.setText(QCoreApplication.translate("StackedWidget", u"Nome do servi\u00e7o", None))
        ___qtablewidgetitem43 = self.tabela_servicos.horizontalHeaderItem(0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("StackedWidget", u"ID", None));
        ___qtablewidgetitem44 = self.tabela_servicos.horizontalHeaderItem(1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("StackedWidget", u"Nome", None));
        ___qtablewidgetitem45 = self.tabela_servicos.horizontalHeaderItem(2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("StackedWidget", u"Valor", None));
        ___qtablewidgetitem46 = self.tabela_servicos.horizontalHeaderItem(3)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("StackedWidget", u"Descri\u00e7\u00e3o", None));
        self.botao_s_anterior.setText(QCoreApplication.translate("StackedWidget", u"ANTERIOR", None))
        self.botao_s_proximo.setText(QCoreApplication.translate("StackedWidget", u"PR\u00d3XIMO", None))
        self.s_botao_editar.setText(QCoreApplication.translate("StackedWidget", u"EDITAR", None))
        self.s_botao_remover.setText(QCoreApplication.translate("StackedWidget", u"REMOVER", None))
        self.s_botao_cadastrar.setText(QCoreApplication.translate("StackedWidget", u"CADASTRAR", None))
        self.label_22.setText(QCoreApplication.translate("StackedWidget", u"Relat\u00f3rios", None))
        self.label_36.setText(QCoreApplication.translate("StackedWidget", u"Valor L\u00edquido", None))
        self.label_32.setText(QCoreApplication.translate("StackedWidget", u"Valor Recebido", None))
        self.label_33.setText(QCoreApplication.translate("StackedWidget", u"Valor Retirado", None))
        self.label_34.setText(QCoreApplication.translate("StackedWidget", u"Valor a Receber", None))
        self.label_29.setText(QCoreApplication.translate("StackedWidget", u"Placa do Ve\u00edculo", None))
        self.label_24.setText(QCoreApplication.translate("StackedWidget", u"Nome do Cliente", None))
        self.label_25.setText(QCoreApplication.translate("StackedWidget", u"Periodo da visualiza\u00e7\u00e3o", None))
        self.label_27.setText(QCoreApplication.translate("StackedWidget", u"Final", None))
        self.label_26.setText(QCoreApplication.translate("StackedWidget", u"Inicial", None))
        self.label_35.setText(QCoreApplication.translate("StackedWidget", u"Estados", None))
        self.label_28.setText(QCoreApplication.translate("StackedWidget", u"Ordem de Servi\u00e7o", None))
        self.re_estado_os.setItemText(0, QCoreApplication.translate("StackedWidget", u"Todas", None))
        self.re_estado_os.setItemText(1, QCoreApplication.translate("StackedWidget", u"Abertas", None))
        self.re_estado_os.setItemText(2, QCoreApplication.translate("StackedWidget", u"Quitadas", None))
        self.re_estado_os.setItemText(3, QCoreApplication.translate("StackedWidget", u"Canceladas", None))

        self.label_30.setText(QCoreApplication.translate("StackedWidget", u"Parcela", None))
        self.re_estado_p.setItemText(0, QCoreApplication.translate("StackedWidget", u"Todas", None))
        self.re_estado_p.setItemText(1, QCoreApplication.translate("StackedWidget", u"Abertas", None))
        self.re_estado_p.setItemText(2, QCoreApplication.translate("StackedWidget", u"Quitadas", None))

        ___qtablewidgetitem47 = self.re_tabela.horizontalHeaderItem(0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("StackedWidget", u"Nome", None));
        ___qtablewidgetitem48 = self.re_tabela.horizontalHeaderItem(1)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("StackedWidget", u"Placa", None));
        ___qtablewidgetitem49 = self.re_tabela.horizontalHeaderItem(2)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("StackedWidget", u"Estado OS", None));
        ___qtablewidgetitem50 = self.re_tabela.horizontalHeaderItem(3)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("StackedWidget", u"Parcela", None));
        ___qtablewidgetitem51 = self.re_tabela.horizontalHeaderItem(4)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("StackedWidget", u"Valor Parcela", None));
        ___qtablewidgetitem52 = self.re_tabela.horizontalHeaderItem(5)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("StackedWidget", u"Vencimento", None));
        self.re_visualizar.setText(QCoreApplication.translate("StackedWidget", u"VISUALIZAR", None))
        self.re_imprimir.setText(QCoreApplication.translate("StackedWidget", u"IMPRIMIR", None))
        self.label_40.setText(QCoreApplication.translate("StackedWidget", u"Hist\u00f3rico de movimentos", None))
        ___qtablewidgetitem53 = self.ca_tabela.horizontalHeaderItem(0)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("StackedWidget", u"Hor\u00e1rio", None));
        ___qtablewidgetitem54 = self.ca_tabela.horizontalHeaderItem(1)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("StackedWidget", u"Ordem de Servi\u00e7o", None));
        ___qtablewidgetitem55 = self.ca_tabela.horizontalHeaderItem(2)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("StackedWidget", u"Tipo", None));
        ___qtablewidgetitem56 = self.ca_tabela.horizontalHeaderItem(3)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("StackedWidget", u"Valor", None));
        ___qtablewidgetitem57 = self.ca_tabela.horizontalHeaderItem(4)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("StackedWidget", u"Parcela", None));
        self.btn_anterior.setText(QCoreApplication.translate("StackedWidget", u"ANTERIOR", None))
        self.btn_proximo.setText(QCoreApplication.translate("StackedWidget", u"PR\u00d3XIMO", None))
        self.desfazer_mov.setText(QCoreApplication.translate("StackedWidget", u"DESFAZER MOVIMENTA\u00c7\u00c3O", None))
        self.label_10.setText(QCoreApplication.translate("StackedWidget", u"Caixa", None))
        self.label_15.setText(QCoreApplication.translate("StackedWidget", u"Saldo do Caixa", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("StackedWidget", u"Movimenta\u00e7\u00e3o Caixa", None))
        self.label_18.setText(QCoreApplication.translate("StackedWidget", u"Valor ", None))
        self.label_16.setText(QCoreApplication.translate("StackedWidget", u"Tipo de Movimenta\u00e7\u00e3o", None))
        self.ca_aporte.setText(QCoreApplication.translate("StackedWidget", u"Entrada", None))
        self.ca_saque.setText(QCoreApplication.translate("StackedWidget", u"Sa\u00edda", None))
        self.label_17.setText(QCoreApplication.translate("StackedWidget", u"Descri\u00e7\u00e3o da Movimenta\u00e7\u00e3o ", None))
        self.ca_botao_efetuar.setText(QCoreApplication.translate("StackedWidget", u"EFETUAR", None))
        self.ca_receber_p.setText(QCoreApplication.translate("StackedWidget", u"RECEBER PARCELA", None))
        self.ca_pagar_f.setText(QCoreApplication.translate("StackedWidget", u"PAGAR FUNCION\u00c1RIO", None))
    # retranslateUi

