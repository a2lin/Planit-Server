import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
import application


def main():
    # start the web app
    app = application.Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start();

if __name__ == "__main__":
    main()
