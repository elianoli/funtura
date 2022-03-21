# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cliente_visualizacaoeetmNq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *



class Ui_Janela_Cliente_Visualizacao(object):
    def setupUi(self, Janela_Cliente_Visualizacao):
        if not Janela_Cliente_Visualizacao.objectName():
            Janela_Cliente_Visualizacao.setObjectName(u"Janela_Cliente_Visualizacao")
        Janela_Cliente_Visualizacao.setWindowModality(Qt.ApplicationModal)
        Janela_Cliente_Visualizacao.resize(650, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Janela_Cliente_Visualizacao.sizePolicy().hasHeightForWidth())
        Janela_Cliente_Visualizacao.setSizePolicy(sizePolicy)
        Janela_Cliente_Visualizacao.setMinimumSize(QSize(650, 500))
        Janela_Cliente_Visualizacao.setMaximumSize(QSize(650, 500))
        self.centralwidget = QWidget(Janela_Cliente_Visualizacao)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(650, 500))
        self.centralwidget.setMaximumSize(QSize(650, 500))
        self.centralwidget.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 0.5px solid #44475a;\n"
"	font:11pt \"MS Shell Dlg 2\";\n"
"	padding: 1px;\n"
"	background-color: #DAEFF0;\n"
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
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, -1, -1, -1)
        self.label_titulo = QLabel(self.frame)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setMinimumSize(QSize(300, 30))
        self.label_titulo.setMaximumSize(QSize(350, 30))
        self.label_titulo.setStyleSheet(u"font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_titulo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_titulo)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.email_label = QLabel(self.frame_2)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.email_label, 3, 1, 1, 1)

        self.numero = QLineEdit(self.frame_2)
        self.numero.setObjectName(u"numero")
        self.numero.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.numero.sizePolicy().hasHeightForWidth())
        self.numero.setSizePolicy(sizePolicy2)
        self.numero.setMinimumSize(QSize(100, 25))
        self.numero.setMaximumSize(QSize(100, 25))
        self.numero.setToolTipDuration(-1)
        self.numero.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhHiddenText|Qt.ImhPreferNumbers)
        self.numero.setMaxLength(32767)
        self.numero.setReadOnly(True)
        self.numero.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.numero, 5, 5, 1, 1)

        self.logradouro = QLineEdit(self.frame_2)
        self.logradouro.setObjectName(u"logradouro")
        self.logradouro.setEnabled(True)
        self.logradouro.setMinimumSize(QSize(300, 25))
        self.logradouro.setMaximumSize(QSize(300, 25))
        self.logradouro.setReadOnly(True)
        self.logradouro.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.logradouro, 5, 2, 1, 1)

        self.sexo_label = QLabel(self.frame_2)
        self.sexo_label.setObjectName(u"sexo_label")
        self.sexo_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.sexo_label, 1, 3, 1, 1)

        self.nome_label = QLabel(self.frame_2)
        self.nome_label.setObjectName(u"nome_label")
        self.nome_label.setLayoutDirection(Qt.LeftToRight)
        self.nome_label.setStyleSheet(u"")
        self.nome_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.nome_label, 0, 1, 1, 1)

        self.nome = QLineEdit(self.frame_2)
        self.nome.setObjectName(u"nome")
        self.nome.setEnabled(True)
        self.nome.setMinimumSize(QSize(250, 25))
        self.nome.setMaximumSize(QSize(250, 25))
        self.nome.setReadOnly(True)
        self.nome.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.nome, 0, 2, 1, 1)

        self.logradouro_label = QLabel(self.frame_2)
        self.logradouro_label.setObjectName(u"logradouro_label")
        self.logradouro_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.logradouro_label, 5, 1, 1, 1)

        self.celular = QLineEdit(self.frame_2)
        self.celular.setObjectName(u"celular")
        self.celular.setEnabled(True)
        self.celular.setMinimumSize(QSize(150, 25))
        self.celular.setMaximumSize(QSize(150, 25))
        self.celular.setFrame(True)
        self.celular.setCursorPosition(1)
        self.celular.setReadOnly(True)
        self.celular.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.celular, 2, 2, 1, 1)

        self.cidade_label = QLabel(self.frame_2)
        self.cidade_label.setObjectName(u"cidade_label")
        self.cidade_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.cidade_label, 4, 1, 1, 1)

        self.cidade = QLineEdit(self.frame_2)
        self.cidade.setObjectName(u"cidade")
        self.cidade.setEnabled(True)
        self.cidade.setMinimumSize(QSize(100, 25))
        self.cidade.setMaximumSize(QSize(150, 25))
        self.cidade.setReadOnly(True)
        self.cidade.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.cidade, 4, 2, 1, 1)

        self.cpf = QLineEdit(self.frame_2)
        self.cpf.setObjectName(u"cpf")
        self.cpf.setEnabled(True)
        self.cpf.setMinimumSize(QSize(150, 25))
        self.cpf.setMaximumSize(QSize(150, 25))
        self.cpf.setCursorPosition(0)
        self.cpf.setReadOnly(True)
        self.cpf.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.cpf, 1, 2, 1, 1)

        self.dataNasc_label = QLabel(self.frame_2)
        self.dataNasc_label.setObjectName(u"dataNasc_label")

        self.gridLayout.addWidget(self.dataNasc_label, 0, 3, 1, 1)

        self.email = QLineEdit(self.frame_2)
        self.email.setObjectName(u"email")
        self.email.setEnabled(True)
        self.email.setMinimumSize(QSize(300, 25))
        self.email.setMaximumSize(QSize(300, 25))
        self.email.setReadOnly(True)
        self.email.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.email, 3, 2, 1, 1)

        self.celular_label = QLabel(self.frame_2)
        self.celular_label.setObjectName(u"celular_label")
        self.celular_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.celular_label, 2, 1, 1, 1)

        self.cpf_label = QLabel(self.frame_2)
        self.cpf_label.setObjectName(u"cpf_label")
        self.cpf_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.cpf_label, 1, 1, 1, 1)

        self.bairro = QLineEdit(self.frame_2)
        self.bairro.setObjectName(u"bairro")
        self.bairro.setEnabled(True)
        self.bairro.setMinimumSize(QSize(170, 25))
        self.bairro.setMaximumSize(QSize(170, 25))
        self.bairro.setReadOnly(True)
        self.bairro.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.bairro, 4, 5, 1, 1)

        self.bairro_label = QLabel(self.frame_2)
        self.bairro_label.setObjectName(u"bairro_label")
        self.bairro_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.bairro_label, 4, 3, 1, 1)

        self.numero_label = QLabel(self.frame_2)
        self.numero_label.setObjectName(u"numero_label")
        self.numero_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.numero_label, 5, 3, 1, 1)

        self.sexo = QLineEdit(self.frame_2)
        self.sexo.setObjectName(u"sexo")
        self.sexo.setMinimumSize(QSize(130, 25))
        self.sexo.setMaximumSize(QSize(130, 25))
        self.sexo.setReadOnly(True)

        self.gridLayout.addWidget(self.sexo, 1, 4, 1, 2)

        self.data_nasc = QLineEdit(self.frame_2)
        self.data_nasc.setObjectName(u"data_nasc")
        self.data_nasc.setMinimumSize(QSize(110, 25))
        self.data_nasc.setMaximumSize(QSize(110, 25))
        self.data_nasc.setReadOnly(True)

        self.gridLayout.addWidget(self.data_nasc, 0, 4, 1, 2)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 80))
        self.frame_3.setMaximumSize(QSize(16777215, 80))
        self.frame_3.setStyleSheet(u"background-color: rgb(75, 117, 132);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 30, -1)

        self.verticalLayout.addWidget(self.frame_3)

        Janela_Cliente_Visualizacao.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.nome, self.cpf)
        QWidget.setTabOrder(self.cpf, self.celular)
        QWidget.setTabOrder(self.celular, self.email)
        QWidget.setTabOrder(self.email, self.cidade)
        QWidget.setTabOrder(self.cidade, self.logradouro)
        QWidget.setTabOrder(self.logradouro, self.bairro)
        QWidget.setTabOrder(self.bairro, self.numero)

        self.retranslateUi(Janela_Cliente_Visualizacao)

        QMetaObject.connectSlotsByName(Janela_Cliente_Visualizacao)
    # setupUi

    def retranslateUi(self, Janela_Cliente_Visualizacao):
        Janela_Cliente_Visualizacao.setWindowTitle(QCoreApplication.translate("Janela_Cliente_Visualizacao", u"MainWindow", None))
        self.label_titulo.setText(QCoreApplication.translate("Janela_Cliente_Visualizacao", u"Dados do Cliente", None))
        self.email_label.setText(QCoreApplication.translate("Janela_Cliente_Visualizacao", u"E-mail", None))
