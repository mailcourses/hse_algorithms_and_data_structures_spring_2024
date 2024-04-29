# n, [(1, 2), (2, 3), (1, 4), (3, 5)], x, y
# V = {1 .. n}
# 1 <= x, y <= n

# n = 6
# 1 <-> 2 -> 3 -> 5
# |     ^
# |     |
# 4  -> 7         6

# x = 1, y = 5 -> 3
# x = 1, y = 6 -> None

from collections import deque, defaultdict


def min_dist(n, edges, x, y) -> int | None:

    queue = deque([(x, 0)])
    graph = defaultdict(list)

    visited = [False] * (n + 1)
    visited[x] = True

    for edge in edges:
        graph[edge[0]].append(edge[1])

    while queue:
        current, dist = queue.popleft()

        for neighbor in graph[current]:
            if visited[neighbor]:
                continue

            if y == neighbor:
                return dist + 1

            visited[neighbor] = True
            queue.append([neighbor, dist + 1])

    return None
