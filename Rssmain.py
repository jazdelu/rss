# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/rssMain.ui'
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

class Ui_RssMain(object):
    def setupUi(self, RssMain):
        RssMain.setObjectName(_fromUtf8("RssMain"))
        RssMain.resize(680, 639)
        self.centralwidget = QtGui.QWidget(RssMain)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 681, 461))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 677, 457))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.resultListWidget = QtGui.QTreeWidget(self.scrollAreaWidgetContents)
        self.resultListWidget.setGeometry(QtCore.QRect(0, 0, 681, 461))
        self.resultListWidget.setObjectName(_fromUtf8("resultListWidget"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.importBtn = QtGui.QPushButton(self.centralwidget)
        self.importBtn.setEnabled(False)
        self.importBtn.setGeometry(QtCore.QRect(230, 520, 111, 41))
        self.importBtn.setObjectName(_fromUtf8("importBtn"))
        self.queryBtn = QtGui.QPushButton(self.centralwidget)
        self.queryBtn.setGeometry(QtCore.QRect(390, 520, 111, 41))
        self.queryBtn.setObjectName(_fromUtf8("queryBtn"))
        self.startBtn = QtGui.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(550, 520, 111, 41))
        self.startBtn.setObjectName(_fromUtf8("startBtn"))
        self.kwBtn = QtGui.QPushButton(self.centralwidget)
        self.kwBtn.setEnabled(False)
        self.kwBtn.setGeometry(QtCore.QRect(10, 520, 111, 41))
        self.kwBtn.setObjectName(_fromUtf8("kwBtn"))
        RssMain.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(RssMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        RssMain.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(RssMain)
        self.statusbar.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.statusbar.setMouseTracking(True)
        self.statusbar.setFocusPolicy(QtCore.Qt.TabFocus)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        RssMain.setStatusBar(self.statusbar)
        self.actionRSS = QtGui.QAction(RssMain)
        self.actionRSS.setObjectName(_fromUtf8("actionRSS"))
        self.actionSys = QtGui.QAction(RssMain)
        self.actionSys.setObjectName(_fromUtf8("actionSys"))
        self.actionQuit = QtGui.QAction(RssMain)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionKw = QtGui.QAction(RssMain)
        self.actionKw.setObjectName(_fromUtf8("actionKw"))
        self.actionAbout = QtGui.QAction(RssMain)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menu.addAction(self.actionRSS)
        self.menu.addAction(self.actionSys)
        self.menu.addAction(self.actionQuit)
        self.menu_2.addAction(self.actionAbout)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(RssMain)
        QtCore.QMetaObject.connectSlotsByName(RssMain)

    def retranslateUi(self, RssMain):
        RssMain.setWindowTitle(_translate("RssMain", "MainWindow", None))
        self.resultListWidget.headerItem().setText(0, _translate("RssMain", "标题", None))
        self.resultListWidget.headerItem().setText(1, _translate("RssMain", "URL", None))
        self.resultListWidget.headerItem().setText(2, _translate("RssMain", "发布日期", None))
        self.importBtn.setText(_translate("RssMain", "导入数据库", None))
        self.queryBtn.setText(_translate("RssMain", "查询数据库", None))
        self.startBtn.setText(_translate("RssMain", "开始采集", None))
        self.kwBtn.setText(_translate("RssMain", "关键字过滤", None))
        self.menu.setTitle(_translate("RssMain", "设置", None))
        self.menu_2.setTitle(_translate("RssMain", "帮助", None))
        self.statusbar.setStatusTip(_translate("RssMain", "准备就绪", None))
        self.actionRSS.setText(_translate("RssMain", "RSS源设置", None))
        self.actionSys.setText(_translate("RssMain", "系统设置", None))
        self.actionQuit.setText(_translate("RssMain", "退出", None))
        self.actionKw.setText(_translate("RssMain", "关键字设置", None))
        self.actionAbout.setText(_translate("RssMain", "关于", None))

