import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum, DATE, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import func
import  time

engine = create_engine('mysql+pymysql://root:lieon1992316@localhost:3306/demo', echo=False)
Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    register_date = Column(DATE)

    # 打印该对象
    def __repr__(self):
        return "<User(name='%s', register_date='%s')>" % (
            self.name, self.register_date)

class StudentRecord(Base):
    __tablename__ = "study_record"
    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    status = Column(String    (32), nullable=False)
    stu_id = Column(Integer, ForeignKey('student.id'))

    student = relationship("Student", backref="my_study_record")

    def __repr__(self):
        return "<StudentRecord(name='%s', day='%s', status='%s', status='%d')>" % (self.student.name,self.day, self.status, self.stu_id)

Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# s1 = Student(name="lieon", register_date="2018-09-01")
# s2 = Student(name="lieo1", register_date="2018-09-02")
# s3 = Student(name="lieon2", register_date="2018-09-03")
# s4 = Student(name="lieon3", register_date="2018-09-04")
# s5 = Student(name="lieon4", register_date="2018-09-05")
#
# studyRecord0 = StudentRecord(day=1, status="yes", stu_id=2)
# studyRecord1 = StudentRecord(day=2, status="yes", stu_id=1)
# studyRecord2 = StudentRecord(day=4, status="false", stu_id=3)
# studyRecord3 = StudentRecord(day=5, status="yes", stu_id=4)
#
# session.add_all([s1, s2, s3, s4, s5, studyRecord0, studyRecord1, studyRecord2, studyRecord3])

stu_obj = session.query(Student).filter(Student.name=="lieon").first()
print(stu_obj.my_study_record)
session.commit()