#
# Preorder Traversal
# Data, Left, Right
#

def postOrder(root):
    if root:
        print(root.data)
        postOrder(root.left)
        postorder(root.right)
