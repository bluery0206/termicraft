""" Crafting """

import numpy as np
from .excepts import EmptyCraftingGrid

class Crafting:
    """ For crafting"""

    def __init__(self, grid:list) -> None:
        self._grid = grid

    def has_items(self) -> bool:
        """ dasd """
        arr = np.array(self._grid)
        arr = arr.flatten()
        arr.sort()
        return arr[-1] > 0

    @property
    def grid(self) -> list:
        """ the grid grid """
        return self._grid

    @grid.setter
    def grid(self, new_grid:list) -> None:
        self._grid = new_grid

    @property
    def height(self) -> int:
        """ dsadsa """
        return len(self._grid)

    @property
    def width(self) -> int:
        """ 
        The number of slots items horizontally

        Example: Let's say Crafting Table is 5x3: 
        ```
            0, 0, 0, 0, i
            i, i, i, i, i
            0, 0, i, i, 0

            where:
                0 - has no item
                1 - has item

            then width = 5
        ```
        """

        # The code in its long form:
        #     longest_col = 0
        #     for row in self._grid:
        #         row_len = len(row)
        #         if row_len > longest_col:
        #             longest_col = row_len
        #     print(F"{max(self._grid, key=len)}")
        #     return longest_col

        return len(max(self._grid, key=len))

    @property
    def shape(self) -> tuple:
        """ dsadsa """
        return (self.height, self.grid)

    @property
    def column_vector(self) -> list:
        """
        A list of sum of `item_signature` values
        within the crafting grid column.

        Example: Crafting Table (3x3)
            0, 1, 0
            0, 1, 0
            0, 2, 0
        
            Where:
                0 - no item
                1 - `Stone` `item_signature`
                2 - `Stick` `item_signature`

            Result(s):
                [4]

                We omit the zeros to allow crafting in different columns and rows
                as long as it can fit

        Paired with row_vector, we can know what the items are,
        where the items are placed, and its order.
        """

        # Initialize the vector by creating a list with the length
        # of total number of columns and assign it with zero as a
        # placeholder so that we can add
        column_vector = [0 for _ in range(self.width)]

        # Getting the sum of each column
        for row in self._grid:
            for col_idx, col in enumerate(row):
                column_vector[col_idx] += col

        return self.trim_zeros(column_vector)

    @property
    def row_vector(self) -> list:
        """
        A list of sum of `item_signature` values
        within the crafting grid row.

        Example: Crafting Table (3x3)
            0, 1, 0
            0, 1, 0
            0, 2, 0
        
            Where:
                0 - no item
                1 - `Stone` `item_signature`
                2 - `Stick` `item_signature`

            Result(s):
                [1, 1, 2]

                We omit the zeros to allow crafting in different columns and rows
                as long as it can fit

        Together with column_vector, we can know what the items are,
        where the items are placed, and its order.

        I just realized how this is like a feature extraction layer of a CNN. We literally
        getting the important parts
        """
        # Sums per row and store in a list
        return self.trim_zeros([sum(row) for row in self._grid])

    def trim_zeros(self, arr:list) -> list:
        """ dsads """
        while arr and arr[0] <= 0:
            arr.pop(0)

        while arr and arr[-1] <= 0:
            arr.pop(-1)

        if not arr:
            raise EmptyCraftingGrid

        return arr

    @property
    def vector(self) -> list:
        """ The comparable form of the recipe """

        if not self.has_items():
            raise EmptyCraftingGrid

        column_vector = self.column_vector
        row_vector = self.row_vector

        return (row_vector, column_vector)
