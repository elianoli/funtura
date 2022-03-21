# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'receber_parcelaWZgomN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_janela_receber_parcela(object):
    def setupUi(self, janela_receber_parcela):
        if not janela_receber_parcela.objectName():
            janela_receber_parcela.setObjectName(u"janela_receber_parcela")
        janela_receber_parcela.setWindowModality(Qt.ApplicationModal)
        janela_receber_parcela.resize(800, 600)
        janela_receber_parcela.setMinimumSize(QSize(800, 600))
        janela_receber_parcela.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(janela_receber_parcela)
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
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 0))
        self.label_2.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.line_os = QLineEdit(self.frame_4)
        self.line_os.setObjectName(u"line_os")
        self.line_os.setMinimumSize(QSize(200, 25))
        self.line_os.setMaximumSize(QSize(200, 25))

        self.horizontalLayout_3.addWidget(self.line_os)

        self.btn_procurar = QPushButton(self.frame_4)
        self.btn_procurar.setObjectName(u"btn_procurar")
        self.btn_procurar.setStyleSheet(u"QPushButton{\n"
"	font: 87 8pt \"Arial Black\";\n"
"	border: 0.5px solid #44475a;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #44475a;\n"
"	min-width: 123;\n"
"	max-width: 123;\n"
"	min-height: 28;\n"
"	max-height: 28;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #4f5368;\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_procurar)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 0))
        self.label_3.setMaximumSize(QSize(120, 16777215))

        self.verticalLayout_2.addWidget(self.label_3)

        self.tab_rec_par = QTableWidget(self.frame_5)
        if (self.tab_rec_par.columnCount() < 6):
            self.tab_rec_par.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tab_rec_par.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tab_rec_par.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tab_rec_par.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tab_rec_par.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tab_rec_par.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tab_rec_par.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tab_rec_par.setObjectName(u"tab_rec_par")

        self.verticalLayout_2.addWidget(self.tab_rec_par)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.btn_anterior = QPushButton(self.frame_6)
        self.btn_anterior.setObjectName(u"btn_anterior")

        self.horizontalLayout_4.addWidget(self.btn_anterior)

        self.btn_proximo = QPushButton(self.frame_6)
        self.btn_proximo.setObjectName(u"btn_proximo")

        self.horizontalLayout_4.addWidget(self.btn_proximo)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_2)

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

        janela_receber_parcela.setCentralWidget(self.centralwidget)

        self.retranslateUi(janela_receber_parcela)

        QMetaObject.connectSlotsByName(janela_receber_parcela)
    # setupUi

    def retranslateUi(self, janela_receber_parcela):
        janela_receber_parcela.setWindowTitle(QCoreApplication.translate("janela_receber_parcela", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("janela_receber_parcela", u"Receber Parcela", None))
        self.label_2.setText(QCoreApplication.translate("janela_receber_parcela", u"Ordem de Servi\u00e7o", None))
        self.btn_procurar.setText(QCoreApplication.translate("janela_receber_parcela", u"PROCURAR", None))
        self.label_3.setText(QCoreApplication.translate("janela_receber_parcela", u"Parcelas", None))
        ___qtablewidgetitem = self.tab_rec_par.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("janela_receber_parcela", u"id ", None));
        ___qtablewidgetitem1 = self.tab_rec_par.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("janela_receber_parcela", u"n\u00ba Parcela", None));
        ___qtablewidgetitem2 = self.tab_rec_par.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("janela_receber_parcela", u"Valor", None));
        ___qtablewidgetitem3 = self.tab_rec_par.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("janela_receber_parcela", u"Vencimento", None));
        ___qtablewidgetitem4 = self.tab_rec_par.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("janela_receber_parcela", u"Pagamento", None));
        ___qtablewidgetitem5 = self.tab_rec_par.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("janela_receber_parcela", u"Estado", None));
        self.btn_anterior.setText(QCoreApplication.translate("janela_receber_parcela", u"ANTERIOR", None))
        self.btn_proximo.setText(QCoreApplication.translate("janela_receber_parcela", u"PR\u00d3XIMO", None))
        self.btn_pagar.setText(QCoreApplication.translate("janela_receber_parcela", u"PAGAR", None))
        self.btn_cancelar.setText(QCoreApplication.translate("janela_receber_parcela", u"CANCELAR", None))
    # retranslateUi

