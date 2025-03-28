"""
This module provides functions for ... .

It includes features like:

Also im trying out python @properties


minecraft/
    models/
        items/
            crafting_table.py
            item_base.py
            plank.py
        recipe.py
        stack_type.py
    main.py
venv/
    
    
...

Author: ...
Date: XXXX-XX-XX
Version: X.X.X
"""

from models.crafting import Crafting

from models.items.crafting_table import CraftingTable
from models.items.plank import Plank 
ct = CraftingTable()
p = Plank()
print(f"{ct.recipe.crafting.vector = }")

c = Crafting(grid=[
    [0, 0, 0],
    [p.item_signature, p.item_signature, 0],
    [p.item_signature, p.item_signature, 0]
])

print(f"{c.vector = }")

print(ct.recipe.crafting.vector == c.vector)