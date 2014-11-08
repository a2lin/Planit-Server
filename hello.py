import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    x = 3

    def get(self):
        self.write(x)

    def post(self):
        x = 5


application = tornado.web.Application([(r"/", MainHandler),])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
