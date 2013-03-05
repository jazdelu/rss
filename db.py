from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship, backref
import ConfigParser
Base = declarative_base()

class Source(Base):
	__tablename__ = 'source'

	id = Column(Integer, Sequence('source_id_seq'), primary_key = True)
	name = Column(String(50))
	url = Column(String(50))

	def __init__(self, name , url):
		self.name=name
		self.url=url

	def __repr__(self):
		return '<Source(%r,%r,%r)>' % (self.id, self.name, self.url)

class News(Base):
	__tablename__ = 'News'

	id = Column(Integer, Sequence('news_id_seq'), primary_key = True)
	title = Column(String(50))
	url = Column(String(100))
	content = Column(Text)
	source_id = Column(Integer, ForeignKey('source.id'))
	source = relationship('Source', backref=backref('News',order_by=id))
	date = Column(Date)

	def __init__(self,title,url,content,date):
		self.title=title
		self.url=url
		self.content=content
		self.date=date

	def __repr__(self):
		return 'News<%s,%s>' % (self.title, self.url)

class Keyword(Base):
	__tablename__='Keyword'

	id = Column(Integer, Sequence('keyword_id_seq'), primary_key = True)
	keyword=Column(String(50))

	def __init__(self,keyword):
		self.keyword=keyword

	def __repr__(self):
		return 'Keyword<%s>' % (self.keyword)


class DB():
	
	config  = ConfigParser.ConfigParser()
	config.readfp(open('rss.ini'))
	Session = sessionmaker()
	engine = create_engine('mysql://%s:%s@%s:%s/%s?charset=%s' % (config.get('db','user'),
		config.get('db','password'),
		config.get('db','host'),
		config.get('db','port'),
		config.get('db','db'),'utf8'),echo=True)
	Session.configure(bind=engine)
	session = Session()

	def __init__(self,config):
		self.config = config









