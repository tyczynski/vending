from flask import Flask

app = Flask(__name__)

from . import routes

app.add_url_rule('/feed/<id>', 'generate_feed', routes.generate_feed)
