import tornado.web
from data.db import *
from sqalchemy import *
import random


class RemoveEventHandler(tornado.web.RequestHandler):
   def post(self):
      try:
         title = self.get_argument('title', '')
         description = self.get_argument('description', '')
         location = self.get_argument('location', '')
         time = self.get_argument('time', '')
         creator = self.get_argument('creator', '')

         event_hash = self.get_argument('event_hash', '')



       '''  tempevent = Events.query.filter_by(event_hash=
         (invalid, ), = session.query(exists().where(Events.event_hash==event_hash))
         while invalid:
            #deleting this event
            session.delete(tempevent)
            tempevent = Events.query.filter_by
            (invalid, ), = session.query(exists().where(Events.event_hash==event_hash))'''


         tempevents = Events.query.filter_by(event_hash=event_hash).all()
         if not tempevents:
            return

         for tempevent in tempevents:
            session.delete(tempevent)

         session.commit()
         self.write(event_hash)

      except:
         raise
         self.write("fuk")
