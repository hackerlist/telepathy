import tornado.web
from core import SocketHandler

class Index(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", messages=SocketHandler.cache)
