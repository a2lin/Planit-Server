import tornado.web
from data.db import *
from sqlalchemy import *

class GetFriendsHandler(tornado.web.RequestHandler):
    def get(self):
       try:
         email = self.get_argument('email', '')
         
         friends_map_raw = session.query(FriendsMap).filter(FriendsMap.email == email)

         friend_list = []
         for friend_map in friends_map_raw:
            friend_list.append(friend_map.friend)

         friend_dict = {}
         i = 0
         for friend in friend_list:
            friend_dict[i] = serialize(session.query(Users).get(friend))
            i += 1
                  
         self.write(friend_dict)
         
       except:
         raise
         self.write("fuk")
