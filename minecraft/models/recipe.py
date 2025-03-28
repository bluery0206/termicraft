""" dsad """

import numpy as np

MAX_N_OUTPUT = 16

class Recipe:
    """ Recipe """
    def __init__(self, grid:list, n_output:int=1) -> None:
        self._grid = grid
        self.n_output = n_output

    @property
    def n_output(self) -> int:
        """ n_output when crafting """
        return self._n_output

    @n_output.setter
    def n_output(self, new_n_output) -> None:
        if new_n_output > MAX_N_OUTPUT:
            raise ValueError("Too many items ig.")

        self._n_output = new_n_output

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
    def vector(self) -> list:

        """ The comparable form of the recipe """

        # Initialize the vector by assigning zeroes

        # Intializing placeholder values table so that we will just replace
        # them values instead of doing a probably more complicated maths
        column_vector = np.zeros((self.width, self.height), dtype=np.int32)

        print(f"{column_vector = }")
        print(f"{self._grid = }")

        # Rearrange the table so that the columns are now in row form, and row are now in col form
        # prev:
        #   x = [[1, 2],
        #       [3, 4]]
        # after:
        #   x = [[1, 3],
        #       [2, 4]]
        # For easy addition of the vector na.
        # Maybe I could make this on the fly calcu but this already took me a lot of time
        #   so thats for the future
        for row_idx, row in enumerate(self._grid):
            for col_idx, col in enumerate(row):
                column_vector[col_idx][row_idx] = col

        print(f"{column_vector = }")

        column_vector = [sum(row) for row in column_vector]

        print(f"{column_vector = }")
        
        row_vector = np.zeros((self.height, self.width), dtype=np.int32)
        print(f"{row_vector = }")

        # return cols
        return 
