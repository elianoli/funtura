# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'veiculo_edicaoSjLRiF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from qt_core import *


class Ui_Janela_Veiculo_Edicao(object):
    def setupUi(self, Janela_Veiculo_Edicao):
        if not Janela_Veiculo_Edicao.objectName():
            Janela_Veiculo_Edicao.setObjectName(u"Janela_Veiculo_Edicao")
        Janela_Veiculo_Edicao.setWindowModality(Qt.ApplicationModal)
        Janela_Veiculo_Edicao.resize(550, 450)
        Janela_Veiculo_Edicao.setMinimumSize(QSize(550, 450))
        Janela_Veiculo_Edicao.setMaximumSize(QSize(550, 450))
        self.centralwidget = QWidget(Janela_Veiculo_Edicao)
        self.centralwidget.setObjectName(u"centralwidget")
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
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_titulo = QLabel(self.frame)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setStyleSheet(u"font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_titulo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_titulo)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(70, 0))
        self.frame_2.setStyleSheet(u"QLineEdit, QTextEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"	background-color: #DAEFF0;\n"
"}\n"
"QLabel{\n"
"	font: 75 11pt \"Arial\";\n"
"}\n"
"QComboBox{\n"
"	font: 9pt \"MS Shell Dlg 2\";\n"
"}\n"
"QDateEdit{\n"
"	font: 9pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 1.5px solid #44475a;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(30, 30, -1, -1)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(70, 0))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.placa = QLineEdit(self.frame_2)
        self.placa.setObjectName(u"placa")
        self.placa.setMinimumSize(QSize(120, 25))
        self.placa.setMaximumSize(QSize(120, 25))
        self.placa.setMaxLength(7)
        self.placa.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.placa)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(70, 0))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.marca = QLineEdit(self.frame_2)
        self.marca.setObjectName(u"marca")
        self.marca.setMinimumSize(QSize(250, 25))
        self.marca.setMaximumSize(QSize(250, 25))
        self.marca.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.marca)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(70, 0))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.cor = QLineEdit(self.frame_2)
        self.cor.setObjectName(u"cor")
        self.cor.setMinimumSize(QSize(250, 25))
        self.cor.setMaximumSize(QSize(250, 25))
        self.cor.setClearButtonEnabled(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cor)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(70, 0))
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.ano_fab = QLineEdit(self.frame_2)
        self.ano_fab.setObjectName(u"ano_fab")
        self.ano_fab.setMinimumSize(QSize(100, 25))
        self.ano_fab.setMaximumSize(QSize(100, 25))
        self.ano_fab.setClearButtonEnabled(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.ano_fab)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.desc = QLineEdit(self.frame_2)
        self.desc.setObjectName(u"desc")
        self.desc.setMinimumSize(QSize(300, 25))
        self.desc.setMaximumSize(QSize(300, 25))
        self.desc.setClearButtonEnabled(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.desc)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 80))
        self.frame_3.setMaximumSize(QSize(16777215, 80))
        self.frame_3.setStyleSheet(u"background-color: rgb(75, 117, 132);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, -1, 25, -1)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(337, 57, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.botao_salvar = QPushButton(self.frame_3)
        self.botao_salvar.setObjectName(u"botao_salvar")
        self.botao_salvar.setMinimumSize(QSize(90, 35))
        self.botao_salvar.setMaximumSize(QSize(90, 35))
        self.botao_salvar.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}font: 9pt \"MS Shell Dlg 2\";\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.botao_salvar)

        self.botao_cancelar = QPushButton(self.frame_3)
        self.botao_cancelar.setObjectName(u"botao_cancelar")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botao_cancelar.sizePolicy().hasHeightForWidth())
        self.botao_cancelar.setSizePolicy(sizePolicy)
        self.botao_cancelar.setMinimumSize(QSize(90, 35))
        self.botao_cancelar.setMaximumSize(QSize(90, 35))
        self.botao_cancelar.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}font: 9pt \"MS Shell Dlg 2\";")

        self.horizontalLayout.addWidget(self.botao_cancelar)


        self.verticalLayout.addWidget(self.frame_3)

        Janela_Veiculo_Edicao.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.botao_salvar, self.botao_cancelar)

        self.retranslateUi(Janela_Veiculo_Edicao)

        QMetaObject.connectSlotsByName(Janela_Veiculo_Edicao)
    # setupUi

    def retranslateUi(self, Janela_Veiculo_Edicao):
        Janela_Veiculo_Edicao.setWindowTitle(QCoreApplication.translate("Janela_Veiculo_Edicao", u"MainWindow", None))
        self.label_titulo.setText(QCoreApplication.translate("Janela_Veiculo_Edicao", u"Edi\u00e7\u00e3o de Ve\u00edculos", None))
        self.label_4.setText(QCoreApplication.translate("Janela_Veiculo_Edicao", u"Placa *", None))
        self.label_2.setText(QCoreApplication.translate("Janela_Veiculo_Edicao", u"Marca *", None))
        self.label_3.setText(QCoreApplication.translate("Janela_Veiculo_Edicao", u"Cor", None))
        self.label_5.setText(QCoreApplication.translate("Janela_Veiculo_Edicao", u"Ano Fab. *", None))
        self.ano_fab.setInputMask(QCoreApplication.translate("Janela_Veiculo_Edicao", u"9999", None))
        self.label_6.setText(QCoreApplication.translate("Janela_Veiculo_Edicao", u"Descri\u00e7\u00e3o", None))
        self.label.setText(QCoreApplication.translate("Janela_Veiculo_Edicao", u"* Campos Obrigat\u00f3rios", None))
        self.botao_salvar.setText(QCoreApplication.translate("Janela_Veiculo_Edicao", u"SALVAR", None))
        self.botao_cancelar.setText(QCoreApplication.translate("Janela_Veiculo_Edicao", u"CANCELAR", None))
    # retranslateUi

