n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

matrix = [[0] * n for _ in range(n)]
adj_list = [[] for _ in range(n)]

for _ in range(e):
    u, v = map(int, input("Enter edge: ").split())

    matrix[u][v] = 1
    matrix[v][u] = 1

    adj_list[u].append(v)
    adj_list[v].append(u)

print("Adjacency Matrix:")
for row in matrix:
    print(row)

print("Adjacency List:")
for i in range(n):
    print(i, "->", adj_list[i])
