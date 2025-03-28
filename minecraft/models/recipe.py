""" dsad """

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

