# 多对多

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum, DATE, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import func, Table
import  time


engine = create_engine('mysql+pymysql://root:lieon1992316@localhost:3306/demo', echo=False)
Base = declarative_base()

book_m2m_author = Table('book_m2m_author', Base.metadata,
                        Column('book_id', Integer, ForeignKey('book.id')),
                        Column('author_id', Integer, ForeignKey('author.id')),
                        )

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    authors = relationship('Author', secondary=book_m2m_author, backref='books')


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)

Base.metadata.create_all(engine)