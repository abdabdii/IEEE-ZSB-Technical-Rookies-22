class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        newNode = Node(val)
        if self.root is None:
            self.root = newNode
            return
        cur = self.root
        while cur:
            if val < cur.info:
                if cur.left is None:
                    cur.left = newNode
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = newNode
                    return
                cur = cur.right


# problem at https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem
