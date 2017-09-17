#
# Delete Node from a Linked List
#
# Given a linked list, delete the node at a given position. Note
# that the list may become empty after the deletion. Return the
# new head of the list.
#

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Delete(head, position):
    current = head

    # Empty list
    if not head: return None;

    # Deleting first node
    if position == 0:
        return head.next

    for i in range(position - 1):
        current = current.next


    current.next = current.next.next
    return head
