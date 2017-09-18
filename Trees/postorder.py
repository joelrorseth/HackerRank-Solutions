#
# Postorder Traversal
# Left, Right, Data
#

def postOrder(root):
    if root:
        postOrder(root.left)
        postorder(root.right)
        print(root.data)
