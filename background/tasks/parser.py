import datetime
import itertools
from decimal import Decimal
from extentions import db
from csmoney.client import Client
from csmoney.market import Market as MarketClient
from models.dota_item import DotaItemHistory, DotaItem
from background.celery_app import app as celery_app


client = MarketClient(client=Client())


@celery_app.task(queue="csmoney_queue", ignore_result=False)
def parse():
    start_datetime = datetime.datetime.now()
    i = 0
    for i in itertools.count(start=0):
        offset = i * 60
        response = client.fetch_items(offset=offset)
        if not response.get("items", None):
            break
        for item in response["items"]:
            detail_item = client.fetch_details(item.get("id"), item.get("appId"))
            heroes = detail_item.get("heroes")
            celery_app.send_task(
                name="update_service_price",
                queue="items_base_queue",
                kwargs={
                    "game_id": 570,
                    "item_hash_name": detail_item.get("steamName"),
                    "price": Decimal(item.get("price")),
                    "service": "CSMONEY",
                    "hero_name": heroes[0] if heroes else None,
                    "rarity": detail_item.get("rarity"),
                    "item_type": detail_item.get("type"),
                    "slot": detail_item.get("slot"),
                    "quality": detail_item.get("quality")
                }
            )
            dota_item, _ = DotaItem.get_or_create(detail_item.get("steamName"))
            if dota_item:
                history = DotaItemHistory(
                    price=item.get("price"),
                    default_price=item.get("defaultPrice"),
                    slots=detail_item.get("slots"),
                    item_id=dota_item.id
                )
                db.session.add(history)
            db.session.commit()
    return {
        "start": str(start_datetime),
        "executed in": str(datetime.datetime.now() - start_datetime),
        "count": i
    }
