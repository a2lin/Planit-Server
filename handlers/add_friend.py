import tornado.web
from data.db import *
from sqlalchemy import *


class AddFriendHandler(tornado.web.RequestHandler):
    def post(self):
       try:
  
         friend = self.get_argument('friend', '')
         email = self.get_argument('email', '')

         friend_map = FriendsMap(email, friend)
         session.add(friend_map)
         friend_map_reverse = FriendsMap(friend, email)
         session.add(friend_map_reverse)
         session.commit()

         self.write('added your buddy ' + friend)
         
       except:
         raise
         self.write("fuk")
