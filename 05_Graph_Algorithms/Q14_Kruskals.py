n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

for _ in range(e):
    u, v, w = map(int, input("Enter u v weight: ").split())
    edges.append((w, u, v))

edges.sort()

parent = list(range(n))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a
        return True

    return False


cost = 0

print("Minimum Spanning Tree:")

for w, u, v in edges:
    if union(u, v):
        print(u, "-", v, ":", w)
        cost += w

print("Minimum Cost:", cost)
