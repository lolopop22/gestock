# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_client.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

from mysql import connector

class Ui_clients_dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(548, 625)
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
"	selction-background-color: #290B9;\n"
"}")
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 548, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 281, 31))
        font = QFont()
        font.setFamilies([u"Courier"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 81, 531, 477))
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Courier"])
        font1.setPointSize(15)
        font1.setBold(False)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.prenom_lineEdit = QLineEdit(self.widget)
        self.prenom_lineEdit.setObjectName(u"prenom_lineEdit")
        self.prenom_lineEdit.setMinimumSize(QSize(0, 35))
        self.prenom_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.prenom_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.nom_lineEdit = QLineEdit(self.widget)
        self.nom_lineEdit.setObjectName(u"nom_lineEdit")
        self.nom_lineEdit.setMinimumSize(QSize(0, 35))
        self.nom_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.nom_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(205, 15))
        font2 = QFont()
        font2.setFamilies([u"Courier"])
        font2.setPointSize(15)
        self.label_6.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_6)

        self.genre_comboBox = QComboBox(self.widget)
        self.genre_comboBox.addItem("")
        self.genre_comboBox.addItem("")
        self.genre_comboBox.setObjectName(u"genre_comboBox")
        self.genre_comboBox.setMaximumSize(QSize(205, 30))

        self.verticalLayout_5.addWidget(self.genre_comboBox)


        self.verticalLayout_8.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.entreprise_lineEdit = QLineEdit(self.widget)
        self.entreprise_lineEdit.setObjectName(u"entreprise_lineEdit")
        self.entreprise_lineEdit.setMinimumSize(QSize(0, 35))
        self.entreprise_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.entreprise_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.adresse_lineEdit = QLineEdit(self.widget)
        self.adresse_lineEdit.setObjectName(u"adresse_lineEdit")
        self.adresse_lineEdit.setMinimumSize(QSize(0, 35))
        self.adresse_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.adresse_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_7)

        self.telephone_lineEdit = QLineEdit(self.widget)
        self.telephone_lineEdit.setObjectName(u"telephone_lineEdit")
        self.telephone_lineEdit.setMinimumSize(QSize(0, 35))
        self.telephone_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_6.addWidget(self.telephone_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_8)

        self.mail_lineEdit = QLineEdit(self.widget)
        self.mail_lineEdit.setObjectName(u"mail_lineEdit")
        self.mail_lineEdit.setMinimumSize(QSize(0, 35))
        self.mail_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_7.addWidget(self.mail_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.widget1 = QWidget(self)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(280, 570, 261, 34))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.annule_buton = QPushButton(self.widget1)
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

        self.ok_bouton = QPushButton(self.widget1)
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


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, clients_dialog):
        clients_dialog.setWindowTitle(QCoreApplication.translate("clients_dialog", u"Ajout nouveau client", None))
        self.label.setText(QCoreApplication.translate("clients_dialog", u"Ajouter nouveau client", None))
        self.label_2.setText(QCoreApplication.translate("clients_dialog", u"Pr\u00e9nom", None))
        self.label_3.setText(QCoreApplication.translate("clients_dialog", u"Nom", None))
        self.label_6.setText(QCoreApplication.translate("clients_dialog", u"S\u00e9lectionner le genre", None))
        self.genre_comboBox.setItemText(0, QCoreApplication.translate("clients_dialog", u"Femme", None))
        self.genre_comboBox.setItemText(1, QCoreApplication.translate("clients_dialog", u"Homme", None))

        self.label_4.setText(QCoreApplication.translate("clients_dialog", u"Entreprise", None))
        self.label_5.setText(QCoreApplication.translate("clients_dialog", u"Adresse", None))
        self.label_7.setText(QCoreApplication.translate("clients_dialog", u"T\u00e9l\u00e9phone", None))
        self.label_8.setText(QCoreApplication.translate("clients_dialog", u"Email", None))
        self.annule_buton.setText(QCoreApplication.translate("clients_dialog", u"Annuler", None))
        self.ok_bouton.setText(QCoreApplication.translate("clients_dialog", u"OK", None))
    # retranslateUi

    # CREATE DATABASE CONNECTION
    def create_connection(self):

        host_name = "localhost"
        user_name = "root"
        pass_word = "root"
        database_name = "gestock_db"

        # Establish conection to mysql server
        self.mydb = connector.connect(
            host = host_name,
            user = user_name,
            password = pass_word
        )

        # Create a cursor to execute SQL queries
        cursor = self.mydb.cursor()

        # Create database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

        # Connect to the created database
        self.mydb = connector.connect(
            host = host_name,
            user = user_name,
            password = pass_word,
            database = database_name
        )

        return self.mydb