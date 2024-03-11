import dataclasses
from typing import Optional


@dataclasses.dataclass
class Node:
    val: int
    next: Optional["Node"] = None

# [1] -> [2] -> [3]: del 2
# [1] -> [3]

# [1] -> [2] -> [3]: del 1
# [2] -> [3]

# [1] -> [2]: del 2
# [1]

def remove(node, k):
    if(node is None):
        return None
    if(node.val == k):
        return node.next

    head = node

    current_node = node
    while current_node.next is not None:
        prev_node = current_node
        current_node = node.next
        if current_node.val == k:
            prev_node.next = current_node.next
            break

    return head

d = {1 : 1, 2: 2, 3: 3, 5: 5, 4:4}
# [1, 2, 3, 5, 4]



# LRU-cache
class LRUCache:
    def __init__(self, limit):
        self.limit = limit
        self.cache = {}

    def get(self, key):
        if key in self.cache:
            val = self.cache[key]
            del self.cache[key]
            self.cache[key] = val
            return val

    def set(self, key, value):
        if key in self.cache:
            self.cache[key] = value
        else:
            if len(self.cache) == limit:
                del self.cache[next(iter(self.cache))]
            self.cache[key] = value



# [1, 2, 3, 4, 5, 6, 7, 8], 3 -> 6
# [1, 2, 3, 4, 5, 6, 7, 8], 1 -> 8
# [1, 2, 3, 4, 5, 6, 7, 8], 8 -> 1

import heapq


# heapq.heappush(heap, elem)
# heapq.heappop(heap)



class NLarge:
    def __init__(self, n):
        self.n = n
        self.h = []

    def add(self, elem) -> int:
        heapq.heappush(self.h, elem)

        if len(self.h) >= self.n:
            while len(self.h) > self.n:
                heapq.heappop(self.h)
            return self.h[0]
        return None




nl = NLarge(3)
assert nl.add(1) == None
assert nl.add(2) == None
assert nl.add(3) == 1
assert nl.add(0) == 1
assert nl.add(5) == 2
assert nl.add(4) == 3

print("ok")
