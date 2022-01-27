import enum
from typing import Optional

INVENTORY_URL = "https://inventories.cs.money/5.0/load_bots_inventory/"


class CSGOType(enum.Enum):
    GLOVES = 13
    KNIFE = 2
    PISTOLS = 5
    SMG = 6
    ASSAULT_RIFLES = 3
    SNIPER_RIFLES = 4
    SHOTGUN = 7
    MACHINE_GUNS = 8
    KEYS = 1
    STICKER = 10
    CASE = 12
    GRAFFITI = 14
    MUSIC_KIT = 11
    PIN = 9
    AGENTS = 18
    PATCH = 19


class DOTAType(enum.Enum):
    SKIN = 1
    GEM = 2
    COURIER = 3
    TAUNT = 4
    ITEMS_SET = 5
    TREASURE = 6
    TOOL = 7
    WARDS = 8
    COMMENTATORS = 9
    INTERFACE = 10
