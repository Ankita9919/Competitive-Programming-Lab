n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[] for _ in range(n)]

for _ in range(e):
    u, v = map(int, input("Enter edge: ").split())

    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting vertex: "))

visited = [False] * n


def dfs(node):
    visited[node] = True
    print(node, end=" ")

    for neighbour in graph[node]:
        if not visited[neighbour]:
            dfs(neighbour)


print("DFS:")
dfs(start)
