# -*- coding: utf-8 -*-
from function import P3dCfgOpr, P3dInfoSrc
import sys
from gui import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

columnContList = ['Active', 'Title', 'Local', 'Layer']

if __name__ == '__main__':
    tableItemDict = {}
    tableItemDict = tableItemDict.fromkeys(columnContList, [])

    sceneCfgCont = P3dCfgOpr()
    app_MainWindow = QApplication(sys.argv)
    obj_MainWindow = QMainWindow()
    gui_MainWindow = Ui_MainWindow()
    gui_MainWindow.setupUi(obj_MainWindow)

    # TEST PART|测试部分
    # gui_MainWindow.tableWidget.setRowCount(
    #     len(sceneCfgCont.sections()) - 1)
    # for i in range(gui_MainWindow.tableWidget.rowCount()):
    #     for j in range(gui_MainWindow.tableWidget.columnCount()):
    #         if j == 0:
    #             tableItemDict[columnContList[j]].insert(
    #                 i, TableCheckBoxWidget())
    #             gui_MainWindow.tableWidget.setCellWidget(
    #                 i, j, tableItemDict[columnContList[j]][i])
    #         else:
    #             tableItemDict[columnContList[j]].insert(i, QTableWidgetItem())
    #             tableItemDict[columnContList[j]][i].setText(sceneCfgCont.get(
    #                 (sceneCfgCont.sections())[i + 1], columnContList[j]))
    #             gui_MainWindow.tableWidget.setItem(
    #                 i, j, tableItemDict[columnContList[j]][i])
    print(P3dInfoSrc.getInstedVerList())
    # TEST PART|测试部分
    obj_MainWindow.show()
    sys.exit(app_MainWindow.exec())
