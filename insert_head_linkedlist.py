#
# Insert Node at the Head of Linked List
#
# Given the head of a linked list, insert a node at the head of the
# linked list and return the new head node. The existing head may be null.
#

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Insert(head, data):
    return Node(data, head)
