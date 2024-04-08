#     2
#   1    20
# 30 5  6  29

[2, 20, 30]


class Node:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


node = Node(1, 1)
n2 = Node(2, 2)
node.left = n2


def max_elements_on_level(tree):
    res_list = list()
    if not tree:
        return []

    list_levels = [tree]

    while list_levels:

        next_list_levels = []
        max_elment = list_levels[0].val

        for node in list_levels:
            max_elment = max(max_elment, node.val)
            if node.left:
                next_list_levels.append(node.left)
            if node.right:
                next_list_levels.append(node.right)

        res_list.append(max_elment)

        list_levels = next_list_levels

    return res_list


assert max_elements_on_level(node) == [1, 2]
assert max_elements_on_level(n2) == [2]
assert max_elements_on_level(None) == []

print("ok")



# check whether given tree is a valid red-black tree
# 1. root is black
# 2. each red node has black parent
# 3. "black height" is constant for all nodes
# -- OK 4. leafs are all black

import collections


class RBNode:
    def __init__(self, key, val, color="red", parent=None, left=None, right=None):
        self.key = key
        self.val = val
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right


def is_red_black_tree(t: RBNode):
    if not t:
        return False

    if t.color != "black":
        return False

    # if left child is present, it must be smaller than parent
    nodes = collections.deque()
    nodes.append((0, (None, None), t))

    leaf_h = None

    while nodes:
        # BFS
        h, (left, right), node = nodes.popleft()

        if node.color == "red" and node.parent.color != "black":
            # violates property 2
            return False

        if node.key < left or node.key > right:
            # not a binary search tree
            return False

        if node.left:
            left_, right_ = left, node.key
            nodes.append((h + node.color == "black", (left_, right_), node.left))

        if node.right:
            left_, right_ = node.key, right
            nodes.append((h + node.color == "black", (left_, right_), node.right))

        if not node.left and not node.right:
            if leaf_h is None:
                leaf_h = h

            if leaf_h != h:
                return False


    return True

    #

    #      4
    #   2     6
    # 1   3   6   7


