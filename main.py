#coding=utf-8
from PyQt4 import QtGui, QtCore
import sys, re, codecs
import ConfigParser
import feedparser
import Rssmain, Rssdialog, Sysdialog, Kwdialog
from db import DB, Source, News
import time
class MainDialog(QtGui.QMainWindow):
	def __init__(self):
		super(MainDialog,self).__init__()
		self.mainUI=Rssmain.Ui_RssMain()
		self.mainUI.setupUi(self)
		self.mainUI.kwBtn.setEnabled(False)
		self.connect(self.mainUI.actionRSS, QtCore.SIGNAL('triggered()'),self.openRD)
		self.connect(self.mainUI.actionSys, QtCore.SIGNAL('triggered()'),self.openSD)
		self.connect(self.mainUI.kwBtn, QtCore.SIGNAL('clicked()'),self.openKD)
		self.connect(self.mainUI.startBtn, QtCore.SIGNAL('clicked()'),self.showNews)


		self.ui_rd=Rssdialog.Ui_RssDialog()
		self.ui_sd=Sysdialog.Ui_SysDialog()
		self.ui_kd=Kwdialog.Ui_KwDialog()

		self.config = ConfigParser.ConfigParser()
		self.config.readfp(codecs.open('rss.ini','r+','utf-8-sig'))
		self.d = DB(self.config)

		self.news=[]
		

	def openRD(self):
		d = QtGui.QDialog()
		self.ui_rd.setupUi(d)
		d.connect(self.ui_rd.addBtn,QtCore.SIGNAL('clicked()'),self.addRSS)
		d.connect(self.ui_rd.delBtn,QtCore.SIGNAL('clicked()'),self.delRSS)
		d.connect(self.ui_rd.closeBtn,QtCore.SIGNAL('clicked()'),QtCore.SLOT('close()'))
		for row in self.d.session.query(Source.url).all():
			self.ui_rd.rssListWidget.addItem(QtGui.QListWidgetItem(row.url))
		d.exec_()

	def addRSS(self):
		r=self.ui_rd.rssAddrEdit.text()
		p=re.compile(r'^.+/\w+.xml$')
		if r.find('rss') != -1:
			f=feedparser.parse(str(r)).feed
			try:
				self.d.session.add(Source(f.title,str(r)))
				self.d.session.commit()
				self.ui_rd.rssListWidget.addItem(QtGui.QListWidgetItem(str(r)))	
			except:
				self.showError('URL exists')
				self.d.session.flush()
		else:
			print 'address error'

	def delRSS(self):
		si=self.ui_rd.rssListWidget.selectedItems()
		for i in si:
			self.ui_rd.rssListWidget.takeItem(self.ui_rd.rssListWidget.row(i))
			self.d.session.query(Source).filter_by(url=i.text()).delete()
			self.d.session.commit()

	def openSD(self):
		d = QtGui.QDialog()
		self.ui_sd.setupUi(d)
		self.ui_sd.dbAddrEdit.setText(self.config.get('db', 'host'))
		self.ui_sd.dbNameEdit.setText(self.config.get('db', 'db'))
		self.ui_sd.dbUserEdit.setText(self.config.get('db', 'user'))
		self.ui_sd.dbPswdEdit.setText(self.config.get('db', 'password'))
		self.ui_sd.dbPortEdit.setText(self.config.get('db', 'port'))
		if d.exec_():
			self.config.set('db','host',self.ui_sd.dbAddrEdit.text())
			self.config.set('db','db',self.ui_sd.dbNameEdit.text())
			self.config.set('db','user',self.ui_sd.dbUserEdit.text())
			self.config.set('db','password',self.ui_sd.dbPswdEdit.text())
			self.config.set('db','port', self.ui_sd.dbPortEdit.text())
			self.config.write(open('rss.ini','r+'))
	def openKD(self):
		d = QtGui.QDialog()
		self.ui_kd.setupUi(d)
		s=''
		for row in self.d.session.query(Keyword.keyword).all():
			s=row.keyword+','

		self.ui_kd.lineEdit.setText(s)
		if d.exec_():
			for k in s.split(','):
				try:
					self.d.session.add(Keyword(k))
					self.d.session.commit()
				except:
					pass


	def showError(self,s):
		QtGui.QMessageBox.warning(self,'Error',s)

	def showNews(self):
		sources=self.d.session.query(Source.url).all()
		self.mainUI.resultListWidget.clear()
		for s in sources:
			r=s.url
			f=feedparser.parse(str(r))
			for entry in f.entries:
					news.append((entry.title,entry.link,entry.description,entry.published_parsed,f.feed.title))
					item = QtGui.QTreeWidgetItem(self.mainUI.resultListWidget)
					item.setText(0,entry.title)
					item.setText(1,entry.link)
					item.setText(2,time.asctime(entry.published_parsed))

		self.mainUI.kwBtn.setEnabled(True)
		self.mainUI.importBtn.setEnabled(True)


def main():   

	app = QtGui.QApplication(sys.argv)
	md = MainDialog()
	md.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()