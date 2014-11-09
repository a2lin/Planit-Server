import tornado.web
from data.db import *
from sqlalchemy import *
import random


class EditEventHandler(tornado.web.RequestHandler):
    def post(self):
       try:
         event_hash = self.get_argument('event_hash', '')
         creator = self.get_argument('creator', '')

         title = self.get_argument('title', '')
         description = self.get_argument('description', '')
         location = self.get_argument('location', '')
         time = self.get_argument('time', '')
         
         #checks if event changer is creator
         (valid, ), = session.query(exists().where(Events.event_hash==event_hash).
                                             where(Events.creator==creator))

         if valid:
            event = session.query(Events).filter(Events.event_hash==event_hash).first()
            if title:
               event.title = title
            if description:
               event.description = description
            if location:
               event.location = location
            if time:
               event.time = time
            session.commit()
            self.write("1")
         else:
            self.write("-1")
       except:
         raise
         self.write("fuk")

         

        
       '''  #no duplicate users, invalid is true if user exists
         (invalid, ), = session.query(exists().where(Events.event_hash==event_hash))

         while invalid:
            event_hash = title + (str)(random.randint(0,1000000))
            (invalid, ), = session.query(exists().where(Events.event_hash==event_hash))

         new_event = Events(event_hash, title, description, location, time, creator)
         new_event_map = EventsMap(event_hash, creator)
         session.add(new_event)
         session.add(new_event_map)
         session.commit()

         self.write(event_hash)
         
       except:
         raise
         self.write("fuk")'''

"""class CreateEventHandler(tornado.web.RequestHandler):
   def post(self):
      try:
         #fetching existing and input data
         title = self.get_argument('title', '')
         description = self.get_argument('description', '')
         location = self.get_argument('location', '')
         creator = self.get_argument('creator', '')

         event_hash = title + (str)(random.randrange(0,1000000)

         invalid =  session.query(exists().where(Events.event_hash==event_hash))

         while invalid:
            event_hash = title + (str)(random.randrange(0,1000000)
            (invalid, ), = session.query(exists().where(Events.event_hash==event_hash))

         new_event = Events(event_hash, title, description, location, creator)
         session.add(new_event)
         session.commit()

         self.write(event_hash)

      except:
         raise
         self.write("you fat-fingered the board again, didn't you bob")"""
