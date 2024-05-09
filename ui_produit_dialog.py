# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'produit_dialog.ui'
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
    QSizePolicy, QSpacerItem, QSplitter, QVBoxLayout,
    QWidget)

class Ui_dialog_produit(object):
    def setupUi(self, dialog_produit):
        if not dialog_produit.objectName():
            dialog_produit.setObjectName(u"dialog_produit")
        dialog_produit.resize(441, 465)
        dialog_produit.setMinimumSize(QSize(421, 310))
        dialog_produit.setMaximumSize(QSize(1000000, 1000000))
        dialog_produit.setStyleSheet(u"QDialog{\n"
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
        dialog_produit.setModal(True)
        self.layoutWidget = QWidget(dialog_produit)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(170, 420, 261, 34))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_annulation = QPushButton(self.layoutWidget)
        self.btn_annulation.setObjectName(u"btn_annulation")
        self.btn_annulation.setMinimumSize(QSize(0, 32))
        self.btn_annulation.setStyleSheet(u"QPushButton{\n"
"	background-color: #585858;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.btn_annulation)

        self.btn_ajout_produit = QPushButton(self.layoutWidget)
        self.btn_ajout_produit.setObjectName(u"btn_ajout_produit")
        self.btn_ajout_produit.setMinimumSize(QSize(0, 32))
        self.btn_ajout_produit.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.btn_ajout_produit)

        self.line = QFrame(dialog_produit)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 40, 421, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(dialog_produit)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 291, 31))
        font = QFont()
        font.setFamilies([u"Courier"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.splitter = QSplitter(dialog_produit)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(10, 60, 424, 341))
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.layoutWidget_2 = QWidget(self.splitter)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setFamilies([u"Courier"])
        font1.setPointSize(15)
        font1.setBold(False)
        self.label_6.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_6)

        self.code_produit = QLineEdit(self.layoutWidget_2)
        self.code_produit.setObjectName(u"code_produit")
        self.code_produit.setMinimumSize(QSize(0, 35))
        self.code_produit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_5.addWidget(self.code_produit)

        self.splitter.addWidget(self.layoutWidget_2)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.nom_produit = QLineEdit(self.widget)
        self.nom_produit.setObjectName(u"nom_produit")
        self.nom_produit.setMinimumSize(QSize(0, 35))
        self.nom_produit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.nom_produit)

        self.splitter.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.fournisseur_produits = QComboBox(self.widget1)
        self.fournisseur_produits.setObjectName(u"fournisseur_produits")

        self.verticalLayout_3.addWidget(self.fournisseur_produits)

        self.splitter.addWidget(self.widget1)
        self.widget2 = QWidget(self.splitter)
        self.widget2.setObjectName(u"widget2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.widget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.prix_de_revient = QLineEdit(self.widget2)
        self.prix_de_revient.setObjectName(u"prix_de_revient")
        self.prix_de_revient.setMinimumSize(QSize(0, 35))
        self.prix_de_revient.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.prix_de_revient)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalSpacer = QSpacerItem(118, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.widget2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_7)

        self.prix_de_vente = QLineEdit(self.widget2)
        self.prix_de_vente.setObjectName(u"prix_de_vente")
        self.prix_de_vente.setMinimumSize(QSize(0, 35))
        self.prix_de_vente.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_6.addWidget(self.prix_de_vente)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.splitter.addWidget(self.widget2)

        self.retranslateUi(dialog_produit)
        self.btn_ajout_produit.clicked.connect(dialog_produit.show)

        QMetaObject.connectSlotsByName(dialog_produit)
    # setupUi

    def retranslateUi(self, dialog_produit):
        dialog_produit.setWindowTitle(QCoreApplication.translate("dialog_produit", u"Dialog", None))
        self.btn_annulation.setText(QCoreApplication.translate("dialog_produit", u"Annuler", None))
        self.btn_ajout_produit.setText(QCoreApplication.translate("dialog_produit", u"OK", None))
        self.label.setText(QCoreApplication.translate("dialog_produit", u"Ajouter nouveau produit", None))
        self.label_6.setText(QCoreApplication.translate("dialog_produit", u"Code produit", None))
        self.label_3.setText(QCoreApplication.translate("dialog_produit", u"Nom", None))
        self.label_4.setText(QCoreApplication.translate("dialog_produit", u"Fournisseur", None))
        self.label_5.setText(QCoreApplication.translate("dialog_produit", u"Prix de revient", None))
        self.label_7.setText(QCoreApplication.translate("dialog_produit", u"Prix de vente", None))
    # retranslateUi

