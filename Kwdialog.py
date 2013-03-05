# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/kwDialog.ui'
#
# Created: Fri Feb 22 09:42:55 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_KwDialog(object):
    def setupUi(self, KwDialog):
        KwDialog.setObjectName(_fromUtf8("KwDialog"))
        KwDialog.resize(400, 129)
        KwDialog.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(KwDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 90, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lineEdit = QtGui.QLineEdit(KwDialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 50, 301, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(KwDialog)
        self.label.setGeometry(QtCore.QRect(60, 30, 261, 21))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(KwDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), KwDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), KwDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(KwDialog)

    def retranslateUi(self, KwDialog):
        KwDialog.setWindowTitle(_translate("KwDialog", "Dialog", None))
        self.label.setText(_translate("KwDialog", "输入关键字，以逗号隔开", None))

