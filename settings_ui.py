# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(806, 640)
        font = QtGui.QFont()
        font.setPointSize(12)
        Settings.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(Settings)
        self.buttonBox.setGeometry(QtCore.QRect(360, 590, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(Settings)
        self.widget.setGeometry(QtCore.QRect(10, 10, 781, 571))
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.iar_rows_to_skip_d = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.iar_rows_to_skip_d.setFont(font)
        self.iar_rows_to_skip_d.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.iar_rows_to_skip_d.setInputMethodHints(QtCore.Qt.ImhNone)
        self.iar_rows_to_skip_d.setInputMask("")
        self.iar_rows_to_skip_d.setText("2")
        self.iar_rows_to_skip_d.setMaxLength(3)
        self.iar_rows_to_skip_d.setPlaceholderText("")
        self.iar_rows_to_skip_d.setObjectName("iar_rows_to_skip_d")
        self.verticalLayout.addWidget(self.iar_rows_to_skip_d)
        self.iamr_rows_end_d = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.iamr_rows_end_d.setFont(font)
        self.iamr_rows_end_d.setObjectName("iamr_rows_end_d")
        self.verticalLayout.addWidget(self.iamr_rows_end_d)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 2, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.losap_sheet_d = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.losap_sheet_d.setFont(font)
        self.losap_sheet_d.setObjectName("losap_sheet_d")
        self.verticalLayout_2.addWidget(self.losap_sheet_d)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.losap_name_pos_d = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.losap_name_pos_d.setFont(font)
        self.losap_name_pos_d.setObjectName("losap_name_pos_d")
        self.gridLayout_2.addWidget(self.losap_name_pos_d, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.losap_SR_Signups_d = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.losap_SR_Signups_d.setFont(font)
        self.losap_SR_Signups_d.setObjectName("losap_SR_Signups_d")
        self.gridLayout_2.addWidget(self.losap_SR_Signups_d, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.losap_SR_Calls_d = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.losap_SR_Calls_d.setFont(font)
        self.losap_SR_Calls_d.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.losap_SR_Calls_d.setObjectName("losap_SR_Calls_d")
        self.gridLayout_2.addWidget(self.losap_SR_Calls_d, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1, QtCore.Qt.AlignRight)
        self.losap_rows_to_skip_d = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.losap_rows_to_skip_d.setFont(font)
        self.losap_rows_to_skip_d.setObjectName("losap_rows_to_skip_d")
        self.gridLayout_2.addWidget(self.losap_rows_to_skip_d, 4, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.label_10 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_11 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.output_file_name_d = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.output_file_name_d.setFont(font)
        self.output_file_name_d.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.output_file_name_d.setObjectName("output_file_name_d")
        self.verticalLayout_3.addWidget(self.output_file_name_d)
        self.output_worksheet_name_d = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.output_worksheet_name_d.setFont(font)
        self.output_worksheet_name_d.setObjectName("output_worksheet_name_d")
        self.verticalLayout_3.addWidget(self.output_worksheet_name_d)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 1, 2, 1)
        self.label_12 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.retranslateUi(Settings)
        self.buttonBox.accepted.connect(Settings.accept) # type: ignore
        self.buttonBox.rejected.connect(Settings.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Dialog"))
        self.label_3.setText(_translate("Settings", "For the \'I am responding\' Export file"))
        self.label.setText(_translate("Settings", "Rows to skip"))
        self.iar_rows_to_skip_d.setAccessibleName(_translate("Settings", "self.iamr_rows_to_skip_edit"))
        self.iamr_rows_end_d.setText(_translate("Settings", "251"))
        self.label_2.setText(_translate("Settings", "Stop reading at row"))
        self.label_6.setText(_translate("Settings", "The CVAC Excel Spreadsheets"))
        self.label_4.setText(_translate("Settings", "Worksheet name"))
        self.losap_sheet_d.setText(_translate("Settings", "point tracker"))
        self.label_7.setText(_translate("Settings", "Position of the person\'s name"))
        self.losap_name_pos_d.setText(_translate("Settings", "D4"))
        self.label_8.setText(_translate("Settings", "Position of the self-reported signup hours"))
        self.losap_SR_Signups_d.setText(_translate("Settings", "E7"))
        self.label_5.setText(_translate("Settings", "Position of the self-reported call hours"))
        self.losap_SR_Calls_d.setAccessibleName(_translate("Settings", "self.iamr_rows_to_skip_edit"))
        self.losap_SR_Calls_d.setText(_translate("Settings", "E8"))
        self.label_9.setText(_translate("Settings", "Skip this number of rows before reading data"))
        self.losap_rows_to_skip_d.setText(_translate("Settings", "10"))
        self.label_10.setText(_translate("Settings", "The Output Excel Spreadsheet"))
        self.label_11.setText(_translate("Settings", "Ouput file name (.xlsx will be added)"))
        self.output_file_name_d.setAccessibleName(_translate("Settings", "self.iamr_rows_to_skip_edit"))
        self.output_file_name_d.setText(_translate("Settings", "2024-01 Points Summary"))
        self.output_worksheet_name_d.setText(_translate("Settings", "Points"))
        self.label_12.setText(_translate("Settings", "Worksheet name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Settings = QtWidgets.QDialog()
    ui = Ui_Settings()
    ui.setupUi(Settings)
    Settings.show()
    sys.exit(app.exec_())
