class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def get_node_by_index(item, index):
    while index:
        item = item.next_item
        index -= 1
    return item

def solution(node, idx):
    if idx == 0:
        return node.next_item

    to_delete = get_node_by_index(node, idx)
    if not to_delete:
        return node
    prev = get_node_by_index(node, idx - 1)
    prev.next_item = to_delete.next_item
    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 3)
