import tornado.web
from data.db import *
from sqlalchemy import *
import random


class GetEventUsersHandler(tornado.web.RequestHandler):
    def get(self):
       try:
         event_hash = self.get_argument('event_hash', '')

         #checks if event is real
         (valid, ), = session.query(exists().where(Events.event_hash==event_hash))


         if valid:
             events_map_raw = session.query(EventsMap)

             event_hash_list = []
             for event_map in events_map_raw:
                print event_map.email
                event_map2 = session.query(EventsMap).filter(and_(EventsMap.event_hash==event_hash,
                                                                EventsMap.email==event_map.email))
                for x in event_map2:
                    event_hash_list.append(x.email)

             user_list = []
             for email in event_hash_list:
                user_list.append(serialize(session.query(Users).get(email)))

             user_wrapper = {}
             user_wrapper[0] = user_list
                      
             self.write(user_wrapper)
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

