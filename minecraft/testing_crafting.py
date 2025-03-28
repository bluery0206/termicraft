"""
dsa
"""

# print(stick.recipe)
# for irow in stick.idk():
#     print(irow)


# class Crafting:
#     """ Class for crafting """
#     def __init__(self, table_size:int) -> None:
#         self._table_size = table_size

#     @property
#     def table_size(self) -> int:
#         """ Getter """
#         return self.table_size

#     @table_size.setter
#     def table_size(self, new_table_size) -> None:
#         self.table_size = new_table_size

#     def calculate_score(self):
#         output = np.zeros((self.table_size, self.table_size), dtype=np.int32)

        # for row_idx, row in enumerate(recipe_table):
        #     for col_idx, col in enumerate(row):
        #         rotated_recipe_table[col_idx][row_idx] = col

        # # Getting rotated recipe table row score
        # cols = []
        # for row in rotated_recipe_table:
        #     cols.append(sum(row))

        # # CALCULATING ROW SCORE
        # rows = []
        # for row in recipe_table:
        #     rows.append(sum(row))


# def calculate_score(self, recipe_table:list) -> tuple[list]:
#     """
#         dsadsa
#     """
    
#     # CALCULATING COLUMN SCORE
#     # Rotating the recipe_table so that columns are now row and rows originally 
#     # are now in column form making calculation and visualization easier

#     # Intializing placeholder values table so that we will just replace
#     # them values instead of doing a probably more complicated maths
#     rotated_recipe_table = list(list(range(self.__table_size))) 

#     for row_idx, row in enumerate(recipe_table):
#         for col_idx, col in enumerate(row):
#             rotated_recipe_table[col_idx][row_idx] = col

#     # Getting rotated recipe table row score
#     cols = []
#     for row in rotated_recipe_table:
#         cols.append(sum(row))

#     # CALCULATING ROW SCORE
#     rows = []
#     for row in recipe_table:
#         rows.append(sum(row))

#     # REMOVING ZEROES
#     while 0 in rows:
#         rows.remove(0)

#     while 0 in cols:
#         cols.remove(0)

#     return (rows, cols)