#if QT_CONFIG(tooltip)
        self.numero.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.numero.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.numero.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.numero.setInputMask("")
        self.logradouro.setText("")
        self.sexo_label.setText(QCoreApplication.translate("Janela_Cliente_Visualizacao", u"Sexo", None))
        self.nome_label.setText(QCoreApplication.translate("Janela_Cliente_Visualizacao", u"Nome ", None))
        self.nome.setText("")
        self.logradouro_label.setText(QCoreApplication.translate("Janela_Cliente_Visualizacao", u"Logradouro", None))
        self.celular.setInputMask(QCoreApplication.translate("Janela_Cliente_Visualizacao", u"(99) 99999-9999", None))
        self.celular.setText(QCoreApplication.translate("Janela_Cliente_Visualizacao", u"() -", None))
        self.cidade_label.setText(QCoreApplication.translate("Janela_Cliente_Visualizacao", u"Cidade", None))
        self.cpf.setInputMask(QCoreApplication.translate("Janela_Cliente_Visualizacao", u"999.999.999-99", None))
        self.dataNasc_label.setText(QCoreApplication.translate("Janela_Cliente_Visualizacao", u"Data Nasc.", None))
        self.celular_label.setText(QCoreApplication.translate("Janela_Cliente_Visualizacao", u"Celular ", None))
        self.cpf_label.setText(QCoreApplication.translate("Janela_Cliente_Visualizacao", u"CPF ", None))
#if QT_CONFIG(tooltip)
        self.bairro.setToolTip(QCoreApplication.translate("Janela_Cliente_Visualizacao", u"<html><head/><body><p>N\u00famero da casa</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bairro_label.setText(QCoreApplication.translate("Janela_Cliente_Visualizacao", u"Bairro", None))
        self.numero_label.setText(QCoreApplication.translate("Janela_Cliente_Visualizacao", u"N\u00famero", None))
    # retranslateUi

