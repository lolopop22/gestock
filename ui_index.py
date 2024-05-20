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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import ressources_rc
import ressources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1256, 879)
        MainWindow.setMinimumSize(QSize(1231, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Courier"])
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setVerticalSpacing(-1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(90, 750))
        self.icon_only_widget.setMaximumSize(QSize(90, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"	height:35px;\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	border-radius:3px\n"
"}\n"
"")
        self.verticalLayout_16 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 0, -1, 2)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 10, -1, 10)
        self.horizontalSpacer_4 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.label_5 = QLabel(self.icon_only_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(40, 40))
        self.label_5.setPixmap(QPixmap(u":/icones/logo.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.horizontalSpacer_5 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_16.addLayout(self.horizontalLayout_6)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(20)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, 10)
        self.btn_dashboard_1 = QPushButton(self.icon_only_widget)
        self.btn_dashboard_1.setObjectName(u"btn_dashboard_1")
        self.btn_dashboard_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icones/small_dashboard1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icones/small_dashboard2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_dashboard_1.setIcon(icon)
        self.btn_dashboard_1.setIconSize(QSize(30, 30))
        self.btn_dashboard_1.setCheckable(True)
        self.btn_dashboard_1.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.btn_dashboard_1)

        self.btn_gestion_referentiels_1 = QPushButton(self.icon_only_widget)
        self.btn_gestion_referentiels_1.setObjectName(u"btn_gestion_referentiels_1")
        self.btn_gestion_referentiels_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icones/small_referentiel1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icones/small_referentiel2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_gestion_referentiels_1.setIcon(icon1)
        self.btn_gestion_referentiels_1.setIconSize(QSize(30, 30))
        self.btn_gestion_referentiels_1.setCheckable(True)
        self.btn_gestion_referentiels_1.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.btn_gestion_referentiels_1)

        self.btn_gestion_stock_1 = QPushButton(self.icon_only_widget)
        self.btn_gestion_stock_1.setObjectName(u"btn_gestion_stock_1")
        self.btn_gestion_stock_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icones/small_stock1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icones/small_stock2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_gestion_stock_1.setIcon(icon2)
        self.btn_gestion_stock_1.setIconSize(QSize(30, 30))
        self.btn_gestion_stock_1.setCheckable(True)
        self.btn_gestion_stock_1.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.btn_gestion_stock_1)

        self.btn_gestion_operations_1 = QPushButton(self.icon_only_widget)
        self.btn_gestion_operations_1.setObjectName(u"btn_gestion_operations_1")
        self.btn_gestion_operations_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icones/small_operation1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icones/small_operation2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_gestion_operations_1.setIcon(icon3)
        self.btn_gestion_operations_1.setIconSize(QSize(30, 30))
        self.btn_gestion_operations_1.setCheckable(True)
        self.btn_gestion_operations_1.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.btn_gestion_operations_1)

        self.btn_gestion_compta_1 = QPushButton(self.icon_only_widget)
        self.btn_gestion_compta_1.setObjectName(u"btn_gestion_compta_1")
        self.btn_gestion_compta_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icones/small_compta1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icones/small_compta2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_gestion_compta_1.setIcon(icon4)
        self.btn_gestion_compta_1.setIconSize(QSize(30, 30))
        self.btn_gestion_compta_1.setCheckable(True)
        self.btn_gestion_compta_1.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.btn_gestion_compta_1)


        self.verticalLayout_16.addLayout(self.verticalLayout_13)

        self.verticalSpacer_4 = QSpacerItem(20, 281, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_4)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, 0, -1, 0)
        self.btn_parametre_1 = QPushButton(self.icon_only_widget)
        self.btn_parametre_1.setObjectName(u"btn_parametre_1")
        self.btn_parametre_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_parametre_1.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icones/small_parametre1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/icones/small_parametre2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_parametre_1.setIcon(icon5)
        self.btn_parametre_1.setIconSize(QSize(30, 30))
        self.btn_parametre_1.setCheckable(True)
        self.btn_parametre_1.setAutoExclusive(True)

        self.verticalLayout_19.addWidget(self.btn_parametre_1)

        self.btn_deconnexion_1 = QPushButton(self.icon_only_widget)
        self.btn_deconnexion_1.setObjectName(u"btn_deconnexion_1")
        self.btn_deconnexion_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_deconnexion_1.setStyleSheet(u"QPushButton{\n"
"	padding-left:10px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icones/small_deconnexion1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/icones/small_deconnexion2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_deconnexion_1.setIcon(icon6)
        self.btn_deconnexion_1.setIconSize(QSize(30, 30))
        self.btn_deconnexion_1.setCheckable(True)
        self.btn_deconnexion_1.setAutoExclusive(True)

        self.verticalLayout_19.addWidget(self.btn_deconnexion_1)


        self.verticalLayout_16.addLayout(self.verticalLayout_19)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_text_widget = QWidget(self.centralwidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setMinimumSize(QSize(240, 750))
        self.icon_text_widget.setMaximumSize(QSize(240, 16777215))
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"	height:35px;\n"
"	border:none;\n"
"}\n"
"\n"
"")
        self.verticalLayout_10 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, 2)
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
        font1 = QFont()
        font1.setFamilies([u"Courier"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.btn_dashboard_2 = QPushButton(self.icon_text_widget)
        self.btn_dashboard_2.setObjectName(u"btn_dashboard_2")
        font2 = QFont()
        font2.setFamilies([u"Courier"])
        font2.setBold(True)
        self.btn_dashboard_2.setFont(font2)
        self.btn_dashboard_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_dashboard_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-25px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	border-radius:3px;\n"
"	background-color: white;\n"
"	color:#2672CC;\n"
"}")
        self.btn_dashboard_2.setIcon(icon)
        self.btn_dashboard_2.setIconSize(QSize(30, 30))
        self.btn_dashboard_2.setCheckable(True)
        self.btn_dashboard_2.setChecked(False)
        self.btn_dashboard_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_dashboard_2)

        self.frame_gestion_referentiels = QFrame(self.icon_text_widget)
        self.frame_gestion_referentiels.setObjectName(u"frame_gestion_referentiels")
        self.frame_gestion_referentiels.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_gestion_referentiels.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_gestion_referentiels)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_gestion_referentiels_2 = QPushButton(self.frame_gestion_referentiels)
        self.btn_gestion_referentiels_2.setObjectName(u"btn_gestion_referentiels_2")
        self.btn_gestion_referentiels_2.setFont(font2)
        self.btn_gestion_referentiels_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gestion_referentiels_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-45px;\n"
