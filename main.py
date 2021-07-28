# -*- coding: utf-8 -*-
from function import P3dCfgOpr
import sys
from typing import Optional
#import function
from gui import *
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import PySide6

if __name__ == '__main__':
    sceneryCfg = P3dCfgOpr()
    ckBoxList = []
    app_MainWindow = QApplication(sys.argv)
    obj_MainWindow = QMainWindow()
    gui_MainWindow = Ui_MainWindow()
    gui_MainWindow.setupUi(obj_MainWindow)

    #TEST PART|测试部分
    gui_MainWindow.tableWidget.setRowCount(len(sceneryCfg.sections()))
    for i in range(gui_MainWindow.tableWidget.rowCount()):
        ckBoxList.insert(i, TableCheckBoxWidget())
        gui_MainWindow.tableWidget.setCellWidget(i, 0, ckBoxList[i])
    
    #
    #gui_MainWindow.tableWidget.setCellWidget(0, 1, tableCheckBoxWidget)
    #TEST PART|测试部分
    obj_MainWindow.show()
    #print(ckBoxList)
    sys.exit(app_MainWindow.exec())


