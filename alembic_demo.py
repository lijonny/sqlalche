#coding:utf8
#date:2017.11.24
#使用alembic 代替sqlalchemy
from sqlalchemy import create_engine,Column,Integer,String,Text,DateTime,ForeignKey,Table
from sqlalchemy.ext.declarative import declarative_base
from  datetime import datetime
from sqlalchemy.orm import sessionmaker,relationship
HOST= '127.0.0.1'
DATABASE= 'articles'
USERNAME= 'root'
PASSWORD= '123456'
PORT='3306'
CHARSET= 'charset=utf8'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?{}'.format(USERNAME,PASSWORD,HOST,PORT,DATABASE,CHARSET)
print DB_URI
engine= create_engine(DB_URI)
Base = declarative_base(engine)
# with engine.connect() as con:
#     rs = con.execute('SELECT 1')
#     print rs.fetchone()
#article
#article 表
session = sessionmaker(engine)()
article_tag = Table('article_tags',Base.metadata,
                    Column('article_id',Integer,ForeignKey('articles.id')),
                    Column('tag_id',Integer,ForeignKey('tag.id')))
class Articles(Base):
    __tablename__='articles'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    detail = Column(Text,nullable=False)
    pu_time = Column(DateTime,default=datetime.now())
    uid = Column(Integer,ForeignKey('authors.id'))
    author = relationship('Author', backref='articles', lazy='select')
    tag = relationship('Tag',secondary=article_tag)
class Author(Base):
    __tablename__='authors'
    id =Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50),nullable=False,unique=True)
    def __repr__(self):
        return '<Author(id=%s,name=%s)>'%(self.id,self.name)
class Tag(Base):
    __tablename__='tag'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name =Column(String(50),nullable=False,unique=True)
    article =relationship('Articles',secondary=article_tag)
#Base.metadata.create_all()