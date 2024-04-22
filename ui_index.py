# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import ressources2_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1231, 725)
        MainWindow.setMinimumSize(QSize(1231, 725))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(85, 0))
        self.icon_only_widget.setMaximumSize(QSize(85, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	border-radius:3px\n"
"}\n"
"")
        self.verticalLayout_14 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(10, -1, -1, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.icon_only_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u":/icones/logo.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_14.addLayout(self.horizontalLayout_2)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(30)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 20, -1, -1)
        self.dashboard_1 = QPushButton(self.icon_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        icon = QIcon()
        icon.addFile(u":/icones/dashboardsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icones/dashboardsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setIconSize(QSize(25, 25))
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.dashboard_1)

        self.entrepots_1 = QPushButton(self.icon_only_widget)
        self.entrepots_1.setObjectName(u"entrepots_1")
        icon1 = QIcon()
        icon1.addFile(u":/icones/entrepotsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icones/entrepotsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.entrepots_1.setIcon(icon1)
        self.entrepots_1.setIconSize(QSize(25, 25))
        self.entrepots_1.setCheckable(True)
        self.entrepots_1.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.entrepots_1)

        self.clients_1 = QPushButton(self.icon_only_widget)
        self.clients_1.setObjectName(u"clients_1")
        icon2 = QIcon()
        icon2.addFile(u":/icones/clientsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icones/clientsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.clients_1.setIcon(icon2)
        self.clients_1.setIconSize(QSize(25, 25))
        self.clients_1.setCheckable(True)
        self.clients_1.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.clients_1)

        self.fournisseurs_1 = QPushButton(self.icon_only_widget)
        self.fournisseurs_1.setObjectName(u"fournisseurs_1")
        icon3 = QIcon()
        icon3.addFile(u":/icones/fournisseursmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icones/fournisseursmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.fournisseurs_1.setIcon(icon3)
        self.fournisseurs_1.setIconSize(QSize(25, 25))
        self.fournisseurs_1.setCheckable(True)
        self.fournisseurs_1.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.fournisseurs_1)

        self.comptabilite_1 = QPushButton(self.icon_only_widget)
        self.comptabilite_1.setObjectName(u"comptabilite_1")
        icon4 = QIcon()
        icon4.addFile(u":/icones/comptabilitesmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icones/comptabilitesmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.comptabilite_1.setIcon(icon4)
        self.comptabilite_1.setIconSize(QSize(25, 25))
        self.comptabilite_1.setCheckable(True)
        self.comptabilite_1.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.comptabilite_1)


        self.verticalLayout_14.addLayout(self.verticalLayout_11)

        self.verticalSpacer_2 = QSpacerItem(20, 281, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_2)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(20)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, -1, -1, 0)
        self.parametre_1 = QPushButton(self.icon_only_widget)
        self.parametre_1.setObjectName(u"parametre_1")
        icon5 = QIcon()
        icon5.addFile(u":/icones/parametresmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/icones/parametresmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.parametre_1.setIcon(icon5)
        self.parametre_1.setIconSize(QSize(25, 25))
        self.parametre_1.setCheckable(True)
        self.parametre_1.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.parametre_1)

        self.deconnexion_1 = QPushButton(self.icon_only_widget)
        self.deconnexion_1.setObjectName(u"deconnexion_1")
        self.deconnexion_1.setStyleSheet(u"QPushButton{\n"
"	padding-left:10px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icones/deconnexionsmall1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/icones/deconnexionsmall2.png", QSize(), QIcon.Normal, QIcon.On)
        self.deconnexion_1.setIcon(icon6)
        self.deconnexion_1.setIconSize(QSize(25, 25))
        self.deconnexion_1.setCheckable(True)
        self.deconnexion_1.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.deconnexion_1)


        self.verticalLayout_14.addLayout(self.verticalLayout_12)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_text_widget = QWidget(self.centralwidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setMaximumSize(QSize(16777215, 16777215))
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"	height:30px;\n"
"	border:none;\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(10, 11, -1, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, -1, -1, -1)
        self.label_2 = QLabel(self.icon_text_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/icones/logo.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_text_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Courier"])
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_13.addLayout(self.horizontalLayout)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(18)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 20, -1, 45)
        self.dashboard_2 = QPushButton(self.icon_text_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-60px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	border-radius:3px\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icones/dashboard1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/icones/dashboard2.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_2.setIcon(icon7)
        self.dashboard_2.setIconSize(QSize(125, 100))
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.dashboard_2)

        self.entrepots = QFrame(self.icon_text_widget)
        self.entrepots.setObjectName(u"entrepots")
        self.entrepots.setFrameShape(QFrame.Shape.StyledPanel)
        self.entrepots.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.entrepots)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.entrepots_2 = QPushButton(self.entrepots)
        self.entrepots_2.setObjectName(u"entrepots_2")
        self.entrepots_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-60px;\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/icones/entrepot_down1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u":/icones/entrepot_up1.png", QSize(), QIcon.Normal, QIcon.On)
        self.entrepots_2.setIcon(icon8)
        self.entrepots_2.setIconSize(QSize(125, 100))
        self.entrepots_2.setCheckable(True)
        self.entrepots_2.setChecked(False)
        self.entrepots_2.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.entrepots_2)

        self.entrepots_dropdown = QFrame(self.entrepots)
        self.entrepots_dropdown.setObjectName(u"entrepots_dropdown")
        self.entrepots_dropdown.setFrameShape(QFrame.Shape.StyledPanel)
        self.entrepots_dropdown.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.entrepots_dropdown)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.entrepots_marchandise = QPushButton(self.entrepots_dropdown)
        self.entrepots_marchandise.setObjectName(u"entrepots_marchandise")
        self.entrepots_marchandise.setStyleSheet(u"QPushButton{\n"
"	padding-left:-30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#679cdb;\n"
"}")
        self.entrepots_marchandise.setCheckable(True)

        self.verticalLayout_3.addWidget(self.entrepots_marchandise)

        self.entrepots_commande = QPushButton(self.entrepots_dropdown)
        self.entrepots_commande.setObjectName(u"entrepots_commande")
        self.entrepots_commande.setStyleSheet(u"QPushButton{\n"
"	padding-left:-35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#679cdb;\n"
"}")
        self.entrepots_commande.setCheckable(True)

        self.verticalLayout_3.addWidget(self.entrepots_commande)


        self.verticalLayout_5.addWidget(self.entrepots_dropdown)


        self.verticalLayout_7.addWidget(self.entrepots)

        self.clients = QFrame(self.icon_text_widget)
        self.clients.setObjectName(u"clients")
        self.clients.setFrameShape(QFrame.Shape.StyledPanel)
        self.clients.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.clients)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.clients_2 = QPushButton(self.clients)
        self.clients_2.setObjectName(u"clients_2")
        self.clients_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-60px;\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icones/client_down1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/icones/client_up1.png", QSize(), QIcon.Normal, QIcon.On)
        self.clients_2.setIcon(icon9)
        self.clients_2.setIconSize(QSize(125, 100))
        self.clients_2.setCheckable(True)
        self.clients_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.clients_2)

        self.clients_dropdown = QFrame(self.clients)
        self.clients_dropdown.setObjectName(u"clients_dropdown")
        self.clients_dropdown.setFrameShape(QFrame.Shape.StyledPanel)
        self.clients_dropdown.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.clients_dropdown)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.client_info = QPushButton(self.clients_dropdown)
        self.client_info.setObjectName(u"client_info")
        self.client_info.setStyleSheet(u"QPushButton{\n"
"	padding-left:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#679cdb;\n"
"}")
        self.client_info.setCheckable(True)

        self.verticalLayout.addWidget(self.client_info)

        self.client_transaction = QPushButton(self.clients_dropdown)
        self.client_transaction.setObjectName(u"client_transaction")
        self.client_transaction.setStyleSheet(u"QPushButton{\n"
"	padding-left:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#679cdb;\n"
"}")
        self.client_transaction.setCheckable(True)

        self.verticalLayout.addWidget(self.client_transaction)


        self.verticalLayout_4.addWidget(self.clients_dropdown)


        self.verticalLayout_7.addWidget(self.clients)

        self.fournisseurs = QFrame(self.icon_text_widget)
        self.fournisseurs.setObjectName(u"fournisseurs")
        self.fournisseurs.setFrameShape(QFrame.Shape.StyledPanel)
        self.fournisseurs.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.fournisseurs)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.fournisseurs_2 = QPushButton(self.fournisseurs)
        self.fournisseurs_2.setObjectName(u"fournisseurs_2")
        self.fournisseurs_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-60px;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icones/fournisseur_down1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u":/icones/fournisseur_up1.png", QSize(), QIcon.Normal, QIcon.On)
        self.fournisseurs_2.setIcon(icon10)
        self.fournisseurs_2.setIconSize(QSize(125, 100))
        self.fournisseurs_2.setCheckable(True)
        self.fournisseurs_2.setChecked(False)
        self.fournisseurs_2.setAutoExclusive(False)

        self.verticalLayout_9.addWidget(self.fournisseurs_2)

        self.fournisseurs_dropdown = QFrame(self.fournisseurs)
        self.fournisseurs_dropdown.setObjectName(u"fournisseurs_dropdown")
        self.fournisseurs_dropdown.setFrameShape(QFrame.Shape.StyledPanel)
        self.fournisseurs_dropdown.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.fournisseurs_dropdown)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.fournisseurs_info = QPushButton(self.fournisseurs_dropdown)
        self.fournisseurs_info.setObjectName(u"fournisseurs_info")
        self.fournisseurs_info.setStyleSheet(u"QPushButton{\n"
"	padding-left:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#679cdb;\n"
"}")
        self.fournisseurs_info.setCheckable(True)

        self.verticalLayout_10.addWidget(self.fournisseurs_info)

        self.fournisseurs_transaction = QPushButton(self.fournisseurs_dropdown)
        self.fournisseurs_transaction.setObjectName(u"fournisseurs_transaction")
        self.fournisseurs_transaction.setStyleSheet(u"QPushButton{\n"
"	padding-left:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#679cdb;\n"
"}")
        self.fournisseurs_transaction.setCheckable(True)

        self.verticalLayout_10.addWidget(self.fournisseurs_transaction)


        self.verticalLayout_9.addWidget(self.fournisseurs_dropdown)


        self.verticalLayout_7.addWidget(self.fournisseurs)

        self.comptabilite = QFrame(self.icon_text_widget)
        self.comptabilite.setObjectName(u"comptabilite")
        self.comptabilite.setFrameShape(QFrame.Shape.StyledPanel)
        self.comptabilite.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.comptabilite)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.comptabilite_2 = QPushButton(self.comptabilite)
        self.comptabilite_2.setObjectName(u"comptabilite_2")
        self.comptabilite_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.comptabilite_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-60px;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icones/comptabilite_down1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon11.addFile(u":/icones/comptabilite_up1.png", QSize(), QIcon.Normal, QIcon.On)
        self.comptabilite_2.setIcon(icon11)
        self.comptabilite_2.setIconSize(QSize(125, 100))
        self.comptabilite_2.setCheckable(True)
        self.comptabilite_2.setAutoExclusive(False)

        self.verticalLayout_6.addWidget(self.comptabilite_2)

        self.comptabilite_dropdown = QFrame(self.comptabilite)
        self.comptabilite_dropdown.setObjectName(u"comptabilite_dropdown")
        self.comptabilite_dropdown.setFrameShape(QFrame.Shape.StyledPanel)
        self.comptabilite_dropdown.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.comptabilite_dropdown)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comptabilite_budget = QPushButton(self.comptabilite_dropdown)
        self.comptabilite_budget.setObjectName(u"comptabilite_budget")
        font1 = QFont()
        font1.setPointSize(13)
        self.comptabilite_budget.setFont(font1)
        self.comptabilite_budget.setStyleSheet(u"QPushButton{\n"
"	padding-left:-72px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#679cdb;\n"
"}")
        self.comptabilite_budget.setCheckable(True)

        self.verticalLayout_2.addWidget(self.comptabilite_budget)

        self.comptabilite_depense = QPushButton(self.comptabilite_dropdown)
        self.comptabilite_depense.setObjectName(u"comptabilite_depense")
        self.comptabilite_depense.setStyleSheet(u"QPushButton{\n"
"	padding-left:-58px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#679cdb;\n"
"}")
        self.comptabilite_depense.setCheckable(True)

        self.verticalLayout_2.addWidget(self.comptabilite_depense)


        self.verticalLayout_6.addWidget(self.comptabilite_dropdown)


        self.verticalLayout_7.addWidget(self.comptabilite)


        self.verticalLayout_13.addLayout(self.verticalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 596, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.parametre_2 = QPushButton(self.icon_text_widget)
        self.parametre_2.setObjectName(u"parametre_2")
        self.parametre_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-60px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	border-radius:3px\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icones/parametre1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon12.addFile(u":/icones/parametre2.png", QSize(), QIcon.Normal, QIcon.On)
        self.parametre_2.setIcon(icon12)
        self.parametre_2.setIconSize(QSize(125, 100))
        self.parametre_2.setCheckable(True)
        self.parametre_2.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.parametre_2)

        self.deconnexion_2 = QPushButton(self.icon_text_widget)
        self.deconnexion_2.setObjectName(u"deconnexion_2")
        self.deconnexion_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-50px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	border-radius:3px\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icones/deconnexion1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon13.addFile(u":/icones/deconnexion2.png", QSize(), QIcon.Normal, QIcon.On)
        self.deconnexion_2.setIcon(icon13)
        self.deconnexion_2.setIconSize(QSize(125, 100))
        self.deconnexion_2.setCheckable(True)
        self.deconnexion_2.setAutoExclusive(False)

        self.verticalLayout_8.addWidget(self.deconnexion_2)


        self.verticalLayout_13.addLayout(self.verticalLayout_8)


        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
