n = int(input("Enter number of vertices: "))

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

source = int(input("Enter source vertex: "))

distance = [float("inf")] * n
visited = [False] * n

distance[source] = 0

for _ in range(n):

    minimum = float("inf")
    current = -1

    for i in range(n):
        if not visited[i] and distance[i] < minimum:
            minimum = distance[i]
            current = i

    if current == -1:
        break

    visited[current] = True

    for j in range(n):
        if graph[current][j] != 0:
            new_distance = distance[current] + graph[current][j]

            if new_distance < distance[j]:
                distance[j] = new_distance

for i in range(n):
    print(source, "to", i, "=", distance[i])
