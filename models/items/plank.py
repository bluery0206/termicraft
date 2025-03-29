""" dasdas """

from .item import Item

class Plank(Item):
    """ Plank """

    def __init__(self):
        super().__init__(
            item_signature = 1,
            recipe = [0],
            n_output = 4
        )