from flask import Flask

from extentions import db, migrate
from settings import config

from csmoney.client import Client
from csmoney.market import Market as MarketClient
from models.dota_item import DotaItemHistory, DotaItem

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
migrate.init_app(app)

client = MarketClient(client=Client())


@app.route("/")
def status():
    # url for testing
    response = client.fetch_items()
    for item in response["items"]:
        detail_item = client.fetch_details(item.get("id"), item.get("appId"))
        dota_item, _ = DotaItem.get_or_create(detail_item.get("steamName"))
        history = DotaItemHistory(
            price=item.get("price"),
            default_price=item.get("defaultPrice"),
            slots=detail_item.get("slots"),
            item_id=dota_item.id
        )
        db.session.add(history)
        db.session.commit()
    return detail_item


if __name__ == "__main__":
    app.run()
