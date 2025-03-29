"""" dasdasdas """

from .item import Item
from .plank import Plank

class Stick(Item):
    """ Stick """

    def __init__(self) -> None:
        plank = Plank()

        super().__init__(
            item_signature = 3,
            recipe = [
                [plank.item_signature],
                [plank.item_signature]
            ],
            n_output = 2
        )
