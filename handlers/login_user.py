import tornado.web
from data.db import *
from sqlalchemy import *


class LoginUserHandler(tornado.web.RequestHandler):
   def get(self):
      try:
         email = self.get_argument('email', True)
         password = self.get_argument('password', True)

         (valid, ), = session.query(exists().where(Users.email==email).
                                             where(Users.password==password))
         if valid:
            self.write("1")
         else:
            self.write("-1")
                           
      except:
         raise
         self.write("fuk")

