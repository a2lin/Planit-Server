import tornado.web
from data.db import *
from sqlalchemy import *
import random


class AddFriendHandler(tornado.web.RequestHandler):
    def post(self):
       try:
  
         friend = self.get_argument('friend', '')
         email = self.get_argument('email', '')

         (user_exists, ), = session.query(exists().where(Users.email == email))
         (friend_exists, ), = session.query(exists().where(Users.email == friend))

         if not user_exists:
            self.write("-2")
            return
         if not friend_exists:
            self.write("-3")
            return

         (invalid, ), = session.query(exists().where(FriendsMap.email.startswith(email))
                                              .where(FriendsMap.friend == friend))

         if invalid:
            self.write("-1")
            return

         friend_map = FriendsMap(email + (str)(random.randint(1,100000000000)), friend)
         session.add(friend_map)
         friend_map_reverse = FriendsMap(friend + (str)(random.randint(1,1000000000000)), email)
         session.add(friend_map_reverse)
         session.commit()

         self.write("1")
         
       except:
         raise
         self.write("fuk")
