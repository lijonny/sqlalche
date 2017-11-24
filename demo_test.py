#coding:utf8
from sqlalchemy import Column,create_engine,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
HOST= '127.0.0.1'
DATABASE= 'sqlalchemy'
USERNAME= 'root'
PASSWORD= '123456'
PORT='3306'
CHARSET= 'charset=utf8'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?{}'.format(USERNAME,PASSWORD,HOST,PORT,DATABASE,CHARSET)
engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()
class User(Base):
    __tablename__ ='users'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username= Column(String(100),nullable=False)
    password=Column(String(100),nullable=False)
    gender = Column(Integer)
    user_extend=relationship('UserExtend',uselist=False,lazy='select')
    def __repr__(self):
        return '<User(id="%s",username="%s",password="%s")>'%(self.id,self.username,self.password)
#表的关系
#一对多
class Address(Base):
    __tablename__='address'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(100),nullable=False)
    #ForeignKey连接外键
    uid  = Column(Integer,ForeignKey('users.id'))
    user = relationship('User',backref='addresses',lazy='select')
# for i in range(10):
#     user = User(username='user%s'%i,password='123456',gender='1')
#     session.add(user)
#session.commit()
class UserExtend(Base):
    __tablename__='user_extend'
    id = Column(Integer,primary_key=True,autoincrement=True)
    school = Column(String(100),nullable=False)
    uid = Column(Integer,ForeignKey('users.id'))
    user = relationship('User',lazy='select')


address = Address(name = '河北省')
user =session.query(User).first()
# user.addresses.append(address)
# print user
# session.commit()
user_extend=UserExtend(school=u'北京航空航天')
user.user_extend=user_extend
session.commit()
# CREATE TABLE `address` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `name` varchar(100) NOT NULL,
#   `uid` int(11) DEFAULT NULL,
#   PRIMARY KEY (`id`),
#   KEY `uid` (`uid`),
#   CONSTRAINT `address_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `users` (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8
Base.metadata.create_all()

#