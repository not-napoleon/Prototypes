from flask import Flask
from main_page import main_site

app = Flask(__name__)
app.register_blueprint(main_site)


