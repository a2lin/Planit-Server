import tornado.web
from data.db import *
from sqlalchemy import *


#separate this into the handler folder shits, keep here for now for testing
class CreateUserHandler(tornado.web.RequestHandler):
    def post(self):
       try:
         name = self.get_argument('name', '')
         password = self.get_argument('password', '')
         email = self.get_argument('email', '')

         if not name or not password or not email:
            self.write("0")
            return
         
         #no duplicate users, invalid is true if user exists
         (invalid, ), = session.query(exists().where(Users.email==email))

         if invalid:
            self.write("-1")
         else:
            new_user = Users(name, password, email)
            session.add(new_user)
            session.commit()
            self.write("1")
         
       except:
         raise
         self.write("fuk")
