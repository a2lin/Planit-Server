import os
import tornado.web
from handlers.create_user import CreateUserHandler
from handlers.login_user import LoginUserHandler
from handlers.create_event import CreateEventHandler
from handlers.create_event_map import CreateEventMapHandler
from handlers.get_events import GetEventsHandler


#separate this into the handler folder shits, keep here for now for testing
class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            name = self.get_argument('user_id', True)
            self.write("you sent me: " + name)
        except :
            raise
            self.write("something horrible happened, fml\nplannit")

class Application(tornado.web.Application):
    def __init__(self):
        # the current list of tracks that are playable
        handlers=[
            (r"/", HelloHandler),
            (r"/create_user", CreateUserHandler),
            (r"/login_user", LoginUserHandler),
            (r"/create_event", CreateEventHandler),
            (r"/create_event_map", CreateEventMapHandler),
            (r"/get_events", GetEventsHandler),
        ]

        tornado.web.Application.__init__(self, handlers)
