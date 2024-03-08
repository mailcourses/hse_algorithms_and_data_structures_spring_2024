# найти в дереве элемент или None, если его нет
# Обходом двоичного дерева в глубину (DFS) называется процедура,
# выполняющая в некотором заданном порядке следующие действия с поддеревом:
# ● просмотр (обработка) узла-корня поддерева,
# ● рекурсивный обход левого поддерева,
# ● рекурсивный обход правого поддерева.


#Используется очередь, в которой хранятся вершины, требующие просмотра.
# За одну итерацию алгоритма:
#● если очередь не пуста, извлекается вершина из очереди,
#● посещается (обрабатывается) извлеченная вершина,
#● в очередь помещаются все дочерние.

import collections


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_dfs(root, k):
    if root is None:
        return None

    if root.val == k:
        return root
    else:
        return find_dfs(root.left, k) or find_dfs(root.right, k)



def find_bfs(root, target):
    if not root:
        return None

    que = collections.deque([root])
    # que = [root]

    while que:
        current_node = que.popleft()
        # current_node = que.pop()
        print(current_node.val)

        if current_node.val == target:
            return current_node

        if current_node.left:
            que.append(current_node.left)
        if current_node.right:
            que.append(current_node.right)
    return None


def find_max_bfs(root):
    if not root:
        return []

    que = collections.deque([(root, 0)])

    maximum = []

    while que:
        current_node, node_lvl = que.popleft()
        # print(current_node.val)
        if len(maximum) <= node_lvl:
            maximum.append(current_node.val)

        elif current_node.val > maximum[node_lvl]:
            maximum[node_lvl] = current_node.val

        if current_node.left:
            que.append((current_node.left, node_lvl + 1))
        if current_node.right:
            que.append((current_node.right, node_lvl + 1))

    return maximum


def invert_tree(root):
    if not root:
        return None

    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)


n3 = TreeNode(3)
n1 = TreeNode(1, left=n3)
n2 = TreeNode(2)
root = TreeNode(0, n1, n2)


find_bfs(root, 5)


# assert find_dfs(root, 2) is n2, f"{find_dfs(root, 5)=}"
# assert find_dfs(root, 0) is root, f"{find_dfs(root, 0)=}"
# assert find_dfs(None, 0) is None
# assert find_dfs(root, 5) is None

# assert find_bfs(root, 2) is n2, f"{find_bfs(root, 5)=}"
# assert find_bfs(root, 0) is root, f"{find_bfs(root, 0)=}"
# assert find_bfs(None, 0) is None
# assert find_bfs(root, 5) is None

assert find_max_bfs(root) == [0, 2, 3]
assert find_max_bfs(n3) == [3]
assert find_max_bfs(None) == []



#    7
#  5   10
#3
#  4

#   0
# 2   1
#      3

def traverse_inorder(root):
    st = []
    node = root
    result = []

    while st or node:
        while node:
            st.append(node)
            node = node.left

        node = st.pop()

        print(f"{node.val=}")
        result.append(node.val)

        node = node.right

    return result


print(traverse_inorder(root))

  [3 6 7 8 10 12]
#        8
#    6     10
#  3   7      12

def is_bst(root, left=float('-inf'), right=float('inf')) -> bool:
    if root is None:
        return True

    if not (left <= root.value <= root.right):
        return False

    return (
        is_bst(root.left, left, root.value)
        and is_bst(root.right, root.value, right)
    )


def build_balanced_bst(nums: list[int]) -> TreeNode:
    if len(nums) == 0:
        return None

    # [3 6 7 8 10 12]

    idx = len(nums) // 2
    cur_value = nums[idx]
    node = TreeNode(cur_value)
    node.left = build_balanced_bst(nums[:idx])
    node.right = build_balanced_bst(nums[idx + 1:])
    return node


print('ok')

