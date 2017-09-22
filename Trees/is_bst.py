#
# Is Binary Search Tree
# Determine if a given tree is a valid binary search tree
#

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkBST(root):
    return check_bounds(root, -float("inf"), float("inf"))
    
    
def check_bounds(root, minimum, maximum):
    
    # Reaching base case (null node) indicates validity
    if not root:
        return True
    
    # If value falls outside of BST bounds at this level, return false
    if root.data <= minimum or root.data >= maximum:
        return False
    
    # Check left and right subtrees, updating min/max bounds for nodes on this path
    return check_bounds(root.left, minimum, root.data) and\
            check_bounds(root.right, root.data, maximum)
