#NOT USED ANYMORE. HERE FOR REFERENCE

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


engine = create_engine('mysql://root:@localhost:3306/planit', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Users(Base):
   __tablename__ = 'users'

   id = Column(Integer, primary_key=True)
   name = Column(String(100))
   password = Column(String(100))
   email = Column(String(100))

   def __init__(self, name, password, email):
      self.name = name
      self.password = password
      self.email = email

   def __repr__(self):
      return "<User(%s, %s, %s>" % (self.name, self.password, self.email)


"""new_user = Users('vincent', 'password', 'fshit@me.com')
session.add(new_user)

session.commit()

for instance in session.query(Users.name):
   print instance.name"""

