def is_valid_cell(row, col, max_row, max_col):
    return 0 <= row < max_row and 0 <= col < max_col

def count_adjacent_mines(mine_grid, r, c, mine_grid_positions, row, col):
    count = 0
    for position in mine_grid_positions:
        new_row, new_col = r + position[0], c + position[1]
        if is_valid_cell(new_row, new_col, row, col) and mine_grid[new_row][new_col] == '#':
            count += 1
    return count

def mine_adj(mine_grid):
    row = len(mine_grid)
    if row == 0:
        return []

    col = len(mine_grid[0])
    mine_grid_positions = [[0, 0], [-1, 0], [1, 0], [0, -1], [-1, -1], [1, 1], [0, 1], [1, -1], [-1, 1]]
    new_grid = [['#' for _ in range(col)] for _ in range(row)]

    for r in range(row):
        for c in range(col):
            if mine_grid[r][c] == '-':
                count = 0
                count = count_adjacent_mines(mine_grid, r, c, mine_grid_positions, row, col)
                new_grid[r][c] = count

    return new_grid

# Example Usage:
mine_grid = [
    ['-', '#', '#', '-', '-'],
    ['-', '-', '-', '-', '#'],
    ['-', '#', '-', '-', '-'],
    ['-', '#', '-', '#', '#'],
    ['#', '#', '#', '-', '-']
]

try:
    new_grid = mine_adj(mine_grid)
    for grid in new_grid:
        print(grid)
except Exception as e:
    print(f"An error occurred: {e}")
