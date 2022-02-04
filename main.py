from flask import Flask

from extentions import db, migrate
from settings import config
from models.dota_item import *

def create_app():
    application = Flask(__name__)
    application.config.from_object(config)
    db.init_app(application)
    migrate.init_app(application)
    return application


app = create_app()


@app.route("/")
def status():
    return {"Hello": "world"}


if __name__ == "__main__":
    app.run(port=5001)
