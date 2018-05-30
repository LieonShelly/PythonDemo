# 多外键关联
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum, DATE, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import func
import  time

engine = create_engine('mysql+pymysql://root:lieon1992316@localhost:3306/demo', echo=False)
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    bill_address_id = Column(Integer, ForeignKey('address.id'))
    ship_address_id = Column(Integer, ForeignKey('address.id'))

    billing_address = relationship('Address', foreign_keys = [bill_address_id])
    shiping_address = relationship('Address',  foreign_keys = [ship_address_id])

    def __repr__(self):
        return "<Customer(name='%s')>" % (self.name)

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(64))

    def __repr__(self):
        return "<Address(street='%s')>" % (self.street)

Base.metadata.create_all(engine)