import falcon
from config import routes,config

app = application = falcon.API();
routes.Router(app)

print(' * ' + config.APP_NAME + ' Initialized')