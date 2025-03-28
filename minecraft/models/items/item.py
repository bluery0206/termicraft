""" dasdsa """

from ..recipe import Recipe
from ..stack_type import StackType
from ..excepts import EmptyCraftingGrid

class Item:
    """ Base Class for every item """
    def __init__(self, item_signature:int, recipe:list|None=None, is_craftable:bool=True,
                 stack_type:StackType=StackType.NORMAL_STACK, n_output:int=1) -> None:
        self._is_craftable = is_craftable
        self._stack_type = stack_type
        self._item_signature = item_signature
        self._raw = recipe
        self._n_output = n_output

    @property
    def n_output(self) -> int:
        """ number of item output when crafting """
        return self._n_output

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
    def is_craftable(self) -> bool:
        """ recipe """
        return self._is_craftable

    @property
    def name(self) -> str:
        """ The name of the Item obtained through its class name"""
        return self.__class__.__name__

    @property
    def identifier(self) -> str:
        """ The identifier of the Item obtained through its class name"""
        return self.__class__.__name__.lower()

    @property
    def item_signature(self) -> int:
        """ Value to calculate the crafting score of a recipe or idk """
        return self._item_signature

    @item_signature.setter
    def item_signature(self, new_item_signature) -> None:
        if new_item_signature > 1000000:
            raise ValueError(f"{new_item_signature} is too large.")

        self._item_signature = new_item_signature
