""" dasdsa """

from .recipe import Recipe
from .stack_type import StackType
from .excepts import EmptyCraftingGrid

class Item:
    """
    Base Class for every item

    Attributes:
        item_id (int): Value to calculate the crafting score of a recipe or idk
        recipe:
        name: Will base
    """

    def __init__(self, item_id:int, name:str,  recipe:list|None=None, n_output:int=1) -> None:
        self._name = name
        self._item_id = item_id
        self._raw = recipe
        self._n_output = n_output

        self. _stack_type = StackType.NORMAL_STACK
        self._is_craftable = True

    @property
    def recipe(self) -> Recipe:
        """ dsad """
        if not self._is_craftable:
            raise AttributeError(f"{self.name} cannot be used for crafting.")

        recipe = Recipe(self._raw, self._n_output)

        if not recipe.crafting.has_items():
            raise EmptyCraftingGrid

        return recipe

    @property
    def item_id(self) -> int:
        """ Value to calculate the crafting score of a recipe or idk """
        return self._item_id

    @item_id.setter
    def item_id(self, new_item_id) -> None:
        if new_item_id > 1000000:
            raise ValueError(f"{new_item_id} is too large.")

        self._item_id = new_item_id
