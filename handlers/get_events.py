import tornado.web
from data.db import *
from sqlalchemy import *
from sqlalchemy.orm import class_mapper
from json import dumps


def serialize(Events):
   columns = [c.key for c in class_mapper(Events.__class__).columns]
   return dict((c, getattr(Events,c)) for c in columns)

class GetEventsHandler(tornado.web.RequestHandler):
    def get(self):
       try:
         email = self.get_argument('email', '')
         
         events_map_raw = session.query(EventsMap).filter(EventsMap.email == email)

         event_hash_list = []
         for event_map in events_map_raw:
            event_hash_list.append(event_map.event_hash)

         event_dict = {}
         i = 0
         for event_hash in event_hash_list:
            event_dict[i] = serialize(session.query(Events).get(event_hash))
            i += 1
                  
         self.write(event_dict)
         
       except:
         raise
         self.write("fuk")
