# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):  
        self.value = value
        self.right = right
        self.left = left


def solution(root):
    def get_height(node):
        if node is None:
            return 0
        return max(get_height(node.left), get_height(node.right)) + 1

    if root is None:
        return True

    height_diff = abs(get_height(root.right) - get_height(root.left))
    balanced = solution(root.left) and solution(root.right)
    return True if 0 <= height_diff <= 1 and balanced else False


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)