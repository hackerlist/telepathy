import controller

urls = [(r"/", controller.home.Index),
        (r"/chatsocket", controller.core.SocketHandler),
        ]
