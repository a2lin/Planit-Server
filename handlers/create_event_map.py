import tornado.web
from data.db import *
from sqlalchemy import *

class CreateEventMapHandler(tornado.web.RequestHandler):
    def post(self):
       try:
         title = self.get_argument('title', '')
         description = self.get_argument('description', '')
         location = self.get_argument('location', '')
         time = self.get_argument('time', '')
         creator = self.get_argument('creator', '')

         event_hash = title + (str)(random.randint(0,1000000))
         
         #no duplicate users, invalid is true if user exists
         (invalid, ), = session.query(exists().where(Events.event_hash==event_hash))

         while invalid:
            event_hash = title + (str)(random.randint(0,1000000))
            (invalid, ), = session.query(exists().where(Events.event_hash==event_hash))

         new_event = Events(event_hash, title, description, location, time, creator)
         session.add(new_event)
         session.commit()

         self.write(event_hash)
         
       except:
         raise
         self.write("fuk")