"}\n"
"")
        self.btn_gestion_referentiels_2.setIcon(icon1)
        self.btn_gestion_referentiels_2.setIconSize(QSize(30, 30))
        self.btn_gestion_referentiels_2.setCheckable(True)
        self.btn_gestion_referentiels_2.setChecked(False)
        self.btn_gestion_referentiels_2.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.btn_gestion_referentiels_2)

        self.dropdown_gestion_referentiels = QFrame(self.frame_gestion_referentiels)
        self.dropdown_gestion_referentiels.setObjectName(u"dropdown_gestion_referentiels")
        self.dropdown_gestion_referentiels.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropdown_gestion_referentiels.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.dropdown_gestion_referentiels)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_ref_clients = QPushButton(self.dropdown_gestion_referentiels)
        self.btn_ref_clients.setObjectName(u"btn_ref_clients")
        font3 = QFont()
        font3.setFamilies([u"Courier"])
        font3.setPointSize(11)
        self.btn_ref_clients.setFont(font3)
        self.btn_ref_clients.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ref_clients.setStyleSheet(u"QPushButton{\n"
"	padding-left:-47px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_ref_clients.setCheckable(True)

        self.verticalLayout_3.addWidget(self.btn_ref_clients)

        self.btn_ref_entrepots = QPushButton(self.dropdown_gestion_referentiels)
        self.btn_ref_entrepots.setObjectName(u"btn_ref_entrepots")
        self.btn_ref_entrepots.setFont(font3)
        self.btn_ref_entrepots.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ref_entrepots.setStyleSheet(u"QPushButton{\n"
"	padding-left:-35px;\n"
"	height:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_ref_entrepots.setCheckable(True)

        self.verticalLayout_3.addWidget(self.btn_ref_entrepots)

        self.btn_ref_fournisseurs = QPushButton(self.dropdown_gestion_referentiels)
        self.btn_ref_fournisseurs.setObjectName(u"btn_ref_fournisseurs")
        self.btn_ref_fournisseurs.setFont(font3)
        self.btn_ref_fournisseurs.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ref_fournisseurs.setStyleSheet(u"QPushButton{\n"
"	padding-left:-15px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_ref_fournisseurs.setCheckable(True)
        self.btn_ref_fournisseurs.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.btn_ref_fournisseurs)

        self.btn_ref_matieres_premieres = QPushButton(self.dropdown_gestion_referentiels)
        self.btn_ref_matieres_premieres.setObjectName(u"btn_ref_matieres_premieres")
        self.btn_ref_matieres_premieres.setFont(font3)
        self.btn_ref_matieres_premieres.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ref_matieres_premieres.setStyleSheet(u"QPushButton{\n"
"	padding-left:24px;\n"
"	height:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_ref_matieres_premieres.setCheckable(True)

        self.verticalLayout_3.addWidget(self.btn_ref_matieres_premieres)

        self.btn_ref_produits = QPushButton(self.dropdown_gestion_referentiels)
        self.btn_ref_produits.setObjectName(u"btn_ref_produits")
        self.btn_ref_produits.setFont(font3)
        self.btn_ref_produits.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ref_produits.setStyleSheet(u"QPushButton{\n"
"	padding-left:-40px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_ref_produits.setCheckable(True)
        self.btn_ref_produits.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.btn_ref_produits)


        self.verticalLayout_4.addWidget(self.dropdown_gestion_referentiels)


        self.verticalLayout_2.addWidget(self.frame_gestion_referentiels)

        self.frame_gestion_stock = QFrame(self.icon_text_widget)
        self.frame_gestion_stock.setObjectName(u"frame_gestion_stock")
        self.frame_gestion_stock.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_gestion_stock.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_gestion_stock)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_gestion_stock_2 = QPushButton(self.frame_gestion_stock)
        self.btn_gestion_stock_2.setObjectName(u"btn_gestion_stock_2")
        self.btn_gestion_stock_2.setFont(font2)
        self.btn_gestion_stock_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gestion_stock_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-100px;\n"
"}\n"
"")
        self.btn_gestion_stock_2.setIcon(icon2)
        self.btn_gestion_stock_2.setIconSize(QSize(30, 30))
        self.btn_gestion_stock_2.setCheckable(True)
        self.btn_gestion_stock_2.setChecked(False)
        self.btn_gestion_stock_2.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.btn_gestion_stock_2)

        self.dropdown_gestion_stocks = QFrame(self.frame_gestion_stock)
        self.dropdown_gestion_stocks.setObjectName(u"dropdown_gestion_stocks")
        self.dropdown_gestion_stocks.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropdown_gestion_stocks.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.dropdown_gestion_stocks)
        self.verticalLayout_25.setSpacing(5)
        self.verticalLayout_25.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.btn_inventaire = QPushButton(self.dropdown_gestion_stocks)
        self.btn_inventaire.setObjectName(u"btn_inventaire")
        self.btn_inventaire.setFont(font3)
        self.btn_inventaire.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_inventaire.setStyleSheet(u"QPushButton{\n"
"	padding-left:-30px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_inventaire.setCheckable(True)

        self.verticalLayout_25.addWidget(self.btn_inventaire)

        self.btn_mvts_des_stocks = QPushButton(self.dropdown_gestion_stocks)
        self.btn_mvts_des_stocks.setObjectName(u"btn_mvts_des_stocks")
        self.btn_mvts_des_stocks.setFont(font3)
        self.btn_mvts_des_stocks.setStyleSheet(u"QPushButton{\n"
"	padding-left:45px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_mvts_des_stocks.setCheckable(True)

        self.verticalLayout_25.addWidget(self.btn_mvts_des_stocks)


        self.verticalLayout_5.addWidget(self.dropdown_gestion_stocks)


        self.verticalLayout_2.addWidget(self.frame_gestion_stock)

        self.frame_gestion_operations = QFrame(self.icon_text_widget)
        self.frame_gestion_operations.setObjectName(u"frame_gestion_operations")
        self.frame_gestion_operations.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_gestion_operations.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_gestion_operations)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_gestion_operations_2 = QPushButton(self.frame_gestion_operations)
        self.btn_gestion_operations_2.setObjectName(u"btn_gestion_operations_2")
        self.btn_gestion_operations_2.setFont(font2)
        self.btn_gestion_operations_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gestion_operations_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-60px;\n"
"}\n"
"")
        self.btn_gestion_operations_2.setIcon(icon3)
        self.btn_gestion_operations_2.setIconSize(QSize(30, 30))
        self.btn_gestion_operations_2.setCheckable(True)
        self.btn_gestion_operations_2.setChecked(False)
        self.btn_gestion_operations_2.setAutoExclusive(False)

        self.verticalLayout_8.addWidget(self.btn_gestion_operations_2)

        self.dropdown_gestion_operations = QFrame(self.frame_gestion_operations)
        self.dropdown_gestion_operations.setObjectName(u"dropdown_gestion_operations")
        self.dropdown_gestion_operations.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropdown_gestion_operations.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.dropdown_gestion_operations)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_ventes_retours = QPushButton(self.dropdown_gestion_operations)
        self.btn_ventes_retours.setObjectName(u"btn_ventes_retours")
        self.btn_ventes_retours.setFont(font3)
        self.btn_ventes_retours.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ventes_retours.setStyleSheet(u"QPushButton{\n"
"	padding-left:18px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_ventes_retours.setCheckable(True)

        self.verticalLayout_6.addWidget(self.btn_ventes_retours)

        self.btn_paiements_factures = QPushButton(self.dropdown_gestion_operations)
        self.btn_paiements_factures.setObjectName(u"btn_paiements_factures")
        self.btn_paiements_factures.setFont(font3)
        self.btn_paiements_factures.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_paiements_factures.setStyleSheet(u"QPushButton{\n"
"	padding-left:45px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_paiements_factures.setCheckable(True)

        self.verticalLayout_6.addWidget(self.btn_paiements_factures)

        self.btn_livraisons = QPushButton(self.dropdown_gestion_operations)
        self.btn_livraisons.setObjectName(u"btn_livraisons")
        self.btn_livraisons.setFont(font3)
        self.btn_livraisons.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_livraisons.setStyleSheet(u"QPushButton{\n"
"	padding-left:-27px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_livraisons.setCheckable(True)

        self.verticalLayout_6.addWidget(self.btn_livraisons)


        self.verticalLayout_8.addWidget(self.dropdown_gestion_operations)


        self.verticalLayout_2.addWidget(self.frame_gestion_operations)

        self.frame_gestion_compta = QFrame(self.icon_text_widget)
        self.frame_gestion_compta.setObjectName(u"frame_gestion_compta")
        self.frame_gestion_compta.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_gestion_compta.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_gestion_compta)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_gestion_compta_2 = QPushButton(self.frame_gestion_compta)
        self.btn_gestion_compta_2.setObjectName(u"btn_gestion_compta_2")
        self.btn_gestion_compta_2.setFont(font2)
        self.btn_gestion_compta_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gestion_compta_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-40px;\n"
"}\n"
"")
        self.btn_gestion_compta_2.setIcon(icon4)
        self.btn_gestion_compta_2.setIconSize(QSize(30, 30))
        self.btn_gestion_compta_2.setCheckable(True)
        self.btn_gestion_compta_2.setChecked(False)
        self.btn_gestion_compta_2.setAutoExclusive(False)

        self.verticalLayout_9.addWidget(self.btn_gestion_compta_2)

        self.dropdown_gestion_compta = QFrame(self.frame_gestion_compta)
        self.dropdown_gestion_compta.setObjectName(u"dropdown_gestion_compta")
        self.dropdown_gestion_compta.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropdown_gestion_compta.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.dropdown_gestion_compta)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_depenses = QPushButton(self.dropdown_gestion_compta)
        self.btn_depenses.setObjectName(u"btn_depenses")
        self.btn_depenses.setFont(font3)
        self.btn_depenses.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_depenses.setStyleSheet(u"QPushButton{\n"
"	padding-left:-34px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#679cdb;\n"
"}")
        self.btn_depenses.setCheckable(True)

        self.verticalLayout_7.addWidget(self.btn_depenses)

        self.btn_flux_monetaires = QPushButton(self.dropdown_gestion_compta)
        self.btn_flux_monetaires.setObjectName(u"btn_flux_monetaires")
        self.btn_flux_monetaires.setFont(font3)
        self.btn_flux_monetaires.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_flux_monetaires.setStyleSheet(u"QPushButton{\n"
"	padding-left:12px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_flux_monetaires.setCheckable(True)

        self.verticalLayout_7.addWidget(self.btn_flux_monetaires)

        self.btn_rapports_financiers = QPushButton(self.dropdown_gestion_compta)
        self.btn_rapports_financiers.setObjectName(u"btn_rapports_financiers")
        self.btn_rapports_financiers.setFont(font3)
        self.btn_rapports_financiers.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_rapports_financiers.setStyleSheet(u"QPushButton{\n"
"	padding-left:38px;\n"
"	height:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:#2672CC;\n"
"}")
        self.btn_rapports_financiers.setCheckable(True)

        self.verticalLayout_7.addWidget(self.btn_rapports_financiers)


        self.verticalLayout_9.addWidget(self.dropdown_gestion_compta)


        self.verticalLayout_2.addWidget(self.frame_gestion_compta)


        self.verticalLayout_10.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 209, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_parametre_2 = QPushButton(self.icon_text_widget)
        self.btn_parametre_2.setObjectName(u"btn_parametre_2")
        self.btn_parametre_2.setFont(font2)
        self.btn_parametre_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_parametre_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-50px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	border-radius:3px;\n"
"	background-color: white;\n"
"	color:#2672CC;\n"
"}")
        self.btn_parametre_2.setIcon(icon5)
        self.btn_parametre_2.setIconSize(QSize(30, 30))
        self.btn_parametre_2.setCheckable(True)
        self.btn_parametre_2.setChecked(False)
        self.btn_parametre_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_parametre_2)

        self.btn_deconnexion_2 = QPushButton(self.icon_text_widget)
        self.btn_deconnexion_2.setObjectName(u"btn_deconnexion_2")
        self.btn_deconnexion_2.setFont(font2)
        self.btn_deconnexion_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_deconnexion_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-40px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	border-radius:3px;\n"
