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
    QVBoxLayout, QWidget, QMessageBox)

import back_logicel_gestion_stock as bk

class Ui_client_dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(520, 491)
        self.setMinimumSize(QSize(520, 440))
        self.setMaximumSize(QSize(520, 16777215))
        font = QFont()
        font.setFamilies([u"Courier"])
        self.setFont(font)
        self.setStyleSheet(u"QDialog{\n"
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
"	selection-background-color: #2980B9;\n"
"}")
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 548, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 281, 31))
        font1 = QFont()
        font1.setFamilies([u"Courier"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 81, 501, 342))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"Courier"])
        font2.setPointSize(15)
        font2.setBold(False)
        self.label_3.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_3)

        self.line_edit_nom = QLineEdit(self.layoutWidget)
        self.line_edit_nom.setObjectName(u"line_edit_nom")
        self.line_edit_nom.setMinimumSize(QSize(0, 35))
        self.line_edit_nom.setMaximumSize(QSize(16777215, 35))
        self.line_edit_nom.setFont(font)

        self.verticalLayout_2.addWidget(self.line_edit_nom)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_6)

        self.line_edit_entreprise = QLineEdit(self.layoutWidget)
        self.line_edit_entreprise.setObjectName(u"line_edit_entreprise")
        self.line_edit_entreprise.setMinimumSize(QSize(0, 35))
        self.line_edit_entreprise.setMaximumSize(QSize(16777215, 35))
        self.line_edit_entreprise.setFont(font)

        self.verticalLayout_5.addWidget(self.line_edit_entreprise)


        self.verticalLayout_8.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_5)

        self.line_edit_adresse = QLineEdit(self.layoutWidget)
        self.line_edit_adresse.setObjectName(u"line_edit_adresse")
        self.line_edit_adresse.setMinimumSize(QSize(0, 35))
        self.line_edit_adresse.setMaximumSize(QSize(16777215, 35))
        self.line_edit_adresse.setFont(font)

        self.verticalLayout_4.addWidget(self.line_edit_adresse)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
#ifndef Q_OS_MAC
        self.verticalLayout_6.setSpacing(-1)
#endif
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_7)

        self.line_edit_contact = QLineEdit(self.layoutWidget)
        self.line_edit_contact.setObjectName(u"line_edit_contact")
        self.line_edit_contact.setMinimumSize(QSize(0, 35))
        self.line_edit_contact.setMaximumSize(QSize(16777215, 35))
        self.line_edit_contact.setFont(font)

        self.verticalLayout_6.addWidget(self.line_edit_contact)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_8)

        self.line_edit_email = QLineEdit(self.layoutWidget)
        self.line_edit_email.setObjectName(u"line_edit_email")
        self.line_edit_email.setMinimumSize(QSize(0, 35))
        self.line_edit_email.setMaximumSize(QSize(16777215, 35))
        self.line_edit_email.setFont(font)

        self.verticalLayout_7.addWidget(self.line_edit_email)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.layoutWidget1 = QWidget(self)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(250, 440, 261, 34))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.annule_buton = QPushButton(self.layoutWidget1)
        self.annule_buton.setObjectName(u"annule_buton")
        self.annule_buton.setMinimumSize(QSize(0, 32))
        font3 = QFont()
        font3.setFamilies([u"Courier"])
        font3.setBold(True)
        self.annule_buton.setFont(font3)
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
        self.ok_bouton.setFont(font3)
        self.ok_bouton.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.ok_bouton)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, client_dialog):
        client_dialog.setWindowTitle(QCoreApplication.translate("client_dialog", u"Client Dialog", None))
        self.label.setText(QCoreApplication.translate("client_dialog", u"Ajouter nouveau client", None))
        self.label_3.setText(QCoreApplication.translate("client_dialog", u"Nom", None))
        self.label_6.setText(QCoreApplication.translate("client_dialog", u"Entreprise", None))
        self.label_5.setText(QCoreApplication.translate("client_dialog", u"Adresse", None))
        self.label_7.setText(QCoreApplication.translate("client_dialog", u"Contact", None))
        self.label_8.setText(QCoreApplication.translate("client_dialog", u"Email", None))
        self.annule_buton.setText(QCoreApplication.translate("client_dialog", u"Annuler", None))
        self.ok_bouton.setText(QCoreApplication.translate("client_dialog", u"OK", None))
    # retranslateUi

        # Add new client when you press on the ok btn
        self.ok_bouton.clicked.connect(self.add_client)
        self.annule_buton.clicked.connect(self.close)

    # INSERT NEW CLIENT
    def insert_new_client(self):
        utilisateur_id = 00
        
        # try:
        nom_client = self.line_edit_nom.text()
        entreprise_client = self.line_edit_entreprise.text()
        adresse_client = self.line_edit_adresse.text()
        contact_client = int(self.line_edit_contact.text())
        email_client = self.line_edit_email.text()

        insert = bk.add_client(nom_client, entreprise_client, adresse_client, contact_client, email_client, utilisateur_id)
        
        self.show_inserted_message(insert)

        # except Exception as e:
        #     print(f"Error: {e}")

    def show_inserted_message(self, ret_insert):
        msg_box = QMessageBox(self)

        # :TODO: the window title doesn't show. Correct it!!

        if ret_insert == "Client ajouté":
            msg_box.setWindowTitle("Succès")
            # msg_box.setIcon(QMessageBox.information)
            msg_box.setText(f"Le client {self.line_edit_nom.text()} a été bien ajouté !")
            msg_box.exec()
        else:
            msg_box.setWindowTitle("Echec")
            # msg_box.setIcon(QMessageBox.warning)
            msg_box.setText(f"Le client {self.line_edit_nom.text()} n'a pas été ajouté.")
            msg_box.exec()
    
    # Signal sent to the front_page.py that says the user has clicked on the ok button and that
    # it is now ok to insert the client in the db and display it on the front page.
    def add_client(self):
        self.insert_new_client()
        self.accept()  # signal sent every time we clicked on the ok btn

