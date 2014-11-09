import tornado.web
from data.db import *
from sqlalchemy import *

class FindFriendHandler(tornado.web.RequestHandler):
    def get(self):
       try:
         string = self.get_argument('string', '')

         if string:
            search_raw = session.query(Users).filter(or_(Users.email.startswith(string),Users.name.startswith(string)))

            search_list = []

            for result in search_raw:
               search_list.append(serialize(result))

            search_wrapper = {}
            search_wrapper[0] = search_list
                     
            self.write(search_wrapper)

         else:
            self.write("0")
            
       except:
         raise
         self.write("fuk")

