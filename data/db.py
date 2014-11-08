from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from collections import OrderedDict


# SQL setup
engine = create_engine('mysql://root:@localhost:3306/planit', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Users class for main user data
class Users(Base):
   __tablename__ = 'users'

   email = Column(String(100), primary_key=True)
   name = Column(String(100))
   password = Column(String(100))

   def __init__(self, name, password, email):
      self.name = name
      self.password = password
      self.email = email

   def __repr__(self):
      return "<User(%s, %s, %s>" % (self.name, self.password, self.email)


class DictSerializable():
   def _asdict(self):
      result = OrderedDict()
      for key in self.__mapper__.c.keys():
         result[key] = getattr(self, key)
      return result

# Events class for event data
class Events(Base, DictSerializable):
   __tablename__ = 'events'

   event_hash = Column(String(100), primary_key=True)
   title = Column(String(100))
   description = Column(String(100))
   location = Column(String(100))
   time = Column(String(100))
   creator = Column(String(100))

   def __init__(self, event_hash, title, description, location, time, creator):
      self.event_hash = event_hash
      self.title = title
      self.description = description
      self.location = location
      self.time = time
      self.creator = creator

   def __repr__(self):
      return "<Event(%s, %s, %s, %s, %s, %s>" % \
             (self.event_hash, self.title, self.description, self.location, self.time, self.creator)


# Events <-> Users map for correlation
class EventsMap(Base):
   __tablename__ = 'events_map'

   event_hash = Column(String(100), primary_key=True)
   email = Column(String(100))

   def __init__(self, event_hash, email):
      self.event_hash = event_hash
      self.email = email

   def __repr__(self):
      return "<EventMap(%s, %s)" % (self.event_hash, self.email)


