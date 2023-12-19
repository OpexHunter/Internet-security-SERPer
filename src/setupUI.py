# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SERPer.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTableView,
    QWidget)
import qrc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1093, 600)
        icon = QIcon()
        icon.addFile(u":/ico/browser_internet_network_6248.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 560, 1071, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.l_search = QLineEdit(self.layoutWidget)
        self.l_search.setObjectName(u"l_search")

        self.horizontalLayout.addWidget(self.l_search)

        self.b_search = QPushButton(self.layoutWidget)
        self.b_search.setObjectName(u"b_search")
        self.b_search.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.b_search)

        self.b_clear = QPushButton(self.layoutWidget)
        self.b_clear.setObjectName(u"b_clear")

        self.horizontalLayout.addWidget(self.b_clear)

        self.SearchView = QTableView(self.centralwidget)
        self.SearchView.setObjectName(u"SearchView")
        self.SearchView.setGeometry(QRect(0, 10, 1101, 541))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Internet security SERPer", None))
        self.l_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u0430\u043f\u0440\u043e\u0441", None))
        self.b_search.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.b_clear.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
    # retranslateUi

