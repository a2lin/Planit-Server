import os
import tornado.web


#separate this into the handler folder shits, keep here for now for testing
class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            name = self.get_argument('user_id', True)
            self.write("you sent me: ", name)
        except:
            self.write("something horrible happened, fml")

class Application(tornado.web.Application):
    def __init__(self):
        # the current list of tracks that are playable
        handlers=[
            (r"/", HelloHandler),
        ]

        tornado.web.Application.__init__(self, handlers)
