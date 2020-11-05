import heapq
n = 8
edges = [[0, 1, 7], [0, 2, 2], [0, 3, 3], [2, 6, 10], [2, 4, 4], [3, 4, 5], [3, 5, 2], [4, 5, 2], [4, 7, 2], [5, 7, 7]]

node_list = {}

for begin, end, cost in edges:
    if begin not in node_list:
        node_list[begin] = set()

    node_list[begin].add((end, cost))

    if end not in node_list:
        node_list[end] = set()

    node_list[end].add((begin, cost))

print(node_list)

p_q = [(0, 0)]

vertices_cost = [float("inf")] * n
vertices_cost[0] = 0
order = []

while p_q:
    cost, vertex = heapq.heappop(p_q)
    order.append(vertex)
    for neighbor, edge_cost in node_list[vertex]:
        new_cost = cost + edge_cost
        if new_cost < vertices_cost[neighbor]:
            vertices_cost[neighbor] = min(vertices_cost[neighbor], new_cost)
            heapq.heappush(p_q, (new_cost, neighbor))

print(vertices_cost)
print(order)