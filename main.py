from flask import Flask

from csmoney.client import Client
from csmoney.market import Market

app = Flask(__name__)

client = Client()


@app.route("/")
def status():
    response = Market(client).fetch_items()
    item = response["items"][1]
    return item
