# -*- coding: utf-8 -*-

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class AlignWidget(QWidget):
    def __init__(self, widget:QWidget, alignment:Qt.Alignment = Qt.AlignCenter) -> None:
        super().__init__()
        self.widgetLayout = QHBoxLayout(self)
        self.widgetLayout.addWidget(widget)
        self.widgetLayout.setAlignment(widget, alignment)


class TableCheckBoxWidget(AlignWidget):
    def __init__(self) -> None:
        self.tableCheckBox = QCheckBox()
        super().__init__(self.tableCheckBox, Qt.AlignCenter)
        self.widgetLayout.setContentsMargins(0, 0, 0, 0)

class TableButtonWidget(AlignWidget):
    def __init__(self) -> None:
        self.tablePushBtn = QPushButton()
        super().__init__(self.tablePushBtn, Qt.AlignCenter)
        self.widgetLayout.setContentsMargins(0, 0, 0, 0)



class Ui_MainWindow(object):  # GUI Main Class|GUI主类
    def setupUi(self, MainWindow):
        # Set objectname|设置对象名
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")


        # Set Window size and ban adjusting|设置窗口大小及禁止调整大小
        MainWindow.resize(815, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")


        # MainWindow Layout Part|主窗口布局部分
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")


        # # Left ListWidget Part|左侧列表框架部分
        self.listWidgetL = QListWidget(self.centralwidget)
        __qlistWidgetLitem = QListWidgetItem()
        self.listWidgetL.insertItem(0, __qlistWidgetLitem)
        self.listWidgetL.setObjectName(u"listWidgetL")
        sizePolicy_ListWidgetL = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy_ListWidgetL.setHorizontalStretch(0)
        sizePolicy_ListWidgetL.setVerticalStretch(0)
        sizePolicy_ListWidgetL.setHeightForWidth(self.listWidgetL.sizePolicy().hasHeightForWidth())
        self.listWidgetL.setSizePolicy(sizePolicy_ListWidgetL)
        self.listWidgetL.setMaximumSize(QSize(150, 16777215))
        self.listWidgetL.setFrameShape(QFrame.WinPanel)
        self.listWidgetL.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.listWidgetL)


        # Central TableWidget Part|中央表格框架部分
        self.tableWidgetC = QTableWidget(self.centralwidget)
        # self.tableWidgetC.verticalHeader().setVisible(False)
        self.tableWidgetC.setSortingEnabled(True)
        self.tableWidgetC.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidgetC.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidgetC.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidgetC.setFocusPolicy(Qt.NoFocus)

        if (self.tableWidgetC.columnCount() < 4):
            self.tableWidgetC.setColumnCount(4)
        __qtableWidgetCItem = QTableWidgetItem()
        self.tableWidgetC.setHorizontalHeaderItem(0, __qtableWidgetCItem)
        __qtableWidgetCItem1 = QTableWidgetItem()
        self.tableWidgetC.setHorizontalHeaderItem(1, __qtableWidgetCItem1)
        __qtableWidgetCItem2 = QTableWidgetItem()
        self.tableWidgetC.setHorizontalHeaderItem(2, __qtableWidgetCItem2)
        __qtableWidgetCItem3 = QTableWidgetItem()
        self.tableWidgetC.setHorizontalHeaderItem(3, __qtableWidgetCItem3)

        self.tableWidgetC.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidgetC.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.tableWidgetC.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)

        self.tableWidgetC.setObjectName(u"tableWidget")
        sizePolicy_TableWidgetC = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy_TableWidgetC.setHorizontalStretch(0)
        sizePolicy_TableWidgetC.setVerticalStretch(0)
        sizePolicy_TableWidgetC.setHeightForWidth(self.tableWidgetC.sizePolicy().hasHeightForWidth())
        self.tableWidgetC.setSizePolicy(sizePolicy_TableWidgetC)
        self.tableWidgetC.setFrameShape(QFrame.WinPanel)
        self.tableWidgetC.setFrameShadow(QFrame.Plain)
        self.tableWidgetC.setShowGrid(True)


        self.horizontalLayout.addWidget(self.tableWidgetC)


        # Right Push Button TableWidget Part|右侧按钮表格框架部分
        self.tableWidgetR = QTableWidget(self.centralwidget)
        self.tableWidgetR.horizontalHeader().setVisible(False)
        self.tableWidgetR.verticalHeader().setVisible(False)
        self.tableWidgetR.setShowGrid(False)
        self.tableWidgetR.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetR.verticalHeader().setDefaultSectionSize(35)
        self.tableWidgetR.setFocusPolicy(Qt.NoFocus)
        self.tableWidgetR.setSelectionMode(QAbstractItemView.NoSelection)

        if (self.tableWidgetR.columnCount() < 1):
            self.tableWidgetR.setColumnCount(1)
        if (self.tableWidgetR.rowCount() < 4):
            self.tableWidgetR.setRowCount(4)
        self.tableWidgetRBtnWidget = TableButtonWidget()
        self.tableWidgetRBtnWidget.tablePushBtn.setText('增加区域增加区域')
        self.tableWidgetR.setCellWidget(0, 0, self.tableWidgetRBtnWidget)
        self.tableWidgetRBtnWidget2 = TableButtonWidget()
        self.tableWidgetRBtnWidget2.tablePushBtn.setText('增加区域增加区域')
        self.tableWidgetR.setCellWidget(1, 0, self.tableWidgetRBtnWidget2)


        self.tableWidgetR.setObjectName(u"tableWidgetR")
        sizePolicy_listWidgetR = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy_listWidgetR.setHorizontalStretch(0)
        sizePolicy_listWidgetR.setVerticalStretch(0)
        sizePolicy_listWidgetR.setHeightForWidth(self.tableWidgetR.sizePolicy().hasHeightForWidth())
        self.tableWidgetR.setSizePolicy(sizePolicy_listWidgetR)
        self.tableWidgetR.setMaximumSize(QSize(130, 16777215))
        self.tableWidgetR.setFrameShape(QFrame.WinPanel)
        self.tableWidgetR.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.tableWidgetR)


        # Menu Bar Part|菜单栏部分
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 815, 22))
        self.menu_Option = QMenu(self.menubar)
        self.menu_Option.setObjectName(u"menu_Options")
        self.menu_Lang = QMenu(self.menubar)
        self.menu_Lang.setObjectName(u"menu_Lang")
        MainWindow.setMenuBar(self.menubar)


        # Several Actions|杂项动作
        self.menubar.addAction(self.menu_Option.menuAction())
        self.menubar.addAction(self.menu_Lang.menuAction())

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):  # About Text|文本相关
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))

        __qlistWidgetLItem = self.listWidgetL.item(0)
        __qlistWidgetLItem.setText(QCoreApplication.translate(
            "MainWindow", u"\u666f\u8c61\u5e93", None))  # LeftList Row 1|左侧列表第一行 景象库
        
        __qtableWidgetCItem = self.tableWidgetC.horizontalHeaderItem(0)
        __qtableWidgetCItem.setText(QCoreApplication.translate(
            "MainWindow", u"\u542f\u7528", None))  #Central Table Column1 ENABLED|第一列 启用
        __qtableWidgetCItem1 = self.tableWidgetC.horizontalHeaderItem(1)
        __qtableWidgetCItem1.setText(QCoreApplication.translate(
            "MainWindow", u"\u666f\u8c61\u533a\u57df", None))  #Central Table Column2 SCENERY AREA|第二列 景象区域
        __qtableWidgetCItem2 = self.tableWidgetC.horizontalHeaderItem(2)
        __qtableWidgetCItem2.setText(QCoreApplication.translate(
            "MainWindow", u"\u4fdd\u5b58\u4f4d\u7f6e", None))  #Central Table Column3 SCENERY LOCATION|第三列 保存位置
        __qtableWidgetCItem3 = self.tableWidgetC.horizontalHeaderItem(3)
        __qtableWidgetCItem3.setText(QCoreApplication.translate(
            "MainWindow", u"\u4f18\u5148\u7ea7", None))  #Central Table Column4 PRIORITY|第四列 优先级

        self.menu_Option.setTitle(QCoreApplication.translate(
            "MainWindow", u"\u8bbe\u7f6e", None))  # MENU1 OPTIONS|菜单1 设置
        self.menu_Lang.setTitle(QCoreApplication.translate(
            "MainWindow", u"\u8bed\u8a00|languages", None))  # MENU1 LANGUAGES|菜单2 语言
    # retranslateUi






