"""This script is for useful classes that are handy in different scripts."""


class Grid:
    """A grid."""

    def __init__(self, grid: list[list]):

        self.grid = grid
        self.rows = len(grid)
        self.columns = len(grid[0])

    def __repr__(self) -> str:

        return "\n".join(["".join(row)
                          for row in self.grid])

    def get_adjacent_points(self, row: int, column: int,
                            include_diagonals: bool = False) -> list[tuple[int]]:
        """Returns the coordinates of all of the adjacent points to a point."""

        grid = self.grid
        num_rows = len(grid)
        num_cols = len(grid[0])

        adjacent_coordinates = [(row+1, column),
                                (row - 1, column),
                                (row, column + 1),
                                (row, column - 1)]

        if include_diagonals:
            adjacent_coordinates.extend([(row+1, column+1),
                                        (row+1, column-1),
                                        (row-1, column+1),
                                        (row-1, column-1)])

        adjacent_points = []

        for coord in adjacent_coordinates:
            if coord[0] in range(0, num_rows) and coord[1] in range(0, num_cols):
                adjacent_points.append(coord)

        return adjacent_points

    def transpose(self) -> list[list]:
        """Returns what the transpose of a grid would be as a nested list."""

        grid = self.grid
        return [[grid[j][i] for j in range(0, len(grid))]
                for i in range(0, len(grid[0]))]
