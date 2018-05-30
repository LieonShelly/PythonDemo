import orm_mfk
from sqlalchemy.orm import  sessionmaker

Session = sessionmaker(bind=orm_mfk.engine)
session = Session()

addr1 = orm_mfk.Address(street="adsfad")
addr2 = orm_mfk.Address(street="123")
addr3 = orm_mfk.Address(street="2321asd")

c1 = orm_mfk.Customer(name="jack", billing_address = addr1, shiping_address=addr2)
c2 = orm_mfk.Customer(name="lieon", billing_address = addr2, shiping_address=addr3)


# session.add_all([addr1, addr2, addr3, c1, c2])

obj = session.query(orm_mfk.Customer).filter_by(name="lieon").first()
print(obj.name, obj.billing_address, obj.shiping_address)
session.commit()