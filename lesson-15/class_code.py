# array of numbers and k
# n[i] + n[j] == k

# массив не отсортирован
# числа только интовые


def find_two_sum(num_arr: list[int], target: int) -> list[int]:
    if len(num_arr) < 2:
        return []

    seen = {}
    for i, num in enumerate(num_arr):
        compl = target - num
        if compl in seen:
            return [seen[compl], i]

        seen[num] = i

    return []


assert find_two_sum([0, 1, 2, 3, 4, 5], 7) == [2, 5]
assert find_two_sum([1], 5) == []
assert find_two_sum([1, 2, 3], 9) == []
assert find_two_sum([2, 3], 5) == [0, 1]
assert find_two_sum([1, 1], 2) == [0, 1]


class LRU:
    def __init__(self, limit: int):
        if limit <= 0:
            raise ValueError(limit)

        self.__cache = {}
        self.__limit = limit

    def get(self, key, default=None):
        if key not in self.__cache:
            return default

        val = self.__cache[key]
        del self.__cache[key]
        self.__cache[key] = val
        return val

    def set(self, key, value):
        if key in self.__cache:
            del self.__cache[key]

        if self.__limit <= len(self.__cache):
            for lru_key in self.__cache:
                del self.__cache[lru_key]
                break

        self.__cache[key] = value



# next(iter(self.__cache))
# del {}[1]

# LRU cache

# [k -> v] + stack
# [k -> v] + priority queue

lru = LRU(limit=2)
lru.set(1, 1)
lru.set(2, 2)
lru.set(3, 3)  # -> del 1

lru.set(1, 1)
lru.set(2, 2)
x = lru.get(1)
lru.set(3, 3)  # -> del 2


#      5
#  3      9
#1   4  7   11


#      5
#   3
#1

# kebab-case это когда вот так
# BST -> sl list в порядке возрастания

TreeNode:
    val: Any
    left: TreeNode
    right: TreeNode





def bst_to_list(root: TreeNode):
    if not root:
        return

    stack = []
    current = root
    list_node = None
    result = None

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()

        if not list_node:
            list_node = ListNode(current.value)
            result = list_node
        else:
            list_node.next = ListNode(current.value)
            list_node = list_node.next

        current = current.right

    return result



# 1 -> 2 -> 3: 3 -> 2 -> 1
# 1 <- 2

class ListNode:
    val: Any
    next: ListNode


def reverse(node):
    prev = None #
    cur = node #1 -> 2

    while cur:
        nnextt = cur.next # 2 -> 3, 3, none
        cur.next = prev # 1 - > none, 1, 2,
        prev = cur #1, 2, 3,
        cur = nnextt# 2, 3,

    return prev


