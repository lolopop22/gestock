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
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
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
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.icon_text_widget = QWidget(self.widget)
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
        self.verticalLayout_17.setSpacing(6)
        self.verticalLayout_17.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.verticalLayout_17.setContentsMargins(5, 0, -1, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 10, 0, 10)
        self.label_9 = QLabel(self.icon_text_widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(40, 40))
        self.label_9.setPixmap(QPixmap(u":/icones/logo.png"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_9)

        self.label_10 = QLabel(self.icon_text_widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(150, 50))
        font = QFont()
        font.setFamilies([u"Courier"])
        font.setPointSize(20)
        font.setBold(True)
        self.label_10.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_10)


        self.verticalLayout_17.addLayout(self.horizontalLayout_7)

        self.groupBox_2 = QGroupBox(self.icon_text_widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_18.setSpacing(6)
        self.verticalLayout_18.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, 1, -1, -1)
        self.btn_dashboard_4 = QPushButton(self.groupBox_2)
        self.btn_dashboard_4.setObjectName(u"btn_dashboard_4")
        self.btn_dashboard_4.setMinimumSize(QSize(0, 0))
        self.btn_dashboard_4.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.btn_dashboard_4.setFont(font1)
        self.btn_dashboard_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_dashboard_4.setStyleSheet(u"QPushButton{\n"
"	padding-left:-3px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	border-radius:3px;\n"
"	background-color: white\n"
"}")
        icon = QIcon()
        icon.addFile(u"icones/small_dashboard1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_dashboard_4.setIcon(icon)
        self.btn_dashboard_4.setIconSize(QSize(95, 25))
        self.btn_dashboard_4.setCheckable(True)
        self.btn_dashboard_4.setChecked(False)
        self.btn_dashboard_4.setAutoExclusive(False)

        self.verticalLayout_18.addWidget(self.btn_dashboard_4)

        self.btn_gestion_referentiels_4 = QPushButton(self.groupBox_2)
        self.btn_gestion_referentiels_4.setObjectName(u"btn_gestion_referentiels_4")
        self.btn_gestion_referentiels_4.setMaximumSize(QSize(150, 16777215))
        self.btn_gestion_referentiels_4.setFont(font1)
        self.btn_gestion_referentiels_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gestion_referentiels_4.setStyleSheet(u"QPushButton{\n"
"	padding-left:-3px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"icones/small_referentiel1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_gestion_referentiels_4.setIcon(icon1)
        self.btn_gestion_referentiels_4.setIconSize(QSize(95, 30))
        self.btn_gestion_referentiels_4.setCheckable(True)
        self.btn_gestion_referentiels_4.setChecked(False)
        self.btn_gestion_referentiels_4.setAutoExclusive(True)

        self.verticalLayout_18.addWidget(self.btn_gestion_referentiels_4)

        self.gestion_referentiels_3 = QFrame(self.groupBox_2)
        self.gestion_referentiels_3.setObjectName(u"gestion_referentiels_3")
        self.gestion_referentiels_3.setMaximumSize(QSize(170, 16777215))
        self.gestion_referentiels_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.gestion_referentiels_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.gestion_referentiels_3)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.dropdown_gestion_referentiels_3 = QFrame(self.gestion_referentiels_3)
        self.dropdown_gestion_referentiels_3.setObjectName(u"dropdown_gestion_referentiels_3")
        self.dropdown_gestion_referentiels_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropdown_gestion_referentiels_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_16 = QGridLayout(self.dropdown_gestion_referentiels_3)
        self.gridLayout_16.setSpacing(6)
        self.gridLayout_16.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.btn_ref_matires_premieres_3 = QPushButton(self.dropdown_gestion_referentiels_3)
        self.btn_ref_matires_premieres_3.setObjectName(u"btn_ref_matires_premieres_3")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.btn_ref_matires_premieres_3.setFont(font2)

        self.gridLayout_16.addWidget(self.btn_ref_matires_premieres_3, 0, 0, 1, 1)

        self.btn_ref_produits_3 = QPushButton(self.dropdown_gestion_referentiels_3)
        self.btn_ref_produits_3.setObjectName(u"btn_ref_produits_3")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setKerning(True)
        self.btn_ref_produits_3.setFont(font3)

        self.gridLayout_16.addWidget(self.btn_ref_produits_3, 1, 0, 1, 1)

        self.btn_ref_fournisseurs_3 = QPushButton(self.dropdown_gestion_referentiels_3)
        self.btn_ref_fournisseurs_3.setObjectName(u"btn_ref_fournisseurs_3")
        self.btn_ref_fournisseurs_3.setFont(font3)

        self.gridLayout_16.addWidget(self.btn_ref_fournisseurs_3, 2, 0, 1, 1)

        self.btn_ref_clients_3 = QPushButton(self.dropdown_gestion_referentiels_3)
        self.btn_ref_clients_3.setObjectName(u"btn_ref_clients_3")
        self.btn_ref_clients_3.setFont(font3)

        self.gridLayout_16.addWidget(self.btn_ref_clients_3, 3, 0, 1, 1)

        self.btn_ref_entrepots_3 = QPushButton(self.dropdown_gestion_referentiels_3)
        self.btn_ref_entrepots_3.setObjectName(u"btn_ref_entrepots_3")
        self.btn_ref_entrepots_3.setFont(font3)

        self.gridLayout_16.addWidget(self.btn_ref_entrepots_3, 4, 0, 1, 1)


        self.verticalLayout_27.addWidget(self.dropdown_gestion_referentiels_3)


        self.verticalLayout_18.addWidget(self.gestion_referentiels_3)

        self.gestion_produits_3 = QFrame(self.groupBox_2)
        self.gestion_produits_3.setObjectName(u"gestion_produits_3")
        self.gestion_produits_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.gestion_produits_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.gestion_produits_3)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.btn_gestion_produits_4 = QPushButton(self.gestion_produits_3)
        self.btn_gestion_produits_4.setObjectName(u"btn_gestion_produits_4")
        self.btn_gestion_produits_4.setMaximumSize(QSize(110, 16777215))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setStyleStrategy(QFont.NoAntialias)
        font4.setHintingPreference(QFont.PreferNoHinting)
        self.btn_gestion_produits_4.setFont(font4)
        self.btn_gestion_produits_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gestion_produits_4.setStyleSheet(u"QPushButton{\n"
"	padding-left:-3px;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"icones/small_stock1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_gestion_produits_4.setIcon(icon2)
        self.btn_gestion_produits_4.setIconSize(QSize(95, 30))
        self.btn_gestion_produits_4.setCheckable(True)
        self.btn_gestion_produits_4.setChecked(False)
        self.btn_gestion_produits_4.setAutoExclusive(False)

        self.verticalLayout_29.addWidget(self.btn_gestion_produits_4)

        self.dropdown_gestion_produits_3 = QFrame(self.gestion_produits_3)
        self.dropdown_gestion_produits_3.setObjectName(u"dropdown_gestion_produits_3")
        self.dropdown_gestion_produits_3.setMaximumSize(QSize(200, 16777215))
        self.dropdown_gestion_produits_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropdown_gestion_produits_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_15 = QGridLayout(self.dropdown_gestion_produits_3)
        self.gridLayout_15.setSpacing(6)
        self.gridLayout_15.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.btn_inventaire_3 = QPushButton(self.dropdown_gestion_produits_3)
        self.btn_inventaire_3.setObjectName(u"btn_inventaire_3")
        self.btn_inventaire_3.setFont(font3)

        self.gridLayout_15.addWidget(self.btn_inventaire_3, 0, 0, 1, 1)

        self.btn_mvts_des_stocks_3 = QPushButton(self.dropdown_gestion_produits_3)
        self.btn_mvts_des_stocks_3.setObjectName(u"btn_mvts_des_stocks_3")
        self.btn_mvts_des_stocks_3.setFont(font3)

        self.gridLayout_15.addWidget(self.btn_mvts_des_stocks_3, 1, 0, 1, 1)


        self.verticalLayout_29.addWidget(self.dropdown_gestion_produits_3)


        self.verticalLayout_18.addWidget(self.gestion_produits_3)

        self.gestion_operations_3 = QFrame(self.groupBox_2)
        self.gestion_operations_3.setObjectName(u"gestion_operations_3")
        self.gestion_operations_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.gestion_operations_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.gestion_operations_3)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.btn_gestion_operations_4 = QPushButton(self.gestion_operations_3)
        self.btn_gestion_operations_4.setObjectName(u"btn_gestion_operations_4")
        self.btn_gestion_operations_4.setMaximumSize(QSize(150, 16777215))
        self.btn_gestion_operations_4.setFont(font1)
        self.btn_gestion_operations_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gestion_operations_4.setStyleSheet(u"QPushButton{\n"
"	padding-left:-3px;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"icones/small_operation1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_gestion_operations_4.setIcon(icon3)
        self.btn_gestion_operations_4.setIconSize(QSize(95, 30))
        self.btn_gestion_operations_4.setCheckable(True)
        self.btn_gestion_operations_4.setChecked(False)
        self.btn_gestion_operations_4.setAutoExclusive(True)

        self.verticalLayout_31.addWidget(self.btn_gestion_operations_4)

        self.dropdown_gestion_operations_3 = QFrame(self.gestion_operations_3)
        self.dropdown_gestion_operations_3.setObjectName(u"dropdown_gestion_operations_3")
        self.dropdown_gestion_operations_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropdown_gestion_operations_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.dropdown_gestion_operations_3)
        self.verticalLayout_32.setSpacing(6)
        self.verticalLayout_32.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.btn_ventes_retours_3 = QPushButton(self.dropdown_gestion_operations_3)
        self.btn_ventes_retours_3.setObjectName(u"btn_ventes_retours_3")
        self.btn_ventes_retours_3.setFont(font3)

        self.verticalLayout_32.addWidget(self.btn_ventes_retours_3)

        self.btn_livraisons_3 = QPushButton(self.dropdown_gestion_operations_3)
        self.btn_livraisons_3.setObjectName(u"btn_livraisons_3")
        self.btn_livraisons_3.setFont(font3)

        self.verticalLayout_32.addWidget(self.btn_livraisons_3)


        self.verticalLayout_31.addWidget(self.dropdown_gestion_operations_3)


        self.verticalLayout_18.addWidget(self.gestion_operations_3)

        self.gestion_compta_3 = QFrame(self.groupBox_2)
        self.gestion_compta_3.setObjectName(u"gestion_compta_3")
        self.gestion_compta_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.gestion_compta_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.gestion_compta_3)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.btn_gestion_compta_4 = QPushButton(self.gestion_compta_3)
        self.btn_gestion_compta_4.setObjectName(u"btn_gestion_compta_4")
        self.btn_gestion_compta_4.setMaximumSize(QSize(170, 16777215))
        self.btn_gestion_compta_4.setFont(font1)
        self.btn_gestion_compta_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gestion_compta_4.setStyleSheet(u"QPushButton{\n"
"	padding-left:-3px;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"icones/small_compta1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_gestion_compta_4.setIcon(icon4)
        self.btn_gestion_compta_4.setIconSize(QSize(95, 30))
        self.btn_gestion_compta_4.setCheckable(True)
        self.btn_gestion_compta_4.setChecked(False)
        self.btn_gestion_compta_4.setAutoExclusive(True)

        self.verticalLayout_33.addWidget(self.btn_gestion_compta_4)

        self.dropdown_gestion_compta_3 = QFrame(self.gestion_compta_3)
        self.dropdown_gestion_compta_3.setObjectName(u"dropdown_gestion_compta_3")
        self.dropdown_gestion_compta_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropdown_gestion_compta_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.dropdown_gestion_compta_3)
        self.verticalLayout_34.setSpacing(6)
        self.verticalLayout_34.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.btn_flux_monetaires_3 = QPushButton(self.dropdown_gestion_compta_3)
        self.btn_flux_monetaires_3.setObjectName(u"btn_flux_monetaires_3")
        self.btn_flux_monetaires_3.setFont(font3)

        self.verticalLayout_34.addWidget(self.btn_flux_monetaires_3)

        self.btn_rapports_financiers_3 = QPushButton(self.dropdown_gestion_compta_3)
        self.btn_rapports_financiers_3.setObjectName(u"btn_rapports_financiers_3")
        self.btn_rapports_financiers_3.setFont(font3)

        self.verticalLayout_34.addWidget(self.btn_rapports_financiers_3)


        self.verticalLayout_33.addWidget(self.dropdown_gestion_compta_3)


        self.verticalLayout_18.addWidget(self.gestion_compta_3)


        self.verticalLayout_17.addWidget(self.groupBox_2)

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
        icon5 = QIcon()
        icon5.addFile(u":/icones/parametre1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/icones/parametre2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_parametre_2.setIcon(icon5)
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
        icon6 = QIcon()
        icon6.addFile(u":/icones/deconnexion1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/icones/deconnexion2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_deconnexion_2.setIcon(icon6)
        self.btn_deconnexion_2.setIconSize(QSize(170, 40))
        self.btn_deconnexion_2.setCheckable(True)
        self.btn_deconnexion_2.setChecked(False)
        self.btn_deconnexion_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_deconnexion_2)


        self.verticalLayout_17.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.icon_text_widget, 1, 1, 1, 1)

        self.icon_only_widget = QWidget(self.widget)
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
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setContentsMargins(9, 9, 9, 9)
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
        icon7 = QIcon()
        icon7.addFile(u":/icones/small_dashboard1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/icones/small_dashboard2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_dashboard_1.setIcon(icon7)
        self.btn_dashboard_1.setIconSize(QSize(27, 27))
        self.btn_dashboard_1.setCheckable(True)
        self.btn_dashboard_1.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.btn_dashboard_1)

        self.btn_gestion_referentiels_1 = QPushButton(self.icon_only_widget)
        self.btn_gestion_referentiels_1.setObjectName(u"btn_gestion_referentiels_1")
        icon8 = QIcon()
        icon8.addFile(u":/icones/small_referentiel1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u":/icones/small_referentiel2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_gestion_referentiels_1.setIcon(icon8)
        self.btn_gestion_referentiels_1.setIconSize(QSize(27, 27))
        self.btn_gestion_referentiels_1.setCheckable(True)
        self.btn_gestion_referentiels_1.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.btn_gestion_referentiels_1)

        self.btn_gestion_produits_1 = QPushButton(self.icon_only_widget)
        self.btn_gestion_produits_1.setObjectName(u"btn_gestion_produits_1")
        icon9 = QIcon()
        icon9.addFile(u":/icones/small_stock1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/icones/small_stock2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_gestion_produits_1.setIcon(icon9)
        self.btn_gestion_produits_1.setIconSize(QSize(27, 27))
        self.btn_gestion_produits_1.setCheckable(True)
        self.btn_gestion_produits_1.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.btn_gestion_produits_1)

        self.btn_gestion_operations_1 = QPushButton(self.icon_only_widget)
        self.btn_gestion_operations_1.setObjectName(u"btn_gestion_operations_1")
        icon10 = QIcon()
        icon10.addFile(u":/icones/small_operation1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u":/icones/small_operation2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_gestion_operations_1.setIcon(icon10)
        self.btn_gestion_operations_1.setIconSize(QSize(27, 27))
        self.btn_gestion_operations_1.setCheckable(True)
        self.btn_gestion_operations_1.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.btn_gestion_operations_1)

        self.btn_gestion_compta_1 = QPushButton(self.icon_only_widget)
        self.btn_gestion_compta_1.setObjectName(u"btn_gestion_compta_1")
        icon11 = QIcon()
        icon11.addFile(u":/icones/small_compta1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon11.addFile(u":/icones/small_compta2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_gestion_compta_1.setIcon(icon11)
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
        icon12 = QIcon()
        icon12.addFile(u":/icones/small_parametre1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon12.addFile(u":/icones/small_parametre2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_parametre_1.setIcon(icon12)
        self.btn_parametre_1.setIconSize(QSize(27, 27))
        self.btn_parametre_1.setCheckable(True)
        self.btn_parametre_1.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.btn_parametre_1)

        self.btn_deconnexion_1 = QPushButton(self.icon_only_widget)
        self.btn_deconnexion_1.setObjectName(u"btn_deconnexion_1")
        self.btn_deconnexion_1.setStyleSheet(u"QPushButton{\n"
"	padding-left:10px;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icones/small_deconnexion1.png", QSize(), QIcon.Normal, QIcon.Off)
        icon13.addFile(u":/icones/small_deconnexion2.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_deconnexion_1.setIcon(icon13)
        self.btn_deconnexion_1.setIconSize(QSize(27, 27))
        self.btn_deconnexion_1.setCheckable(True)
        self.btn_deconnexion_1.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.btn_deconnexion_1)


        self.verticalLayout_14.addLayout(self.verticalLayout_12)


        self.gridLayout.addWidget(self.icon_only_widget, 1, 0, 1, 1)

        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.gridLayout_2 = QGridLayout(self.widget1)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.header_widget = QWidget(self.widget1)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMinimumSize(QSize(895, 66))
        self.header_widget.setMaximumSize(QSize(16777215, 66))
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 5, -1, 15)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")

        self.horizontalLayout_4.addLayout(self.verticalLayout_15)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.pushButton = QPushButton(self.header_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border:none;")
        icon14 = QIcon()
        icon14.addFile(u":/icones/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon14)
        self.pushButton.setIconSize(QSize(29, 35))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.horizontalSpacer_3 = QSpacerItem(358, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.widget2 = QWidget(self.header_widget)
        self.widget2.setObjectName(u"widget2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 10, -1)
        self.lineEdit = QLineEdit(self.widget2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 31))
        self.lineEdit.setMaximumSize(QSize(16777215, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_6 = QLabel(self.widget2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(40, 40))
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setPixmap(QPixmap(u":/icones/profile.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.widget2)


        self.gridLayout_2.addWidget(self.header_widget, 0, 0, 1, 1)

        self.main_screen_widget = QWidget(self.widget1)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(895, 672))
        self.main_screen_widget.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.main_screen_widget)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.main_screen_widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(895, 672))
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setIconSize(QSize(30, 30))
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tab_dashboard = QWidget()
        self.tab_dashboard.setObjectName(u"tab_dashboard")
        self.label_20 = QLabel(self.tab_dashboard)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(290, 90, 271, 71))
        font5 = QFont()
        font5.setPointSize(25)
        self.label_20.setFont(font5)
        self.tabWidget.addTab(self.tab_dashboard, "")
        self.tab_produits = QWidget()
        self.tab_produits.setObjectName(u"tab_produits")
        self.gridLayout_12 = QGridLayout(self.tab_produits)
        self.gridLayout_12.setSpacing(6)
        self.gridLayout_12.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.cherche_produit = QLineEdit(self.tab_produits)
        self.cherche_produit.setObjectName(u"cherche_produit")
        self.cherche_produit.setMinimumSize(QSize(0, 32))
        self.cherche_produit.setMaximumSize(QSize(407, 31))
        self.cherche_produit.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")

        self.gridLayout_12.addWidget(self.cherche_produit, 1, 1, 1, 1)

        self.table_infos_client_4 = QTableWidget(self.tab_produits)
        if (self.table_infos_client_4.columnCount() < 7):
            self.table_infos_client_4.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_infos_client_4.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_infos_client_4.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_infos_client_4.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_infos_client_4.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_infos_client_4.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_infos_client_4.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_infos_client_4.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table_infos_client_4.setObjectName(u"table_infos_client_4")
        self.table_infos_client_4.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_client_4.setAlternatingRowColors(True)
        self.table_infos_client_4.horizontalHeader().setCascadingSectionResizes(True)
        self.table_infos_client_4.horizontalHeader().setDefaultSectionSize(150)
        self.table_infos_client_4.horizontalHeader().setProperty("showSortIndicator", True)
        self.table_infos_client_4.horizontalHeader().setStretchLastSection(True)
        self.table_infos_client_4.verticalHeader().setVisible(False)

        self.gridLayout_12.addWidget(self.table_infos_client_4, 2, 0, 1, 2)

        self.widget_12 = QWidget(self.tab_produits)
        self.widget_12.setObjectName(u"widget_12")
        self.btn_ajout_produit = QPushButton(self.widget_12)
        self.btn_ajout_produit.setObjectName(u"btn_ajout_produit")
        self.btn_ajout_produit.setGeometry(QRect(0, 0, 122, 32))
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
        icon15 = QIcon()
        icon15.addFile(u":/icones/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ajout_produit.setIcon(icon15)
        self.btn_export_excel_produit = QPushButton(self.widget_12)
        self.btn_export_excel_produit.setObjectName(u"btn_export_excel_produit")
        self.btn_export_excel_produit.setGeometry(QRect(140, 0, 122, 32))
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
        icon16 = QIcon()
        icon16.addFile(u":/icones/excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_export_excel_produit.setIcon(icon16)
        self.btn_export_pdf_produit = QPushButton(self.widget_12)
        self.btn_export_pdf_produit.setObjectName(u"btn_export_pdf_produit")
        self.btn_export_pdf_produit.setGeometry(QRect(280, 0, 122, 32))
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

        self.gridLayout_12.addWidget(self.widget_12, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_produits, "")
        self.tab_fournisseurs = QWidget()
        self.tab_fournisseurs.setObjectName(u"tab_fournisseurs")
        self.gridLayout_11 = QGridLayout(self.tab_fournisseurs)
        self.gridLayout_11.setSpacing(6)
        self.gridLayout_11.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.cherche_fournisseur = QLineEdit(self.tab_fournisseurs)
        self.cherche_fournisseur.setObjectName(u"cherche_fournisseur")
        self.cherche_fournisseur.setMinimumSize(QSize(0, 32))
        self.cherche_fournisseur.setMaximumSize(QSize(407, 31))
        self.cherche_fournisseur.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")

        self.gridLayout_11.addWidget(self.cherche_fournisseur, 1, 1, 1, 1)

        self.table_infos_fournisseur = QTableWidget(self.tab_fournisseurs)
        if (self.table_infos_fournisseur.columnCount() < 8):
            self.table_infos_fournisseur.setColumnCount(8)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_infos_fournisseur.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_infos_fournisseur.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_infos_fournisseur.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_infos_fournisseur.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_infos_fournisseur.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_infos_fournisseur.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_infos_fournisseur.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_infos_fournisseur.setHorizontalHeaderItem(7, __qtablewidgetitem14)
        self.table_infos_fournisseur.setObjectName(u"table_infos_fournisseur")
        self.table_infos_fournisseur.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_fournisseur.setAlternatingRowColors(True)
        self.table_infos_fournisseur.horizontalHeader().setDefaultSectionSize(150)
        self.table_infos_fournisseur.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_11.addWidget(self.table_infos_fournisseur, 2, 0, 1, 2)

        self.widget_11 = QWidget(self.tab_fournisseurs)
        self.widget_11.setObjectName(u"widget_11")
        self.btn_ajout_fournisseur = QPushButton(self.widget_11)
        self.btn_ajout_fournisseur.setObjectName(u"btn_ajout_fournisseur")
        self.btn_ajout_fournisseur.setGeometry(QRect(0, 0, 122, 32))
        self.btn_ajout_fournisseur.setMinimumSize(QSize(0, 32))
        self.btn_ajout_fournisseur.setMaximumSize(QSize(122, 32))
        self.btn_ajout_fournisseur.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_ajout_fournisseur.setIcon(icon15)
        self.export_excel_btn_fournisseur = QPushButton(self.widget_11)
        self.export_excel_btn_fournisseur.setObjectName(u"export_excel_btn_fournisseur")
        self.export_excel_btn_fournisseur.setGeometry(QRect(140, 0, 122, 32))
        self.export_excel_btn_fournisseur.setMinimumSize(QSize(0, 32))
        self.export_excel_btn_fournisseur.setMaximumSize(QSize(122, 32))
        self.export_excel_btn_fournisseur.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.export_excel_btn_fournisseur.setIcon(icon16)
        self.export_pdf_btn_fournisseur = QPushButton(self.widget_11)
        self.export_pdf_btn_fournisseur.setObjectName(u"export_pdf_btn_fournisseur")
        self.export_pdf_btn_fournisseur.setGeometry(QRect(280, 0, 122, 32))
        self.export_pdf_btn_fournisseur.setMinimumSize(QSize(0, 32))
        self.export_pdf_btn_fournisseur.setMaximumSize(QSize(122, 32))
        self.export_pdf_btn_fournisseur.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 58, 21);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.export_pdf_btn_fournisseur.setIcon(icon17)

        self.gridLayout_11.addWidget(self.widget_11, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_fournisseurs, "")
        self.tab_entrepots = QWidget()
        self.tab_entrepots.setObjectName(u"tab_entrepots")
        self.gridLayout_10 = QGridLayout(self.tab_entrepots)
        self.gridLayout_10.setSpacing(6)
        self.gridLayout_10.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.cherche_entrepot = QLineEdit(self.tab_entrepots)
        self.cherche_entrepot.setObjectName(u"cherche_entrepot")
        self.cherche_entrepot.setMinimumSize(QSize(0, 32))
        self.cherche_entrepot.setMaximumSize(QSize(407, 31))
        self.cherche_entrepot.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")

        self.gridLayout_10.addWidget(self.cherche_entrepot, 1, 1, 1, 1)

        self.table_infos_entrepot = QTableWidget(self.tab_entrepots)
        if (self.table_infos_entrepot.columnCount() < 6):
            self.table_infos_entrepot.setColumnCount(6)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_infos_entrepot.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_infos_entrepot.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_infos_entrepot.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_infos_entrepot.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_infos_entrepot.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_infos_entrepot.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        self.table_infos_entrepot.setObjectName(u"table_infos_entrepot")
        self.table_infos_entrepot.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_entrepot.setAlternatingRowColors(True)
        self.table_infos_entrepot.horizontalHeader().setDefaultSectionSize(150)
        self.table_infos_entrepot.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_10.addWidget(self.table_infos_entrepot, 2, 0, 1, 2)

        self.widget_10 = QWidget(self.tab_entrepots)
        self.widget_10.setObjectName(u"widget_10")
        self.btn_ajout_entrepot = QPushButton(self.widget_10)
        self.btn_ajout_entrepot.setObjectName(u"btn_ajout_entrepot")
        self.btn_ajout_entrepot.setGeometry(QRect(0, 0, 122, 32))
        self.btn_ajout_entrepot.setMinimumSize(QSize(0, 32))
        self.btn_ajout_entrepot.setMaximumSize(QSize(122, 32))
        self.btn_ajout_entrepot.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_ajout_entrepot.setIcon(icon15)
        self.export_excel_entrepot = QPushButton(self.widget_10)
        self.export_excel_entrepot.setObjectName(u"export_excel_entrepot")
        self.export_excel_entrepot.setGeometry(QRect(140, 0, 122, 32))
        self.export_excel_entrepot.setMinimumSize(QSize(0, 32))
        self.export_excel_entrepot.setMaximumSize(QSize(122, 32))
        self.export_excel_entrepot.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.export_excel_entrepot.setIcon(icon16)
        self.export_pdf_entrepot = QPushButton(self.widget_10)
        self.export_pdf_entrepot.setObjectName(u"export_pdf_entrepot")
        self.export_pdf_entrepot.setGeometry(QRect(280, 0, 122, 32))
        self.export_pdf_entrepot.setMinimumSize(QSize(0, 32))
        self.export_pdf_entrepot.setMaximumSize(QSize(122, 32))
        self.export_pdf_entrepot.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 58, 21);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.export_pdf_entrepot.setIcon(icon17)

        self.gridLayout_10.addWidget(self.widget_10, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_entrepots, "")
        self.tab_client = QWidget()
        self.tab_client.setObjectName(u"tab_client")
        self.gridLayout_9 = QGridLayout(self.tab_client)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.widget_9 = QWidget(self.tab_client)
        self.widget_9.setObjectName(u"widget_9")
        self.btn_ajout_client = QPushButton(self.widget_9)
        self.btn_ajout_client.setObjectName(u"btn_ajout_client")
        self.btn_ajout_client.setGeometry(QRect(0, 0, 122, 32))
        self.btn_ajout_client.setMinimumSize(QSize(0, 32))
        self.btn_ajout_client.setMaximumSize(QSize(122, 32))
        self.btn_ajout_client.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_ajout_client.setIcon(icon15)
        self.export_excel_btn_2 = QPushButton(self.widget_9)
        self.export_excel_btn_2.setObjectName(u"export_excel_btn_2")
        self.export_excel_btn_2.setGeometry(QRect(140, 0, 114, 32))
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
        self.export_excel_btn_2.setIcon(icon16)
        self.export_pdf_btn_2 = QPushButton(self.widget_9)
        self.export_pdf_btn_2.setObjectName(u"export_pdf_btn_2")
        self.export_pdf_btn_2.setGeometry(QRect(270, 0, 111, 32))
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

        self.gridLayout_9.addWidget(self.widget_9, 1, 0, 1, 1)

        self.table_infos_client_2 = QTableWidget(self.tab_client)
        if (self.table_infos_client_2.columnCount() < 9):
            self.table_infos_client_2.setColumnCount(9)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_infos_client_2.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_infos_client_2.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_infos_client_2.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_infos_client_2.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_infos_client_2.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_infos_client_2.setHorizontalHeaderItem(5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_infos_client_2.setHorizontalHeaderItem(6, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.table_infos_client_2.setHorizontalHeaderItem(7, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.table_infos_client_2.setHorizontalHeaderItem(8, __qtablewidgetitem29)
        self.table_infos_client_2.setObjectName(u"table_infos_client_2")
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
        self.table_infos_client_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.table_infos_client_2.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_infos_client_2.setDragEnabled(True)
        self.table_infos_client_2.setAlternatingRowColors(True)
        self.table_infos_client_2.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.table_infos_client_2.setShowGrid(True)
        self.table_infos_client_2.setGridStyle(Qt.PenStyle.CustomDashLine)
        self.table_infos_client_2.horizontalHeader().setVisible(True)
        self.table_infos_client_2.horizontalHeader().setCascadingSectionResizes(True)
        self.table_infos_client_2.horizontalHeader().setDefaultSectionSize(150)
        self.table_infos_client_2.horizontalHeader().setProperty("showSortIndicator", True)
        self.table_infos_client_2.horizontalHeader().setStretchLastSection(True)
        self.table_infos_client_2.verticalHeader().setVisible(False)

        self.gridLayout_9.addWidget(self.table_infos_client_2, 3, 0, 1, 2)

        self.cherche_client_2 = QLineEdit(self.tab_client)
        self.cherche_client_2.setObjectName(u"cherche_client_2")
        self.cherche_client_2.setMinimumSize(QSize(0, 32))
        self.cherche_client_2.setMaximumSize(QSize(407, 31))
        self.cherche_client_2.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")

        self.gridLayout_9.addWidget(self.cherche_client_2, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_client, "")
        self.tab_inventaires = QWidget()
        self.tab_inventaires.setObjectName(u"tab_inventaires")
        self.gridLayout_8 = QGridLayout(self.tab_inventaires)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.table_infos_inventaire = QTableWidget(self.tab_inventaires)
        if (self.table_infos_inventaire.columnCount() < 9):
            self.table_infos_inventaire.setColumnCount(9)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.table_infos_inventaire.setHorizontalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.table_infos_inventaire.setHorizontalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.table_infos_inventaire.setHorizontalHeaderItem(2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.table_infos_inventaire.setHorizontalHeaderItem(3, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.table_infos_inventaire.setHorizontalHeaderItem(4, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.table_infos_inventaire.setHorizontalHeaderItem(5, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.table_infos_inventaire.setHorizontalHeaderItem(6, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.table_infos_inventaire.setHorizontalHeaderItem(7, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.table_infos_inventaire.setHorizontalHeaderItem(8, __qtablewidgetitem38)
        self.table_infos_inventaire.setObjectName(u"table_infos_inventaire")
        self.table_infos_inventaire.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_inventaire.setAlternatingRowColors(True)
        self.table_infos_inventaire.horizontalHeader().setDefaultSectionSize(150)
        self.table_infos_inventaire.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_8.addWidget(self.table_infos_inventaire, 2, 0, 1, 2)

        self.widget_7 = QWidget(self.tab_inventaires)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(0, 0, 458, 31))
        self.btn_ajout_inventaire = QPushButton(self.widget_8)
        self.btn_ajout_inventaire.setObjectName(u"btn_ajout_inventaire")
        self.btn_ajout_inventaire.setGeometry(QRect(0, 0, 122, 32))
        self.btn_ajout_inventaire.setMinimumSize(QSize(0, 32))
        self.btn_ajout_inventaire.setMaximumSize(QSize(122, 32))
        self.btn_ajout_inventaire.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_ajout_inventaire.setIcon(icon15)
        self.export_excel_btn_inventaire = QPushButton(self.widget_8)
        self.export_excel_btn_inventaire.setObjectName(u"export_excel_btn_inventaire")
        self.export_excel_btn_inventaire.setGeometry(QRect(140, 0, 122, 32))
        self.export_excel_btn_inventaire.setMinimumSize(QSize(0, 32))
        self.export_excel_btn_inventaire.setMaximumSize(QSize(122, 32))
        self.export_excel_btn_inventaire.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.export_excel_btn_inventaire.setIcon(icon16)
        self.export_pdf_btn_inventaire = QPushButton(self.widget_8)
        self.export_pdf_btn_inventaire.setObjectName(u"export_pdf_btn_inventaire")
        self.export_pdf_btn_inventaire.setGeometry(QRect(280, 0, 122, 32))
        self.export_pdf_btn_inventaire.setMinimumSize(QSize(0, 32))
        self.export_pdf_btn_inventaire.setMaximumSize(QSize(122, 32))
        self.export_pdf_btn_inventaire.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 58, 21);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.export_pdf_btn_inventaire.setIcon(icon17)

        self.gridLayout_8.addWidget(self.widget_7, 0, 0, 2, 1)

        self.cherche_inventaire = QLineEdit(self.tab_inventaires)
        self.cherche_inventaire.setObjectName(u"cherche_inventaire")
        self.cherche_inventaire.setMinimumSize(QSize(0, 32))
        self.cherche_inventaire.setMaximumSize(QSize(407, 31))
        self.cherche_inventaire.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")

        self.gridLayout_8.addWidget(self.cherche_inventaire, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_inventaires, "")
        self.tab_vente_retour = QWidget()
        self.tab_vente_retour.setObjectName(u"tab_vente_retour")
        self.gridLayout_6 = QGridLayout(self.tab_vente_retour)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.cherche_vente_retour = QLineEdit(self.tab_vente_retour)
        self.cherche_vente_retour.setObjectName(u"cherche_vente_retour")
        self.cherche_vente_retour.setMinimumSize(QSize(0, 32))
        self.cherche_vente_retour.setMaximumSize(QSize(407, 31))
        self.cherche_vente_retour.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")

        self.gridLayout_6.addWidget(self.cherche_vente_retour, 0, 1, 1, 1)

        self.table_infos_ventes_retours = QTableWidget(self.tab_vente_retour)
        if (self.table_infos_ventes_retours.columnCount() < 8):
            self.table_infos_ventes_retours.setColumnCount(8)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.table_infos_ventes_retours.setHorizontalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.table_infos_ventes_retours.setHorizontalHeaderItem(1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.table_infos_ventes_retours.setHorizontalHeaderItem(2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.table_infos_ventes_retours.setHorizontalHeaderItem(3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.table_infos_ventes_retours.setHorizontalHeaderItem(4, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.table_infos_ventes_retours.setHorizontalHeaderItem(5, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.table_infos_ventes_retours.setHorizontalHeaderItem(6, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.table_infos_ventes_retours.setHorizontalHeaderItem(7, __qtablewidgetitem46)
        self.table_infos_ventes_retours.setObjectName(u"table_infos_ventes_retours")
        self.table_infos_ventes_retours.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_ventes_retours.setAlternatingRowColors(True)
        self.table_infos_ventes_retours.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.table_infos_ventes_retours.setSortingEnabled(True)
        self.table_infos_ventes_retours.horizontalHeader().setCascadingSectionResizes(True)
        self.table_infos_ventes_retours.horizontalHeader().setDefaultSectionSize(150)
        self.table_infos_ventes_retours.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_6.addWidget(self.table_infos_ventes_retours, 3, 0, 1, 2)

        self.widget_2 = QWidget(self.tab_vente_retour)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setEnabled(True)
        self.btn_ajout_inventaire_2 = QPushButton(self.widget_2)
        self.btn_ajout_inventaire_2.setObjectName(u"btn_ajout_inventaire_2")
        self.btn_ajout_inventaire_2.setGeometry(QRect(0, 0, 122, 32))
        self.btn_ajout_inventaire_2.setMinimumSize(QSize(0, 32))
        self.btn_ajout_inventaire_2.setMaximumSize(QSize(122, 32))
        self.btn_ajout_inventaire_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_ajout_inventaire_2.setIcon(icon15)
        self.export_excel_btn_vente_retour = QPushButton(self.widget_2)
        self.export_excel_btn_vente_retour.setObjectName(u"export_excel_btn_vente_retour")
        self.export_excel_btn_vente_retour.setGeometry(QRect(140, 0, 122, 32))
        self.export_excel_btn_vente_retour.setMinimumSize(QSize(0, 32))
        self.export_excel_btn_vente_retour.setMaximumSize(QSize(122, 32))
        self.export_excel_btn_vente_retour.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.export_excel_btn_vente_retour.setIcon(icon16)
        self.export_pdf_btn_vente_retour = QPushButton(self.widget_2)
        self.export_pdf_btn_vente_retour.setObjectName(u"export_pdf_btn_vente_retour")
        self.export_pdf_btn_vente_retour.setGeometry(QRect(280, 0, 122, 32))
        self.export_pdf_btn_vente_retour.setMinimumSize(QSize(0, 32))
        self.export_pdf_btn_vente_retour.setMaximumSize(QSize(122, 32))
        self.export_pdf_btn_vente_retour.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 58, 21);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.export_pdf_btn_vente_retour.setIcon(icon17)

        self.gridLayout_6.addWidget(self.widget_2, 0, 0, 2, 1)

        self.tabWidget.addTab(self.tab_vente_retour, "")
        self.tab_mvt_stock = QWidget()
        self.tab_mvt_stock.setObjectName(u"tab_mvt_stock")
        self.gridLayout_7 = QGridLayout(self.tab_mvt_stock)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.table_infos_mvt_stock = QTableWidget(self.tab_mvt_stock)
        if (self.table_infos_mvt_stock.columnCount() < 8):
            self.table_infos_mvt_stock.setColumnCount(8)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.table_infos_mvt_stock.setHorizontalHeaderItem(0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.table_infos_mvt_stock.setHorizontalHeaderItem(1, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.table_infos_mvt_stock.setHorizontalHeaderItem(2, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.table_infos_mvt_stock.setHorizontalHeaderItem(3, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.table_infos_mvt_stock.setHorizontalHeaderItem(4, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.table_infos_mvt_stock.setHorizontalHeaderItem(5, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.table_infos_mvt_stock.setHorizontalHeaderItem(6, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.table_infos_mvt_stock.setHorizontalHeaderItem(7, __qtablewidgetitem54)
        self.table_infos_mvt_stock.setObjectName(u"table_infos_mvt_stock")
        self.table_infos_mvt_stock.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_mvt_stock.setAlternatingRowColors(True)
        self.table_infos_mvt_stock.horizontalHeader().setDefaultSectionSize(150)
        self.table_infos_mvt_stock.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_7.addWidget(self.table_infos_mvt_stock, 9, 0, 1, 4)

        self.cherche_mvt_stock = QLineEdit(self.tab_mvt_stock)
        self.cherche_mvt_stock.setObjectName(u"cherche_mvt_stock")
        self.cherche_mvt_stock.setMinimumSize(QSize(0, 32))
        self.cherche_mvt_stock.setMaximumSize(QSize(407, 31))
        self.cherche_mvt_stock.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")

        self.gridLayout_7.addWidget(self.cherche_mvt_stock, 0, 3, 1, 1)

        self.widget_13 = QWidget(self.tab_mvt_stock)
        self.widget_13.setObjectName(u"widget_13")
        self.export_excel_btn_mvt_stock = QPushButton(self.widget_13)
        self.export_excel_btn_mvt_stock.setObjectName(u"export_excel_btn_mvt_stock")
        self.export_excel_btn_mvt_stock.setGeometry(QRect(0, 0, 122, 32))
        self.export_excel_btn_mvt_stock.setMinimumSize(QSize(0, 32))
        self.export_excel_btn_mvt_stock.setMaximumSize(QSize(122, 32))
        self.export_excel_btn_mvt_stock.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.export_excel_btn_mvt_stock.setIcon(icon16)
        self.export_pdf_btn_mvt_stock = QPushButton(self.widget_13)
        self.export_pdf_btn_mvt_stock.setObjectName(u"export_pdf_btn_mvt_stock")
        self.export_pdf_btn_mvt_stock.setGeometry(QRect(130, 0, 122, 32))
        self.export_pdf_btn_mvt_stock.setMinimumSize(QSize(0, 32))
        self.export_pdf_btn_mvt_stock.setMaximumSize(QSize(122, 32))
        self.export_pdf_btn_mvt_stock.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 58, 21);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.export_pdf_btn_mvt_stock.setIcon(icon17)

        self.gridLayout_7.addWidget(self.widget_13, 0, 0, 1, 2)

        self.tabWidget.addTab(self.tab_mvt_stock, "")
        self.tab_livraison = QWidget()
        self.tab_livraison.setObjectName(u"tab_livraison")
        self.gridLayout_5 = QGridLayout(self.tab_livraison)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.cherche_livraison = QLineEdit(self.tab_livraison)
        self.cherche_livraison.setObjectName(u"cherche_livraison")
        self.cherche_livraison.setMinimumSize(QSize(0, 32))
        self.cherche_livraison.setMaximumSize(QSize(407, 31))
        self.cherche_livraison.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")

        self.gridLayout_5.addWidget(self.cherche_livraison, 1, 2, 1, 1)

        self.table_infos_livraison = QTableWidget(self.tab_livraison)
        if (self.table_infos_livraison.columnCount() < 10):
            self.table_infos_livraison.setColumnCount(10)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.table_infos_livraison.setHorizontalHeaderItem(0, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.table_infos_livraison.setHorizontalHeaderItem(1, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.table_infos_livraison.setHorizontalHeaderItem(2, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.table_infos_livraison.setHorizontalHeaderItem(3, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.table_infos_livraison.setHorizontalHeaderItem(4, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.table_infos_livraison.setHorizontalHeaderItem(5, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.table_infos_livraison.setHorizontalHeaderItem(6, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.table_infos_livraison.setHorizontalHeaderItem(7, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.table_infos_livraison.setHorizontalHeaderItem(8, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.table_infos_livraison.setHorizontalHeaderItem(9, __qtablewidgetitem64)
        self.table_infos_livraison.setObjectName(u"table_infos_livraison")
        self.table_infos_livraison.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_livraison.setAlternatingRowColors(True)
        self.table_infos_livraison.horizontalHeader().setDefaultSectionSize(150)
        self.table_infos_livraison.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_5.addWidget(self.table_infos_livraison, 3, 0, 1, 3)

        self.widget_4 = QWidget(self.tab_livraison)
        self.widget_4.setObjectName(u"widget_4")
        self.btn_ajout_livraison = QPushButton(self.widget_4)
        self.btn_ajout_livraison.setObjectName(u"btn_ajout_livraison")
        self.btn_ajout_livraison.setGeometry(QRect(0, 0, 122, 32))
        self.btn_ajout_livraison.setMinimumSize(QSize(0, 32))
        self.btn_ajout_livraison.setMaximumSize(QSize(122, 32))
        self.btn_ajout_livraison.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_ajout_livraison.setIcon(icon15)
        self.export_excel_btn_livraison = QPushButton(self.widget_4)
        self.export_excel_btn_livraison.setObjectName(u"export_excel_btn_livraison")
        self.export_excel_btn_livraison.setGeometry(QRect(140, 0, 122, 32))
        self.export_excel_btn_livraison.setMinimumSize(QSize(0, 32))
        self.export_excel_btn_livraison.setMaximumSize(QSize(122, 32))
        self.export_excel_btn_livraison.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.export_excel_btn_livraison.setIcon(icon16)
        self.export_pdf_btn_livraison = QPushButton(self.widget_4)
        self.export_pdf_btn_livraison.setObjectName(u"export_pdf_btn_livraison")
        self.export_pdf_btn_livraison.setGeometry(QRect(280, 0, 122, 32))
        self.export_pdf_btn_livraison.setMinimumSize(QSize(0, 32))
        self.export_pdf_btn_livraison.setMaximumSize(QSize(122, 32))
        self.export_pdf_btn_livraison.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 58, 21);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.export_pdf_btn_livraison.setIcon(icon17)

        self.gridLayout_5.addWidget(self.widget_4, 1, 0, 1, 2)

        self.tabWidget.addTab(self.tab_livraison, "")
        self.tab_flux_monetaire = QWidget()
        self.tab_flux_monetaire.setObjectName(u"tab_flux_monetaire")
        self.gridLayout_14 = QGridLayout(self.tab_flux_monetaire)
        self.gridLayout_14.setSpacing(6)
        self.gridLayout_14.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.table_infos_flux_monetaire_cate = QTableWidget(self.tab_flux_monetaire)
        if (self.table_infos_flux_monetaire_cate.columnCount() < 3):
            self.table_infos_flux_monetaire_cate.setColumnCount(3)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.table_infos_flux_monetaire_cate.setHorizontalHeaderItem(0, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.table_infos_flux_monetaire_cate.setHorizontalHeaderItem(1, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.table_infos_flux_monetaire_cate.setHorizontalHeaderItem(2, __qtablewidgetitem67)
        self.table_infos_flux_monetaire_cate.setObjectName(u"table_infos_flux_monetaire_cate")
        self.table_infos_flux_monetaire_cate.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_flux_monetaire_cate.setAlternatingRowColors(True)
        self.table_infos_flux_monetaire_cate.horizontalHeader().setDefaultSectionSize(120)
        self.table_infos_flux_monetaire_cate.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_14.addWidget(self.table_infos_flux_monetaire_cate, 2, 0, 1, 1)

        self.widget_5 = QWidget(self.tab_flux_monetaire)
        self.widget_5.setObjectName(u"widget_5")
        self.export_excel_btn_flux_monetaire = QPushButton(self.widget_5)
        self.export_excel_btn_flux_monetaire.setObjectName(u"export_excel_btn_flux_monetaire")
        self.export_excel_btn_flux_monetaire.setGeometry(QRect(140, 0, 122, 32))
        self.export_excel_btn_flux_monetaire.setMinimumSize(QSize(0, 32))
        self.export_excel_btn_flux_monetaire.setMaximumSize(QSize(122, 32))
        self.export_excel_btn_flux_monetaire.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.export_excel_btn_flux_monetaire.setIcon(icon16)
        self.btn_ajout_inventaire_3 = QPushButton(self.widget_5)
        self.btn_ajout_inventaire_3.setObjectName(u"btn_ajout_inventaire_3")
        self.btn_ajout_inventaire_3.setGeometry(QRect(10, 0, 121, 32))
        self.btn_ajout_inventaire_3.setMinimumSize(QSize(0, 32))
        self.btn_ajout_inventaire_3.setMaximumSize(QSize(122, 32))
        self.btn_ajout_inventaire_3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.btn_ajout_inventaire_3.setIcon(icon15)
        self.export_pdf_btn_flux_monetaire = QPushButton(self.widget_5)
        self.export_pdf_btn_flux_monetaire.setObjectName(u"export_pdf_btn_flux_monetaire")
        self.export_pdf_btn_flux_monetaire.setGeometry(QRect(270, 0, 121, 32))
        self.export_pdf_btn_flux_monetaire.setMinimumSize(QSize(0, 32))
        self.export_pdf_btn_flux_monetaire.setMaximumSize(QSize(122, 32))
        self.export_pdf_btn_flux_monetaire.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 58, 21);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 12px\n"
"}")
        self.export_pdf_btn_flux_monetaire.setIcon(icon17)

        self.gridLayout_14.addWidget(self.widget_5, 0, 0, 1, 1)

        self.table_infos_flux_monetaire_3 = QTableWidget(self.tab_flux_monetaire)
        if (self.table_infos_flux_monetaire_3.columnCount() < 2):
            self.table_infos_flux_monetaire_3.setColumnCount(2)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.table_infos_flux_monetaire_3.setHorizontalHeaderItem(0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.table_infos_flux_monetaire_3.setHorizontalHeaderItem(1, __qtablewidgetitem69)
        self.table_infos_flux_monetaire_3.setObjectName(u"table_infos_flux_monetaire_3")
        self.table_infos_flux_monetaire_3.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_flux_monetaire_3.setAlternatingRowColors(True)
        self.table_infos_flux_monetaire_3.horizontalHeader().setDefaultSectionSize(150)
        self.table_infos_flux_monetaire_3.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_14.addWidget(self.table_infos_flux_monetaire_3, 2, 1, 1, 1)

        self.table_infos_flux_monetaire = QTableWidget(self.tab_flux_monetaire)
        if (self.table_infos_flux_monetaire.columnCount() < 7):
            self.table_infos_flux_monetaire.setColumnCount(7)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.table_infos_flux_monetaire.setHorizontalHeaderItem(0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.table_infos_flux_monetaire.setHorizontalHeaderItem(1, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.table_infos_flux_monetaire.setHorizontalHeaderItem(2, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.table_infos_flux_monetaire.setHorizontalHeaderItem(3, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.table_infos_flux_monetaire.setHorizontalHeaderItem(4, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.table_infos_flux_monetaire.setHorizontalHeaderItem(5, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.table_infos_flux_monetaire.setHorizontalHeaderItem(6, __qtablewidgetitem76)
        self.table_infos_flux_monetaire.setObjectName(u"table_infos_flux_monetaire")
        self.table_infos_flux_monetaire.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_flux_monetaire.setAlternatingRowColors(True)
        self.table_infos_flux_monetaire.setShowGrid(False)
        self.table_infos_flux_monetaire.setSortingEnabled(True)
        self.table_infos_flux_monetaire.horizontalHeader().setVisible(True)
        self.table_infos_flux_monetaire.horizontalHeader().setDefaultSectionSize(120)
        self.table_infos_flux_monetaire.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_14.addWidget(self.table_infos_flux_monetaire, 3, 0, 1, 2)

        self.cherche_flux_monetaire = QLineEdit(self.tab_flux_monetaire)
        self.cherche_flux_monetaire.setObjectName(u"cherche_flux_monetaire")
        self.cherche_flux_monetaire.setMinimumSize(QSize(0, 32))
        self.cherche_flux_monetaire.setMaximumSize(QSize(407, 31))
        self.cherche_flux_monetaire.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius:10px\n"
"}")

        self.gridLayout_14.addWidget(self.cherche_flux_monetaire, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_flux_monetaire, "")
        self.tab_rapports_financiers = QWidget()
        self.tab_rapports_financiers.setObjectName(u"tab_rapports_financiers")
        self.gridLayout_13 = QGridLayout(self.tab_rapports_financiers)
        self.gridLayout_13.setSpacing(6)
        self.gridLayout_13.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_11 = QLabel(self.tab_rapports_financiers)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(50, 1))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setUnderline(True)
        self.label_11.setFont(font6)

        self.gridLayout_13.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_13 = QLabel(self.tab_rapports_financiers)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(50, 1))
        self.label_13.setFont(font6)

        self.gridLayout_13.addWidget(self.label_13, 0, 1, 1, 1)

        self.table_infos_actifs_immo = QTableWidget(self.tab_rapports_financiers)
        if (self.table_infos_actifs_immo.columnCount() < 2):
            self.table_infos_actifs_immo.setColumnCount(2)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.table_infos_actifs_immo.setHorizontalHeaderItem(0, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.table_infos_actifs_immo.setHorizontalHeaderItem(1, __qtablewidgetitem78)
        self.table_infos_actifs_immo.setObjectName(u"table_infos_actifs_immo")
        self.table_infos_actifs_immo.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_actifs_immo.setAlternatingRowColors(True)
        self.table_infos_actifs_immo.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_13.addWidget(self.table_infos_actifs_immo, 1, 0, 1, 1)

        self.table_infos_Capitaux_propres = QTableWidget(self.tab_rapports_financiers)
        if (self.table_infos_Capitaux_propres.columnCount() < 2):
            self.table_infos_Capitaux_propres.setColumnCount(2)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.table_infos_Capitaux_propres.setHorizontalHeaderItem(0, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.table_infos_Capitaux_propres.setHorizontalHeaderItem(1, __qtablewidgetitem80)
        self.table_infos_Capitaux_propres.setObjectName(u"table_infos_Capitaux_propres")
        self.table_infos_Capitaux_propres.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_Capitaux_propres.setAlternatingRowColors(True)
        self.table_infos_Capitaux_propres.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_13.addWidget(self.table_infos_Capitaux_propres, 1, 1, 1, 1)

        self.label_12 = QLabel(self.tab_rapports_financiers)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(50, 1))
        self.label_12.setFont(font6)

        self.gridLayout_13.addWidget(self.label_12, 2, 0, 1, 1)

        self.label_14 = QLabel(self.tab_rapports_financiers)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(50, 1))
        self.label_14.setFont(font6)

        self.gridLayout_13.addWidget(self.label_14, 2, 1, 1, 1)

        self.table_infos_actifs_circulants = QTableWidget(self.tab_rapports_financiers)
        if (self.table_infos_actifs_circulants.columnCount() < 2):
            self.table_infos_actifs_circulants.setColumnCount(2)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.table_infos_actifs_circulants.setHorizontalHeaderItem(0, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.table_infos_actifs_circulants.setHorizontalHeaderItem(1, __qtablewidgetitem82)
        self.table_infos_actifs_circulants.setObjectName(u"table_infos_actifs_circulants")
        self.table_infos_actifs_circulants.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_actifs_circulants.setAlternatingRowColors(True)
        self.table_infos_actifs_circulants.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_13.addWidget(self.table_infos_actifs_circulants, 3, 0, 1, 1)

        self.table_infos_actifs_circulants_2 = QTableWidget(self.tab_rapports_financiers)
        if (self.table_infos_actifs_circulants_2.columnCount() < 2):
            self.table_infos_actifs_circulants_2.setColumnCount(2)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.table_infos_actifs_circulants_2.setHorizontalHeaderItem(0, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.table_infos_actifs_circulants_2.setHorizontalHeaderItem(1, __qtablewidgetitem84)
        self.table_infos_actifs_circulants_2.setObjectName(u"table_infos_actifs_circulants_2")
        self.table_infos_actifs_circulants_2.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTablewidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.table_infos_actifs_circulants_2.setAlternatingRowColors(True)
        self.table_infos_actifs_circulants_2.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_13.addWidget(self.table_infos_actifs_circulants_2, 3, 1, 1, 1)

        self.tabWidget.addTab(self.tab_rapports_financiers, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.main_screen_widget, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget1, 1, 2, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1256, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"GeStock", None))
        self.btn_dashboard_4.setText(QCoreApplication.translate("MainWindow", u"    Dashboard", None))
        self.btn_gestion_referentiels_4.setText(QCoreApplication.translate("MainWindow", u"    R\u00e9f\u00e9rentiel", None))
        self.btn_ref_matires_premieres_3.setText(QCoreApplication.translate("MainWindow", u"Mati\u00e8res premi\u00e8res", None))
        self.btn_ref_produits_3.setText(QCoreApplication.translate("MainWindow", u"Produits", None))
        self.btn_ref_fournisseurs_3.setText(QCoreApplication.translate("MainWindow", u"Fournisseurs", None))
        self.btn_ref_clients_3.setText(QCoreApplication.translate("MainWindow", u"Clients", None))
        self.btn_ref_entrepots_3.setText(QCoreApplication.translate("MainWindow", u"Entrepot", None))
        self.btn_gestion_produits_4.setText(QCoreApplication.translate("MainWindow", u"    Stock", None))
        self.btn_inventaire_3.setText(QCoreApplication.translate("MainWindow", u"Inventaires", None))
        self.btn_mvts_des_stocks_3.setText(QCoreApplication.translate("MainWindow", u"Mouvements du stock", None))
        self.btn_gestion_operations_4.setText(QCoreApplication.translate("MainWindow", u"    Op\u00e9rations", None))
        self.btn_ventes_retours_3.setText(QCoreApplication.translate("MainWindow", u"Ventes et retours", None))
        self.btn_livraisons_3.setText(QCoreApplication.translate("MainWindow", u"Livraisons", None))
        self.btn_gestion_compta_4.setText(QCoreApplication.translate("MainWindow", u"    Comptabilit\u00e9", None))
        self.btn_flux_monetaires_3.setText(QCoreApplication.translate("MainWindow", u"Flux mon\u00e9taire", None))
        self.btn_rapports_financiers_3.setText(QCoreApplication.translate("MainWindow", u"Rapports financiers", None))
        self.btn_parametre_2.setText("")
        self.btn_deconnexion_2.setText("")
        self.label_4.setText("")
        self.btn_dashboard_1.setText("")
        self.btn_gestion_referentiels_1.setText("")
        self.btn_gestion_produits_1.setText("")
        self.btn_gestion_operations_1.setText("")
        self.btn_gestion_compta_1.setText("")
        self.btn_parametre_1.setText("")
        self.btn_deconnexion_1.setText("")
        self.pushButton.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recherche...", None))
        self.label_6.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Tableau de bord", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dashboard), QCoreApplication.translate("MainWindow", u"Tableau de bord", None))
        self.cherche_produit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher produit...", None))
        ___qtablewidgetitem = self.table_infos_client_4.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.table_infos_client_4.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem2 = self.table_infos_client_4.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Fournisseur", None));
        ___qtablewidgetitem3 = self.table_infos_client_4.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Prix de revient", None));
        ___qtablewidgetitem4 = self.table_infos_client_4.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Prix de vente", None));
        ___qtablewidgetitem5 = self.table_infos_client_4.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem6 = self.table_infos_client_4.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.btn_ajout_produit.setText(QCoreApplication.translate("MainWindow", u"Ajouter Produit", None))
        self.btn_export_excel_produit.setText(QCoreApplication.translate("MainWindow", u"Export Excel", None))
        self.btn_export_pdf_produit.setText(QCoreApplication.translate("MainWindow", u"Export PDF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_produits), QCoreApplication.translate("MainWindow", u"Produits", None))
        self.cherche_fournisseur.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher client...", None))
        ___qtablewidgetitem7 = self.table_infos_fournisseur.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem8 = self.table_infos_fournisseur.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem9 = self.table_infos_fournisseur.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"prenom", None));
        ___qtablewidgetitem10 = self.table_infos_fournisseur.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Entreprise", None));
        ___qtablewidgetitem11 = self.table_infos_fournisseur.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Adresse", None));
        ___qtablewidgetitem12 = self.table_infos_fournisseur.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"T\u00e9l\u00e9phone", None));
        ___qtablewidgetitem13 = self.table_infos_fournisseur.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem14 = self.table_infos_fournisseur.horizontalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.btn_ajout_fournisseur.setText(QCoreApplication.translate("MainWindow", u"Ajouter fournisseur", None))
        self.export_excel_btn_fournisseur.setText(QCoreApplication.translate("MainWindow", u"Export Excel", None))
        self.export_pdf_btn_fournisseur.setText(QCoreApplication.translate("MainWindow", u"Export PDF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fournisseurs), QCoreApplication.translate("MainWindow", u"Fournisseur", None))
        self.cherche_entrepot.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher client...", None))
        ___qtablewidgetitem15 = self.table_infos_entrepot.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem16 = self.table_infos_entrepot.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Code", None));
        ___qtablewidgetitem17 = self.table_infos_entrepot.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Adresse", None));
        ___qtablewidgetitem18 = self.table_infos_entrepot.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"T\u00e9l\u00e9phone", None));
        ___qtablewidgetitem19 = self.table_infos_entrepot.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"E-mail", None));
        ___qtablewidgetitem20 = self.table_infos_entrepot.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.btn_ajout_entrepot.setText(QCoreApplication.translate("MainWindow", u"Ajouter entrepot", None))
        self.export_excel_entrepot.setText(QCoreApplication.translate("MainWindow", u"Export Excel", None))
        self.export_pdf_entrepot.setText(QCoreApplication.translate("MainWindow", u"Export PDF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_entrepots), QCoreApplication.translate("MainWindow", u"Entrep\u00f4ts", None))
        self.btn_ajout_client.setText(QCoreApplication.translate("MainWindow", u"Ajouter client", None))
        self.export_excel_btn_2.setText(QCoreApplication.translate("MainWindow", u"Export Excel", None))
        self.export_pdf_btn_2.setText(QCoreApplication.translate("MainWindow", u"Export PDF", None))
        ___qtablewidgetitem21 = self.table_infos_client_2.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"ID Client", None));
        ___qtablewidgetitem22 = self.table_infos_client_2.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom", None));
        ___qtablewidgetitem23 = self.table_infos_client_2.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem24 = self.table_infos_client_2.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Genre", None));
        ___qtablewidgetitem25 = self.table_infos_client_2.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Entreprise", None));
        ___qtablewidgetitem26 = self.table_infos_client_2.horizontalHeaderItem(5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Adresse", None));
        ___qtablewidgetitem27 = self.table_infos_client_2.horizontalHeaderItem(6)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"T\u00e9l\u00e9phone", None));
        ___qtablewidgetitem28 = self.table_infos_client_2.horizontalHeaderItem(7)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem29 = self.table_infos_client_2.horizontalHeaderItem(8)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.cherche_client_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher client...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_client), QCoreApplication.translate("MainWindow", u"Clients", None))
        ___qtablewidgetitem30 = self.table_infos_inventaire.horizontalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"ID Inventaire", None));
        ___qtablewidgetitem31 = self.table_infos_inventaire.horizontalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Date inventaire", None));
        ___qtablewidgetitem32 = self.table_infos_inventaire.horizontalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Code produit", None));
        ___qtablewidgetitem33 = self.table_infos_inventaire.horizontalHeaderItem(3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem34 = self.table_infos_inventaire.horizontalHeaderItem(4)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Quantit\u00e9 th\u00e9orique", None));
        ___qtablewidgetitem35 = self.table_infos_inventaire.horizontalHeaderItem(5)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Quantit\u00e9 r\u00e9elle", None));
        ___qtablewidgetitem36 = self.table_infos_inventaire.horizontalHeaderItem(6)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Ecart", None));
        ___qtablewidgetitem37 = self.table_infos_inventaire.horizontalHeaderItem(7)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Unit\u00e9", None));
        ___qtablewidgetitem38 = self.table_infos_inventaire.horizontalHeaderItem(8)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Agent", None));
        self.btn_ajout_inventaire.setText(QCoreApplication.translate("MainWindow", u"D\u00e9buter", None))
        self.export_excel_btn_inventaire.setText(QCoreApplication.translate("MainWindow", u"Export Excel", None))
        self.export_pdf_btn_inventaire.setText(QCoreApplication.translate("MainWindow", u"Export PDF", None))
        self.cherche_inventaire.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher client...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_inventaires), QCoreApplication.translate("MainWindow", u"Inventaire", None))
        self.cherche_vente_retour.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher client...", None))
        ___qtablewidgetitem39 = self.table_infos_ventes_retours.horizontalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"ID Vente", None));
        ___qtablewidgetitem40 = self.table_infos_ventes_retours.horizontalHeaderItem(1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Date de vente", None));
        ___qtablewidgetitem41 = self.table_infos_ventes_retours.horizontalHeaderItem(2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Client", None));
        ___qtablewidgetitem42 = self.table_infos_ventes_retours.horizontalHeaderItem(3)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Nombre d'articles", None));
        ___qtablewidgetitem43 = self.table_infos_ventes_retours.horizontalHeaderItem(4)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Prix total", None));
        ___qtablewidgetitem44 = self.table_infos_ventes_retours.horizontalHeaderItem(5)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Montant r\u00e9gl\u00e9", None));
        ___qtablewidgetitem45 = self.table_infos_ventes_retours.horizontalHeaderItem(6)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Montant restant", None));
        ___qtablewidgetitem46 = self.table_infos_ventes_retours.horizontalHeaderItem(7)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Utilisateur", None));
        self.btn_ajout_inventaire_2.setText(QCoreApplication.translate("MainWindow", u"Vendre/Retourner", None))
        self.export_excel_btn_vente_retour.setText(QCoreApplication.translate("MainWindow", u"Export Excel", None))
        self.export_pdf_btn_vente_retour.setText(QCoreApplication.translate("MainWindow", u"Export PDF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_vente_retour), QCoreApplication.translate("MainWindow", u"Ventes & Retours", None))
        ___qtablewidgetitem47 = self.table_infos_mvt_stock.horizontalHeaderItem(0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"ID mouvement", None));
        ___qtablewidgetitem48 = self.table_infos_mvt_stock.horizontalHeaderItem(1)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Code produit", None));
        ___qtablewidgetitem49 = self.table_infos_mvt_stock.horizontalHeaderItem(2)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem50 = self.table_infos_mvt_stock.horizontalHeaderItem(3)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem51 = self.table_infos_mvt_stock.horizontalHeaderItem(4)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Quantit\u00e9 disponible", None));
        ___qtablewidgetitem52 = self.table_infos_mvt_stock.horizontalHeaderItem(5)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Unit\u00e9", None));
        ___qtablewidgetitem53 = self.table_infos_mvt_stock.horizontalHeaderItem(6)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Utilisateur", None));
        ___qtablewidgetitem54 = self.table_infos_mvt_stock.horizontalHeaderItem(7)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        self.cherche_mvt_stock.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher client...", None))
        self.export_excel_btn_mvt_stock.setText(QCoreApplication.translate("MainWindow", u"Export Excel", None))
        self.export_pdf_btn_mvt_stock.setText(QCoreApplication.translate("MainWindow", u"Export PDF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mvt_stock), QCoreApplication.translate("MainWindow", u"Mvts Stocks", None))
        self.cherche_livraison.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher client...", None))
        ___qtablewidgetitem55 = self.table_infos_livraison.horizontalHeaderItem(0)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Date de livraison", None));
        ___qtablewidgetitem56 = self.table_infos_livraison.horizontalHeaderItem(1)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Date de vente", None));
        ___qtablewidgetitem57 = self.table_infos_livraison.horizontalHeaderItem(2)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Client", None));
        ___qtablewidgetitem58 = self.table_infos_livraison.horizontalHeaderItem(3)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Nombre d'articles", None));
        ___qtablewidgetitem59 = self.table_infos_livraison.horizontalHeaderItem(4)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Prix total", None));
        ___qtablewidgetitem60 = self.table_infos_livraison.horizontalHeaderItem(5)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Montant r\u00e9gl\u00e9", None));
        ___qtablewidgetitem61 = self.table_infos_livraison.horizontalHeaderItem(6)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Montant restant", None));
        ___qtablewidgetitem62 = self.table_infos_livraison.horizontalHeaderItem(7)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Livreur", None));
        ___qtablewidgetitem63 = self.table_infos_livraison.horizontalHeaderItem(8)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"Statut", None));
        ___qtablewidgetitem64 = self.table_infos_livraison.horizontalHeaderItem(9)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"Utilisateur", None));
        self.btn_ajout_livraison.setText(QCoreApplication.translate("MainWindow", u"Vendre/Retourner", None))
        self.export_excel_btn_livraison.setText(QCoreApplication.translate("MainWindow", u"Export Excel", None))
        self.export_pdf_btn_livraison.setText(QCoreApplication.translate("MainWindow", u"Export PDF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_livraison), QCoreApplication.translate("MainWindow", u"Livraisons", None))
        ___qtablewidgetitem65 = self.table_infos_flux_monetaire_cate.horizontalHeaderItem(0)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"Cat\u00e9gorie", None));
        ___qtablewidgetitem66 = self.table_infos_flux_monetaire_cate.horizontalHeaderItem(1)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem67 = self.table_infos_flux_monetaire_cate.horizontalHeaderItem(2)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"Montant", None));
        self.export_excel_btn_flux_monetaire.setText(QCoreApplication.translate("MainWindow", u"Export Excel", None))
        self.btn_ajout_inventaire_3.setText(QCoreApplication.translate("MainWindow", u"Ajouter un flux", None))
        self.export_pdf_btn_flux_monetaire.setText(QCoreApplication.translate("MainWindow", u"Export PDF", None))
        ___qtablewidgetitem68 = self.table_infos_flux_monetaire_3.horizontalHeaderItem(0)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem69 = self.table_infos_flux_monetaire_3.horizontalHeaderItem(1)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Montant", None));
        ___qtablewidgetitem70 = self.table_infos_flux_monetaire.horizontalHeaderItem(0)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"ID mouvement", None));
        ___qtablewidgetitem71 = self.table_infos_flux_monetaire.horizontalHeaderItem(1)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem72 = self.table_infos_flux_monetaire.horizontalHeaderItem(2)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"Cat\u00e9gorie", None));
        ___qtablewidgetitem73 = self.table_infos_flux_monetaire.horizontalHeaderItem(3)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem74 = self.table_infos_flux_monetaire.horizontalHeaderItem(4)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Montant", None));
        ___qtablewidgetitem75 = self.table_infos_flux_monetaire.horizontalHeaderItem(5)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem76 = self.table_infos_flux_monetaire.horizontalHeaderItem(6)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"Utilisateur", None));
        self.cherche_flux_monetaire.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Chercher client...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_flux_monetaire), QCoreApplication.translate("MainWindow", u"Flux Mon\u00e9taires", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Actifs Immobilis\u00e9s", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Capitaux propres", None))
        ___qtablewidgetitem77 = self.table_infos_actifs_immo.horizontalHeaderItem(0)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"Cat\u00e9gorie", None));
        ___qtablewidgetitem78 = self.table_infos_actifs_immo.horizontalHeaderItem(1)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"Montant", None));
        ___qtablewidgetitem79 = self.table_infos_Capitaux_propres.horizontalHeaderItem(0)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"Cat\u00e9gorie", None));
        ___qtablewidgetitem80 = self.table_infos_Capitaux_propres.horizontalHeaderItem(1)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"Montant", None));
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Actifs Circulant", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Dettes", None))
        ___qtablewidgetitem81 = self.table_infos_actifs_circulants.horizontalHeaderItem(0)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"Cat\u00e9gorie", None));
        ___qtablewidgetitem82 = self.table_infos_actifs_circulants.horizontalHeaderItem(1)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"Montant", None));
        ___qtablewidgetitem83 = self.table_infos_actifs_circulants_2.horizontalHeaderItem(0)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"Cat\u00e9gorie", None));
        ___qtablewidgetitem84 = self.table_infos_actifs_circulants_2.horizontalHeaderItem(1)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"Montant", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_rapports_financiers), QCoreApplication.translate("MainWindow", u"Rapports Financiers", None))
    # retranslateUi

