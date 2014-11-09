import tornado.web
from data.db import *
from sqlalchemy import *


class RemoveEventHandler(tornado.web.RequestHandler):
   def post(self):
      try:
         event_hash = self.get_argument('event_hash', '')
         email = self.get_argument('email', '')

         (valid, ), = session.query(exists().where(Events.event_hash==event_hash).
                                             where(Events.creator==email))

         if valid:
            events = session.query(Events).filter(Events.event_hash==event_hash)
            for event in events:
               session.delete(event)

            events_map = session.query(EventsMap).filter(EventsMap.event_hash==event_hash)
            for event_map in events_map:
               session.delete(event_map)
            session.commit()
            self.write("1")
         else:
            self.write("-1")

      except:
            self.write("fuk")
