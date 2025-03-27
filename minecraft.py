from enum import Enum

class Player:
    def __init__(self, name:str, can_pickup_items:bool=True) -> None:
        self.name = name
        self.can_pickup_items = can_pickup_items