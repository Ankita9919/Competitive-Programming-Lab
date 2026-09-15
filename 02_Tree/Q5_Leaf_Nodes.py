class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def count_leaf(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    return count_leaf(root.left) + count_leaf(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Number of leaf nodes:", count_leaf(root))
