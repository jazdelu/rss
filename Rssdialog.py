# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/rssDialog.ui'
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

class Ui_RssDialog(object):
    def setupUi(self, RssDialog):
        RssDialog.setObjectName(_fromUtf8("RssDialog"))
        RssDialog.setEnabled(True)
        RssDialog.resize(398, 330)
        RssDialog.setSizeGripEnabled(False)
        RssDialog.setModal(True)
        self.label = QtGui.QLabel(RssDialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 171, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.scrollArea = QtGui.QScrollArea(RssDialog)
        self.scrollArea.setGeometry(QtCore.QRect(20, 120, 261, 131))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 259, 129))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.rssListWidget = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.rssListWidget.setGeometry(QtCore.QRect(0, 0, 261, 131))
        self.rssListWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.rssListWidget.setObjectName(_fromUtf8("rssListWidget"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_2 = QtGui.QLabel(RssDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.delBtn = QtGui.QPushButton(RssDialog)
        self.delBtn.setGeometry(QtCore.QRect(294, 120, 75, 23))
        self.delBtn.setObjectName(_fromUtf8("delBtn"))
        self.addBtn = QtGui.QPushButton(RssDialog)
        self.addBtn.setGeometry(QtCore.QRect(295, 50, 75, 23))
        self.addBtn.setObjectName(_fromUtf8("addBtn"))
        self.rssAddrEdit = QtGui.QLineEdit(RssDialog)
        self.rssAddrEdit.setGeometry(QtCore.QRect(21, 50, 261, 20))
        self.rssAddrEdit.setObjectName(_fromUtf8("rssAddrEdit"))
        self.closeBtn = QtGui.QPushButton(RssDialog)
        self.closeBtn.setGeometry(QtCore.QRect(290, 280, 75, 23))
        self.closeBtn.setObjectName(_fromUtf8("closeBtn"))

        self.retranslateUi(RssDialog)
        QtCore.QMetaObject.connectSlotsByName(RssDialog)

    def retranslateUi(self, RssDialog):
        RssDialog.setWindowTitle(_translate("RssDialog", "Dialog", None))
        self.label.setText(_translate("RssDialog", "输入rss源地址", None))
        self.label_2.setText(_translate("RssDialog", "rss源", None))
        self.delBtn.setText(_translate("RssDialog", "删除", None))
        self.addBtn.setText(_translate("RssDialog", "添加", None))
        self.closeBtn.setText(_translate("RssDialog", "关闭", None))

