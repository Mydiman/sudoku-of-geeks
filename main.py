# N is the size of the 2D matrix   N*N
N = 9
 
# A utility function to print grid
def printing(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()
 
# Checks whether it will be
# legal to assign num to the
# given row, col
def isSafe(grid, row, col, num):
   
    # Check if we find the same num
    # in the similar row , we
    # return false
    for x in range(9):
        if grid[row][x] == num:
            return False
 
    # Check if we find the same num in
    # the similar column , we
    # return false
    for x in range(9):
        if grid[x][col] == num:
            return False
 
    # Check if we find the same num in
    # the particular 3*3 matrix,
    # we return false
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
# Takes a partially filled-in grid and attempts
# to assign values to all unassigned locations in
# such a way to meet the requirements for
# Sudoku solution (non-duplication across rows,
# columns, and boxes) */
def solveSudoku(grid, row, col):
   
    # Check if we have reached the 8th
    # row and 9th column (0
    # indexed matrix) , we are
    # returning true to avoid
    # further backtracking
    if (row == N - 1 and col == N):
        return True
       
    # Check if column value  becomes 9 ,
    # we move to next row and
    # column start from 0
    if col == N:
        row += 1
        col = 0
 
    # Check if the current position of
    # the grid already contains
    # value >0, we iterate for next column
    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)
    for num in range(1, N + 1, 1):
       
        # Check if it is safe to place
        # the num (1-9)  in the
        # given row ,col  ->we
        # move to next column
        if isSafe(grid, row, col, num):
           
            # Assigning the num in
            # the current (row,col)
            # position of the grid
            # and assuming our assigned
            # num in the position
            # is correct
            grid[row][col] = num
 
            # Checking for next possibility with next
            # column
            if solveSudoku(grid, row, col + 1):
                return True
 
        # Removing the assigned num ,
        # since our assumption
        # was wrong , and we go for
        # next assumption with
        # diff num value
        grid[row][col] = 0
    return False
 
# Driver Code
 
# 0 means unassigned cells
from random import randint, shuffle
def random_sub_board(count):
  global grid
  grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
  for i in range(count):
    while True:
      x_rand = randint(0, 8)
      y_rand = randint(0, 8)
      if grid [y_rand][x_rand] == 0:
        temp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
          temp [grid [j][x_rand]] = 0
          temp [grid [y_rand][j]] = 0
        x_rand_box = x_to_xbox(x_rand)
        y_rand_box = y_to_ybox(y_rand)
        for j in range(y_rand_box, y_rand_box + 3):
          for k in range(x_rand_box, x_rand_box + 3):
            temp [grid [j][k]] = 0
        if temp != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
          while temp [0] == 0:
            shuffle(temp)
          grid [y_rand][x_rand] = temp [0]
          break

def x_to_xbox(x):
  while x != 0 and x != 3 and x != 6:
    x -= 1
  return x

def y_to_ybox(y):
  while y != 0 and y != 3 and y != 6:
    y -= 1
  return y

random_sub_board(30)
if (solveSudoku(grid, 0, 0)):
    printing(grid)
else:
    print("no solution  exists ")
