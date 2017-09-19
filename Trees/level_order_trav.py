#
# Level Order Traversal
# Implement a traversal where elements are printed left to right, level
# by level
#

def levelOrder(root):

    # Easy to treat list as a queue, just pop from front!
    q = [root]

    while q:
        cur = q.pop(0)
        print(cur.data)

        if (cur.left):
            q.append(cur.left)
        if (cur.right):
            q.append(cur.right)
