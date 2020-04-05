# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


# this class represents a node in a binary tree
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


# this function reads the input and returns binary tree built from the input
# based on the sample input stated in main() function, below is the value of n, key, left, and right list
# n = 10
# key = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# left = [7, -1, -1, 8, 3, -1, 1, 5, -1, -1]
# right = [2, -1, 6, 9, -1, -1, -1, 4, -1, -1]
def read():
    n = int(sys.stdin.readline())
    key = [0 for i in range(n)]
    left = [0 for i in range(n)]
    right = [0 for i in range(n)]
    for i in range(n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      key[i] = a
      left[i] = b
      right[i] = c

    tree = [Node(key[i], left[i], right[i]) for i in range(n)]

  # build a binary tree
    for i in range(n):
        if tree[i].left != -1:
            temp = tree[i].left
            tree[i].left = tree[temp]
        if tree[i].right != -1:
            temp = tree[i].right
            tree[i].right = tree[temp]

    return tree[0] # return the root of the binary tree


# this function traverses through a binary tree in an in-order fashion
# and returns the traversal path taken
def inOrder(tree, result):
    # if the current tree (represented as a node) is a leaf, append the tree's key (node's key) to result to document the traversal path and then return to the tree's parent
    if tree.left == -1 and tree.right == -1:
        result.append(tree.key)
        return

    # if the subtree has a left child, traverse down the left child subtree
    if tree.left != -1:
        inOrder(tree.left, result)

    # append the tree's key after done traversing its left child
    result.append(tree.key)

    # traverse down the tree's right child(
    if tree.right != -1:
        inOrder(tree.right, result)

# this function traverses through a binary tree in a pre-order fashion
# and returns the traversal path taken
def preOrder(tree, result):
    # if the current tree (represented as a node) is a leaf, append the tree's key (node's key) to result to document the traversal path
    # and then return to the tree's parent
    if tree.left == -1 and tree.right == -1:
        result.append(tree.key)
        return
    # append the tree's key to result before traversing its left and right child
    result.append(tree.key)

    # if the tree has a left child, traverse down that path
    if tree.left != -1:
        preOrder(tree.left, result)

    # if the tree has a right child, traverse down that path
    if tree.right != -1:
        preOrder(tree.right, result)


# this function traverses through a binary tree in a post-order fashion
# and returns the traversal path taken
def postOrder(tree, result):
    # if the current tree (represented as a node) is a leaf,
    # append the tree's key to result to document the traversal path and then return to the key's parent
    if tree.left == -1 and tree.right == -1:
        result.append(tree.key)
        return

    # if the tree has a left child, traverse down that path
    if tree.left != -1:
        postOrder(tree.left, result)

    # if the tree has a right child, traverse down that path
    if tree.right != -1:
        postOrder(tree.right, result)

    # append the tree's key to result after done traversing through its left descendents and right descendants
    result.append(tree.key)


# this function reads the input, build a binary tree from the input,
# traverse through the tree in inOrder, preOrder, and postOrder
# and prints out the traversal paths
# input format:
#### The first line contains the number of vertices 𝑛. The vertices of the tree are numbered from 0 to 𝑛 − 1. Vertex 0 is the root.
#### The next 𝑛 lines contain information about vertices 0, 1, ..., 𝑛−1 in order. Each of these lines contains
#### three integers 𝑘𝑒𝑦𝑖, 𝑙𝑒𝑓𝑡𝑖 and 𝑟𝑖𝑔ℎ𝑡𝑖 — 𝑘𝑒𝑦𝑖 is the key of the 𝑖-th vertex, 𝑙𝑒𝑓𝑡𝑖 is the index of the left
#### child of the 𝑖-th vertex, and 𝑟𝑖𝑔ℎ𝑡𝑖 is the index of the right child of the 𝑖-th vertex. If 𝑖 doesn’t have
#### left or right child (or both), the corresponding 𝑙𝑒𝑓𝑡𝑖 or 𝑟𝑖𝑔ℎ𝑡𝑖 (or both) will be equal to −1.
# output format:
#### Print three lines. The first line should contain the keys of the vertices in the in-order
#### traversal of the tree. The second line should contain the keys of the vertices in the pre-order traversal
#### of the tree. The third line should contain the keys of the vertices in the post-order traversal of the tree
# example:
# input:
# 10
# 0 7 2
# 10 -1 -1
# 20 -1 6
# 30 8 9
# 40 3 -1
# 50 -1 -1
# 60 1 -1
# 70 5 4
# 80 -1 -1
# 90 -1 -1
# tree built from the input using read() operation
#           0 (root)
#         /  \
#       70   20
#     /  \     \
#   50   40    60
#       /     /
#     30    10
#    / \
#  80  90
# below is the output in this order: in-order --> pre-order --> post-order traversal path
# 50 70 80 30 90 40 0 20 10 60
# 0 70 50 40 30 80 90 20 60 10
# 50 80 90 30 40 70 10 60 20 0
def main():
    tree = read()
    result_inorder = []
    result_preorder = []
    result_postorder = []
    inOrder(tree, result_inorder)
    preOrder(tree, result_preorder)
    postOrder(tree, result_postorder)
    print(' '.join(str(x) for x in result_inorder))
    print(' '.join(str(x) for x in result_preorder))
    print(' '.join(str(x) for x in result_postorder))


threading.Thread(target=main).start()
