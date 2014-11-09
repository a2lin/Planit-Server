import tornado.web
from data.db import *
from sqlalchemy import *

class GetEventsHandler(tornado.web.RequestHandler):
    def get(self):
       try:
         email = self.get_argument('email', '')

         (valid, ), = session.query(exists().where(Users.email==email))
      
         if not valid:
            self.write("-1")
            return
         
         events_map_raw = session.query(EventsMap).filter(EventsMap.email == email)

         event_hash_list = []
         for event_map in events_map_raw:
            event_hash_list.append(event_map.event_hash)

         event_list = []
         for event_hash in event_hash_list:
            event_list.append(serialize(session.query(Events).get(event_hash)))

         event_wrapper = {}
         event_wrapper[0] = event_list
                  
         self.write(event_wrapper)
         
       except:
         raise
         self.write("fuk")
