# 0 - пусто
# 1 - свежий апельсин
# 2 - тухлый апельсин

from collections import deque


# . . 1 .
# 2 1 . .
# . . 2 .


# 1 1 1 .
# 2 1 . .
# 1 1 1 .



def find_largest_path(m):
    max_age = 0
    rotten = deque()

    for i, line in enumerate(m):
        for j, item in enumerate(line):
            if item != 2:
                continue

            rotten.append(((i, j), max_age))

    def neighbours(r):
        i, j = r

        for i, j in (
            (i - 1, j),
            (i + 1, j),
            (i, j + 1),
            (i, j - 1),
        ):
            if i < 0 or i >= len(m):
                continue
            if j < 0 or j >= len(m[0]):
                continue

            yield i, j

    while rotten:
        r, age = rotten.popleft()
        for pos in neighbours(r):
            i, j = pos

            if m[i][j] != 1:
                continue

            m[i][j] = 2
            rotten.append((pos, age + 1))

        max_age = max(max_age, age)

    return max_age


# . . 1 .
# 2 1 . .
# 1 1 1 .

x = find_largest_path(
    [
        [0, 0, 1, 0],
        [2, 1, 0, 0],
        [1, 1, 1, 0],
    ],
)

print(x)

x = find_largest_path(
    [
        [0, 0, 1, 0],
        [2, 1, 0, 0],
        [0, 0, 0, 0],
    ],
)

print(x)

