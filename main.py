# -*- coding: utf-8 -*-
from function import P3dCfgOpr, P3dInfoSrc
import sys
from gui import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

columnContList = ['Active', 'Title', 'Local', 'Layer']
localP3dVerList = P3dInfoSrc.getInstedVerList()

class MainClass():  # 主类，GUI相关操作暂时也放这
    def __init__(self) -> None:  # 初始化操作，不包括创建QApplication对象
        self.infoSrc = P3dInfoSrc()
        self.sceneCfgOpr = P3dCfgOpr()
        self.__qtObj = QMainWindow()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self.__qtObj)


    def setVisible(self, TF: 'bool' = True) -> None:
        self.__qtObj.setVisible(TF)


    def fillTable(self) -> None:
        self.gui.tableWidgetC.clearContents()
        tableItemDict = {}
        tableItemDict = tableItemDict.fromkeys(columnContList, [])
        # self.sceneCfgOpr = P3dCfgOpr()
        self.gui.tableWidgetC.setRowCount(
            len(self.sceneCfgOpr.sections()) - 1)
        for i in range(self.gui.tableWidgetC.rowCount()):
            for j in range(self.gui.tableWidgetC.columnCount()):
                if columnContList[j] == 'Active':
                    self.__initCkBoxCell(tableItemDict[columnContList[j]], i, j)
                    # tableItemDict[columnContList[j]].insert(i, (TableCheckBoxWidget(), QTableWidgetItem()))
                    # self.setCkBoxState(tableItemDict[columnContList[j]][i][0], sceneCfgCont.get((sceneCfgCont.sections())[i + 1], 'Active'), sceneCfgCont.get((sceneCfgCont.sections())[i + 1], 'Required'))
                    # self.gui.tableWidgetC.setCellWidget(i, j, tableItemDict[columnContList[j]][i][0])
                elif columnContList[j] == 'Layer':
                    tableItemDict[columnContList[j]].insert(i, QTableWidgetItem())
                    tableItemDict[columnContList[j]][i].setData(Qt.DisplayRole, int(self.sceneCfgOpr.get((self.sceneCfgOpr.sections())[i + 1], columnContList[j])))
                    self.gui.tableWidgetC.setItem(i, j, tableItemDict[columnContList[j]][i])
                else:
                    tableItemDict[columnContList[j]].insert(i, QTableWidgetItem())
                    tableItemDict[columnContList[j]][i].setText(self.sceneCfgOpr.get((self.sceneCfgOpr.sections())[i + 1], columnContList[j]))
                    self.gui.tableWidgetC.setItem(i, j, tableItemDict[columnContList[j]][i])


    def setCkCellState(self, columnSet:set, actStr:str = 'FALSE', reqStr:str = 'FALSE'):
        if actStr.upper() == 'TRUE':
            columnSet[0].tableCheckBox.setChecked(True)
            columnSet[1].setText('b')
            if reqStr.upper() == 'TRUE':
                columnSet[0].tableCheckBox.setDisabled(True)
                columnSet[1].setText('c')
            elif reqStr.upper() == 'FALSE':
                columnSet[0].tableCheckBox.setDisabled(False)
        elif actStr.upper() == 'FALSE':
            columnSet[0].tableCheckBox.setChecked(False)
            columnSet[1].setText('a')



    def __initCkBoxCell(self, list:list, row:int, column:int):
        __font = QFont()
        __font.setPointSize(1)
        
        list.insert(row, (TableCheckBoxWidget(), QTableWidgetItem()))
        list[row][1].setData(Qt.FontRole, __font)

        list[row][1].setTextAlignment(Qt.AlignCenter)
        self.gui.tableWidgetC.setItem(row, column, list[row][1])
        self.setCkCellState(list[row], self.sceneCfgOpr.get((self.sceneCfgOpr.sections())[row + 1], 'Active'), self.sceneCfgOpr.get((self.sceneCfgOpr.sections())[row + 1], 'Required'))
        self.gui.tableWidgetC.setCellWidget(row, column, list[row][0])






if __name__ == '__main__':  # 负责启动窗口及一系列操作
    mainInfoSrc = P3dInfoSrc()
    __qtApp = QApplication(sys.argv)
    mainObj = MainClass()
    mainObj.gui.listWidgetL.setCurrentRow(0)
    mainObj.fillTable()
    mainObj.gui.tableWidgetC.selectRow(0)
    print(mainInfoSrc.getInstPath())



    mainObj.setVisible()
    sys.exit(__qtApp.exec())