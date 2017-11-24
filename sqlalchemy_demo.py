#coding:utf8
import sqlalchemy
from sqlalchemy import create_engine,Column,Integer,String,Text,DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from  datetime import datetime
from sqlalchemy.orm import sessionmaker,relationship
HOST= '127.0.0.1'
DATABASE= 'sqlalchemy'
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
class Articles(Base):
    __tablename__='articles'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    detail = Column(Text,nullable=False)
    pu_time = Column(DateTime,default=datetime.now())
    uid = Column(Integer,ForeignKey('authors.id'))
    author = relationship('Author', backref='articles', lazy='select')

class Author(Base):
    __tablename__='authors'
    id =Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50),nullable=False,unique=True)
    def __repr__(self):
        return '<Author(id=%s,name=%s)>'%(self.id,self.name)
Base.metadata.create_all()
# article = Articles(id=5)
# print article.author
# author = session.query(Author).first()
# print author.article[1]
#print session.query(Author).filter(Author.name==u'李白').all()

#author = Author(name='jonny')
# articles =Articles(title='123',detail='testdetail',uid=1)
# session.add(articles)
# session.commit()
#if __name__ =='__main__':
#    print



