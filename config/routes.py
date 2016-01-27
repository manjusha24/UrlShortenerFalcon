from controllers import URL

class Router:
    def __init__(self, app):
        app.add_route('/getURL/{url}', URL.ShortenedURL())
        app.add_route('/createShortURL',URL.CreateShortURL())