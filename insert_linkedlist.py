#
# Insert Node at Specific Position in linked List
#
# Insert a node at a specific position in a linked list. The given
# list may be null / empty.
#

class Node(object):
    def __init(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def InsertNth(head, data, position):
    current = head

    # Handle NULL list
    if not head: return Node(data)

    # Handle inserting at head of list
    if position == 0:
        return Node(data, head)

    # Determine insertion position
    for i in range(position - 1):
        current = current.next

    new_node = Node(data, current.next)
    current.next = new_node
    return head
