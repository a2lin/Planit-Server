import tornado.web
from data.db import *
from sqlalchemy import *
import random


#separate this into the handler folder shits, keep here for now for testing
class CreateUserHandler(tornado.web.RequestHandler):
    def post(self):
       try:
         name = self.get_argument('name', '')
         password = self.get_argument('password', '')
         email = self.get_argument('email', '')
         img_uri = self.get_argument('img_uri', '')

         if not name or not password or not email:
            self.write("0")
            return

         #no duplicate users, invalid is true if user exists
         (invalid, ), = session.query(exists().where(Users.email==email))

         if invalid:
            self.write("-1")
         else:
            user_hash = random.randint(1,10000000)
            (hash_conflict, ), = session.query(exists().where(Users.user_hash==user_hash))

            while hash_conflict:
               user_hash = random.randint(1,10000000)
               (hash_conflict, ), = session.query(exists().where(Users.user_hash==user_hash))
               
            new_user = Users(name, password, email, img_uri, user_hash)
            session.add(new_user)
            session.commit()
            self.write("1")
         
       except:
         raise
         self.write("fuk")
