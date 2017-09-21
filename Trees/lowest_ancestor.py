#
# Lowest Common Ancestor
# Determine the lowest common ancestor of two nodes in a binary search tree
# This is the lowest node from which both given nodes descend from
#

def lca(root , v1 , v2):
    
    while (True):
        
        if root.data < v1 and root.data < v2:
            root = root.right
        
        elif root.data > v1 and root.data > v2:
            root = root.left
        
        else:
            return root
