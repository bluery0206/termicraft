""" dasdsa """

from ..recipe import Recipe
from ..stack_type import StackType

class Item:
    """ Base Class for every item """
    def __init__(self, item_signature:int, recipe:list|None=None, is_craftable:bool=True,
                 stack_type:StackType=StackType.NORMAL_STACK, n_output:int=1) -> None:
        self._is_craftable = is_craftable
        self._stack_type = stack_type
        self._item_signature = item_signature
        self._recipe = Recipe(grid=recipe, n_output=n_output)

    @property
    def recipe(self) -> Recipe:
        """ recipe """
        return self._recipe

    @property
    def is_craftable(self) -> bool:
        """ recipe """
        return self._is_craftable

    @property
    def stack_type(self) -> StackType:
        """ recipe """
        return self._stack_type

    @property
    def n_output(self) -> int:
        """ n_output when crafting """
        return self._recipe.n_output

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
