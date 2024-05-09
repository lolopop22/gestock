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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import ressources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1231, 775)
        MainWindow.setMinimumSize(QSize(1231, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1231, 752))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.layoutWidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(90, 750))
        self.icon_only_widget.setMaximumSize(QSize(90, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"	height:30px;\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	border-radius:3px\n"
"}\n"
"")
        self.verticalLayout_14 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, 10)
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
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 10)
        self.btn_dashboard_1 = QPushButton(self.icon_only_widget)
        self.btn_dashboard_1.setObjectName(u"btn_dashboard_1")
        icon = QIcon()
        icon.addFile(u":/icones/small_dashboard1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icones/small_dashboard2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_dashboard_1.setIcon(icon)
        self.btn_dashboard_1.setIconSize(QSize(27, 27))
        self.btn_dashboard_1.setCheckable(True)
        self.btn_dashboard_1.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.btn_dashboard_1)

        self.btn_gestion_referentiels_1 = QPushButton(self.icon_only_widget)
        self.btn_gestion_referentiels_1.setObjectName(u"btn_gestion_referentiels_1")
        icon1 = QIcon()
        icon1.addFile(u":/icones/small_referentiel1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icones/small_referentiel2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_gestion_referentiels_1.setIcon(icon1)
        self.btn_gestion_referentiels_1.setIconSize(QSize(27, 27))
        self.btn_gestion_referentiels_1.setCheckable(True)
        self.btn_gestion_referentiels_1.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.btn_gestion_referentiels_1)

        self.btn_gestion_produits_1 = QPushButton(self.icon_only_widget)
        self.btn_gestion_produits_1.setObjectName(u"btn_gestion_produits_1")
        icon2 = QIcon()
        icon2.addFile(u":/icones/small_stock1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icones/small_stock2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_gestion_produits_1.setIcon(icon2)
        self.btn_gestion_produits_1.setIconSize(QSize(27, 27))
        self.btn_gestion_produits_1.setCheckable(True)
        self.btn_gestion_produits_1.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.btn_gestion_produits_1)

        self.btn_gestion_operations_1 = QPushButton(self.icon_only_widget)
        self.btn_gestion_operations_1.setObjectName(u"btn_gestion_operations_1")
        icon3 = QIcon()
        icon3.addFile(u":/icones/small_operation1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icones/small_operation2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_gestion_operations_1.setIcon(icon3)
        self.btn_gestion_operations_1.setIconSize(QSize(27, 27))
        self.btn_gestion_operations_1.setCheckable(True)
        self.btn_gestion_operations_1.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.btn_gestion_operations_1)

        self.btn_gestion_compta_1 = QPushButton(self.icon_only_widget)
        self.btn_gestion_compta_1.setObjectName(u"btn_gestion_compta_1")
        icon4 = QIcon()
        icon4.addFile(u":/icones/small_compta1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icones/small_compta2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_gestion_compta_1.setIcon(icon4)
        self.btn_gestion_compta_1.setIconSize(QSize(27, 27))
        self.btn_gestion_compta_1.setCheckable(True)
        self.btn_gestion_compta_1.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.btn_gestion_compta_1)


        self.verticalLayout_14.addLayout(self.verticalLayout_11)

        self.verticalSpacer_2 = QSpacerItem(20, 281, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_2)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(20)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.btn_parametre_1 = QPushButton(self.icon_only_widget)
        self.btn_parametre_1.setObjectName(u"btn_parametre_1")
        self.btn_parametre_1.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icones/small_parametre1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/icones/small_parametre2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_parametre_1.setIcon(icon5)
        self.btn_parametre_1.setIconSize(QSize(27, 27))
        self.btn_parametre_1.setCheckable(True)
        self.btn_parametre_1.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.btn_parametre_1)

        self.btn_deconnexion_1 = QPushButton(self.icon_only_widget)
        self.btn_deconnexion_1.setObjectName(u"btn_deconnexion_1")
        self.btn_deconnexion_1.setStyleSheet(u"QPushButton{\n"
"	padding-left:10px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icones/small_deconnexion1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/icones/small_deconnexion2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_deconnexion_1.setIcon(icon6)
        self.btn_deconnexion_1.setIconSize(QSize(27, 27))
        self.btn_deconnexion_1.setCheckable(True)
        self.btn_deconnexion_1.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.btn_deconnexion_1)


        self.verticalLayout_14.addLayout(self.verticalLayout_12)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_text_widget = QWidget(self.layoutWidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setMinimumSize(QSize(222, 750))
        self.icon_text_widget.setMaximumSize(QSize(222, 16777215))
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"	height:30px;\n"
"	border:none;\n"
"}")
        self.verticalLayout_17 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 10, 0, 10)
        self.label_2 = QLabel(self.icon_text_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/icones/logo.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_text_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(150, 50))
        font = QFont()
        font.setFamilies([u"Courier"])
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_17.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(18)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.btn_dashboard_2 = QPushButton(self.icon_text_widget)
        self.btn_dashboard_2.setObjectName(u"btn_dashboard_2")
        self.btn_dashboard_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-3px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	border-radius:3px;\n"
