from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from collections import OrderedDict

# stuff for json dumps
from sqlalchemy.orm import class_mapper
from json import dumps


# SQL setup
engine = create_engine('mysql://root:gowild!!@localhost:3306/planit', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Users class for main user data
class Users(Base):
   __tablename__ = 'users'

   email = Column(String(100), primary_key=True)
   name = Column(String(100))
   password = Column(String(100))
   img_uri = Column(String(100))
   user_hash = Column(String(100))

   def __init__(self, name, password, email, img_uri, user_hash):
      self.name = name
      self.password = password
      self.email = email
      self.img_uri = img_uri
      self.user_hash = user_hash; 

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
   image_path = Column(String(100))
   location = Column(String(100))
   time = Column(String(100))
   creator = Column(String(100))

   def __init__(self, event_hash, title, description, image_path, location, time, creator):
      self.event_hash = event_hash
      self.title = title
      self.description = description
      self.image_path = image_path
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


# Events <-> Users map for correlation
class FriendsMap(Base):
   __tablename__ = 'friends_map'

   email = Column(String(100), primary_key=True)
   friend = Column(String(100))

   def __init__(self, email, friend):
      self.email = email
      self.friend = friend


   def __repr__(self):
      return "<FriendMap(%s, %s)" % (self.email, self.friend)



def serialize(Events):
   columns = [c.key for c in class_mapper(Events.__class__).columns]
   return dict((c, getattr(Events,c)) for c in columns)
