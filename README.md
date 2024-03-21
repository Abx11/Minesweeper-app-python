
# Minesweeper App

## Overview

This Python project is a Minesweeper app that provides a function to analyze a given mine grid and generate a new grid with counts of adjacent mines for each mine-free spot.

## Features

- **mine_adj Function:**
  - Takes a mine grid as input.
  - Iterates through each column and row of the mine grid.
  - Counts the number of mine-free spots adjacent to each mine ('#') in the grid.

- **Usage Example:**
  ```python
  mine_grid = [
     ['-', '#', '#', '-', '-'],
     ['-', '-', '-', '-', '#'],
     ['-', '#', '-', '-', '-'],
     ['-', '#', '-', '#', '#'],
     ['#', '#', '#', '-', '-']
  ]
  new_grid = mine_adj(mine_grid)
  for grid in new_grid:
      print(grid)
  ```

## Implementation Details

- The `mine_adj` function calculates the number of adjacent mines for each mine-free spot in the grid, utilizing a predefined set of mine positions.
- The resulting grid with mine counts is stored in the `new_grid` variable.

## Function Explanation

- **mine_adj Function Parameters:**
  - `mine_grid` (list of lists): The input mine grid.

- **Algorithm:**
  - Iterates through each cell in the mine grid.
  - For each mine-free spot ('-'), counts the number of adjacent mines.
  - Updates the corresponding cell in the new grid with the mine count.

## Example Output

The provided example mine grid:

```
['-', '#', '#', '-', '-']
['-', '-', '-', '-', '#']
['-', '#', '-', '-', '-']
['-', '#', '-', '#', '#']
['#', '#', '#', '-', '-']
```

Generates the following output:

```
[1, '#', '#', 3, 1]
[3, 4, 3, 4, '#']
[2, '#', 5, 4, 3]
[2, '#', 4, '#', '#']
['#', '#', '#', 3, 1]
```

## Getting Started

To use the Minesweeper app in your project, follow these steps:

1. Clone the repository https://github.com/Abx11/Minesweeper-app-python.git
2. Open terminal or command prompt 'cd' to the directory of the repository
3. Copy the `mine_adj` function into your codebase.
4. Provide a valid mine grid as input to the `mine_adj` function.
5. Use the generated `new_grid` to access the mine counts for each spot.

Feel free to explore and integrate this Minesweeper app into your Python projects!

## Authors
This project was done by Abel Nyakale
## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an [issue](https://github.com/Abx11/Minesweeper-app-python/issues) or submit a [pull request](https://github.com/Abx11/Minesweeper-app-python/pulls).
"# Minesweeper-app-python" 
