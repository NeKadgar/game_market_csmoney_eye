from flask import Blueprint, abort
from models.dota_item import DotaItem
from csmoney.client import Client
from csmoney.market import Market as MarketClient


items_route = Blueprint("items", __name__, url_prefix="/items")
client = MarketClient(client=Client())


@items_route.route("/<int:item_id>")
def get_item_by_id(item_id: int):
    item = DotaItem.query.filter_by(id=item_id).one_or_none()
    if not item:
        return abort(404, "Can't find item")
    return item.as_dict


@items_route.route("/parse")
def test_task():
    response = client.fetch_items(offset=0)
    a = []
    # parse.delay()
    print(response["items"])
    print(response["items"][0].get("id"))
    print(response["items"][0].get("appId"))
    for item in response["items"]:
        detail_item = client.fetch_details(item.get("id"), item.get("appId"))
        a.append(detail_item)
        break
    return {"items": a}


@items_route.route("/<item_hash_name>")
def get_item_by_name(item_hash_name: str):
    item = DotaItem.query.filter_by(name=item_hash_name).one_or_none()
    if not item:
        return abort(404, "Can't find item")
    return item.as_dict
