def cavityMap(grid):
   new_grid = []
   for j in grid:
      new_grid.append(list(j))



   for x in range(1, len(grid) - 1):
      for y in range(1, len(grid) - 1):
         if grid[x][y] > grid[x - 1][y] and grid[x][y] > grid[x + 1][y] and grid[x][y] > grid[x][y - 1] and grid[x][y] > grid[x][y + 1]:
             new_grid[x][y] = "X"

   for k in range(len(new_grid)):
      grid[k] = "".join(new_grid[k])


   return grid
