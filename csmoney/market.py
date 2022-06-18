from typing import Optional

from csmoney.core import INVENTORY_URL, SKIN_INFO_URL
from csmoney.client import Client


class Market:
    def __init__(self, client: Client):
        self.client = client

    def fetch_items(self, game_id: int = 570, limit: int = 60, offset: int = 0, order: str = "desc",
                    sort: str = "price", item_type: Optional[int] = None, weapon: Optional[str] = None,
                    is_market: bool = False, with_stack: bool = True) -> dict:
        """Get platform list data

        :param game_id: id of game
        :param limit: how many items return
        :param offset: how many items skip
        :param order: order type (asc or desc)
        :param sort: sort by value of this field
        :param item_type: type of item to get, if none will parse all types
        :param weapon: type of weapon ex. AWP
        :param is_market: get all items from site and auction, or only from site
        :param with_stack: combine items or return one by one?
        :return: requested items
        """
        params = {
            "limit": limit,
            "offset": offset,
            "order": order,
            "sort": sort,
            "isMarket": is_market,
            "withStack": with_stack
        }
        if item_type:
            params["type"] = item_type
        if weapon:
            params["weapon"] = weapon
        response = self.client.get(f"{INVENTORY_URL}{game_id}", params=params)
        return response.json()

    def fetch_details(self, item_id: int, game_id: int = 570, is_bot: bool = True, bot_inventory: bool = True):
        """Get detail platform data

        :param item_id: id of item at platform
        :param game_id: id of game
        :param is_bot:
        :param bot_inventory:
        :return: detail data about item
        """
        params = {
            "appId": game_id,
            "id": item_id,
            "isBot": "true" if is_bot else "false",
            "botInventory": "true" if bot_inventory else "false"
        }
        response = self.client.get(f"{SKIN_INFO_URL}", params=params)
        return response.json()
