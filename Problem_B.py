# Function to perform DFS to find connected regions of cells that can pool water
def dfs(x, y, height):
    # Check if the cell is out of bounds
    if x < 0 or x >= rows or y < 0 or y >= cols or visited[x][y] or garden[x][y] > height:
        return False

    # Mark the cell as visited
    visited[x][y] = True

    # Check if water can pool in this cell
    can_pool_water = True
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and garden[nx][ny] <= height:
            can_pool_water = can_pool_water and dfs(nx, ny, height)

    return can_pool_water

# Read input dimensions from stdin.txt
with open("stdin.txt", "r") as input_file:
    rows, cols = map(int, input_file.readline().split())

    # Read garden heights
    garden = []
    for _ in range(rows):
        row = list(map(int, input_file.readline().split()))
        garden.append(row)

# Initialize visited array
visited = [[False for _ in range(cols)] for _ in range(rows)]

# Initialize total square meters of land that can grow rice
total_square_meters = 0

# Iterate through each cell in the garden
for i in range(rows):
    for j in range(cols):
        # Check if this cell can pool water and add its area to the total
        if not visited[i][j] and dfs(i, j, garden[i][j]):
            total_square_meters += 1

# Write the total square meters of land that can grow rice to stdout.txt
with open("stdout.txt", "w") as output_file:
    output_file.write(str(total_square_meters))