"	background-color: white;\n"
"	color:#2672CC;\n"
"}")
        self.btn_deconnexion_2.setIcon(icon6)
        self.btn_deconnexion_2.setIconSize(QSize(30, 30))
        self.btn_deconnexion_2.setCheckable(True)
        self.btn_deconnexion_2.setChecked(False)
        self.btn_deconnexion_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_deconnexion_2)


        self.verticalLayout_10.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 1, 1)

        self.main_screen_widget = QWidget(self.centralwidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setEnabled(True)
        self.main_screen_widget.setMinimumSize(QSize(920, 0))
        self.verticalLayout_11 = QVBoxLayout(self.main_screen_widget)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.header_widget_2 = QWidget(self.main_screen_widget)
        self.header_widget_2.setObjectName(u"header_widget_2")
        self.header_widget_2.setMinimumSize(QSize(895, 0))
        self.header_widget_2.setMaximumSize(QSize(16777215, 66))
        self.horizontalLayout_3 = QHBoxLayout(self.header_widget_2)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 10, 5, 5)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(-1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.pushButton = QPushButton(self.header_widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border:none;")
        icon7 = QIcon()
        icon7.addFile(u":/icones/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QSize(29, 35))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 5, -1, -1)
        self.label = QLabel(self.header_widget_2)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"Courier"])
        font4.setPointSize(15)
        font4.setBold(True)
        self.label.setFont(font4)

        self.verticalLayout_15.addWidget(self.label)

        self.label_6 = QLabel(self.header_widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(169, 169, 169);")

        self.verticalLayout_15.addWidget(self.label_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout_15)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_6 = QSpacerItem(358, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_2 = QLineEdit(self.header_widget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.label_7 = QLabel(self.header_widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(40, 40))
        self.label_7.setMaximumSize(QSize(40, 40))
        self.label_7.setPixmap(QPixmap(u":/icones/profile.png"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_7)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_11.addWidget(self.header_widget_2)

        self.main_screen_infos = QWidget(self.main_screen_widget)
        self.main_screen_infos.setObjectName(u"main_screen_infos")
        self.main_screen_infos.setMinimumSize(QSize(895, 672))
        self.main_screen_infos.setStyleSheet(u"")
        self.gridLayout_20 = QGridLayout(self.main_screen_infos)
        self.gridLayout_20.setSpacing(6)
        self.gridLayout_20.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setVerticalSpacing(-1)
        self.gridLayout_20.setContentsMargins(2, 13, 2, 2)
        self.tab_widget = QTabWidget(self.main_screen_infos)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_widget.setEnabled(True)
        self.tab_widget.setMinimumSize(QSize(895, 672))
        font5 = QFont()
        font5.setFamilies([u"Courier"])
        font5.setPointSize(13)
        self.tab_widget.setFont(font5)
        self.tab_widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tab_widget.setAutoFillBackground(False)
        self.tab_widget.setStyleSheet(u"")
        self.tab_widget.setTabPosition(QTabWidget.TabPosition.North)
        self.tab_widget.setIconSize(QSize(30, 30))
        self.tab_widget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tab_widget.setUsesScrollButtons(True)
        self.tab_widget.setDocumentMode(False)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.setMovable(False)
        self.tab_widget.setTabBarAutoHide(False)
        self.tab_dashboard = QWidget()
        self.tab_dashboard.setObjectName(u"tab_dashboard")
        self.label_21 = QLabel(self.tab_dashboard)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(290, 90, 271, 71))
        font6 = QFont()
        font6.setFamilies([u"Courier"])
        font6.setPointSize(25)
        self.label_21.setFont(font6)
        self.tab_widget.addTab(self.tab_dashboard, "")
        self.tab_matieres_premieres = QWidget()
        self.tab_matieres_premieres.setObjectName(u"tab_matieres_premieres")
        self.tab_matieres_premieres.setEnabled(True)
        self.gridLayout_7 = QGridLayout(self.tab_matieres_premieres)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_ajout_matiere_premiere = QPushButton(self.tab_matieres_premieres)
        self.btn_ajout_matiere_premiere.setObjectName(u"btn_ajout_matiere_premiere")
        self.btn_ajout_matiere_premiere.setMinimumSize(QSize(160, 32))
        self.btn_ajout_matiere_premiere.setMaximumSize(QSize(205, 32))
        self.btn_ajout_matiere_premiere.setFont(font2)
        self.btn_ajout_matiere_premiere.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ajout_matiere_premiere.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icones/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ajout_matiere_premiere.setIcon(icon8)

        self.horizontalLayout_12.addWidget(self.btn_ajout_matiere_premiere)

        self.btn_export_matieres_premieres_excel = QPushButton(self.tab_matieres_premieres)
        self.btn_export_matieres_premieres_excel.setObjectName(u"btn_export_matieres_premieres_excel")
        self.btn_export_matieres_premieres_excel.setMinimumSize(QSize(115, 32))
        self.btn_export_matieres_premieres_excel.setMaximumSize(QSize(115, 32))
        self.btn_export_matieres_premieres_excel.setFont(font2)
        self.btn_export_matieres_premieres_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_matieres_premieres_excel.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icones/excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_export_matieres_premieres_excel.setIcon(icon9)

        self.horizontalLayout_12.addWidget(self.btn_export_matieres_premieres_excel)

        self.btn_export_matieres_premieres_pdf = QPushButton(self.tab_matieres_premieres)
        self.btn_export_matieres_premieres_pdf.setObjectName(u"btn_export_matieres_premieres_pdf")
        self.btn_export_matieres_premieres_pdf.setMinimumSize(QSize(0, 32))
        self.btn_export_matieres_premieres_pdf.setMaximumSize(QSize(125, 32))
        self.btn_export_matieres_premieres_pdf.setFont(font2)
        self.btn_export_matieres_premieres_pdf.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_matieres_premieres_pdf.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 58, 21);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icones/pdf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_export_matieres_premieres_pdf.setIcon(icon10)

        self.horizontalLayout_12.addWidget(self.btn_export_matieres_premieres_pdf)

        self.horizontalSpacer_10 = QSpacerItem(38, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_10)

        self.cherche_matiere_premiere = QLineEdit(self.tab_matieres_premieres)
        self.cherche_matiere_premiere.setObjectName(u"cherche_matiere_premiere")
        self.cherche_matiere_premiere.setMinimumSize(QSize(395, 30))
        self.cherche_matiere_premiere.setMaximumSize(QSize(407, 30))
        self.cherche_matiere_premiere.setFont(font3)
        self.cherche_matiere_premiere.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")
        self.cherche_matiere_premiere.setClearButtonEnabled(True)

        self.horizontalLayout_12.addWidget(self.cherche_matiere_premiere)


        self.gridLayout_7.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)

        self.table_infos_matieres_premieres = QTableWidget(self.tab_matieres_premieres)
        if (self.table_infos_matieres_premieres.columnCount() < 8):
            self.table_infos_matieres_premieres.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_infos_matieres_premieres.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_infos_matieres_premieres.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_infos_matieres_premieres.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_infos_matieres_premieres.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_infos_matieres_premieres.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_infos_matieres_premieres.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_infos_matieres_premieres.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_infos_matieres_premieres.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.table_infos_matieres_premieres.setObjectName(u"table_infos_matieres_premieres")
        font7 = QFont()
        font7.setFamilies([u"Courier"])
        font7.setPointSize(12)
        self.table_infos_matieres_premieres.setFont(font7)
        self.table_infos_matieres_premieres.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	/*background-color: black;*/\n"
"	/*color: white;*/\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_matieres_premieres.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_infos_matieres_premieres.setAlternatingRowColors(True)
        self.table_infos_matieres_premieres.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.table_infos_matieres_premieres.setSortingEnabled(True)
        self.table_infos_matieres_premieres.horizontalHeader().setVisible(True)
        self.table_infos_matieres_premieres.horizontalHeader().setCascadingSectionResizes(True)
        self.table_infos_matieres_premieres.horizontalHeader().setMinimumSectionSize(80)
        self.table_infos_matieres_premieres.horizontalHeader().setDefaultSectionSize(150)
        self.table_infos_matieres_premieres.horizontalHeader().setProperty("showSortIndicator", True)
        self.table_infos_matieres_premieres.horizontalHeader().setStretchLastSection(True)
        self.table_infos_matieres_premieres.verticalHeader().setVisible(False)

        self.gridLayout_7.addWidget(self.table_infos_matieres_premieres, 1, 0, 1, 1)

        self.tab_widget.addTab(self.tab_matieres_premieres, "")
        self.tab_produits = QWidget()
        self.tab_produits.setObjectName(u"tab_produits")
        self.gridLayout_9 = QGridLayout(self.tab_produits)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.btn_ajout_produit = QPushButton(self.tab_produits)
        self.btn_ajout_produit.setObjectName(u"btn_ajout_produit")
        self.btn_ajout_produit.setMinimumSize(QSize(160, 32))
        self.btn_ajout_produit.setMaximumSize(QSize(160, 32))
        self.btn_ajout_produit.setFont(font2)
        self.btn_ajout_produit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ajout_produit.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_ajout_produit.setIcon(icon8)

        self.horizontalLayout_14.addWidget(self.btn_ajout_produit)

        self.btn_export_produit_excel = QPushButton(self.tab_produits)
        self.btn_export_produit_excel.setObjectName(u"btn_export_produit_excel")
        self.btn_export_produit_excel.setMinimumSize(QSize(115, 32))
        self.btn_export_produit_excel.setMaximumSize(QSize(115, 32))
        self.btn_export_produit_excel.setFont(font2)
        self.btn_export_produit_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_produit_excel.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_export_produit_excel.setIcon(icon9)

        self.horizontalLayout_14.addWidget(self.btn_export_produit_excel)

        self.btn_export_produit_pdf = QPushButton(self.tab_produits)
        self.btn_export_produit_pdf.setObjectName(u"btn_export_produit_pdf")
        self.btn_export_produit_pdf.setMinimumSize(QSize(0, 32))
        self.btn_export_produit_pdf.setMaximumSize(QSize(125, 32))
        self.btn_export_produit_pdf.setFont(font2)
        self.btn_export_produit_pdf.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_produit_pdf.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 58, 21);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_export_produit_pdf.setIcon(icon10)

        self.horizontalLayout_14.addWidget(self.btn_export_produit_pdf)

        self.horizontalSpacer_12 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_12)

        self.cherche_produit = QLineEdit(self.tab_produits)
        self.cherche_produit.setObjectName(u"cherche_produit")
        self.cherche_produit.setMinimumSize(QSize(407, 32))
        self.cherche_produit.setMaximumSize(QSize(407, 31))
        self.cherche_produit.setFont(font3)
        self.cherche_produit.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")
        self.cherche_produit.setClearButtonEnabled(True)

        self.horizontalLayout_14.addWidget(self.cherche_produit)


        self.gridLayout_9.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)

        self.table_infos_produits = QTableWidget(self.tab_produits)
        if (self.table_infos_produits.columnCount() < 8):
            self.table_infos_produits.setColumnCount(8)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_infos_produits.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_infos_produits.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_infos_produits.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_infos_produits.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_infos_produits.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_infos_produits.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_infos_produits.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_infos_produits.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        self.table_infos_produits.setObjectName(u"table_infos_produits")
        self.table_infos_produits.setFont(font7)
        self.table_infos_produits.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	/*background-color: black;*/\n"
"	/*color: white;*/\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_produits.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_infos_produits.setAlternatingRowColors(True)
        self.table_infos_produits.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.table_infos_produits.setSortingEnabled(True)
        self.table_infos_produits.horizontalHeader().setCascadingSectionResizes(True)
        self.table_infos_produits.horizontalHeader().setMinimumSectionSize(80)
        self.table_infos_produits.horizontalHeader().setDefaultSectionSize(150)
        self.table_infos_produits.horizontalHeader().setProperty("showSortIndicator", True)
        self.table_infos_produits.horizontalHeader().setStretchLastSection(True)
        self.table_infos_produits.verticalHeader().setVisible(False)

        self.gridLayout_9.addWidget(self.table_infos_produits, 1, 0, 1, 1)

        self.tab_widget.addTab(self.tab_produits, "")
        self.tab_fournisseurs = QWidget()
        self.tab_fournisseurs.setObjectName(u"tab_fournisseurs")
        self.gridLayout_4 = QGridLayout(self.tab_fournisseurs)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_ajout_fournisseur = QPushButton(self.tab_fournisseurs)
        self.btn_ajout_fournisseur.setObjectName(u"btn_ajout_fournisseur")
        self.btn_ajout_fournisseur.setMinimumSize(QSize(160, 32))
        self.btn_ajout_fournisseur.setMaximumSize(QSize(160, 32))
        self.btn_ajout_fournisseur.setFont(font2)
        self.btn_ajout_fournisseur.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ajout_fournisseur.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_ajout_fournisseur.setIcon(icon8)

        self.horizontalLayout_9.addWidget(self.btn_ajout_fournisseur)

        self.btn_export_fournisseurs_excel = QPushButton(self.tab_fournisseurs)
        self.btn_export_fournisseurs_excel.setObjectName(u"btn_export_fournisseurs_excel")
        self.btn_export_fournisseurs_excel.setMinimumSize(QSize(115, 32))
        self.btn_export_fournisseurs_excel.setMaximumSize(QSize(115, 32))
        self.btn_export_fournisseurs_excel.setFont(font2)
        self.btn_export_fournisseurs_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_fournisseurs_excel.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_export_fournisseurs_excel.setIcon(icon9)

        self.horizontalLayout_9.addWidget(self.btn_export_fournisseurs_excel)

        self.btn_export_fournisseurs_pdf = QPushButton(self.tab_fournisseurs)
        self.btn_export_fournisseurs_pdf.setObjectName(u"btn_export_fournisseurs_pdf")
        self.btn_export_fournisseurs_pdf.setMinimumSize(QSize(0, 32))
        self.btn_export_fournisseurs_pdf.setMaximumSize(QSize(125, 32))
        self.btn_export_fournisseurs_pdf.setFont(font2)
        self.btn_export_fournisseurs_pdf.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_fournisseurs_pdf.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 58, 21);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_export_fournisseurs_pdf.setIcon(icon10)

        self.horizontalLayout_9.addWidget(self.btn_export_fournisseurs_pdf)

        self.horizontalSpacer_7 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.cherche_fournisseur = QLineEdit(self.tab_fournisseurs)
        self.cherche_fournisseur.setObjectName(u"cherche_fournisseur")
        self.cherche_fournisseur.setMinimumSize(QSize(407, 32))
        self.cherche_fournisseur.setMaximumSize(QSize(407, 31))
        self.cherche_fournisseur.setFont(font3)
        self.cherche_fournisseur.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")
        self.cherche_fournisseur.setClearButtonEnabled(True)

        self.horizontalLayout_9.addWidget(self.cherche_fournisseur)


        self.gridLayout_4.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        self.table_infos_fournisseurs = QTableWidget(self.tab_fournisseurs)
        if (self.table_infos_fournisseurs.columnCount() < 6):
            self.table_infos_fournisseurs.setColumnCount(6)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_infos_fournisseurs.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_infos_fournisseurs.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_infos_fournisseurs.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_infos_fournisseurs.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_infos_fournisseurs.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_infos_fournisseurs.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        self.table_infos_fournisseurs.setObjectName(u"table_infos_fournisseurs")
        self.table_infos_fournisseurs.setFont(font7)
        self.table_infos_fournisseurs.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	/*background-color: black;*/\n"
