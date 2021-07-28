# -*- coding: utf-8 -*-

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore



class Ui_MainWindow(object):#GUI Class|GUI类
    def setupUi(self, MainWindow):
        #Set objectname|设置对象名
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        
        #Set Window size and ban adjusting|设置窗口大小及禁止调整大小
        MainWindow.resize(783, 510)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        #TableWidget Part|TableWidget部分
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)

        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 10, 761, 471))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setSortingEnabled(False)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 783, 22))
        self.menu_Option = QMenu(self.menubar)
        self.menu_Option.setObjectName(u"menu_Options")
        self.menu_Lang = QMenu(self.menubar)
        self.menu_Lang.setObjectName(u"menu_Lang")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_Option.menuAction())
        self.menubar.addAction(self.menu_Lang.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        __qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        __qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u542f\u7528", None))#Column1 ENABLED|第一列 启用
        __qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        __qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u666f\u8c61\u533a\u57df", None))#Column2 SCENERY AREA|第二列 景象区域
        __qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        __qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u5b58\u50a8\u4f4d\u7f6e", None))#Column3 SCENERY LOCATION|第三列 存储位置
        __qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        __qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u4f18\u5148\u7ea7", None))#Column4 PRIORITY|第四列 优先级
        self.menu_Option.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))#MENU1 OPTIONS|菜单1 设置
        self.menu_Lang.setTitle(QCoreApplication.translate("MainWindow", u"\u8bed\u8a00\u007c\u004c\u0061\u006e\u0067\u0075\u0061\u0067\u0065\u0073", None))#MENU1 LANGUAGES|菜单2 语言
    # retranslateUi

class TableCheckBoxWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.tableCheckBox = QCheckBox()
        self.tableCheckBoxLayout = QHBoxLayout()
        self.tableCheckBoxLayout.addWidget(self.tableCheckBox)
        self.tableCheckBoxLayout.setAlignment(self.tableCheckBox, Qt.AlignCenter)
        self.setLayout(self.tableCheckBoxLayout)

