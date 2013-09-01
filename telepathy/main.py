import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
from routes import urls
from settings import configurations

def run():
    app = tornado.web.Application(urls, **configurations)
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    define("port", default=8888, help="run on the given port", type=int)
    tornado.options.parse_command_line()
    run()
