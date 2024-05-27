# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_windows.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(922, 421)
        MainWindow.setMinimumSize(QtCore.QSize(922, 421))
        MainWindow.setMaximumSize(QtCore.QSize(922, 421))
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(
            """
                QWidget{
                    background-color:rgb(255, 255, 255);
                }

                QMenu::item:selected{
                    background-color:rgb(235, 235, 235);
                    color: rgb(0, 0, 255);
                }
            """
        )
        self.centralwidget.setObjectName("centralwidget")

        self.original_sound = None
        self.converted_sound = None

        self.inputs_box = QtWidgets.QGroupBox(self.centralwidget)
        self.inputs_box.setEnabled(True)
        self.inputs_box.setGeometry(QtCore.QRect(760, 10, 151, 91))
        self.inputs_box.setObjectName("inputs_box")
        self.import_btn = None
        self.record_btn = None
        self.outputs_box = QtWidgets.QGroupBox(self.centralwidget)
        self.outputs_box.setGeometry(QtCore.QRect(760, 110, 151, 81))
        self.outputs_box.setObjectName("outputs_box")
        self.export_btn = None
        self.realtime_box = QtWidgets.QGroupBox(self.centralwidget)
        self.realtime_box.setGeometry(QtCore.QRect(760, 340, 151, 71))
        self.realtime_box.setObjectName("realtime_box")
        self.mic_pipeline_cbox = QtWidgets.QCheckBox(self.realtime_box)
        self.mic_pipeline_cbox.setGeometry(QtCore.QRect(40, 30, 81, 17))
        self.mic_pipeline_cbox.setChecked(True)
        self.mic_pipeline_cbox.setObjectName("mic_pipeline_cbox")
        self.actions_box = QtWidgets.QGroupBox(self.centralwidget)
        self.actions_box.setGeometry(QtCore.QRect(760, 200, 151, 131))
        self.actions_box.setObjectName("actions_box")
        self.norm_in_cbox = QtWidgets.QCheckBox(self.actions_box)
        self.norm_in_cbox.setGeometry(QtCore.QRect(30, 20, 101, 17))
        self.norm_in_cbox.setChecked(True)
        self.norm_in_cbox.setObjectName("norm_in_cbox")
        self.norm_out_cbox = QtWidgets.QCheckBox(self.actions_box)
        self.norm_out_cbox.setGeometry(QtCore.QRect(30, 40, 101, 17))
        self.norm_out_cbox.setChecked(True)
        self.norm_out_cbox.setObjectName("norm_out_cbox")
        self.convert_btn = None
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(30, 390, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.status.setFont(font)
        self.status.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.status.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.status.setTextFormat(QtCore.Qt.PlainText)
        self.status.setObjectName("status")
        self.status_icon = None
        self.movie = None
        self.config_btn = None
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Noise Reduction"))
        self.inputs_box.setTitle(_translate("MainWindow", "Inputs"))
        self.outputs_box.setTitle(_translate("MainWindow", "Outputs"))
        self.realtime_box.setTitle(_translate("MainWindow", "Realtime NS"))
        self.mic_pipeline_cbox.setText(_translate("MainWindow", "Microphone"))
        self.actions_box.setTitle(_translate("MainWindow", "Actions"))
        self.norm_in_cbox.setText(_translate("MainWindow", "Normalize input"))
        self.norm_out_cbox.setText(_translate("MainWindow", "Normalize output"))
        self.status.setText(_translate("MainWindow", "Status"))


import icons_rc
