# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagar_parcelajcneRw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_pagar_parcela(object):
    def setupUi(self, pagar_parcela):
        if not pagar_parcela.objectName():
            pagar_parcela.setObjectName(u"pagar_parcela")
        pagar_parcela.setWindowModality(Qt.ApplicationModal)
        pagar_parcela.resize(320, 450)
        pagar_parcela.setMinimumSize(QSize(300, 450))
        pagar_parcela.setMaximumSize(QSize(320, 450))
        self.centralwidget = QWidget(pagar_parcela)
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
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.line_id = QLineEdit(self.frame_2)
        self.line_id.setObjectName(u"line_id")
        self.line_id.setEnabled(True)
        self.line_id.setMinimumSize(QSize(100, 0))
        self.line_id.setMaximumSize(QSize(150, 16777215))
        self.line_id.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.line_id)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.line_numero = QLineEdit(self.frame_2)
        self.line_numero.setObjectName(u"line_numero")
        self.line_numero.setEnabled(True)
        self.line_numero.setMaximumSize(QSize(100, 16777215))
        self.line_numero.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.line_numero)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.line_valor = QLineEdit(self.frame_2)
        self.line_valor.setObjectName(u"line_valor")
        self.line_valor.setEnabled(True)
        self.line_valor.setMaximumSize(QSize(150, 16777215))
        self.line_valor.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.line_valor)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.line_estado = QLineEdit(self.frame_2)
        self.line_estado.setObjectName(u"line_estado")
        self.line_estado.setEnabled(True)
        self.line_estado.setMaximumSize(QSize(150, 16777215))
        self.line_estado.setReadOnly(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.line_estado)

        self.line_vencimento = QLineEdit(self.frame_2)
        self.line_vencimento.setObjectName(u"line_vencimento")
        self.line_vencimento.setMaximumSize(QSize(100, 16777215))
        self.line_vencimento.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.line_vencimento)

        self.line_pagamento = QLineEdit(self.frame_2)
        self.line_pagamento.setObjectName(u"line_pagamento")
        self.line_pagamento.setMaximumSize(QSize(100, 16777215))
        self.line_pagamento.setReadOnly(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.line_pagamento)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.checkBox = QCheckBox(self.frame_5)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_3.addWidget(self.checkBox)

        self.horizontalSpacer_2 = QSpacerItem(169, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_novo_valor = QFrame(self.centralwidget)
        self.frame_novo_valor.setObjectName(u"frame_novo_valor")
        self.frame_novo_valor.setFrameShape(QFrame.StyledPanel)
        self.frame_novo_valor.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_novo_valor)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.label_8 = QLabel(self.frame_novo_valor)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 0))

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.line_novo_valor = QLineEdit(self.frame_novo_valor)
        self.line_novo_valor.setObjectName(u"line_novo_valor")
        self.line_novo_valor.setMaximumSize(QSize(150, 16777215))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.line_novo_valor)


        self.verticalLayout.addWidget(self.frame_novo_valor)

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

        pagar_parcela.setCentralWidget(self.centralwidget)

        self.retranslateUi(pagar_parcela)

        QMetaObject.connectSlotsByName(pagar_parcela)
    # setupUi

    def retranslateUi(self, pagar_parcela):
        pagar_parcela.setWindowTitle(QCoreApplication.translate("pagar_parcela", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("pagar_parcela", u" Parcela", None))
        self.label_2.setText(QCoreApplication.translate("pagar_parcela", u"id", None))
        self.label_3.setText(QCoreApplication.translate("pagar_parcela", u"n\u00ba", None))
        self.label_4.setText(QCoreApplication.translate("pagar_parcela", u"Valor", None))
        self.label_5.setText(QCoreApplication.translate("pagar_parcela", u"Vencimento", None))
        self.label_6.setText(QCoreApplication.translate("pagar_parcela", u"Pagamento", None))
        self.label_7.setText(QCoreApplication.translate("pagar_parcela", u"Estado", None))
        self.checkBox.setText(QCoreApplication.translate("pagar_parcela", u"Pagar parte do valor", None))
        self.label_8.setText(QCoreApplication.translate("pagar_parcela", u"Novo Valor", None))
        self.btn_pagar.setText(QCoreApplication.translate("pagar_parcela", u"PAGAR", None))
        self.btn_cancelar.setText(QCoreApplication.translate("pagar_parcela", u"CANCELAR", None))
    # retranslateUi

