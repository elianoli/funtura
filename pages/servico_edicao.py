# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'servico_edicaozsefOr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_Janela_Servico_Edicao(object):
    def setupUi(self, Janela_Servico_Edicao):
        if not Janela_Servico_Edicao.objectName():
            Janela_Servico_Edicao.setObjectName(u"Janela_Servico_Edicao")
        Janela_Servico_Edicao.setWindowModality(Qt.ApplicationModal)
        Janela_Servico_Edicao.resize(550, 450)
        Janela_Servico_Edicao.setMinimumSize(QSize(550, 450))
        Janela_Servico_Edicao.setMaximumSize(QSize(550, 450))
        self.centralwidget = QWidget(Janela_Servico_Edicao)
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
"color: rgb(255, 255, 255);\n"
"")
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
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setContentsMargins(30, 60, -1, -1)
        self.nome_label = QLabel(self.frame_2)
        self.nome_label.setObjectName(u"nome_label")
        self.nome_label.setMinimumSize(QSize(70, 0))
        self.nome_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.nome_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nome_label)

        self.nome = QLineEdit(self.frame_2)
        self.nome.setObjectName(u"nome")
        self.nome.setMinimumSize(QSize(250, 25))
        self.nome.setMaximumSize(QSize(250, 25))
        self.nome.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nome)

        self.valor_label = QLabel(self.frame_2)
        self.valor_label.setObjectName(u"valor_label")
        self.valor_label.setMinimumSize(QSize(70, 0))
        self.valor_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.valor_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.valor_label)

        self.valor = QLineEdit(self.frame_2)
        self.valor.setObjectName(u"valor")
        self.valor.setMinimumSize(QSize(100, 25))
        self.valor.setMaximumSize(QSize(100, 25))
        self.valor.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.valor)

        self.descricao_label = QLabel(self.frame_2)
        self.descricao_label.setObjectName(u"descricao_label")
        self.descricao_label.setMinimumSize(QSize(70, 0))
        self.descricao_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.descricao_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.descricao_label)

        self.descricao = QLineEdit(self.frame_2)
        self.descricao.setObjectName(u"descricao")
        self.descricao.setMinimumSize(QSize(300, 25))
        self.descricao.setMaximumSize(QSize(300, 25))
        self.descricao.setClearButtonEnabled(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.descricao)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 80))
        self.frame_3.setMaximumSize(QSize(16777215, 80))
        self.frame_3.setStyleSheet(u"background-color: rgb(75, 117, 132);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, -1, 15, -1)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(337, 57, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.botao_salvar = QPushButton(self.frame_3)
        self.botao_salvar.setObjectName(u"botao_salvar")
        self.botao_salvar.setMinimumSize(QSize(80, 30))
        self.botao_salvar.setMaximumSize(QSize(80, 30))
        self.botao_salvar.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}\n"
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
        self.botao_cancelar.setMinimumSize(QSize(80, 30))
        self.botao_cancelar.setMaximumSize(QSize(80, 30))
        self.botao_cancelar.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}")

        self.horizontalLayout.addWidget(self.botao_cancelar)


        self.verticalLayout.addWidget(self.frame_3)

        Janela_Servico_Edicao.setCentralWidget(self.centralwidget)

        self.retranslateUi(Janela_Servico_Edicao)

        QMetaObject.connectSlotsByName(Janela_Servico_Edicao)
    # setupUi

    def retranslateUi(self, Janela_Servico_Edicao):
        Janela_Servico_Edicao.setWindowTitle(QCoreApplication.translate("Janela_Servico_Edicao", u"MainWindow", None))
        self.label_titulo.setText(QCoreApplication.translate("Janela_Servico_Edicao", u"Edi\u00e7\u00e3o de Servi\u00e7os", None))
        self.nome_label.setText(QCoreApplication.translate("Janela_Servico_Edicao", u"Nome *", None))
        self.valor_label.setText(QCoreApplication.translate("Janela_Servico_Edicao", u"Valor *", None))
        self.descricao_label.setText(QCoreApplication.translate("Janela_Servico_Edicao", u"Descri\u00e7\u00e3o", None))
        self.label.setText(QCoreApplication.translate("Janela_Servico_Edicao", u"* Campos Obrigat\u00f3rios", None))
        self.botao_salvar.setText(QCoreApplication.translate("Janela_Servico_Edicao", u"SALVAR", None))
        self.botao_cancelar.setText(QCoreApplication.translate("Janela_Servico_Edicao", u"CANCELAR", None))
    # retranslateUi

