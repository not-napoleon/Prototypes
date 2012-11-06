from flask import Flask
from main_page import main_site
from admin_page import admin_site

app = Flask(__name__)
app.register_blueprint(admin_site)
app.register_blueprint(main_site)

