MOD = 1000000009

# Function to perform modular exponentiation
def mod_pow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

# Read input from stdin.txt
with open("stdin.txt", "r") as input_file:
    N, M = map(int, input_file.readline().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input_file.readline().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

# Count the number of connected components using Depth-First Search
def dfs(node, visited):
    size = 1
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            size += dfs(neighbor, visited)
    return size

visited = [False] * N
even_components = []
odd_components = []

for i in range(N):
    if not visited[i]:
        component_size = dfs(i, visited)
        if component_size % 2 == 0:
            even_components.append(component_size)
        else:
            odd_components.append(component_size)

# Calculate the number of ways to make all intersections even
total_ways = 1
for component_size in even_components:
    total_ways = (total_ways * mod_pow(2, component_size, MOD)) % MOD

# Output the result to stdout.txt
with open("stdout.txt", "w") as output_file:
    output_file.write(str(total_ways))
