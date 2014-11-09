import tornado.web
from data.db import *
from sqlalchemy import *

class GetFriendsHandler(tornado.web.RequestHandler):
    def get(self):
       try:
         email = self.get_argument('email', '')

         (valid, ), = session.query(exists().where(Users.email==email))

         if not valid:
            self.write("-1")
            return
            
#friends_map_raw = session.query(FriendsMap).filter_by(email = email)
         friends_map_raw = session.query(FriendsMap).filter(FriendsMap.email.startswith(email))

         friend_list = []
         for friend_map in friends_map_raw:
            friend_list.append(friend_map.friend)

         friend_list_serial = []
         for friend in friend_list:
            friend_list_serial.append(serialize(session.query(Users).get(friend)))

         friend_wrapper = {}
         friend_wrapper[0] = friend_list_serial
                  
         self.write(friend_wrapper)
         
       except:
         raise
         self.write("fuk")
