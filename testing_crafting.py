""" dasddasd das das das d """

# Weapon: range, damage, interval, durability
# Tools: durability, damage, range, interval, mining_speed
# Equipment: durability, multiplier
# Consumables: hunger_level, saturation_level

# {
#     "name": "Crafting Table",
#     "identifier": "crafting_table`",
#     "item_signature": 3,
#     "recipe":[
#         ["plank", "plank"],
#         ["plank", "plank"]
#     ]
# }

import json

from src.item import Item
from src.stack_type import StackType

data = json.load(open("crafting_table.json"))

class Loader:
    def __init__(self) -> None:
        pass

    def load_item(self, data:dict) -> None:
        pass

# loader = Loader()
# loader.item(data)

# item = Item(
#     identifier="target_block",
#     item_signature=1,
#     n_output=2,
#     recipe=[
#         [None],
#     ]
# )

# print(item.name)