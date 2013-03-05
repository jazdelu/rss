# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/sysDialog.ui'
#
# Created: Fri Feb 22 09:42:56 2013
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

class Ui_SysDialog(object):
    def setupUi(self, SysDialog):
        SysDialog.setObjectName(_fromUtf8("SysDialog"))
        SysDialog.resize(400, 337)
        SysDialog.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(SysDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 290, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.dbAddrEdit = QtGui.QLineEdit(SysDialog)
        self.dbAddrEdit.setGeometry(QtCore.QRect(170, 40, 191, 20))
        self.dbAddrEdit.setObjectName(_fromUtf8("dbAddrEdit"))
        self.dbNameEdit = QtGui.QLineEdit(SysDialog)
        self.dbNameEdit.setGeometry(QtCore.QRect(170, 90, 191, 20))
        self.dbNameEdit.setObjectName(_fromUtf8("dbNameEdit"))
        self.label = QtGui.QLabel(SysDialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 71, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(SysDialog)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 61, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.dbPswdEdit = QtGui.QLineEdit(SysDialog)
        self.dbPswdEdit.setGeometry(QtCore.QRect(170, 190, 191, 20))
        self.dbPswdEdit.setText(_fromUtf8(""))
        self.dbPswdEdit.setObjectName(_fromUtf8("dbPswdEdit"))
        self.label_3 = QtGui.QLabel(SysDialog)
        self.label_3.setGeometry(QtCore.QRect(50, 190, 61, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(SysDialog)
        self.label_4.setGeometry(QtCore.QRect(50, 240, 61, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.dbPortEdit = QtGui.QLineEdit(SysDialog)
        self.dbPortEdit.setGeometry(QtCore.QRect(170, 240, 191, 20))
        self.dbPortEdit.setText(_fromUtf8(""))
        self.dbPortEdit.setObjectName(_fromUtf8("dbPortEdit"))
        self.label_5 = QtGui.QLabel(SysDialog)
        self.label_5.setGeometry(QtCore.QRect(50, 140, 61, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.dbUserEdit = QtGui.QLineEdit(SysDialog)
        self.dbUserEdit.setGeometry(QtCore.QRect(170, 140, 191, 20))
        self.dbUserEdit.setObjectName(_fromUtf8("dbUserEdit"))

        self.retranslateUi(SysDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SysDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SysDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SysDialog)

    def retranslateUi(self, SysDialog):
        SysDialog.setWindowTitle(_translate("SysDialog", "Dialog", None))
        self.label.setText(_translate("SysDialog", "数据库地址", None))
        self.label_2.setText(_translate("SysDialog", "数据库名称", None))
        self.label_3.setText(_translate("SysDialog", "密码", None))
        self.label_4.setText(_translate("SysDialog", "端口", None))
        self.label_5.setText(_translate("SysDialog", "用户名", None))

