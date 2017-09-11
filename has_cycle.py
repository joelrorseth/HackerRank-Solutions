class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

def has_cycle(head):
    node_map = {}

    while (head):
        if head.data in node_map:
            return True
        else:
            node_map[head.data] = 1
            head = head.next

    return False

def main():

    n3 = Node(4)
    n2 = Node (3, n3)
    n1 = Node(2, n2)
    head = Node(1, n1)

    # Make the linked list a cycle
    n3.next = n1

    print(has_cycle(head))

main()