"	/*color: white;*/\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_fournisseurs.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_infos_fournisseurs.setAlternatingRowColors(True)
        self.table_infos_fournisseurs.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.table_infos_fournisseurs.setSortingEnabled(True)
        self.table_infos_fournisseurs.horizontalHeader().setMinimumSectionSize(20)
        self.table_infos_fournisseurs.horizontalHeader().setDefaultSectionSize(120)
        self.table_infos_fournisseurs.horizontalHeader().setStretchLastSection(True)
        self.table_infos_fournisseurs.verticalHeader().setVisible(False)
        self.table_infos_fournisseurs.verticalHeader().setCascadingSectionResizes(False)
        self.table_infos_fournisseurs.verticalHeader().setMinimumSectionSize(21)
        self.table_infos_fournisseurs.verticalHeader().setDefaultSectionSize(30)
        self.table_infos_fournisseurs.verticalHeader().setHighlightSections(False)
        self.table_infos_fournisseurs.verticalHeader().setProperty("showSortIndicator", False)
        self.table_infos_fournisseurs.verticalHeader().setStretchLastSection(False)

        self.gridLayout_4.addWidget(self.table_infos_fournisseurs, 1, 0, 1, 1)

        self.tab_widget.addTab(self.tab_fournisseurs, "")
        self.tab_entrepots = QWidget()
        self.tab_entrepots.setObjectName(u"tab_entrepots")
        self.gridLayout_24 = QGridLayout(self.tab_entrepots)
        self.gridLayout_24.setSpacing(6)
        self.gridLayout_24.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setHorizontalSpacing(2)
        self.gridLayout_24.setVerticalSpacing(-1)
        self.gridLayout_24.setContentsMargins(0, 0, 0, 2)
        self.table_infos_entrepots = QTableWidget(self.tab_entrepots)
        if (self.table_infos_entrepots.columnCount() < 6):
            self.table_infos_entrepots.setColumnCount(6)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_infos_entrepots.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_infos_entrepots.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_infos_entrepots.setHorizontalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_infos_entrepots.setHorizontalHeaderItem(3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_infos_entrepots.setHorizontalHeaderItem(4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_infos_entrepots.setHorizontalHeaderItem(5, __qtablewidgetitem27)
        self.table_infos_entrepots.setObjectName(u"table_infos_entrepots")
        self.table_infos_entrepots.setFont(font7)
        self.table_infos_entrepots.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	/*background-color: black;*/\n"
"	/*color: white;*/\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_entrepots.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_infos_entrepots.setAlternatingRowColors(True)
        self.table_infos_entrepots.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.table_infos_entrepots.setSortingEnabled(True)
        self.table_infos_entrepots.horizontalHeader().setCascadingSectionResizes(True)
        self.table_infos_entrepots.horizontalHeader().setDefaultSectionSize(150)
        self.table_infos_entrepots.horizontalHeader().setStretchLastSection(True)
        self.table_infos_entrepots.verticalHeader().setVisible(False)
        self.table_infos_entrepots.verticalHeader().setCascadingSectionResizes(False)
        self.table_infos_entrepots.verticalHeader().setMinimumSectionSize(21)
        self.table_infos_entrepots.verticalHeader().setDefaultSectionSize(30)
        self.table_infos_entrepots.verticalHeader().setHighlightSections(False)
        self.table_infos_entrepots.verticalHeader().setProperty("showSortIndicator", False)
        self.table_infos_entrepots.verticalHeader().setStretchLastSection(False)

        self.gridLayout_24.addWidget(self.table_infos_entrepots, 1, 0, 1, 2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_ajout_entrepot = QPushButton(self.tab_entrepots)
        self.btn_ajout_entrepot.setObjectName(u"btn_ajout_entrepot")
        self.btn_ajout_entrepot.setMinimumSize(QSize(0, 32))
        self.btn_ajout_entrepot.setMaximumSize(QSize(125, 32))
        self.btn_ajout_entrepot.setFont(font2)
        self.btn_ajout_entrepot.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ajout_entrepot.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_ajout_entrepot.setIcon(icon8)

        self.horizontalLayout_7.addWidget(self.btn_ajout_entrepot)

        self.btn_export_entrepots_excel = QPushButton(self.tab_entrepots)
        self.btn_export_entrepots_excel.setObjectName(u"btn_export_entrepots_excel")
        self.btn_export_entrepots_excel.setMinimumSize(QSize(0, 32))
        self.btn_export_entrepots_excel.setMaximumSize(QSize(125, 32))
        self.btn_export_entrepots_excel.setFont(font2)
        self.btn_export_entrepots_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_entrepots_excel.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_export_entrepots_excel.setIcon(icon9)

        self.horizontalLayout_7.addWidget(self.btn_export_entrepots_excel)

        self.btn_export_entrepots_pdf = QPushButton(self.tab_entrepots)
        self.btn_export_entrepots_pdf.setObjectName(u"btn_export_entrepots_pdf")
        self.btn_export_entrepots_pdf.setMinimumSize(QSize(0, 32))
        self.btn_export_entrepots_pdf.setMaximumSize(QSize(125, 32))
        self.btn_export_entrepots_pdf.setFont(font2)
        self.btn_export_entrepots_pdf.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_entrepots_pdf.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 58, 21);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_export_entrepots_pdf.setIcon(icon10)

        self.horizontalLayout_7.addWidget(self.btn_export_entrepots_pdf)

        self.horizontalSpacer_2 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.cherche_entrepot = QLineEdit(self.tab_entrepots)
        self.cherche_entrepot.setObjectName(u"cherche_entrepot")
        self.cherche_entrepot.setMinimumSize(QSize(407, 32))
        self.cherche_entrepot.setMaximumSize(QSize(407, 31))
        self.cherche_entrepot.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")
        self.cherche_entrepot.setClearButtonEnabled(True)

        self.horizontalLayout_7.addWidget(self.cherche_entrepot)


        self.gridLayout_24.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.tab_widget.addTab(self.tab_entrepots, "")
        self.tab_clients = QWidget()
        self.tab_clients.setObjectName(u"tab_clients")
        self.tab_clients.setEnabled(True)
        self.gridLayout_2 = QGridLayout(self.tab_clients)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 2)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_ajout_client = QPushButton(self.tab_clients)
        self.btn_ajout_client.setObjectName(u"btn_ajout_client")
        self.btn_ajout_client.setMinimumSize(QSize(0, 32))
        self.btn_ajout_client.setMaximumSize(QSize(125, 32))
        self.btn_ajout_client.setFont(font2)
        self.btn_ajout_client.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ajout_client.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_ajout_client.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.btn_ajout_client)

        self.btn_export_clients_excel = QPushButton(self.tab_clients)
        self.btn_export_clients_excel.setObjectName(u"btn_export_clients_excel")
        self.btn_export_clients_excel.setMinimumSize(QSize(0, 32))
        self.btn_export_clients_excel.setMaximumSize(QSize(125, 32))
        self.btn_export_clients_excel.setFont(font2)
        self.btn_export_clients_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_clients_excel.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_export_clients_excel.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.btn_export_clients_excel)

        self.btn_export_clients_pdf = QPushButton(self.tab_clients)
        self.btn_export_clients_pdf.setObjectName(u"btn_export_clients_pdf")
        self.btn_export_clients_pdf.setMinimumSize(QSize(0, 32))
        self.btn_export_clients_pdf.setMaximumSize(QSize(125, 32))
        self.btn_export_clients_pdf.setFont(font2)
        self.btn_export_clients_pdf.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_clients_pdf.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 58, 21);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_export_clients_pdf.setIcon(icon10)

        self.horizontalLayout_5.addWidget(self.btn_export_clients_pdf)

        self.horizontalSpacer = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.cherche_client = QLineEdit(self.tab_clients)
        self.cherche_client.setObjectName(u"cherche_client")
        self.cherche_client.setMinimumSize(QSize(407, 32))
        self.cherche_client.setMaximumSize(QSize(407, 31))
        self.cherche_client.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")
        self.cherche_client.setClearButtonEnabled(True)

        self.horizontalLayout_5.addWidget(self.cherche_client)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.table_infos_clients = QTableWidget(self.tab_clients)
        if (self.table_infos_clients.columnCount() < 7):
            self.table_infos_clients.setColumnCount(7)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.table_infos_clients.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.table_infos_clients.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.table_infos_clients.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.table_infos_clients.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.table_infos_clients.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.table_infos_clients.setHorizontalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.table_infos_clients.setHorizontalHeaderItem(6, __qtablewidgetitem34)
        self.table_infos_clients.setObjectName(u"table_infos_clients")
        self.table_infos_clients.setMinimumSize(QSize(915, 710))
        self.table_infos_clients.setFont(font7)
        self.table_infos_clients.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	/*background-color: black;*/\n"
