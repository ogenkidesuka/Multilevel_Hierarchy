# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multiagent_structure_main_win.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1103, 760)
        self.gridLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 261, 741))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit__maxSlaves = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit__maxSlaves.setObjectName("lineEdit__maxSlaves")
        self.gridLayout.addWidget(self.lineEdit__maxSlaves, 10, 1, 1, 1)
        self.label__maxSlaves = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label__maxSlaves.setObjectName("label__maxSlaves")
        self.gridLayout.addWidget(self.label__maxSlaves, 10, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 8, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 12, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        self.checkBox__recalculate_probs = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox__recalculate_probs.setObjectName("checkBox__recalculate_probs")
        self.gridLayout.addWidget(self.checkBox__recalculate_probs, 9, 0, 1, 1)
        self.lineEdit__treeDepth = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit__treeDepth.setObjectName("lineEdit__treeDepth")
        self.gridLayout.addWidget(self.lineEdit__treeDepth, 11, 1, 1, 1)
        self.label__nodesCoords = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label__nodesCoords.setObjectName("label__nodesCoords")
        self.gridLayout.addWidget(self.label__nodesCoords, 4, 0, 1, 1)
        self.lineEdit__nodeAmount = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit__nodeAmount.setObjectName("lineEdit__nodeAmount")
        self.gridLayout.addWidget(self.lineEdit__nodeAmount, 3, 1, 1, 1)
        self.label__System_nodeAmount = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label__System_nodeAmount.setObjectName("label__System_nodeAmount")
        self.gridLayout.addWidget(self.label__System_nodeAmount, 3, 0, 1, 1)
        self.tableWidget__nodesCoords = QtWidgets.QTableWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tableWidget__nodesCoords.sizePolicy().hasHeightForWidth())
        self.tableWidget__nodesCoords.setSizePolicy(sizePolicy)
        self.tableWidget__nodesCoords.setColumnCount(2)
        self.tableWidget__nodesCoords.setObjectName("tableWidget__nodesCoords")
        self.tableWidget__nodesCoords.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget__nodesCoords, 5, 0, 1, 2)
        self.label__treeDepth = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label__treeDepth.setObjectName("label__treeDepth")
        self.gridLayout.addWidget(self.label__treeDepth, 11, 0, 1, 1)
        self.label__head_addLimits = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label__head_addLimits.setObjectName("label__head_addLimits")
        self.gridLayout.addWidget(self.label__head_addLimits, 7, 0, 1, 1)
        self.pushButton__buildStructure = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton__buildStructure.setObjectName("pushButton__buildStructure")
        self.gridLayout.addWidget(self.pushButton__buildStructure, 13, 0, 1, 2)
        self.label__head_System = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label__head_System.setObjectName("label__head_System")
        self.gridLayout.addWidget(self.label__head_System, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 2)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(MainWindow)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(280, 10, 811, 741))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget__connectionsPower = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tableWidget__connectionsPower.sizePolicy().hasHeightForWidth())
        self.tableWidget__connectionsPower.setSizePolicy(sizePolicy)
        self.tableWidget__connectionsPower.setObjectName("tableWidget__connectionsPower")
        self.tableWidget__connectionsPower.setColumnCount(0)
        self.tableWidget__connectionsPower.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget__connectionsPower, 2, 0, 1, 1)
        self.label__connectionsPower = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label__connectionsPower.setObjectName("label__connectionsPower")
        self.gridLayout_2.addWidget(self.label__connectionsPower, 1, 0, 1, 1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dialog"))
        self.label__maxSlaves.setText(_translate("MainWindow", "Макс. количество дочерних узлов"))
        self.checkBox__recalculate_probs.setText(_translate("MainWindow", "Пересчитать силы соединения"))
        self.label__nodesCoords.setText(_translate("MainWindow", "Координаты узлов"))
        self.label__System_nodeAmount.setText(_translate("MainWindow", "Количество узлов"))
        self.label__treeDepth.setText(_translate("MainWindow", "Макс. глубина дерева"))
        self.label__head_addLimits.setText(_translate("MainWindow", "Дополнительные ограничения"))
        self.pushButton__buildStructure.setText(_translate("MainWindow", "Построить структуру"))
        self.label__head_System.setText(_translate("MainWindow", "Система"))
        self.label__connectionsPower.setText(_translate("MainWindow", "Матрица силы связи"))
