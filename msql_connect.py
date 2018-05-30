import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum, DATE
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import  time

engine = create_engine('mysql+pymysql://root:lieon1992316@localhost:3306/demo', echo=False)
Base = declarative_base()

class User(Base):
    __tablename__ = 'test_user'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    fullname = Column(String(64))
    password = Column(String(64))

    # 打印该对象
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)



class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    register_date = Column(DATE)
    sex = Column(Enum("M", "F"))

    # 打印该对象
    def __repr__(self):
        return "<User(name='%s', register_date='%s', sex='%s')>" % (
            self.name, self.register_date, self.sex)

Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# 增加数据
ed_user = User()
ed_user.name = "lieon"
ed_user.fullname = "lieon lee"
ed_user.password = "lieon1992316"
# session.add(ed_user)

student = Student()
student.name = "test"
student.register_date = "2018-09-09"
student.sex = "M"
# session.add(student)

# 查数据
quryUser = session.query(User).filter_by(name='lieon').first()
print(quryUser)
# Querying with Joins
print(session.query(User, Student).filter(User.id == Student.id).all())
#统计
print(session.query(User).filter(User.name.like('li%')).count())
#分组
print(session.query(func.count(User.name), User.name).group_by(User.name).all())
# 改数据
quryUser.password = "21321qw";

session.commit()

# | id | name  | register_date | sex  |

