# Comment it before submitting
class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left


def solution(root):
    max_root = max_left = max_right = root.value

    if root.left:
        max_left = solution(root.left)
    if root.right:
        max_right = solution(root.right)

    return max(max_root, max_left, max_right)



def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3