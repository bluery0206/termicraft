""" dasdsa """

from src.recipe import Recipe
from src.stack_type import StackType
from src.excepts import EmptyCraftingGrid

class Item:
    """
    Base Class for every item

    Attributes:
        attr_one (type): decription
    """

    def __init__(self) -> None:
        self.id = 1
        self.name = ""
        self.is_craftable = True
        self.recipe = [None]
        self.stack_stype = StackType.NORMAL_STACK
        self.is_enchantable = False
        self.enchantments = [None, None]


class Consumable(Item):
    """ das """
    def __init__(self):
        super().__init__()

        self.hunger_level = 1.
        self.saturation_level = 1.


class Gear(Item):
    """ das """
    def __init__(self):
        super().__init__()

        self.durability = 1034
        self.damage = 10
        self.interval = 1.5


class Tools(Gear):
    """ das """
    def __init__(self):
        super().__init__()

        self.mining_speed = 3


class Weapon(Gear):
    """ das """
    def __init__(self):
        super().__init__()

        self.interval = 1.5
        self.range = 4.5 # in blocks
        self.multiplier = 1.5


if __name__ == "__main__":
    item = Item(

    )
