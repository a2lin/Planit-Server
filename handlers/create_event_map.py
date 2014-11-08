import tornado.web
from data.db import *
from sqlalchemy import *

class CreateEventMapHandler(tornado.web.RequestHandler):
    def post(self):
       try:
         event_hash = self.get_argument('event_hash', '')
         email = self.get_argument('email', '')

         new_event_map = EventsMap(event_hash, email)
         session.add(new_event_map)
         session.commit()

         self.write(event_hash)
         
       except:
         raise
         self.write("fuk")
