# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agreement.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Agreement_Dialog(object):
    def setupUi(self, Agreement_Dialog):
        Agreement_Dialog.setObjectName("Agreement_Dialog")
        Agreement_Dialog.resize(728, 604)
        self.label = QtWidgets.QLabel(Agreement_Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Agreement_Dialog)
        self.textEdit.setGeometry(QtCore.QRect(40, 60, 411, 251))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.layoutWidget = QtWidgets.QWidget(Agreement_Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(173, 330, 271, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Yes = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Yes.setFont(font)
        self.pushButton_Yes.setObjectName("pushButton_Yes")
        self.horizontalLayout.addWidget(self.pushButton_Yes)
        self.pushButton_No = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_No.setFont(font)
        self.pushButton_No.setObjectName("pushButton_No")
        self.horizontalLayout.addWidget(self.pushButton_No)

        self.retranslateUi(Agreement_Dialog)
        self.pushButton_Yes.clicked.connect(Agreement_Dialog.accept) # type: ignore
        self.pushButton_No.clicked.connect(Agreement_Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Agreement_Dialog)

    def retranslateUi(self, Agreement_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Agreement_Dialog.setWindowTitle(_translate("Agreement_Dialog", "Dialog"))
        self.label.setText(_translate("Agreement_Dialog", "License agreement "))
        self.textEdit.setHtml(_translate("Agreement_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Serif\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">LOSAP Points Calculator</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Copyright (C) 2024  William A Coetzee</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">You should have received a copy of the GNU General Public License along with this program.  If not, see &lt;http://www.gnu.org/licenses/&gt;.</span></p></body></html>"))
        self.pushButton_Yes.setText(_translate("Agreement_Dialog", "I agree"))
        self.pushButton_No.setText(_translate("Agreement_Dialog", "I do not agree"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Agreement_Dialog = QtWidgets.QDialog()
    ui = Ui_Agreement_Dialog()
    ui.setupUi(Agreement_Dialog)
    Agreement_Dialog.show()
    sys.exit(app.exec_())