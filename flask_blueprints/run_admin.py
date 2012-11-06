from web.admin_app import app

from pprint import pprint
pprint(app.url_map)

app.run('0.0.0.0', 40001, True)
