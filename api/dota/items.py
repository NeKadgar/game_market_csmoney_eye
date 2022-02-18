from flask import Blueprint, abort
from models.dota_item import DotaItem

items_route = Blueprint("items", __name__, url_prefix="/items")


@items_route.route("/<int:item_id>")
def get_item_by_id(item_id: int):
    item = DotaItem.query.filter_by(id=item_id).one_or_none()
    if not item:
        return abort(404, "Can't find item")
    return item.as_dict


@items_route.route("/<item_hash_name>")
def get_item_by_name(item_hash_name: str):
    item = DotaItem.query.filter_by(name=item_hash_name).one_or_none()
    if not item:
        return abort(404, "Can't find item")
    return item.as_dict