"	/*color: white;*/\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"	test-align: center;\n"
"}")
        self.table_infos_clients.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.table_infos_clients.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_infos_clients.setDragEnabled(False)
        self.table_infos_clients.setAlternatingRowColors(True)
        self.table_infos_clients.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.table_infos_clients.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.table_infos_clients.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.table_infos_clients.setShowGrid(True)
        self.table_infos_clients.setGridStyle(Qt.PenStyle.CustomDashLine)
        self.table_infos_clients.setSortingEnabled(True)
        self.table_infos_clients.horizontalHeader().setVisible(True)
        self.table_infos_clients.horizontalHeader().setCascadingSectionResizes(True)
        self.table_infos_clients.horizontalHeader().setMinimumSectionSize(80)
        self.table_infos_clients.horizontalHeader().setDefaultSectionSize(150)
        self.table_infos_clients.horizontalHeader().setProperty("showSortIndicator", True)
        self.table_infos_clients.horizontalHeader().setStretchLastSection(True)
        self.table_infos_clients.verticalHeader().setVisible(False)
        self.table_infos_clients.verticalHeader().setCascadingSectionResizes(False)
        self.table_infos_clients.verticalHeader().setMinimumSectionSize(21)
        self.table_infos_clients.verticalHeader().setDefaultSectionSize(30)
        self.table_infos_clients.verticalHeader().setHighlightSections(False)
        self.table_infos_clients.verticalHeader().setProperty("showSortIndicator", False)
        self.table_infos_clients.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.table_infos_clients, 1, 0, 1, 1)

        self.tab_widget.addTab(self.tab_clients, "")
        self.tab_inventaires = QWidget()
        self.tab_inventaires.setObjectName(u"tab_inventaires")
        self.gridLayout_5 = QGridLayout(self.tab_inventaires)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_debut_inventaire = QPushButton(self.tab_inventaires)
        self.btn_debut_inventaire.setObjectName(u"btn_debut_inventaire")
        self.btn_debut_inventaire.setMinimumSize(QSize(160, 32))
        self.btn_debut_inventaire.setMaximumSize(QSize(160, 32))
        self.btn_debut_inventaire.setFont(font2)
        self.btn_debut_inventaire.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_debut_inventaire.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_debut_inventaire.setIcon(icon8)

        self.horizontalLayout_10.addWidget(self.btn_debut_inventaire)

        self.btn_export_inventaire_excel = QPushButton(self.tab_inventaires)
        self.btn_export_inventaire_excel.setObjectName(u"btn_export_inventaire_excel")
        self.btn_export_inventaire_excel.setMinimumSize(QSize(115, 32))
        self.btn_export_inventaire_excel.setMaximumSize(QSize(115, 32))
        self.btn_export_inventaire_excel.setFont(font2)
        self.btn_export_inventaire_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_inventaire_excel.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_export_inventaire_excel.setIcon(icon9)

        self.horizontalLayout_10.addWidget(self.btn_export_inventaire_excel)

        self.btn_export_inventaire_pdf = QPushButton(self.tab_inventaires)
        self.btn_export_inventaire_pdf.setObjectName(u"btn_export_inventaire_pdf")
        self.btn_export_inventaire_pdf.setMinimumSize(QSize(0, 32))
        self.btn_export_inventaire_pdf.setMaximumSize(QSize(125, 32))
        self.btn_export_inventaire_pdf.setFont(font2)
        self.btn_export_inventaire_pdf.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_inventaire_pdf.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 58, 21);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_export_inventaire_pdf.setIcon(icon10)

        self.horizontalLayout_10.addWidget(self.btn_export_inventaire_pdf)

        self.horizontalSpacer_8 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.cherche_inventaire = QLineEdit(self.tab_inventaires)
        self.cherche_inventaire.setObjectName(u"cherche_inventaire")
        self.cherche_inventaire.setMinimumSize(QSize(407, 32))
        self.cherche_inventaire.setMaximumSize(QSize(407, 31))
        self.cherche_inventaire.setFont(font3)
        self.cherche_inventaire.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")
        self.cherche_inventaire.setClearButtonEnabled(True)

        self.horizontalLayout_10.addWidget(self.cherche_inventaire)


        self.gridLayout_5.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)

        self.table_infos_inventaire = QTableWidget(self.tab_inventaires)
        if (self.table_infos_inventaire.columnCount() < 9):
            self.table_infos_inventaire.setColumnCount(9)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.table_infos_inventaire.setHorizontalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.table_infos_inventaire.setHorizontalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.table_infos_inventaire.setHorizontalHeaderItem(2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.table_infos_inventaire.setHorizontalHeaderItem(3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.table_infos_inventaire.setHorizontalHeaderItem(4, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.table_infos_inventaire.setHorizontalHeaderItem(5, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.table_infos_inventaire.setHorizontalHeaderItem(6, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.table_infos_inventaire.setHorizontalHeaderItem(7, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.table_infos_inventaire.setHorizontalHeaderItem(8, __qtablewidgetitem43)
        self.table_infos_inventaire.setObjectName(u"table_infos_inventaire")
        self.table_infos_inventaire.setFont(font7)
        self.table_infos_inventaire.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	/*background-color: black;*/\n"
"	/*color: white;*/\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_inventaire.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_infos_inventaire.setAlternatingRowColors(True)
        self.table_infos_inventaire.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.table_infos_inventaire.setSortingEnabled(True)
        self.table_infos_inventaire.horizontalHeader().setMinimumSectionSize(20)
        self.table_infos_inventaire.horizontalHeader().setDefaultSectionSize(120)
        self.table_infos_inventaire.horizontalHeader().setStretchLastSection(True)
        self.table_infos_inventaire.verticalHeader().setVisible(False)
        self.table_infos_inventaire.verticalHeader().setCascadingSectionResizes(False)
        self.table_infos_inventaire.verticalHeader().setMinimumSectionSize(21)
        self.table_infos_inventaire.verticalHeader().setDefaultSectionSize(30)
        self.table_infos_inventaire.verticalHeader().setHighlightSections(False)
        self.table_infos_inventaire.verticalHeader().setProperty("showSortIndicator", False)
        self.table_infos_inventaire.verticalHeader().setStretchLastSection(False)

        self.gridLayout_5.addWidget(self.table_infos_inventaire, 1, 0, 1, 1)

        self.tab_widget.addTab(self.tab_inventaires, "")
        self.tab_ventes_retours = QWidget()
        self.tab_ventes_retours.setObjectName(u"tab_ventes_retours")
        self.gridLayout_10 = QGridLayout(self.tab_ventes_retours)
        self.gridLayout_10.setSpacing(6)
        self.gridLayout_10.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btn_ajout_vente_retour = QPushButton(self.tab_ventes_retours)
        self.btn_ajout_vente_retour.setObjectName(u"btn_ajout_vente_retour")
        self.btn_ajout_vente_retour.setMinimumSize(QSize(160, 32))
        self.btn_ajout_vente_retour.setMaximumSize(QSize(160, 32))
        self.btn_ajout_vente_retour.setFont(font2)
        self.btn_ajout_vente_retour.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ajout_vente_retour.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_ajout_vente_retour.setIcon(icon8)

        self.horizontalLayout_15.addWidget(self.btn_ajout_vente_retour)

        self.btn_export_ventes_retours_excel = QPushButton(self.tab_ventes_retours)
        self.btn_export_ventes_retours_excel.setObjectName(u"btn_export_ventes_retours_excel")
        self.btn_export_ventes_retours_excel.setMinimumSize(QSize(115, 32))
        self.btn_export_ventes_retours_excel.setMaximumSize(QSize(115, 32))
        self.btn_export_ventes_retours_excel.setFont(font2)
        self.btn_export_ventes_retours_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_ventes_retours_excel.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_export_ventes_retours_excel.setIcon(icon9)

        self.horizontalLayout_15.addWidget(self.btn_export_ventes_retours_excel)

        self.btn_export_vente_retour_pdf = QPushButton(self.tab_ventes_retours)
        self.btn_export_vente_retour_pdf.setObjectName(u"btn_export_vente_retour_pdf")
        self.btn_export_vente_retour_pdf.setMinimumSize(QSize(0, 32))
        self.btn_export_vente_retour_pdf.setMaximumSize(QSize(125, 32))
        self.btn_export_vente_retour_pdf.setFont(font2)
        self.btn_export_vente_retour_pdf.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_vente_retour_pdf.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 58, 21);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_export_vente_retour_pdf.setIcon(icon10)

        self.horizontalLayout_15.addWidget(self.btn_export_vente_retour_pdf)

        self.horizontalSpacer_13 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_13)

        self.cherche_vente_retour = QLineEdit(self.tab_ventes_retours)
        self.cherche_vente_retour.setObjectName(u"cherche_vente_retour")
        self.cherche_vente_retour.setMinimumSize(QSize(407, 32))
        self.cherche_vente_retour.setMaximumSize(QSize(407, 31))
        self.cherche_vente_retour.setFont(font3)
        self.cherche_vente_retour.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")
        self.cherche_vente_retour.setClearButtonEnabled(True)

        self.horizontalLayout_15.addWidget(self.cherche_vente_retour)


        self.gridLayout_10.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)

        self.table_infos_ventes_retours = QTableWidget(self.tab_ventes_retours)
        if (self.table_infos_ventes_retours.columnCount() < 8):
            self.table_infos_ventes_retours.setColumnCount(8)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.table_infos_ventes_retours.setHorizontalHeaderItem(0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.table_infos_ventes_retours.setHorizontalHeaderItem(1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.table_infos_ventes_retours.setHorizontalHeaderItem(2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.table_infos_ventes_retours.setHorizontalHeaderItem(3, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.table_infos_ventes_retours.setHorizontalHeaderItem(4, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.table_infos_ventes_retours.setHorizontalHeaderItem(5, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.table_infos_ventes_retours.setHorizontalHeaderItem(6, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.table_infos_ventes_retours.setHorizontalHeaderItem(7, __qtablewidgetitem51)
        self.table_infos_ventes_retours.setObjectName(u"table_infos_ventes_retours")
        self.table_infos_ventes_retours.setFont(font7)
        self.table_infos_ventes_retours.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	/*background-color: black;*/\n"
"	/*color: white;*/\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_ventes_retours.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_infos_ventes_retours.setAlternatingRowColors(True)
        self.table_infos_ventes_retours.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.table_infos_ventes_retours.setSortingEnabled(True)
        self.table_infos_ventes_retours.horizontalHeader().setCascadingSectionResizes(True)
        self.table_infos_ventes_retours.horizontalHeader().setMinimumSectionSize(80)
        self.table_infos_ventes_retours.horizontalHeader().setDefaultSectionSize(150)
        self.table_infos_ventes_retours.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_10.addWidget(self.table_infos_ventes_retours, 1, 0, 1, 1)

        self.tab_widget.addTab(self.tab_ventes_retours, "")
        self.tab_mvts_stocks = QWidget()
        self.tab_mvts_stocks.setObjectName(u"tab_mvts_stocks")
        self.tab_mvts_stocks.setEnabled(True)
        self.gridLayout_8 = QGridLayout(self.tab_mvts_stocks)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_export_mvts_stocks_excel = QPushButton(self.tab_mvts_stocks)
        self.btn_export_mvts_stocks_excel.setObjectName(u"btn_export_mvts_stocks_excel")
        self.btn_export_mvts_stocks_excel.setMinimumSize(QSize(115, 32))
        self.btn_export_mvts_stocks_excel.setMaximumSize(QSize(115, 32))
        self.btn_export_mvts_stocks_excel.setFont(font2)
        self.btn_export_mvts_stocks_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_mvts_stocks_excel.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_export_mvts_stocks_excel.setIcon(icon9)

        self.horizontalLayout_13.addWidget(self.btn_export_mvts_stocks_excel)

        self.btn_export_mvts_stocks_pdf = QPushButton(self.tab_mvts_stocks)
        self.btn_export_mvts_stocks_pdf.setObjectName(u"btn_export_mvts_stocks_pdf")
        self.btn_export_mvts_stocks_pdf.setMinimumSize(QSize(0, 32))
        self.btn_export_mvts_stocks_pdf.setMaximumSize(QSize(125, 32))
        self.btn_export_mvts_stocks_pdf.setFont(font2)
        self.btn_export_mvts_stocks_pdf.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_mvts_stocks_pdf.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 58, 21);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_export_mvts_stocks_pdf.setIcon(icon10)

        self.horizontalLayout_13.addWidget(self.btn_export_mvts_stocks_pdf)

        self.horizontalSpacer_11 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_11)

        self.cherche_mvt_stock = QLineEdit(self.tab_mvts_stocks)
        self.cherche_mvt_stock.setObjectName(u"cherche_mvt_stock")
        self.cherche_mvt_stock.setMinimumSize(QSize(407, 32))
        self.cherche_mvt_stock.setMaximumSize(QSize(407, 31))
        self.cherche_mvt_stock.setFont(font3)
        self.cherche_mvt_stock.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")
        self.cherche_mvt_stock.setClearButtonEnabled(True)

        self.horizontalLayout_13.addWidget(self.cherche_mvt_stock)


        self.gridLayout_8.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)

        self.table_infos_mvts_stocks = QTableWidget(self.tab_mvts_stocks)
        if (self.table_infos_mvts_stocks.columnCount() < 8):
            self.table_infos_mvts_stocks.setColumnCount(8)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.table_infos_mvts_stocks.setHorizontalHeaderItem(0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.table_infos_mvts_stocks.setHorizontalHeaderItem(1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.table_infos_mvts_stocks.setHorizontalHeaderItem(2, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.table_infos_mvts_stocks.setHorizontalHeaderItem(3, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.table_infos_mvts_stocks.setHorizontalHeaderItem(4, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.table_infos_mvts_stocks.setHorizontalHeaderItem(5, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.table_infos_mvts_stocks.setHorizontalHeaderItem(6, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.table_infos_mvts_stocks.setHorizontalHeaderItem(7, __qtablewidgetitem59)
        self.table_infos_mvts_stocks.setObjectName(u"table_infos_mvts_stocks")
        self.table_infos_mvts_stocks.setFont(font7)
        self.table_infos_mvts_stocks.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	/*background-color: black;*/\n"
"	/*color: white;*/\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_mvts_stocks.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_infos_mvts_stocks.setAlternatingRowColors(True)
        self.table_infos_mvts_stocks.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.table_infos_mvts_stocks.setSortingEnabled(True)
        self.table_infos_mvts_stocks.horizontalHeader().setCascadingSectionResizes(True)
        self.table_infos_mvts_stocks.horizontalHeader().setMinimumSectionSize(80)
        self.table_infos_mvts_stocks.horizontalHeader().setDefaultSectionSize(150)
        self.table_infos_mvts_stocks.horizontalHeader().setProperty("showSortIndicator", True)
        self.table_infos_mvts_stocks.horizontalHeader().setStretchLastSection(True)
        self.table_infos_mvts_stocks.verticalHeader().setVisible(False)

        self.gridLayout_8.addWidget(self.table_infos_mvts_stocks, 1, 0, 1, 1)

        self.tab_widget.addTab(self.tab_mvts_stocks, "")
        self.tab_livraisons = QWidget()
        self.tab_livraisons.setObjectName(u"tab_livraisons")
        self.gridLayout_6 = QGridLayout(self.tab_livraisons)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_ajout_livraison = QPushButton(self.tab_livraisons)
        self.btn_ajout_livraison.setObjectName(u"btn_ajout_livraison")
        self.btn_ajout_livraison.setMinimumSize(QSize(160, 32))
        self.btn_ajout_livraison.setMaximumSize(QSize(160, 32))
        self.btn_ajout_livraison.setFont(font2)
        self.btn_ajout_livraison.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ajout_livraison.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_ajout_livraison.setIcon(icon8)

        self.horizontalLayout_11.addWidget(self.btn_ajout_livraison)

        self.btn_export_livraisons_excel = QPushButton(self.tab_livraisons)
        self.btn_export_livraisons_excel.setObjectName(u"btn_export_livraisons_excel")
        self.btn_export_livraisons_excel.setMinimumSize(QSize(115, 32))
        self.btn_export_livraisons_excel.setMaximumSize(QSize(115, 32))
        self.btn_export_livraisons_excel.setFont(font2)
        self.btn_export_livraisons_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_livraisons_excel.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_export_livraisons_excel.setIcon(icon9)

        self.horizontalLayout_11.addWidget(self.btn_export_livraisons_excel)

        self.btn_export_livraisons_pdf = QPushButton(self.tab_livraisons)
        self.btn_export_livraisons_pdf.setObjectName(u"btn_export_livraisons_pdf")
        self.btn_export_livraisons_pdf.setMinimumSize(QSize(0, 32))
        self.btn_export_livraisons_pdf.setMaximumSize(QSize(125, 32))
        self.btn_export_livraisons_pdf.setFont(font2)
        self.btn_export_livraisons_pdf.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_livraisons_pdf.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 58, 21);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_export_livraisons_pdf.setIcon(icon10)

        self.horizontalLayout_11.addWidget(self.btn_export_livraisons_pdf)

        self.horizontalSpacer_9 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)

        self.cherche_livraison = QLineEdit(self.tab_livraisons)
        self.cherche_livraison.setObjectName(u"cherche_livraison")
        self.cherche_livraison.setMinimumSize(QSize(407, 32))
        self.cherche_livraison.setMaximumSize(QSize(407, 31))
        self.cherche_livraison.setFont(font3)
        self.cherche_livraison.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")
        self.cherche_livraison.setClearButtonEnabled(True)

        self.horizontalLayout_11.addWidget(self.cherche_livraison)


        self.gridLayout_6.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)

        self.table_infos_livraison = QTableWidget(self.tab_livraisons)
        if (self.table_infos_livraison.columnCount() < 10):
            self.table_infos_livraison.setColumnCount(10)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.table_infos_livraison.setHorizontalHeaderItem(0, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.table_infos_livraison.setHorizontalHeaderItem(1, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.table_infos_livraison.setHorizontalHeaderItem(2, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.table_infos_livraison.setHorizontalHeaderItem(3, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.table_infos_livraison.setHorizontalHeaderItem(4, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.table_infos_livraison.setHorizontalHeaderItem(5, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.table_infos_livraison.setHorizontalHeaderItem(6, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.table_infos_livraison.setHorizontalHeaderItem(7, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.table_infos_livraison.setHorizontalHeaderItem(8, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.table_infos_livraison.setHorizontalHeaderItem(9, __qtablewidgetitem69)
        self.table_infos_livraison.setObjectName(u"table_infos_livraison")
        self.table_infos_livraison.setFont(font7)
        self.table_infos_livraison.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	/*background-color: black;*/\n"
"	/*color: white;*/\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_livraison.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_infos_livraison.setAlternatingRowColors(True)
        self.table_infos_livraison.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.table_infos_livraison.setSortingEnabled(True)
        self.table_infos_livraison.horizontalHeader().setCascadingSectionResizes(True)
        self.table_infos_livraison.horizontalHeader().setMinimumSectionSize(20)
        self.table_infos_livraison.horizontalHeader().setDefaultSectionSize(120)
        self.table_infos_livraison.horizontalHeader().setProperty("showSortIndicator", True)
        self.table_infos_livraison.horizontalHeader().setStretchLastSection(True)
        self.table_infos_livraison.verticalHeader().setVisible(False)
        self.table_infos_livraison.verticalHeader().setCascadingSectionResizes(False)
        self.table_infos_livraison.verticalHeader().setMinimumSectionSize(21)
        self.table_infos_livraison.verticalHeader().setDefaultSectionSize(30)
        self.table_infos_livraison.verticalHeader().setHighlightSections(False)
        self.table_infos_livraison.verticalHeader().setProperty("showSortIndicator", False)
        self.table_infos_livraison.verticalHeader().setStretchLastSection(False)

        self.gridLayout_6.addWidget(self.table_infos_livraison, 1, 0, 1, 1)

        self.tab_widget.addTab(self.tab_livraisons, "")
        self.tab_flux_monetaires = QWidget()
        self.tab_flux_monetaires.setObjectName(u"tab_flux_monetaires")
        self.gridLayout_3 = QGridLayout(self.tab_flux_monetaires)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_ajout_flux = QPushButton(self.tab_flux_monetaires)
        self.btn_ajout_flux.setObjectName(u"btn_ajout_flux")
        self.btn_ajout_flux.setMinimumSize(QSize(0, 32))
        self.btn_ajout_flux.setMaximumSize(QSize(125, 32))
        self.btn_ajout_flux.setFont(font2)
        self.btn_ajout_flux.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ajout_flux.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_ajout_flux.setIcon(icon8)

        self.horizontalLayout_8.addWidget(self.btn_ajout_flux)

        self.btn_export_flux_excel = QPushButton(self.tab_flux_monetaires)
        self.btn_export_flux_excel.setObjectName(u"btn_export_flux_excel")
        self.btn_export_flux_excel.setMinimumSize(QSize(0, 32))
        self.btn_export_flux_excel.setMaximumSize(QSize(125, 32))
        self.btn_export_flux_excel.setFont(font2)
        self.btn_export_flux_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_flux_excel.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_export_flux_excel.setIcon(icon9)

        self.horizontalLayout_8.addWidget(self.btn_export_flux_excel)

        self.btn_export_flux_pdf = QPushButton(self.tab_flux_monetaires)
        self.btn_export_flux_pdf.setObjectName(u"btn_export_flux_pdf")
        self.btn_export_flux_pdf.setMinimumSize(QSize(0, 32))
        self.btn_export_flux_pdf.setMaximumSize(QSize(125, 32))
        self.btn_export_flux_pdf.setFont(font2)
        self.btn_export_flux_pdf.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_export_flux_pdf.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 58, 21);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_export_flux_pdf.setIcon(icon10)

        self.horizontalLayout_8.addWidget(self.btn_export_flux_pdf)

        self.horizontalSpacer_3 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.cherche_flux = QLineEdit(self.tab_flux_monetaires)
        self.cherche_flux.setObjectName(u"cherche_flux")
        self.cherche_flux.setMinimumSize(QSize(407, 32))
        self.cherche_flux.setMaximumSize(QSize(407, 31))
        self.cherche_flux.setFont(font3)
        self.cherche_flux.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")
        self.cherche_flux.setClearButtonEnabled(True)

        self.horizontalLayout_8.addWidget(self.cherche_flux)


        self.gridLayout_3.addLayout(self.horizontalLayout_8, 0, 0, 1, 2)

        self.table_infos_flux_monetaires_global = QTableWidget(self.tab_flux_monetaires)
        if (self.table_infos_flux_monetaires_global.columnCount() < 7):
            self.table_infos_flux_monetaires_global.setColumnCount(7)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.table_infos_flux_monetaires_global.setHorizontalHeaderItem(0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.table_infos_flux_monetaires_global.setHorizontalHeaderItem(1, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.table_infos_flux_monetaires_global.setHorizontalHeaderItem(2, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.table_infos_flux_monetaires_global.setHorizontalHeaderItem(3, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.table_infos_flux_monetaires_global.setHorizontalHeaderItem(4, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.table_infos_flux_monetaires_global.setHorizontalHeaderItem(5, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.table_infos_flux_monetaires_global.setHorizontalHeaderItem(6, __qtablewidgetitem76)
        self.table_infos_flux_monetaires_global.setObjectName(u"table_infos_flux_monetaires_global")
        self.table_infos_flux_monetaires_global.setMinimumSize(QSize(880, 0))
        self.table_infos_flux_monetaires_global.setFont(font7)
        self.table_infos_flux_monetaires_global.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	/*background-color: black;*/\n"
"	/*color: white;*/\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_flux_monetaires_global.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_infos_flux_monetaires_global.setAlternatingRowColors(True)
        self.table_infos_flux_monetaires_global.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.table_infos_flux_monetaires_global.setShowGrid(True)
        self.table_infos_flux_monetaires_global.setSortingEnabled(True)
        self.table_infos_flux_monetaires_global.horizontalHeader().setVisible(True)
        self.table_infos_flux_monetaires_global.horizontalHeader().setDefaultSectionSize(120)
        self.table_infos_flux_monetaires_global.horizontalHeader().setStretchLastSection(True)
        self.table_infos_flux_monetaires_global.verticalHeader().setVisible(False)
        self.table_infos_flux_monetaires_global.verticalHeader().setCascadingSectionResizes(False)
        self.table_infos_flux_monetaires_global.verticalHeader().setMinimumSectionSize(21)
        self.table_infos_flux_monetaires_global.verticalHeader().setDefaultSectionSize(30)
        self.table_infos_flux_monetaires_global.verticalHeader().setHighlightSections(False)
        self.table_infos_flux_monetaires_global.verticalHeader().setProperty("showSortIndicator", False)
        self.table_infos_flux_monetaires_global.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.table_infos_flux_monetaires_global, 1, 0, 1, 2)

        self.table_infos_flux_monetaires_cat = QTableWidget(self.tab_flux_monetaires)
        if (self.table_infos_flux_monetaires_cat.columnCount() < 3):
            self.table_infos_flux_monetaires_cat.setColumnCount(3)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.table_infos_flux_monetaires_cat.setHorizontalHeaderItem(0, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.table_infos_flux_monetaires_cat.setHorizontalHeaderItem(1, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.table_infos_flux_monetaires_cat.setHorizontalHeaderItem(2, __qtablewidgetitem79)
        self.table_infos_flux_monetaires_cat.setObjectName(u"table_infos_flux_monetaires_cat")
        self.table_infos_flux_monetaires_cat.setFont(font7)
        self.table_infos_flux_monetaires_cat.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	/*background-color: black;*/\n"
"	/*color: white;*/\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_flux_monetaires_cat.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_infos_flux_monetaires_cat.setTabKeyNavigation(True)
        self.table_infos_flux_monetaires_cat.setAlternatingRowColors(True)
        self.table_infos_flux_monetaires_cat.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.table_infos_flux_monetaires_cat.setSortingEnabled(True)
        self.table_infos_flux_monetaires_cat.horizontalHeader().setCascadingSectionResizes(True)
        self.table_infos_flux_monetaires_cat.horizontalHeader().setDefaultSectionSize(120)
        self.table_infos_flux_monetaires_cat.horizontalHeader().setProperty("showSortIndicator", True)
        self.table_infos_flux_monetaires_cat.horizontalHeader().setStretchLastSection(True)
        self.table_infos_flux_monetaires_cat.verticalHeader().setVisible(False)
        self.table_infos_flux_monetaires_cat.verticalHeader().setCascadingSectionResizes(False)
        self.table_infos_flux_monetaires_cat.verticalHeader().setMinimumSectionSize(21)
        self.table_infos_flux_monetaires_cat.verticalHeader().setDefaultSectionSize(30)
        self.table_infos_flux_monetaires_cat.verticalHeader().setHighlightSections(False)
        self.table_infos_flux_monetaires_cat.verticalHeader().setProperty("showSortIndicator", False)
        self.table_infos_flux_monetaires_cat.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.table_infos_flux_monetaires_cat, 2, 0, 1, 1)

        self.table_infos_flux_monetaires_type = QTableWidget(self.tab_flux_monetaires)
        if (self.table_infos_flux_monetaires_type.columnCount() < 2):
            self.table_infos_flux_monetaires_type.setColumnCount(2)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.table_infos_flux_monetaires_type.setHorizontalHeaderItem(0, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.table_infos_flux_monetaires_type.setHorizontalHeaderItem(1, __qtablewidgetitem81)
        self.table_infos_flux_monetaires_type.setObjectName(u"table_infos_flux_monetaires_type")
        self.table_infos_flux_monetaires_type.setFont(font7)
        self.table_infos_flux_monetaires_type.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	/*background-color: black;*/\n"
"	/*color: white;*/\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_flux_monetaires_type.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_infos_flux_monetaires_type.setAlternatingRowColors(True)
        self.table_infos_flux_monetaires_type.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.table_infos_flux_monetaires_type.setSortingEnabled(True)
        self.table_infos_flux_monetaires_type.horizontalHeader().setCascadingSectionResizes(True)
        self.table_infos_flux_monetaires_type.horizontalHeader().setDefaultSectionSize(150)
        self.table_infos_flux_monetaires_type.horizontalHeader().setProperty("showSortIndicator", True)
        self.table_infos_flux_monetaires_type.horizontalHeader().setStretchLastSection(True)
        self.table_infos_flux_monetaires_type.verticalHeader().setVisible(False)
        self.table_infos_flux_monetaires_type.verticalHeader().setCascadingSectionResizes(False)
        self.table_infos_flux_monetaires_type.verticalHeader().setMinimumSectionSize(21)
        self.table_infos_flux_monetaires_type.verticalHeader().setDefaultSectionSize(30)
        self.table_infos_flux_monetaires_type.verticalHeader().setHighlightSections(False)
        self.table_infos_flux_monetaires_type.verticalHeader().setProperty("showSortIndicator", False)
        self.table_infos_flux_monetaires_type.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.table_infos_flux_monetaires_type, 2, 1, 1, 1)

        self.tab_widget.addTab(self.tab_flux_monetaires, "")
        self.tab_rapports_financiers = QWidget()
        self.tab_rapports_financiers.setObjectName(u"tab_rapports_financiers")
        self.gridLayout_31 = QGridLayout(self.tab_rapports_financiers)
        self.gridLayout_31.setSpacing(6)
        self.gridLayout_31.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.table_infos_actifs_immo = QTableWidget(self.tab_rapports_financiers)
        if (self.table_infos_actifs_immo.columnCount() < 2):
            self.table_infos_actifs_immo.setColumnCount(2)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.table_infos_actifs_immo.setHorizontalHeaderItem(0, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.table_infos_actifs_immo.setHorizontalHeaderItem(1, __qtablewidgetitem83)
        self.table_infos_actifs_immo.setObjectName(u"table_infos_actifs_immo")
        self.table_infos_actifs_immo.setFont(font7)
        self.table_infos_actifs_immo.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	/*background-color: black;*/\n"
"	/*color: white;*/\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_actifs_immo.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_infos_actifs_immo.setAlternatingRowColors(True)
        self.table_infos_actifs_immo.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.table_infos_actifs_immo.setSortingEnabled(True)
        self.table_infos_actifs_immo.horizontalHeader().setCascadingSectionResizes(True)
        self.table_infos_actifs_immo.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_31.addWidget(self.table_infos_actifs_immo, 1, 0, 1, 1)

        self.label_19 = QLabel(self.tab_rapports_financiers)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(50, 1))
        font8 = QFont()
        font8.setFamilies([u"Courier"])
        font8.setPointSize(12)
        font8.setBold(True)
        font8.setUnderline(True)
        self.label_19.setFont(font8)

        self.gridLayout_31.addWidget(self.label_19, 2, 0, 1, 1)

        self.label_17 = QLabel(self.tab_rapports_financiers)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(50, 1))
        self.label_17.setFont(font8)

        self.gridLayout_31.addWidget(self.label_17, 0, 0, 1, 1)

        self.table_infos_dettes = QTableWidget(self.tab_rapports_financiers)
        if (self.table_infos_dettes.columnCount() < 2):
            self.table_infos_dettes.setColumnCount(2)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.table_infos_dettes.setHorizontalHeaderItem(0, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.table_infos_dettes.setHorizontalHeaderItem(1, __qtablewidgetitem85)
        self.table_infos_dettes.setObjectName(u"table_infos_dettes")
        self.table_infos_dettes.setFont(font7)
        self.table_infos_dettes.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	/*background-color: black;*/\n"
"	/*color: white;*/\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_dettes.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_infos_dettes.setAlternatingRowColors(True)
        self.table_infos_dettes.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.table_infos_dettes.setSortingEnabled(True)
        self.table_infos_dettes.horizontalHeader().setCascadingSectionResizes(True)
        self.table_infos_dettes.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_31.addWidget(self.table_infos_dettes, 3, 1, 1, 1)

        self.label_18 = QLabel(self.tab_rapports_financiers)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(50, 1))
        self.label_18.setFont(font8)

        self.gridLayout_31.addWidget(self.label_18, 0, 1, 1, 1)

        self.label_22 = QLabel(self.tab_rapports_financiers)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(50, 1))
        self.label_22.setFont(font8)

        self.gridLayout_31.addWidget(self.label_22, 2, 1, 1, 1)

        self.table_infos_capitaux_propres = QTableWidget(self.tab_rapports_financiers)
        if (self.table_infos_capitaux_propres.columnCount() < 2):
            self.table_infos_capitaux_propres.setColumnCount(2)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.table_infos_capitaux_propres.setHorizontalHeaderItem(0, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.table_infos_capitaux_propres.setHorizontalHeaderItem(1, __qtablewidgetitem87)
        self.table_infos_capitaux_propres.setObjectName(u"table_infos_capitaux_propres")
        self.table_infos_capitaux_propres.setFont(font7)
        self.table_infos_capitaux_propres.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	/*background-color: black;*/\n"
"	/*color: white;*/\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_capitaux_propres.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_infos_capitaux_propres.setAlternatingRowColors(True)
        self.table_infos_capitaux_propres.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.table_infos_capitaux_propres.setSortingEnabled(True)
        self.table_infos_capitaux_propres.horizontalHeader().setCascadingSectionResizes(True)
        self.table_infos_capitaux_propres.horizontalHeader().setProperty("showSortIndicator", True)
        self.table_infos_capitaux_propres.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_31.addWidget(self.table_infos_capitaux_propres, 1, 1, 1, 1)

        self.table_infos_actifs_circulants = QTableWidget(self.tab_rapports_financiers)
        if (self.table_infos_actifs_circulants.columnCount() < 2):
            self.table_infos_actifs_circulants.setColumnCount(2)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.table_infos_actifs_circulants.setHorizontalHeaderItem(0, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.table_infos_actifs_circulants.setHorizontalHeaderItem(1, __qtablewidgetitem89)
        self.table_infos_actifs_circulants.setObjectName(u"table_infos_actifs_circulants")
        self.table_infos_actifs_circulants.setFont(font7)
        self.table_infos_actifs_circulants.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	/*background-color: black;*/\n"
"	/*color: white;*/\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_actifs_circulants.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_infos_actifs_circulants.setAlternatingRowColors(True)
        self.table_infos_actifs_circulants.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.table_infos_actifs_circulants.setSortingEnabled(True)
        self.table_infos_actifs_circulants.horizontalHeader().setCascadingSectionResizes(True)
        self.table_infos_actifs_circulants.horizontalHeader().setProperty("showSortIndicator", True)
        self.table_infos_actifs_circulants.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_31.addWidget(self.table_infos_actifs_circulants, 3, 0, 1, 1)

        self.tab_widget.addTab(self.tab_rapports_financiers, "")

        self.gridLayout_20.addWidget(self.tab_widget, 0, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.main_screen_infos)


        self.gridLayout.addWidget(self.main_screen_widget, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1256, 24))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_only_widget.setVisible)
        self.btn_dashboard_2.toggled.connect(self.btn_dashboard_1.setChecked)
        self.btn_gestion_referentiels_2.toggled.connect(self.btn_gestion_referentiels_1.setChecked)
        self.btn_gestion_stock_2.toggled.connect(self.btn_gestion_stock_1.setChecked)
        self.btn_gestion_operations_2.toggled.connect(self.btn_gestion_operations_1.setChecked)
        self.btn_gestion_compta_2.toggled.connect(self.btn_gestion_compta_1.setChecked)
        self.btn_parametre_2.toggled.connect(self.btn_parametre_1.setChecked)
        self.btn_deconnexion_2.toggled.connect(self.btn_deconnexion_1.setChecked)

        self.tab_widget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText("")
        self.btn_dashboard_1.setText("")
        self.btn_gestion_referentiels_1.setText("")
        self.btn_gestion_stock_1.setText("")
        self.btn_gestion_operations_1.setText("")
        self.btn_gestion_compta_1.setText("")
        self.btn_parametre_1.setText("")
        self.btn_deconnexion_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"GeStock", None))
        self.btn_dashboard_2.setText(QCoreApplication.translate("MainWindow", u"  Tableau de bord", None))
        self.btn_gestion_referentiels_2.setText(QCoreApplication.translate("MainWindow", u"  R\u00e9f\u00e9rentiels", None))
        self.btn_ref_clients.setText(QCoreApplication.translate("MainWindow", u"Clients", None))
        self.btn_ref_entrepots.setText(QCoreApplication.translate("MainWindow", u"Entrep\u00f4ts", None))
        self.btn_ref_fournisseurs.setText(QCoreApplication.translate("MainWindow", u"Fournisseurs", None))
        self.btn_ref_matieres_premieres.setText(QCoreApplication.translate("MainWindow", u"Mati\u00e8res premi\u00e8res", None))
        self.btn_ref_produits.setText(QCoreApplication.translate("MainWindow", u"Produits", None))
        self.btn_gestion_stock_2.setText(QCoreApplication.translate("MainWindow", u"  Stock", None))
        self.btn_inventaire.setText(QCoreApplication.translate("MainWindow", u"Inventaire", None))
        self.btn_mvts_des_stocks.setText(QCoreApplication.translate("MainWindow", u"Mouvements des stocks", None))
        self.btn_gestion_operations_2.setText(QCoreApplication.translate("MainWindow", u"  Op\u00e9rations", None))
        self.btn_ventes_retours.setText(QCoreApplication.translate("MainWindow", u"Ventes et Retours", None))
        self.btn_paiements_factures.setText(QCoreApplication.translate("MainWindow", u"Paiements et Factures", None))
        self.btn_livraisons.setText(QCoreApplication.translate("MainWindow", u"Livraisons", None))
        self.btn_gestion_compta_2.setText(QCoreApplication.translate("MainWindow", u"  Comptabilit\u00e9", None))
        self.btn_depenses.setText(QCoreApplication.translate("MainWindow", u"D\u00e9penses", None))
        self.btn_flux_monetaires.setText(QCoreApplication.translate("MainWindow", u"Flux mon\u00e9taires", None))
        self.btn_rapports_financiers.setText(QCoreApplication.translate("MainWindow", u"Rapports financiers", None))
        self.btn_parametre_2.setText(QCoreApplication.translate("MainWindow", u"  Param\u00e8tres", None))
        self.btn_deconnexion_2.setText(QCoreApplication.translate("MainWindow", u" D\u00e9connexion", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bonjour Tartapion,", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Bienvenue!!!", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recherche...", None))
        self.label_7.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Tableau de bord", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_dashboard), QCoreApplication.translate("MainWindow", u"Tableau de bord", None))
        self.btn_ajout_matiere_premiere.setText(QCoreApplication.translate("MainWindow", u" Ajout mati\u00e8re premi\u00e8re", None))
        self.btn_export_matieres_premieres_excel.setText(QCoreApplication.translate("MainWindow", u" Export Excel", None))
        self.btn_export_matieres_premieres_pdf.setText(QCoreApplication.translate("MainWindow", u" Export PDF", None))
        self.cherche_matiere_premiere.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher mati\u00e8re premi\u00e8re...", None))
        ___qtablewidgetitem = self.table_infos_matieres_premieres.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.table_infos_matieres_premieres.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem2 = self.table_infos_matieres_premieres.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Unit\u00e9", None));
        ___qtablewidgetitem3 = self.table_infos_matieres_premieres.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Fournisseur", None));
        ___qtablewidgetitem4 = self.table_infos_matieres_premieres.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Prix de revient", None));
        ___qtablewidgetitem5 = self.table_infos_matieres_premieres.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Prix de vente", None));
        ___qtablewidgetitem6 = self.table_infos_matieres_premieres.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem7 = self.table_infos_matieres_premieres.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_matieres_premieres), QCoreApplication.translate("MainWindow", u"Mati\u00e8res premi\u00e8res", None))
        self.btn_ajout_produit.setText(QCoreApplication.translate("MainWindow", u" Ajout produit", None))
        self.btn_export_produit_excel.setText(QCoreApplication.translate("MainWindow", u" Export Excel", None))
        self.btn_export_produit_pdf.setText(QCoreApplication.translate("MainWindow", u" Export PDF", None))
        self.cherche_produit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher produit...", None))
        ___qtablewidgetitem8 = self.table_infos_produits.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem9 = self.table_infos_produits.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem10 = self.table_infos_produits.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Produit compos\u00e9", None));
        ___qtablewidgetitem11 = self.table_infos_produits.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Fournisseur", None));
        ___qtablewidgetitem12 = self.table_infos_produits.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Prix de revient", None));
        ___qtablewidgetitem13 = self.table_infos_produits.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Prix de vente", None));
        ___qtablewidgetitem14 = self.table_infos_produits.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem15 = self.table_infos_produits.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_produits), QCoreApplication.translate("MainWindow", u"Produits", None))
        self.btn_ajout_fournisseur.setText(QCoreApplication.translate("MainWindow", u" Ajout fournisseur", None))
        self.btn_export_fournisseurs_excel.setText(QCoreApplication.translate("MainWindow", u" Export Excel", None))
        self.btn_export_fournisseurs_pdf.setText(QCoreApplication.translate("MainWindow", u" Export PDF", None))
        self.cherche_fournisseur.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher fournisseur...", None))
        ___qtablewidgetitem16 = self.table_infos_fournisseurs.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem17 = self.table_infos_fournisseurs.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem18 = self.table_infos_fournisseurs.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Adresse", None));
        ___qtablewidgetitem19 = self.table_infos_fournisseurs.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Contact", None));
        ___qtablewidgetitem20 = self.table_infos_fournisseurs.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem21 = self.table_infos_fournisseurs.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_fournisseurs), QCoreApplication.translate("MainWindow", u"Fournisseurs", None))
        ___qtablewidgetitem22 = self.table_infos_entrepots.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem23 = self.table_infos_entrepots.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Code", None));
        ___qtablewidgetitem24 = self.table_infos_entrepots.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Adresse", None));
        ___qtablewidgetitem25 = self.table_infos_entrepots.horizontalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"T\u00e9l\u00e9phone", None));
        ___qtablewidgetitem26 = self.table_infos_entrepots.horizontalHeaderItem(4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"E-mail", None));
        ___qtablewidgetitem27 = self.table_infos_entrepots.horizontalHeaderItem(5)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.btn_ajout_entrepot.setText(QCoreApplication.translate("MainWindow", u"Ajouter entrep\u00f4t", None))
        self.btn_export_entrepots_excel.setText(QCoreApplication.translate("MainWindow", u"Export Excel", None))
        self.btn_export_entrepots_pdf.setText(QCoreApplication.translate("MainWindow", u"Export PDF", None))
        self.cherche_entrepot.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher entrep\u00f4t...", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_entrepots), QCoreApplication.translate("MainWindow", u"Entrep\u00f4ts", None))
        self.btn_ajout_client.setText(QCoreApplication.translate("MainWindow", u"Ajouter client", None))
        self.btn_export_clients_excel.setText(QCoreApplication.translate("MainWindow", u"Export Excel", None))
        self.btn_export_clients_pdf.setText(QCoreApplication.translate("MainWindow", u"Export PDF", None))
        self.cherche_client.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher client...", None))
        ___qtablewidgetitem28 = self.table_infos_clients.horizontalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"ID Client", None));
        ___qtablewidgetitem29 = self.table_infos_clients.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem30 = self.table_infos_clients.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Entreprise", None));
        ___qtablewidgetitem31 = self.table_infos_clients.horizontalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Adresse", None));
        ___qtablewidgetitem32 = self.table_infos_clients.horizontalHeaderItem(4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"T\u00e9l\u00e9phone", None));
        ___qtablewidgetitem33 = self.table_infos_clients.horizontalHeaderItem(5)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem34 = self.table_infos_clients.horizontalHeaderItem(6)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_clients), QCoreApplication.translate("MainWindow", u"Clients", None))
        self.btn_debut_inventaire.setText(QCoreApplication.translate("MainWindow", u" D\u00e9buter", None))
        self.btn_export_inventaire_excel.setText(QCoreApplication.translate("MainWindow", u" Export Excel", None))
        self.btn_export_inventaire_pdf.setText(QCoreApplication.translate("MainWindow", u" Export PDF", None))
        self.cherche_inventaire.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher inventaire...", None))
        ___qtablewidgetitem35 = self.table_infos_inventaire.horizontalHeaderItem(0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"ID Inventaire", None));
        ___qtablewidgetitem36 = self.table_infos_inventaire.horizontalHeaderItem(1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Date inventaire", None));
        ___qtablewidgetitem37 = self.table_infos_inventaire.horizontalHeaderItem(2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Code produit", None));
        ___qtablewidgetitem38 = self.table_infos_inventaire.horizontalHeaderItem(3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem39 = self.table_infos_inventaire.horizontalHeaderItem(4)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Quantit\u00e9 th\u00e9orique", None));
        ___qtablewidgetitem40 = self.table_infos_inventaire.horizontalHeaderItem(5)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Quantit\u00e9 r\u00e9elle", None));
        ___qtablewidgetitem41 = self.table_infos_inventaire.horizontalHeaderItem(6)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Ecart", None));
        ___qtablewidgetitem42 = self.table_infos_inventaire.horizontalHeaderItem(7)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Unit\u00e9", None));
        ___qtablewidgetitem43 = self.table_infos_inventaire.horizontalHeaderItem(8)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Agent", None));
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_inventaires), QCoreApplication.translate("MainWindow", u"Inventaire", None))
        self.btn_ajout_vente_retour.setText(QCoreApplication.translate("MainWindow", u" Vente / Retour", None))
        self.btn_export_ventes_retours_excel.setText(QCoreApplication.translate("MainWindow", u" Export Excel", None))
        self.btn_export_vente_retour_pdf.setText(QCoreApplication.translate("MainWindow", u" Export PDF", None))
        self.cherche_vente_retour.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher vente/retour...", None))
        ___qtablewidgetitem44 = self.table_infos_ventes_retours.horizontalHeaderItem(0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"ID Vente", None));
        ___qtablewidgetitem45 = self.table_infos_ventes_retours.horizontalHeaderItem(1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Date de vente", None));
        ___qtablewidgetitem46 = self.table_infos_ventes_retours.horizontalHeaderItem(2)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Client", None));
        ___qtablewidgetitem47 = self.table_infos_ventes_retours.horizontalHeaderItem(3)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Nombre d'articles", None));
        ___qtablewidgetitem48 = self.table_infos_ventes_retours.horizontalHeaderItem(4)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Prix total", None));
        ___qtablewidgetitem49 = self.table_infos_ventes_retours.horizontalHeaderItem(5)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Montant r\u00e9gl\u00e9", None));
        ___qtablewidgetitem50 = self.table_infos_ventes_retours.horizontalHeaderItem(6)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Montant restant", None));
        ___qtablewidgetitem51 = self.table_infos_ventes_retours.horizontalHeaderItem(7)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Utilisateur", None));
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_ventes_retours), QCoreApplication.translate("MainWindow", u"Ventes et Retours", None))
        self.btn_export_mvts_stocks_excel.setText(QCoreApplication.translate("MainWindow", u" Export Excel", None))
        self.btn_export_mvts_stocks_pdf.setText(QCoreApplication.translate("MainWindow", u" Export PDF", None))
        self.cherche_mvt_stock.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher mouvement...", None))
        ___qtablewidgetitem52 = self.table_infos_mvts_stocks.horizontalHeaderItem(0)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"ID mouvement", None));
        ___qtablewidgetitem53 = self.table_infos_mvts_stocks.horizontalHeaderItem(1)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Code produit", None));
        ___qtablewidgetitem54 = self.table_infos_mvts_stocks.horizontalHeaderItem(2)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem55 = self.table_infos_mvts_stocks.horizontalHeaderItem(3)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem56 = self.table_infos_mvts_stocks.horizontalHeaderItem(4)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Quantit\u00e9 disponible", None));
        ___qtablewidgetitem57 = self.table_infos_mvts_stocks.horizontalHeaderItem(5)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Unit\u00e9", None));
        ___qtablewidgetitem58 = self.table_infos_mvts_stocks.horizontalHeaderItem(6)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Utilisateur", None));
        ___qtablewidgetitem59 = self.table_infos_mvts_stocks.horizontalHeaderItem(7)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_mvts_stocks), QCoreApplication.translate("MainWindow", u"Mvts Stocks", None))
        self.btn_ajout_livraison.setText(QCoreApplication.translate("MainWindow", u" Ajout livraison", None))
        self.btn_export_livraisons_excel.setText(QCoreApplication.translate("MainWindow", u" Export Excel", None))
        self.btn_export_livraisons_pdf.setText(QCoreApplication.translate("MainWindow", u" Export PDF", None))
        self.cherche_livraison.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher livraison...", None))
        ___qtablewidgetitem60 = self.table_infos_livraison.horizontalHeaderItem(0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Date de livraison", None));
        ___qtablewidgetitem61 = self.table_infos_livraison.horizontalHeaderItem(1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Date de vente", None));
        ___qtablewidgetitem62 = self.table_infos_livraison.horizontalHeaderItem(2)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Client", None));
        ___qtablewidgetitem63 = self.table_infos_livraison.horizontalHeaderItem(3)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"Nombre d'articles", None));
        ___qtablewidgetitem64 = self.table_infos_livraison.horizontalHeaderItem(4)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"Prix total", None));
        ___qtablewidgetitem65 = self.table_infos_livraison.horizontalHeaderItem(5)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"Montant r\u00e9gl\u00e9", None));
        ___qtablewidgetitem66 = self.table_infos_livraison.horizontalHeaderItem(6)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"Montant restant", None));
        ___qtablewidgetitem67 = self.table_infos_livraison.horizontalHeaderItem(7)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"Livreur", None));
        ___qtablewidgetitem68 = self.table_infos_livraison.horizontalHeaderItem(8)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"Statut", None));
        ___qtablewidgetitem69 = self.table_infos_livraison.horizontalHeaderItem(9)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Utilisateur", None));
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_livraisons), QCoreApplication.translate("MainWindow", u"Livraisons", None))
        self.btn_ajout_flux.setText(QCoreApplication.translate("MainWindow", u"Ajouter flux", None))
        self.btn_export_flux_excel.setText(QCoreApplication.translate("MainWindow", u"Export Excel", None))
        self.btn_export_flux_pdf.setText(QCoreApplication.translate("MainWindow", u"Export PDF", None))
        self.cherche_flux.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher flux...", None))
        ___qtablewidgetitem70 = self.table_infos_flux_monetaires_global.horizontalHeaderItem(0)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"ID mouvement", None));
        ___qtablewidgetitem71 = self.table_infos_flux_monetaires_global.horizontalHeaderItem(1)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem72 = self.table_infos_flux_monetaires_global.horizontalHeaderItem(2)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"Cat\u00e9gorie", None));
        ___qtablewidgetitem73 = self.table_infos_flux_monetaires_global.horizontalHeaderItem(3)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem74 = self.table_infos_flux_monetaires_global.horizontalHeaderItem(4)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Montant", None));
        ___qtablewidgetitem75 = self.table_infos_flux_monetaires_global.horizontalHeaderItem(5)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem76 = self.table_infos_flux_monetaires_global.horizontalHeaderItem(6)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"Utilisateur", None));
        ___qtablewidgetitem77 = self.table_infos_flux_monetaires_cat.horizontalHeaderItem(0)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"Cat\u00e9gorie", None));
        ___qtablewidgetitem78 = self.table_infos_flux_monetaires_cat.horizontalHeaderItem(1)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem79 = self.table_infos_flux_monetaires_cat.horizontalHeaderItem(2)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"Montant", None));
        ___qtablewidgetitem80 = self.table_infos_flux_monetaires_type.horizontalHeaderItem(0)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem81 = self.table_infos_flux_monetaires_type.horizontalHeaderItem(1)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"Montant", None));
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_flux_monetaires), QCoreApplication.translate("MainWindow", u"Flux Mon\u00e9taires", None))
        ___qtablewidgetitem82 = self.table_infos_actifs_immo.horizontalHeaderItem(0)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"Cat\u00e9gorie", None));
        ___qtablewidgetitem83 = self.table_infos_actifs_immo.horizontalHeaderItem(1)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"Montant", None));
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Actifs Circulant", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Actifs Immobilis\u00e9s", None))
        ___qtablewidgetitem84 = self.table_infos_dettes.horizontalHeaderItem(0)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"Cat\u00e9gorie", None));
        ___qtablewidgetitem85 = self.table_infos_dettes.horizontalHeaderItem(1)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"Montant", None));
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Capitaux propres", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Dettes", None))
        ___qtablewidgetitem86 = self.table_infos_capitaux_propres.horizontalHeaderItem(0)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"Cat\u00e9gorie", None));
        ___qtablewidgetitem87 = self.table_infos_capitaux_propres.horizontalHeaderItem(1)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"Montant", None));
        ___qtablewidgetitem88 = self.table_infos_actifs_circulants.horizontalHeaderItem(0)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"Cat\u00e9gorie", None));
        ___qtablewidgetitem89 = self.table_infos_actifs_circulants.horizontalHeaderItem(1)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"Montant", None));
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_rapports_financiers), QCoreApplication.translate("MainWindow", u"Rapports Financiers", None))
    # retranslateUi

