import datetime
import itertools

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
            celery_app.send_task(name="update_items_base", queue="items_base_queue", kwargs=detail_item)
            dota_item, _ = DotaItem.get_or_create(detail_item.get("steamName"))
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
