# -*- coding: utf-8 -*-
from function import P3dCfgOpr, P3dInfoSrc
import sys
from gui import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

columnContList = ['Active', 'Title', 'Local', 'Layer']

class MainClass():
    def __init__(self) -> None:  # 初始化GUI，不包括创建QApplication对象
        self.__qtObj = QMainWindow()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self.__qtObj)

    def fillTable(self) -> None:
        self.gui.tableWidgetC.clearContents()
        tableItemDict = {}
        tableItemDict = tableItemDict.fromkeys(columnContList, [])
        sceneCfgCont = P3dCfgOpr()
        self.gui.tableWidgetC.setRowCount(
            len(sceneCfgCont.sections()) - 1)
        for i in range(self.gui.tableWidgetC.rowCount()):
            for j in range(self.gui.tableWidgetC.columnCount()):
                if columnContList[j] == 'Active':
                    tableItemDict[columnContList[j]].insert(
                        i, TableCheckBoxWidget())
                    self.gui.tableWidgetC.setCellWidget(
                        i, j, tableItemDict[columnContList[j]][i])
                elif columnContList[j] == 'Layer':
                    tableItemDict[columnContList[j]].insert(i, QTableWidgetItem())
                    tableItemDict[columnContList[j]][i].setData(Qt.DisplayRole, int(sceneCfgCont.get((sceneCfgCont.sections())[i + 1], columnContList[j])))
                    self.gui.tableWidgetC.setItem(i, j, tableItemDict[columnContList[j]][i])
                else:
                    tableItemDict[columnContList[j]].insert(i, QTableWidgetItem())
                    tableItemDict[columnContList[j]][i].setText(sceneCfgCont.get((sceneCfgCont.sections())[i + 1], columnContList[j]))
                    self.gui.tableWidgetC.setItem(i, j, tableItemDict[columnContList[j]][i])

    def setVisible(self, TF: 'bool' = True) -> None:
        self.__qtObj.setVisible(TF)

if __name__ == '__main__':  # 负责启动窗口及一系列操作
    localP3dVerList = P3dInfoSrc.getInstedVerList()
    mainInfoSrc = P3dInfoSrc()
    __qtApp = QApplication(sys.argv)
    mainObj = MainClass()
    mainObj.gui.listWidgetL.setCurrentRow(0)
    mainObj.fillTable()
    mainObj.gui.tableWidgetC.selectRow(0)
    print(mainInfoSrc.getInstPath())



    mainObj.setVisible()
    # mainObj2 = MainClass()
    # mainObj2.setVisible()
    sys.exit(__qtApp.exec())