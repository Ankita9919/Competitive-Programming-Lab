n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

for _ in range(e):
    u, v, w = map(int, input("Enter u v weight: ").split())
    edges.append((w, u, v))

edges.sort()

parent = list(range(n))

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x


cost = 0

print("Minimum Spanning Tree:")

for w, u, v in edges:
    pu = find(u)
    pv = find(v)

    if pu != pv:
        parent[pu] = pv
        print(u, "-", v, ":", w)
        cost += w

print("Total Cost:", cost)
