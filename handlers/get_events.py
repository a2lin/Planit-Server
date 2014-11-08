import tornado.web
from data.db import *
from sqlalchemy import *

class GetEventsHandler(tornado.web.RequestHandler):
    def get(self):
       try:
         email = self.get_argument('email', '')
         
         events = session.query(EventsMap).filter(EventsMap.email == email)

         events_dict = {}
         i = 0
         for event in events:
            events_dict[i] = event.event_hash
            i += 1

         self.write(events_dict)
         
       except:
         raise
         self.write("fuk")

