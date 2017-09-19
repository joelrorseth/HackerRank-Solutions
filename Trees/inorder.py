#
# Inorder Traversal
# Left, Data, Right
#

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)
