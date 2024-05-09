# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_clients_dialog(QDialog):
    def setupUi(self, clients_dialog):
        if not clients_dialog.objectName():
            clients_dialog.setObjectName(u"clients_dialog")
        clients_dialog.resize(548, 625)
        clients_dialog.setStyleSheet(u"QDialog{\n"
"	background-color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 1px solid grey;\n"
"	border-radius: 6px;\n"
"	padding-left: 15px;\n"
"	height: 35px;\n"
"}\n"
"\n"
"QComboBox{\n"
"	border: 2px solid white;\n"
"	border-radius: 8px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background-color: black;\n"
"	color: white;\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight: bold;\n"
"	selction-background-color: #290B9;\n"
"}")
        self.line = QFrame(clients_dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 548, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(clients_dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 281, 31))
        font = QFont()
        font.setFamilies([u"Courier"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.layoutWidget = QWidget(clients_dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 81, 531, 477))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Courier"])
        font1.setPointSize(15)
        font1.setBold(False)
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.nom_lineEdit = QLineEdit(self.layoutWidget)
        self.nom_lineEdit.setObjectName(u"nom_lineEdit")
        self.nom_lineEdit.setMinimumSize(QSize(0, 35))
        self.nom_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.nom_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.entreprise_lineEdit = QLineEdit(self.layoutWidget)
        self.entreprise_lineEdit.setObjectName(u"entreprise_lineEdit")
        self.entreprise_lineEdit.setMinimumSize(QSize(0, 35))
        self.entreprise_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.entreprise_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.adresse_lineEdit = QLineEdit(self.layoutWidget)
        self.adresse_lineEdit.setObjectName(u"adresse_lineEdit")
        self.adresse_lineEdit.setMinimumSize(QSize(0, 35))
        self.adresse_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.adresse_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_7)

        self.telephone_lineEdit = QLineEdit(self.layoutWidget)
        self.telephone_lineEdit.setObjectName(u"telephone_lineEdit")
        self.telephone_lineEdit.setMinimumSize(QSize(0, 35))
        self.telephone_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_6.addWidget(self.telephone_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_8)

        self.mail_lineEdit = QLineEdit(self.layoutWidget)
        self.mail_lineEdit.setObjectName(u"mail_lineEdit")
        self.mail_lineEdit.setMinimumSize(QSize(0, 35))
        self.mail_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_7.addWidget(self.mail_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.layoutWidget1 = QWidget(clients_dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(280, 570, 261, 34))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.annule_buton = QPushButton(self.layoutWidget1)
        self.annule_buton.setObjectName(u"annule_buton")
        self.annule_buton.setMinimumSize(QSize(0, 32))
        self.annule_buton.setStyleSheet(u"QPushButton{\n"
"	background-color: #585858;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.annule_buton)

        self.ok_bouton = QPushButton(self.layoutWidget1)
        self.ok_bouton.setObjectName(u"ok_bouton")
        self.ok_bouton.setMinimumSize(QSize(0, 32))
        self.ok_bouton.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.ok_bouton)


        self.retranslateUi(clients_dialog)

        QMetaObject.connectSlotsByName(clients_dialog)
    # setupUi

    def retranslateUi(self, clients_dialog):
        clients_dialog.setWindowTitle(QCoreApplication.translate("clients_dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("clients_dialog", u"Ajouter nouveau client", None))
        self.label_3.setText(QCoreApplication.translate("clients_dialog", u"Nom", None))
        self.label_4.setText(QCoreApplication.translate("clients_dialog", u"Entreprise", None))
        self.label_5.setText(QCoreApplication.translate("clients_dialog", u"Adresse", None))
        self.label_7.setText(QCoreApplication.translate("clients_dialog", u"T\u00e9l\u00e9phone", None))
        self.label_8.setText(QCoreApplication.translate("clients_dialog", u"Email", None))
        self.annule_buton.setText(QCoreApplication.translate("clients_dialog", u"Annuler", None))
        self.ok_bouton.setText(QCoreApplication.translate("clients_dialog", u"OK", None))
    # retranslateUi