#ifndef Q_OS_MAC
        self.verticalLayout_16.setSpacing(-1)
#endif
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 6, -1, -1)
        self.header_widget = QWidget(self.centralwidget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMinimumSize(QSize(881, 66))
        self.header_widget.setMaximumSize(QSize(16777215, 66))
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 5, -1, 15)
        self.pushButton = QPushButton(self.header_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border:none;")
        icon14 = QIcon()
        icon14.addFile(u":/icones/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon14)
        self.pushButton.setIconSize(QSize(29, 35))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label = QLabel(self.header_widget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label.setFont(font2)

        self.verticalLayout_15.addWidget(self.label)

        self.label_5 = QLabel(self.header_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(169, 169, 169);")

        self.verticalLayout_15.addWidget(self.label_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_15)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(358, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 10, -1)
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 31))
        self.lineEdit.setMaximumSize(QSize(16777215, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_6 = QLabel(self.header_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(40, 40))
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setPixmap(QPixmap(u":/icones/profile.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_6)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_16.addWidget(self.header_widget)

        self.main_screen_widget = QWidget(self.centralwidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(883, 765))
        self.main_screen_widget.setStyleSheet(u"")
        self.verticalLayout_17 = QVBoxLayout(self.main_screen_widget)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 2, 0)
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(883, 765))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget.setStyleSheet(u"")
        self.page_00 = QWidget()
        self.page_00.setObjectName(u"page_00")
        self.label_7 = QLabel(self.page_00)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(290, 290, 271, 71))
        font3 = QFont()
        font3.setPointSize(25)
        self.label_7.setFont(font3)
        self.stackedWidget.addWidget(self.page_00)
        self.page_01 = QWidget()
        self.page_01.setObjectName(u"page_01")
        self.label_8 = QLabel(self.page_01)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(350, 270, 271, 71))
        self.label_8.setFont(font3)
        self.stackedWidget.addWidget(self.page_01)
        self.page_02 = QWidget()
        self.page_02.setObjectName(u"page_02")
        self.label_9 = QLabel(self.page_02)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(410, 240, 271, 71))
        self.label_9.setFont(font3)
        self.stackedWidget.addWidget(self.page_02)
        self.page_03 = QWidget()
        self.page_03.setObjectName(u"page_03")
        self.page_03.setMinimumSize(QSize(883, 0))
        self.label_10 = QLabel(self.page_03)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 0, 291, 51))
        font4 = QFont()
        font4.setFamilies([u"Courier"])
        font4.setPointSize(23)
        font4.setWeight(QFont.DemiBold)
        self.label_10.setFont(font4)
        self.label_17 = QLabel(self.page_03)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 40, 291, 51))
        font5 = QFont()
        font5.setFamilies([u"Courier"])
        font5.setPointSize(12)
        font5.setBold(False)
        self.label_17.setFont(font5)
        self.table_infos_client = QTableWidget(self.page_03)
        if (self.table_infos_client.columnCount() < 9):
            self.table_infos_client.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_infos_client.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_infos_client.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_infos_client.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_infos_client.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_infos_client.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_infos_client.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_infos_client.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_infos_client.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_infos_client.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.table_infos_client.setObjectName(u"table_infos_client")
        self.table_infos_client.setGeometry(QRect(10, 141, 885, 461))
        self.table_infos_client.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_client.setAlternatingRowColors(True)
        self.widget = QWidget(self.page_03)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 80, 821, 45))
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ajout_client_btn = QPushButton(self.widget)
        self.ajout_client_btn.setObjectName(u"ajout_client_btn")
        self.ajout_client_btn.setMinimumSize(QSize(0, 32))
        self.ajout_client_btn.setMaximumSize(QSize(122, 32))
        self.ajout_client_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/icones/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ajout_client_btn.setIcon(icon15)

        self.horizontalLayout_6.addWidget(self.ajout_client_btn)

        self.export_excel_btn = QPushButton(self.widget)
        self.export_excel_btn.setObjectName(u"export_excel_btn")
        self.export_excel_btn.setMinimumSize(QSize(0, 32))
        self.export_excel_btn.setMaximumSize(QSize(122, 32))
        self.export_excel_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/icones/excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.export_excel_btn.setIcon(icon16)

        self.horizontalLayout_6.addWidget(self.export_excel_btn)

        self.export_pdf_btn = QPushButton(self.widget)
        self.export_pdf_btn.setObjectName(u"export_pdf_btn")
        self.export_pdf_btn.setMinimumSize(QSize(0, 32))
        self.export_pdf_btn.setMaximumSize(QSize(122, 32))
        self.export_pdf_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 58, 21);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/icones/pdf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.export_pdf_btn.setIcon(icon17)

        self.horizontalLayout_6.addWidget(self.export_pdf_btn)

        self.cherche_client = QLineEdit(self.widget)
        self.cherche_client.setObjectName(u"cherche_client")
        self.cherche_client.setMinimumSize(QSize(0, 32))
        self.cherche_client.setMaximumSize(QSize(407, 31))
        self.cherche_client.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")

        self.horizontalLayout_6.addWidget(self.cherche_client)

        self.stackedWidget.addWidget(self.page_03)
        self.page_04 = QWidget()
        self.page_04.setObjectName(u"page_04")
        self.label_11 = QLabel(self.page_04)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(260, 250, 271, 71))
        self.label_11.setFont(font3)
        self.stackedWidget.addWidget(self.page_04)
        self.page_05 = QWidget()
        self.page_05.setObjectName(u"page_05")
        self.label_12 = QLabel(self.page_05)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(290, 240, 271, 71))
        self.label_12.setFont(font3)
        self.stackedWidget.addWidget(self.page_05)
        self.page_06 = QWidget()
        self.page_06.setObjectName(u"page_06")
        self.label_13 = QLabel(self.page_06)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(260, 260, 281, 71))
        self.label_13.setFont(font3)
        self.stackedWidget.addWidget(self.page_06)
        self.page_07 = QWidget()
        self.page_07.setObjectName(u"page_07")
        self.label_14 = QLabel(self.page_07)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(340, 240, 271, 71))
        self.label_14.setFont(font3)
        self.stackedWidget.addWidget(self.page_07)
        self.page_08 = QWidget()
        self.page_08.setObjectName(u"page_08")
        self.label_15 = QLabel(self.page_08)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(520, 210, 271, 71))
        self.label_15.setFont(font3)
        self.stackedWidget.addWidget(self.page_08)
        self.page_09 = QWidget()
        self.page_09.setObjectName(u"page_09")
        self.label_16 = QLabel(self.page_09)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(310, 250, 271, 71))
        self.label_16.setFont(font3)
        self.stackedWidget.addWidget(self.page_09)

        self.verticalLayout_17.addWidget(self.stackedWidget)


        self.verticalLayout_16.addWidget(self.main_screen_widget)


        self.gridLayout.addLayout(self.verticalLayout_16, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1231, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.clients_2.toggled.connect(self.clients_dropdown.setHidden)
        self.entrepots_2.toggled.connect(self.entrepots_dropdown.setHidden)
        self.comptabilite_2.toggled.connect(self.comptabilite_dropdown.setHidden)
        self.fournisseurs_2.toggled.connect(self.fournisseurs_dropdown.setHidden)
        self.entrepots_2.toggled.connect(self.entrepots_1.setChecked)
        self.clients_2.toggled.connect(self.clients_1.setChecked)
        self.fournisseurs_2.toggled.connect(self.fournisseurs_1.setChecked)
        self.comptabilite_2.toggled.connect(self.comptabilite_1.setChecked)
        self.parametre_2.toggled.connect(self.parametre_1.setChecked)
        self.deconnexion_2.toggled.connect(self.deconnexion_1.setChecked)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.deconnexion_1.toggled.connect(MainWindow.close)
        self.deconnexion_2.toggled.connect(MainWindow.close)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_only_widget.setVisible)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.dashboard_1.setText("")
        self.entrepots_1.setText("")
        self.clients_1.setText("")
        self.fournisseurs_1.setText("")
        self.comptabilite_1.setText("")
        self.parametre_1.setText("")
        self.deconnexion_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"GeStock", None))
        self.dashboard_2.setText("")
        self.entrepots_2.setText("")
        self.entrepots_marchandise.setText(QCoreApplication.translate("MainWindow", u"Marchandises", None))
        self.entrepots_commande.setText(QCoreApplication.translate("MainWindow", u"Commandes", None))
        self.clients_2.setText("")
        self.client_info.setText(QCoreApplication.translate("MainWindow", u"Informations clients", None))
        self.client_transaction.setText(QCoreApplication.translate("MainWindow", u"Transactions clients", None))
        self.fournisseurs_2.setText("")
        self.fournisseurs_info.setText(QCoreApplication.translate("MainWindow", u"Informations fournisseurs", None))
        self.fournisseurs_transaction.setText(QCoreApplication.translate("MainWindow", u"Transactions fournisseurs", None))
        self.comptabilite_2.setText("")
        self.comptabilite_budget.setText(QCoreApplication.translate("MainWindow", u"Budget", None))
        self.comptabilite_depense.setText(QCoreApplication.translate("MainWindow", u"D\u00e9penses", None))
        self.parametre_2.setText("")
        self.deconnexion_2.setText("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bonjour Tartapion,", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Bienvenue!!!", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recherche...", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tableau de bord", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Marchandises", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Commandes", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Informations clients", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Hello", None))
        ___qtablewidgetitem = self.table_infos_client.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID Client", None));
        ___qtablewidgetitem1 = self.table_infos_client.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom", None));
        ___qtablewidgetitem2 = self.table_infos_client.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem3 = self.table_infos_client.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Genre", None));
        ___qtablewidgetitem4 = self.table_infos_client.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Entreprise", None));
        ___qtablewidgetitem5 = self.table_infos_client.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Adresse", None));
        ___qtablewidgetitem6 = self.table_infos_client.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"T\u00e9l\u00e9phone", None));
        ___qtablewidgetitem7 = self.table_infos_client.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem8 = self.table_infos_client.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.ajout_client_btn.setText(QCoreApplication.translate("MainWindow", u"Ajouter client", None))
        self.export_excel_btn.setText(QCoreApplication.translate("MainWindow", u"Export Excel", None))
        self.export_pdf_btn.setText(QCoreApplication.translate("MainWindow", u"Export PDF", None))
        self.cherche_client.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher client...", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Transactions Clients", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Informations fournisseurs", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Transactions fournisseurs", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Budget", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"D\u00e9penses", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Param\u00e8tres", None))
    # retranslateUi

