import picounicorn
import random
import time

grid_w = 16
grid_h = 7

picounicorn.init()

# initialise random grid and empty next grid
grid = [[random.randint(0, 1) for col in range(grid_w)] for row in range(grid_h)]
next_grid = [[0 for col in range(grid_w)] for row in range(grid_h)]
    
#update grid
def next_generation(grid, next_grid):
    for row in range(grid_h):
        for col in range(grid_w):
            # get live neighbours
            live_neighbours = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if not (i == 0 and j == 0):
                        live_neighbours += grid[((row + i) % grid_h)][((col + j) % grid_w)]          
            
            # process rules
            if live_neighbours < 2 or live_neighbours > 3:
                next_grid[row][col] = 0
            elif live_neighbours == 3 and grid[row][col] == 0:
                next_grid[row][col] = 1
            else:
                next_grid[row][col] = grid[row][col]
    return next_grid

# display grid on unicorn
def display_grid(grid, picounicorn, w, h):
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 0:
                picounicorn.set_pixel(x, y, 0, 0, 0)
            else:
                picounicorn.set_pixel(x, y, 100, 100, 150)

display_grid(grid, picounicorn, grid_w, grid_h)
next_grid = next_generation(grid, next_grid)

while True:
    time.sleep_ms(100)
    display_grid(next_grid, picounicorn, grid_w, grid_h)
    next_grid = next_generation(next_grid, next_grid)
