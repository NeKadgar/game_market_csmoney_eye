from datetime import datetime
from background.celery_app import app


@app.task(queue="items_base_queue")
def update_items(item_hash_name: str, game_id: int, price: float, dtime: datetime):
    print(item_hash_name, game_id, price, dtime)
    return "Updated"
