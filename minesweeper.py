# Line 4 is creating a function that takes in a mine grid
# Iterates through each column and row of the mine grid
# Then for each mine free spot '-' in the grid adjacent to the mine '#'  counts the number of free mine spots 
def mine_adj(mine_grid):
   row = len(mine_grid)
   if row == 0:
      pass
   
# Line 10 creates an array of the possible mine positions in the mine grid to iterate through 
   mine_grid_positions = [[0, 0], [-1, 0], [1, 0], [0, -1], [-1, -1], [1, 1], [0, 1], [1, -1], [-1, 1]]

   col = len(mine_grid[0])


   new_grid = [['#' for j in range(col)] for i in range(row)]
# Line 17 - 27 Uses a for loop to iterate each column and row and counts the '-' incrementing the count if there is an adjacent '#' in the next column or row
   for r in range(row):
      for c in range(col):
         if mine_grid[r][c] == '-':
            count = 0
            for position in mine_grid_positions:
               new_row =  r + position[0]
               new_col = c + position[1]
               if (new_row >= 0 and new_row < row) and (new_col >= 0 and new_col < col) and mine_grid[new_row][new_col] == '#':
                  count += 1
               new_grid[r][c] = count
   return new_grid


         
mine_grid = [
   ['-', '#', '#', '-', '-'],
   ['-', '-', '-', '-', '#'],
   ['-', '#', '-', '-', '-'],
   ['-', '#', '-', '#', '#'],
   ['#', '#', '#', '-', '-']
]

# Line 40 - 43 Takes creates a new grid using the mine_adj function and prints the grid
new_grid = mine_adj(mine_grid)
for grid in new_grid:
   
   print(grid)