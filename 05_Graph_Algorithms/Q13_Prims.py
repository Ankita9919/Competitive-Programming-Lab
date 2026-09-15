n = int(input("Enter number of vertices: "))

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

selected = [False] * n
selected[0] = True

cost = 0

print("Minimum Spanning Tree:")

for _ in range(n - 1):
    minimum = float("inf")
    x = 0
    y = 0

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(x, "-", y, ":", minimum)

    cost += minimum
    selected[y] = True

print("Minimum Cost:", cost)
