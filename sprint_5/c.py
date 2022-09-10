# Comment it before submitting
class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left


def solution(root):
    def is_anagram(node1, node2):
        if node1 is None and node2 is None:
            return True

        if node1 is None or node2 is None:
            return False
        
        result1 = is_anagram(node1.left, node2.right)
        result2 = is_anagram(node1.right, node2.left)
        return node1.value == node2.value and result1 and result2
    
    return is_anagram(root.left, root.right)


def test():
    node1 = Node(3,  None,  None)
    node2 = Node(4,  None,  None)
    node3 = Node(4,  None,  None)
    node4 = Node(3,  None,  None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert solution(node7)