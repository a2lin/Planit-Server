import tornado.web
from data.db import *
from sqlalchemy import *

class CreateEventMapHandler(tornado.web.RequestHandler):
    def post(self):
       try:
         event_hash = self.get_argument('event_hash', '')
         email = self.get_argument('email', '')

         (validEmail, ), = session.query(exists().where(Users.email==email)) 
         (validEvent, ), = session.query(exists().where(Events.event_hash==event_hash)) 

         if not validEmail:
            self.write("-1")
            return
         if not validEvent:
            self.write("-2")
            return

         (invalid, ), = session.query(exists().where(EventsMap.event_hash==event_hash)
                                              .where(EventsMap.email==email))
         if invalid:
            self.write("-3")
            return

         new_event_map = EventsMap(event_hash, email)
         session.add(new_event_map)
         session.commit()

         self.write(event_hash)
         
       except:
         print "FUCK"
         raise
         self.write("fuk")
