"""" dasdasdas """

from .item import Item
from .plank import Plank

class CraftingTable(Item):
    """ CraftingTable """

    def __init__(self):
        plank = Plank()

        super().__init__(
            item_signature = 2,
            recipe = [
                [plank.item_signature, plank.item_signature],
                [plank.item_signature, plank.item_signature]
            ]
        )
