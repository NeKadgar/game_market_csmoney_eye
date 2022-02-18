from flask import Flask, jsonify

from extentions import db, migrate
from settings import config
from models.dota_item import *


def create_app():
    application = Flask(__name__)
    application.config.from_object(config)
    db.init_app(application)
    migrate.init_app(application)

    from api import dota_routes
    application.register_blueprint(dota_routes)

    return application


app = create_app()


@app.route("/")
def sitemap():
    return jsonify([
        {
            "function": app.view_functions.get(rule.endpoint).__name__,
            "url": str(rule)
        } for rule in app.url_map.iter_rules()])


if __name__ == "__main__":
    app.run(port=5001, debug=True)
