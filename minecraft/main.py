"""
This module provides functions for ... .

It includes features like:
...

Author: ...
Date: XXXX-XX-XX
Version: X.X.X
"""

from enum import Enum

class StackType(Enum):
    """ Class for Stack Types """

    NON_STACKABLE   = 1
    SMALL_STACK     = 16
    NORMAL_STACK    = 64

class Item:
    """ Base Class for every item """
    def __init__(self, name:str, numeric_id:int, is_craftable:bool=True,
                stack_type:StackType=StackType.NORMAL_STACK) -> None:
        self.__max_stack_value  = stack_type.value
        self.__numeric_id       = numeric_id
        self.__name             = name
        self.__is_craftable     = is_craftable

    @property
    def max_stack_value(self) -> int:
        """ Getter method """
        return self.__max_stack_value

    @max_stack_value.setter
    def max_stack_value(self, new_max_stack_value:int) -> None:
        self.__max_stack_value = new_max_stack_value

    @property
    def numeric_id(self) -> int:
        """ Getter method """
        return self.__numeric_id

    @numeric_id.setter
    def numeric_id(self, new_numeric_id:int) -> None:
        self.__numeric_id = new_numeric_id

    @property
    def name(self) -> str:
        """ Getter method """
        return self.__name

    @name.setter
    def name(self, new_name:int) -> None:
        self.__name = new_name

    @property
    def is_craftable(self) -> bool:
        """ Getter method """
        return self.__is_craftable

    @is_craftable.setter
    def is_craftable(self, new_is_craftable:int) -> None:
        self.__is_craftable = new_is_craftable

class Stick(Item):
    """ Stick """
    def __init__(self):
        super().__init__("Stick", 1)

class Bucket(Item):
    """ Bucket """
    def __init__(self):
        super().__init__("Bucket", 2, StackType.SMALL_STACK)

class Sword(Item):
    """ Sword """
    def __init__(self):
        super().__init__("Sword", 3, StackType.NON_STACKABLE)

stick = Stick()
print(stick.name)