"	background-color: white\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icones/dashboard1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/icones/dashboard2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_dashboard_2.setIcon(icon7)
        self.btn_dashboard_2.setIconSize(QSize(170, 40))
        self.btn_dashboard_2.setCheckable(True)
        self.btn_dashboard_2.setChecked(False)
        self.btn_dashboard_2.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.btn_dashboard_2)

        self.gestion_referentiels = QFrame(self.icon_text_widget)
        self.gestion_referentiels.setObjectName(u"gestion_referentiels")
        self.gestion_referentiels.setFrameShape(QFrame.Shape.StyledPanel)
        self.gestion_referentiels.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.gestion_referentiels)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_gestion_referentiels_2 = QPushButton(self.gestion_referentiels)
        self.btn_gestion_referentiels_2.setObjectName(u"btn_gestion_referentiels_2")
        self.btn_gestion_referentiels_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-3px;\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/icones/up_referentiel.png", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u":/icones/down_referentiel.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_gestion_referentiels_2.setIcon(icon8)
        self.btn_gestion_referentiels_2.setIconSize(QSize(170, 40))
        self.btn_gestion_referentiels_2.setCheckable(True)
        self.btn_gestion_referentiels_2.setChecked(False)
        self.btn_gestion_referentiels_2.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.btn_gestion_referentiels_2)

        self.dropdown_gestion_referentiels = QFrame(self.gestion_referentiels)
        self.dropdown_gestion_referentiels.setObjectName(u"dropdown_gestion_referentiels")
        self.dropdown_gestion_referentiels.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropdown_gestion_referentiels.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.dropdown_gestion_referentiels)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_ref_produits = QPushButton(self.dropdown_gestion_referentiels)
        self.btn_ref_produits.setObjectName(u"btn_ref_produits")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.btn_ref_produits.setFont(font1)
        self.btn_ref_produits.setStyleSheet(u"QPushButton{\n"
"	padding-left:-40px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_ref_produits.setCheckable(True)

        self.verticalLayout_3.addWidget(self.btn_ref_produits)

        self.btn_ref_fournisseurs = QPushButton(self.dropdown_gestion_referentiels)
        self.btn_ref_fournisseurs.setObjectName(u"btn_ref_fournisseurs")
        self.btn_ref_fournisseurs.setFont(font1)
        self.btn_ref_fournisseurs.setStyleSheet(u"QPushButton{\n"
"	padding-left:-17px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_ref_fournisseurs.setCheckable(True)

        self.verticalLayout_3.addWidget(self.btn_ref_fournisseurs)

        self.btn_ref_entrepots = QPushButton(self.dropdown_gestion_referentiels)
        self.btn_ref_entrepots.setObjectName(u"btn_ref_entrepots")
        self.btn_ref_entrepots.setFont(font1)
        self.btn_ref_entrepots.setStyleSheet(u"QPushButton{\n"
"	padding-left:-35px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_ref_entrepots.setCheckable(True)

        self.verticalLayout_3.addWidget(self.btn_ref_entrepots)

        self.btn_ref_clients = QPushButton(self.dropdown_gestion_referentiels)
        self.btn_ref_clients.setObjectName(u"btn_ref_clients")
        self.btn_ref_clients.setFont(font1)
        self.btn_ref_clients.setStyleSheet(u"QPushButton{\n"
"	padding-left:-50px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_ref_clients.setCheckable(True)

        self.verticalLayout_3.addWidget(self.btn_ref_clients)


        self.verticalLayout_5.addWidget(self.dropdown_gestion_referentiels)


        self.verticalLayout.addWidget(self.gestion_referentiels)

        self.gestion_produits = QFrame(self.icon_text_widget)
        self.gestion_produits.setObjectName(u"gestion_produits")
        self.gestion_produits.setFrameShape(QFrame.Shape.StyledPanel)
        self.gestion_produits.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.gestion_produits)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.btn_gestion_produits_2 = QPushButton(self.gestion_produits)
        self.btn_gestion_produits_2.setObjectName(u"btn_gestion_produits_2")
        self.btn_gestion_produits_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-3px;\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icones/up_stock.png", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/icones/down_stock.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_gestion_produits_2.setIcon(icon9)
        self.btn_gestion_produits_2.setIconSize(QSize(170, 40))
        self.btn_gestion_produits_2.setCheckable(True)
        self.btn_gestion_produits_2.setChecked(False)
        self.btn_gestion_produits_2.setAutoExclusive(False)

        self.verticalLayout_13.addWidget(self.btn_gestion_produits_2)

        self.dropdown_gestion_produits = QFrame(self.gestion_produits)
        self.dropdown_gestion_produits.setObjectName(u"dropdown_gestion_produits")
        self.dropdown_gestion_produits.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropdown_gestion_produits.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.dropdown_gestion_produits)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.btn_inventaire = QPushButton(self.dropdown_gestion_produits)
        self.btn_inventaire.setObjectName(u"btn_inventaire")
        self.btn_inventaire.setFont(font1)
        self.btn_inventaire.setStyleSheet(u"QPushButton{\n"
"	padding-left:-30px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_inventaire.setCheckable(True)

        self.verticalLayout_16.addWidget(self.btn_inventaire)

        self.btn_mvts_des_stocks = QPushButton(self.dropdown_gestion_produits)
        self.btn_mvts_des_stocks.setObjectName(u"btn_mvts_des_stocks")
        self.btn_mvts_des_stocks.setFont(font1)
        self.btn_mvts_des_stocks.setStyleSheet(u"QPushButton{\n"
"	padding-left:39px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_mvts_des_stocks.setCheckable(True)

        self.verticalLayout_16.addWidget(self.btn_mvts_des_stocks)


        self.verticalLayout_13.addWidget(self.dropdown_gestion_produits)


        self.verticalLayout.addWidget(self.gestion_produits)

        self.gestion_operations = QFrame(self.icon_text_widget)
        self.gestion_operations.setObjectName(u"gestion_operations")
        self.gestion_operations.setFrameShape(QFrame.Shape.StyledPanel)
        self.gestion_operations.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.gestion_operations)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_gestion_operations_2 = QPushButton(self.gestion_operations)
        self.btn_gestion_operations_2.setObjectName(u"btn_gestion_operations_2")
        self.btn_gestion_operations_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-3px;\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/icones/up_operations.png", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u":/icones/down_operations.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_gestion_operations_2.setIcon(icon10)
        self.btn_gestion_operations_2.setIconSize(QSize(170, 40))
        self.btn_gestion_operations_2.setCheckable(True)
        self.btn_gestion_operations_2.setChecked(False)
        self.btn_gestion_operations_2.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.btn_gestion_operations_2)

        self.dropdown_gestion_operations = QFrame(self.gestion_operations)
        self.dropdown_gestion_operations.setObjectName(u"dropdown_gestion_operations")
        self.dropdown_gestion_operations.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropdown_gestion_operations.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.dropdown_gestion_operations)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_ventes_retours = QPushButton(self.dropdown_gestion_operations)
        self.btn_ventes_retours.setObjectName(u"btn_ventes_retours")
        self.btn_ventes_retours.setFont(font1)
        self.btn_ventes_retours.setStyleSheet(u"QPushButton{\n"
"	padding-left:8px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_ventes_retours.setCheckable(True)

        self.verticalLayout_4.addWidget(self.btn_ventes_retours)

        self.btn_paiements_factures = QPushButton(self.dropdown_gestion_operations)
        self.btn_paiements_factures.setObjectName(u"btn_paiements_factures")
        self.btn_paiements_factures.setFont(font1)
        self.btn_paiements_factures.setStyleSheet(u"QPushButton{\n"
"	padding-left:30px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_paiements_factures.setCheckable(True)

        self.verticalLayout_4.addWidget(self.btn_paiements_factures)

        self.btn_livraisons = QPushButton(self.dropdown_gestion_operations)
        self.btn_livraisons.setObjectName(u"btn_livraisons")
        self.btn_livraisons.setFont(font1)
        self.btn_livraisons.setStyleSheet(u"QPushButton{\n"
"	padding-left:-35px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_livraisons.setCheckable(True)

        self.verticalLayout_4.addWidget(self.btn_livraisons)


        self.verticalLayout_9.addWidget(self.dropdown_gestion_operations)


        self.verticalLayout.addWidget(self.gestion_operations)

        self.gestion_compta = QFrame(self.icon_text_widget)
        self.gestion_compta.setObjectName(u"gestion_compta")
        self.gestion_compta.setFrameShape(QFrame.Shape.StyledPanel)
        self.gestion_compta.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.gestion_compta)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btn_gestion_compta_2 = QPushButton(self.gestion_compta)
        self.btn_gestion_compta_2.setObjectName(u"btn_gestion_compta_2")
        self.btn_gestion_compta_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-3px;\n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/icones/up_compta.png", QSize(), QIcon.Normal, QIcon.Off)
        icon11.addFile(u":/icones/down_compta.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_gestion_compta_2.setIcon(icon11)
        self.btn_gestion_compta_2.setIconSize(QSize(170, 40))
        self.btn_gestion_compta_2.setCheckable(True)
        self.btn_gestion_compta_2.setChecked(False)
        self.btn_gestion_compta_2.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.btn_gestion_compta_2)

        self.dropdown_gestion_compta = QFrame(self.gestion_compta)
        self.dropdown_gestion_compta.setObjectName(u"dropdown_gestion_compta")
        self.dropdown_gestion_compta.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropdown_gestion_compta.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.dropdown_gestion_compta)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_depenses = QPushButton(self.dropdown_gestion_compta)
        self.btn_depenses.setObjectName(u"btn_depenses")
        self.btn_depenses.setFont(font1)
        self.btn_depenses.setStyleSheet(u"QPushButton{\n"
"	padding-left:-30px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#679cdb;\n"
"}")
        self.btn_depenses.setCheckable(True)

        self.verticalLayout_6.addWidget(self.btn_depenses)

        self.btn_flux_monetaires = QPushButton(self.dropdown_gestion_compta)
        self.btn_flux_monetaires.setObjectName(u"btn_flux_monetaires")
        self.btn_flux_monetaires.setFont(font1)
        self.btn_flux_monetaires.setStyleSheet(u"QPushButton{\n"
"	padding-left:0px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_flux_monetaires.setCheckable(True)

        self.verticalLayout_6.addWidget(self.btn_flux_monetaires)

        self.btn_rapports_financiers = QPushButton(self.dropdown_gestion_compta)
        self.btn_rapports_financiers.setObjectName(u"btn_rapports_financiers")
        self.btn_rapports_financiers.setFont(font1)
        self.btn_rapports_financiers.setStyleSheet(u"QPushButton{\n"
"	padding-left:15px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_rapports_financiers.setCheckable(True)

        self.verticalLayout_6.addWidget(self.btn_rapports_financiers)


        self.verticalLayout_10.addWidget(self.dropdown_gestion_compta)


        self.verticalLayout.addWidget(self.gestion_compta)


        self.verticalLayout_17.addLayout(self.verticalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 2, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(21)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 6, -1, 5)
        self.btn_parametre_2 = QPushButton(self.icon_text_widget)
        self.btn_parametre_2.setObjectName(u"btn_parametre_2")
        self.btn_parametre_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-3px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	border-radius:3px;\n"
"	background-color: white\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icones/parametre1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon12.addFile(u":/icones/parametre2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_parametre_2.setIcon(icon12)
        self.btn_parametre_2.setIconSize(QSize(170, 40))
        self.btn_parametre_2.setCheckable(True)
        self.btn_parametre_2.setChecked(False)
        self.btn_parametre_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_parametre_2)

        self.btn_deconnexion_2 = QPushButton(self.icon_text_widget)
        self.btn_deconnexion_2.setObjectName(u"btn_deconnexion_2")
        self.btn_deconnexion_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-3px;\n"
"	height:25px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	border-radius:3px;\n"
"	background-color: white\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icones/deconnexion1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon13.addFile(u":/icones/deconnexion2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_deconnexion_2.setIcon(icon13)
        self.btn_deconnexion_2.setIconSize(QSize(170, 40))
        self.btn_deconnexion_2.setCheckable(True)
        self.btn_deconnexion_2.setChecked(False)
        self.btn_deconnexion_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_deconnexion_2)


        self.verticalLayout_17.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.header_widget = QWidget(self.layoutWidget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMinimumSize(QSize(895, 66))
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


        self.verticalLayout_18.addWidget(self.header_widget)

        self.main_screen_widget = QWidget(self.layoutWidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(895, 672))
        self.main_screen_widget.setStyleSheet(u"")
        self.tabWidget = QTabWidget(self.main_screen_widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 895, 672))
        self.tabWidget.setMinimumSize(QSize(895, 672))
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_00 = QWidget()
        self.tab_00.setObjectName(u"tab_00")
        self.label_20 = QLabel(self.tab_00)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(290, 90, 271, 71))
        font3 = QFont()
        font3.setPointSize(25)
        self.label_20.setFont(font3)
        self.tabWidget.addTab(self.tab_00, "")
        self.tab_01 = QWidget()
        self.tab_01.setObjectName(u"tab_01")
        self.btn_export_excel_produit = QPushButton(self.tab_01)
        self.btn_export_excel_produit.setObjectName(u"btn_export_excel_produit")
        self.btn_export_excel_produit.setGeometry(QRect(137, 36, 122, 32))
        self.btn_export_excel_produit.setMinimumSize(QSize(0, 32))
        self.btn_export_excel_produit.setMaximumSize(QSize(122, 32))
        self.btn_export_excel_produit.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/icones/excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_export_excel_produit.setIcon(icon15)
        self.btn_ajout_produit = QPushButton(self.tab_01)
        self.btn_ajout_produit.setObjectName(u"btn_ajout_produit")
        self.btn_ajout_produit.setGeometry(QRect(2, 36, 121, 32))
        self.btn_ajout_produit.setMinimumSize(QSize(0, 32))
        self.btn_ajout_produit.setMaximumSize(QSize(122, 32))
        self.btn_ajout_produit.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/icones/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ajout_produit.setIcon(icon16)
        self.table_infos_client_3 = QTableWidget(self.tab_01)
        if (self.table_infos_client_3.columnCount() < 7):
            self.table_infos_client_3.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_infos_client_3.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_infos_client_3.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_infos_client_3.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_infos_client_3.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_infos_client_3.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_infos_client_3.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_infos_client_3.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table_infos_client_3.setObjectName(u"table_infos_client_3")
        self.table_infos_client_3.setGeometry(QRect(1, 90, 891, 561))
        self.table_infos_client_3.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_client_3.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.table_infos_client_3.setAlternatingRowColors(True)
        self.table_infos_client_3.horizontalHeader().setCascadingSectionResizes(False)
        self.cherche_produit = QLineEdit(self.tab_01)
        self.cherche_produit.setObjectName(u"cherche_produit")
        self.cherche_produit.setGeometry(QRect(414, 37, 407, 32))
        self.cherche_produit.setMinimumSize(QSize(0, 32))
        self.cherche_produit.setMaximumSize(QSize(407, 31))
        self.cherche_produit.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")
        self.label_21 = QLabel(self.tab_01)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 10, 381, 16))
        font4 = QFont()
        font4.setFamilies([u"Courier"])
        font4.setPointSize(23)
        font4.setWeight(QFont.DemiBold)
        self.label_21.setFont(font4)
        self.btn_export_pdf_produit = QPushButton(self.tab_01)
        self.btn_export_pdf_produit.setObjectName(u"btn_export_pdf_produit")
        self.btn_export_pdf_produit.setGeometry(QRect(273, 36, 121, 32))
        self.btn_export_pdf_produit.setMinimumSize(QSize(0, 32))
        self.btn_export_pdf_produit.setMaximumSize(QSize(122, 32))
        self.btn_export_pdf_produit.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 58, 21);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/icones/pdf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_export_pdf_produit.setIcon(icon17)
        self.tabWidget.addTab(self.tab_01, "")
        self.tab_02 = QWidget()
        self.tab_02.setObjectName(u"tab_02")
        self.label_22 = QLabel(self.tab_02)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(320, 200, 351, 71))
        self.label_22.setFont(font3)
        self.tabWidget.addTab(self.tab_02, "")
        self.tab_03 = QWidget()
        self.tab_03.setObjectName(u"tab_03")
        self.label_23 = QLabel(self.tab_03)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(380, 200, 351, 71))
        self.label_23.setFont(font3)
        self.tabWidget.addTab(self.tab_03, "")
        self.tab_04 = QWidget()
        self.tab_04.setObjectName(u"tab_04")
        self.export_pdf_btn_2 = QPushButton(self.tab_04)
        self.export_pdf_btn_2.setObjectName(u"export_pdf_btn_2")
        self.export_pdf_btn_2.setGeometry(QRect(282, 36, 121, 32))
        self.export_pdf_btn_2.setMinimumSize(QSize(0, 32))
        self.export_pdf_btn_2.setMaximumSize(QSize(122, 32))
        self.export_pdf_btn_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 58, 21);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.export_pdf_btn_2.setIcon(icon17)
        self.ajout_client_btn_2 = QPushButton(self.tab_04)
        self.ajout_client_btn_2.setObjectName(u"ajout_client_btn_2")
        self.ajout_client_btn_2.setGeometry(QRect(11, 36, 121, 32))
        self.ajout_client_btn_2.setMinimumSize(QSize(0, 32))
        self.ajout_client_btn_2.setMaximumSize(QSize(122, 32))
        self.ajout_client_btn_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.ajout_client_btn_2.setIcon(icon16)
        self.export_excel_btn_2 = QPushButton(self.tab_04)
        self.export_excel_btn_2.setObjectName(u"export_excel_btn_2")
        self.export_excel_btn_2.setGeometry(QRect(146, 36, 122, 32))
        self.export_excel_btn_2.setMinimumSize(QSize(0, 32))
        self.export_excel_btn_2.setMaximumSize(QSize(122, 32))
        self.export_excel_btn_2.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.export_excel_btn_2.setIcon(icon15)
        self.cherche_client_2 = QLineEdit(self.tab_04)
        self.cherche_client_2.setObjectName(u"cherche_client_2")
        self.cherche_client_2.setGeometry(QRect(423, 37, 407, 32))
        self.cherche_client_2.setMinimumSize(QSize(0, 32))
        self.cherche_client_2.setMaximumSize(QSize(407, 31))
        self.cherche_client_2.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")
        self.label_18 = QLabel(self.tab_04)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(9, 70, 291, 51))
        font5 = QFont()
        font5.setFamilies([u"Courier"])
        font5.setPointSize(12)
        font5.setBold(False)
        self.label_18.setFont(font5)
        self.label_19 = QLabel(self.tab_04)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(9, 10, 381, 16))
        self.label_19.setFont(font4)
        self.table_infos_client_2 = QTableWidget(self.tab_04)
        if (self.table_infos_client_2.columnCount() < 9):
            self.table_infos_client_2.setColumnCount(9)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_infos_client_2.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_infos_client_2.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_infos_client_2.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_infos_client_2.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_infos_client_2.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_infos_client_2.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_infos_client_2.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_infos_client_2.setHorizontalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_infos_client_2.setHorizontalHeaderItem(8, __qtablewidgetitem15)
        self.table_infos_client_2.setObjectName(u"table_infos_client_2")
        self.table_infos_client_2.setGeometry(QRect(10, 140, 885, 91))
        self.table_infos_client_2.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_client_2.setAlternatingRowColors(True)
        self.tabWidget.addTab(self.tab_04, "")
        self.tab_05 = QWidget()
        self.tab_05.setObjectName(u"tab_05")
        self.label_24 = QLabel(self.tab_05)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(210, 140, 351, 71))
        self.label_24.setFont(font3)
        self.tabWidget.addTab(self.tab_05, "")
        self.tab_06 = QWidget()
        self.tab_06.setObjectName(u"tab_06")
        self.label_25 = QLabel(self.tab_06)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(270, 170, 351, 71))
        self.label_25.setFont(font3)
        self.tabWidget.addTab(self.tab_06, "")
        self.tab_07 = QWidget()
        self.tab_07.setObjectName(u"tab_07")
        self.label_26 = QLabel(self.tab_07)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(290, 200, 351, 71))
        self.label_26.setFont(font3)
        self.tabWidget.addTab(self.tab_07, "")
        self.tab_08 = QWidget()
        self.tab_08.setObjectName(u"tab_08")
        self.label_27 = QLabel(self.tab_08)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(460, 240, 351, 71))
        self.label_27.setFont(font3)
        self.tabWidget.addTab(self.tab_08, "")
        self.tab_09 = QWidget()
        self.tab_09.setObjectName(u"tab_09")
        self.label_28 = QLabel(self.tab_09)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(270, 180, 351, 71))
        self.label_28.setFont(font3)
        self.tabWidget.addTab(self.tab_09, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.label_29 = QLabel(self.tab_10)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(250, 210, 351, 71))
        self.label_29.setFont(font3)
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.label_30 = QLabel(self.tab_11)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(230, 120, 351, 71))
        self.label_30.setFont(font3)
        self.tabWidget.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.label_31 = QLabel(self.tab_12)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(320, 180, 351, 71))
        self.label_31.setFont(font3)
        self.tabWidget.addTab(self.tab_12, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_18.addWidget(self.main_screen_widget)


        self.gridLayout.addLayout(self.verticalLayout_18, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1231, 24))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.btn_deconnexion_1.toggled.connect(MainWindow.close)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_only_widget.setVisible)
        self.btn_gestion_produits_2.toggled.connect(self.dropdown_gestion_produits.setHidden)
        self.btn_gestion_operations_2.toggled.connect(self.dropdown_gestion_operations.setHidden)
        self.btn_gestion_compta_2.toggled.connect(self.dropdown_gestion_compta.setHidden)
        self.btn_dashboard_2.toggled.connect(self.btn_dashboard_1.setChecked)
        self.btn_parametre_2.toggled.connect(self.btn_parametre_1.setChecked)
        self.btn_deconnexion_2.toggled.connect(self.btn_deconnexion_1.setChecked)
        self.btn_gestion_referentiels_2.toggled.connect(self.btn_gestion_referentiels_1.setChecked)
        self.btn_gestion_produits_2.toggled.connect(self.btn_gestion_produits_1.setChecked)
        self.btn_gestion_operations_2.toggled.connect(self.btn_gestion_operations_1.setChecked)
        self.btn_gestion_compta_2.toggled.connect(self.btn_gestion_compta_1.setChecked)
        self.btn_gestion_referentiels_2.toggled.connect(self.dropdown_gestion_referentiels.setHidden)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.btn_dashboard_1.setText("")
        self.btn_gestion_referentiels_1.setText("")
        self.btn_gestion_produits_1.setText("")
        self.btn_gestion_operations_1.setText("")
        self.btn_gestion_compta_1.setText("")
        self.btn_parametre_1.setText("")
        self.btn_deconnexion_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"GeStock", None))
        self.btn_dashboard_2.setText("")
        self.btn_gestion_referentiels_2.setText("")
        self.btn_ref_produits.setText(QCoreApplication.translate("MainWindow", u"Produits", None))
        self.btn_ref_fournisseurs.setText(QCoreApplication.translate("MainWindow", u"Fournisseurs", None))
        self.btn_ref_entrepots.setText(QCoreApplication.translate("MainWindow", u"Entrep\u00f4ts", None))
        self.btn_ref_clients.setText(QCoreApplication.translate("MainWindow", u"Clients", None))
        self.btn_gestion_produits_2.setText("")
        self.btn_inventaire.setText(QCoreApplication.translate("MainWindow", u"Inventaire", None))
        self.btn_mvts_des_stocks.setText(QCoreApplication.translate("MainWindow", u"Mouvements des stocks", None))
        self.btn_gestion_operations_2.setText("")
        self.btn_ventes_retours.setText(QCoreApplication.translate("MainWindow", u"Ventes et Retours", None))
        self.btn_paiements_factures.setText(QCoreApplication.translate("MainWindow", u"Paiements et Factures", None))
        self.btn_livraisons.setText(QCoreApplication.translate("MainWindow", u"Livraisons", None))
        self.btn_gestion_compta_2.setText("")
        self.btn_depenses.setText(QCoreApplication.translate("MainWindow", u"D\u00e9penses", None))
        self.btn_flux_monetaires.setText(QCoreApplication.translate("MainWindow", u"Flux mon\u00e9taires", None))
        self.btn_rapports_financiers.setText(QCoreApplication.translate("MainWindow", u"Rapports financiers", None))
        self.btn_parametre_2.setText("")
        self.btn_deconnexion_2.setText("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bonjour Tartapion,", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Bienvenue!!!", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recherche...", None))
        self.label_6.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Tableau de bord", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_00), QCoreApplication.translate("MainWindow", u"Tableau de bord", None))
        self.btn_export_excel_produit.setText(QCoreApplication.translate("MainWindow", u"Export Excel", None))
        self.btn_ajout_produit.setText(QCoreApplication.translate("MainWindow", u"Ajouter Produit", None))
        ___qtablewidgetitem = self.table_infos_client_3.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID Produit", None));
        ___qtablewidgetitem1 = self.table_infos_client_3.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem2 = self.table_infos_client_3.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Fournisseur", None));
        ___qtablewidgetitem3 = self.table_infos_client_3.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Prix de Revient", None));
        ___qtablewidgetitem4 = self.table_infos_client_3.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Prix de Vente", None));
        ___qtablewidgetitem5 = self.table_infos_client_3.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem6 = self.table_infos_client_3.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.cherche_produit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher produit...", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Gestion R\u00e9f\u00e9rentiel Produit", None))
        self.btn_export_pdf_produit.setText(QCoreApplication.translate("MainWindow", u"Export PDF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_01), QCoreApplication.translate("MainWindow", u"Produits", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Gestion des fournisseurs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_02), QCoreApplication.translate("MainWindow", u"Fournisseur", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Gestion des entrep\u00f4ts", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_03), QCoreApplication.translate("MainWindow", u"Entrep\u00f4ts", None))
        self.export_pdf_btn_2.setText(QCoreApplication.translate("MainWindow", u"Export PDF", None))
        self.ajout_client_btn_2.setText(QCoreApplication.translate("MainWindow", u"Ajouter client", None))
        self.export_excel_btn_2.setText(QCoreApplication.translate("MainWindow", u"Export Excel", None))
        self.cherche_client_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher client...", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Hello", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Gestion R\u00e9f\u00e9rentiel Client", None))
        ___qtablewidgetitem7 = self.table_infos_client_2.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"ID Client", None));
        ___qtablewidgetitem8 = self.table_infos_client_2.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom", None));
        ___qtablewidgetitem9 = self.table_infos_client_2.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem10 = self.table_infos_client_2.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Genre", None));
        ___qtablewidgetitem11 = self.table_infos_client_2.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Entreprise", None));
        ___qtablewidgetitem12 = self.table_infos_client_2.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Adresse", None));
        ___qtablewidgetitem13 = self.table_infos_client_2.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"T\u00e9l\u00e9phone", None));
        ___qtablewidgetitem14 = self.table_infos_client_2.horizontalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem15 = self.table_infos_client_2.horizontalHeaderItem(8)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_04), QCoreApplication.translate("MainWindow", u"Clients", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Inventaire", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_05), QCoreApplication.translate("MainWindow", u"Inventaire", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Mouvements des stocks", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_06), QCoreApplication.translate("MainWindow", u"Mvts Stocks", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Ventes et Retours", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_07), QCoreApplication.translate("MainWindow", u"Ventes & Retours", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Paiements et Factures", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_08), QCoreApplication.translate("MainWindow", u"Paiements & Factures", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Livraisons", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_09), QCoreApplication.translate("MainWindow", u"Livraisons", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"D\u00e9penses", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"D\u00e9penses", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Flux mon\u00e9taires", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"Flux Mon\u00e9taires", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Rapports Financiers", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"Rapports Financiers", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Page", None))
    # retranslateUi

