import orm_m2m
from sqlalchemy.orm import  sessionmaker

Session = sessionmaker(bind=orm_m2m.engine)
session = Session()

author0 = orm_m2m.Author(name="lieon0")
author1 = orm_m2m.Author(name="lieon1")
author2 = orm_m2m.Author(name="lieon2")
author3 = orm_m2m.Author(name="lieon3")

book0 = orm_m2m.Book(name="asdf",authors=[author0, author1])
book1 = orm_m2m.Book(name="we",authors=[author1, author2])
book2 = orm_m2m.Book(name="ew",authors=[author1, author3])

# session.add_all([author0, author1, author2, author3])
# session.add_all([book0, book1, book2])

author_obj = session.query(orm_m2m.Author).filter_by(name="lieon0").first()
print(author_obj, author_obj.books)

book_obj = session.query(orm_m2m.Book).filter_by(id=3).first()
print(book_obj, book_obj.authors)
book_obj.authors.remove()
session.commit()