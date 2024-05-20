# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QSizePolicy,
    QSpacerItem, QToolButton, QWidget)
import ressources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 800, 450))
        self.widget_2.setStyleSheet(u"background-color: #D3D3D3;")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 121, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 121, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.toolButton_providers_3 = QToolButton(self.widget_2)
        self.toolButton_providers_3.setObjectName(u"toolButton_providers_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_providers_3.sizePolicy().hasHeightForWidth())
        self.toolButton_providers_3.setSizePolicy(sizePolicy)
        self.toolButton_providers_3.setMinimumSize(QSize(230, 130))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        self.toolButton_providers_3.setFont(font)
        self.toolButton_providers_3.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/images/customer_256px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_providers_3.setIcon(icon)
        self.toolButton_providers_3.setIconSize(QSize(100, 100))
        self.toolButton_providers_3.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.toolButton_providers_3, 2, 0, 1, 1)

        self.toolButton_providers = QToolButton(self.widget_2)
        self.toolButton_providers.setObjectName(u"toolButton_providers")
        sizePolicy.setHeightForWidth(self.toolButton_providers.sizePolicy().hasHeightForWidth())
        self.toolButton_providers.setSizePolicy(sizePolicy)
        self.toolButton_providers.setMinimumSize(QSize(230, 130))
        self.toolButton_providers.setFont(font)
        self.toolButton_providers.setStyleSheet(u"")
        self.toolButton_providers.setIcon(icon)
        self.toolButton_providers.setIconSize(QSize(100, 100))
        self.toolButton_providers.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.toolButton_providers, 2, 1, 1, 1)

        self.toolButton_providers_4 = QToolButton(self.widget_2)
        self.toolButton_providers_4.setObjectName(u"toolButton_providers_4")
        sizePolicy.setHeightForWidth(self.toolButton_providers_4.sizePolicy().hasHeightForWidth())
        self.toolButton_providers_4.setSizePolicy(sizePolicy)
        self.toolButton_providers_4.setMinimumSize(QSize(230, 0))
        self.toolButton_providers_4.setFont(font)
        self.toolButton_providers_4.setStyleSheet(u"")
        self.toolButton_providers_4.setIcon(icon)
        self.toolButton_providers_4.setIconSize(QSize(100, 100))
        self.toolButton_providers_4.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.toolButton_providers_4, 3, 0, 1, 1)

        self.toolButton_providers_2 = QToolButton(self.widget_2)
        self.toolButton_providers_2.setObjectName(u"toolButton_providers_2")
        sizePolicy.setHeightForWidth(self.toolButton_providers_2.sizePolicy().hasHeightForWidth())
        self.toolButton_providers_2.setSizePolicy(sizePolicy)
        self.toolButton_providers_2.setMinimumSize(QSize(230, 130))
        self.toolButton_providers_2.setFont(font)
        self.toolButton_providers_2.setStyleSheet(u"")
        self.toolButton_providers_2.setIcon(icon)
        self.toolButton_providers_2.setIconSize(QSize(100, 100))
        self.toolButton_providers_2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.toolButton_providers_2, 3, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GeStock", None))
        self.toolButton_providers_3.setText(QCoreApplication.translate("MainWindow", u"COMMANDES", None))
        self.toolButton_providers.setText(QCoreApplication.translate("MainWindow", u"PRODUITS", None))
        self.toolButton_providers_4.setText(QCoreApplication.translate("MainWindow", u"CLIENTS", None))
        self.toolButton_providers_2.setText(QCoreApplication.translate("MainWindow", u"FOURNISSEURS", None))

    # retranslateUi

