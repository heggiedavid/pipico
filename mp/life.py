import random
 
def get_live_neighbours(row, col):
    global grid
    live = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                live += grid[((row + i) % 11)][((col + j) % 24)]
    return live

def update_grid():
    global grid
    for row in range(11):
        for col in range(24):
            living = get_live_neighbours(row, col)
            if living < 2 or living > 3:
                grid[row][col] = 0
            elif living == 3 and grid[row][col] == 0:
                grid[row][col] = 1
            else:
                grid[row][col] = grid[row][col]

grid = [[0] * 25] * 12
for f in range(0, 25):
    for g in range(0, 12):
        grid[g][f] = random.randint(0, 1)
        
for row in range(0, 12):
    for col in range(0, 25):
        grid[row][col] = random.randint(0, 1)


update_grid()