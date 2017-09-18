#
# Preorder Traversal
# Data, Left, Right
#

def preOrder(root):
    if root:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)
