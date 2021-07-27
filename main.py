# -*- coding: utf-8 -*-
import sys
from typing import Optional
#import function
from gui import Ui_MainWindow
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import PySide6

if __name__ == '__main__':
    app_MainWindow = QApplication(sys.argv)
    obj_MainWindow = QMainWindow()
    gui_MainWindow = Ui_MainWindow()
    gui_MainWindow.setupUi(obj_MainWindow)
    obj_MainWindow.show()

    #TEST PART|测试部分
    tableCheckBox = QCheckBox()
    tableCheckBoxLayout = QVBoxLayout()
    tableCheckBoxWidget = QWidget()
    tableCheckBoxWidget.setLayout(tableCheckBoxLayout)
    tableCheckBoxLayout.addWidget(tableCheckBox)
    tableCheckBoxLayout.setAlignment(tableCheckBox, Qt.AlignCenter)
    
    gui_MainWindow.tableWidget.setCellWidget(0, 0, tableCheckBoxWidget)
    #TEST PART|测试部分
    sys.exit(app_MainWindow.exec())


