
class EmptyCraftingGrid(Exception):
    def __init__(self):
        super().__init__("Crafting grid cannot be empty.")
        