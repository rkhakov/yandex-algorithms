"""
ID: 70245737
ПРИЦИП РАБОТЫ
    1. Находим нужный узел по ключу.
    Если искомое значение меньше значений текущей ноды, идем в левое поддерево, иначе в правое

    2. После того как нода найдена, определяем есть ли у нее потомки
    - Если дочерних узлов нет, то просто удаляем узел
    - Если есть один из двух дочерних узлов, удаляемый узел заменяется потомком
    - Если имеются 2 потомка, то ищем минимальный в правом поддереве, заменяем его вместо удаляемого

    https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/

ВРЕМЕННАЯ СЛОЖНОСТЬ:
    O(h) - где h высота дерева
    O(n) - худший случай, если дерево несбалансированно, то может потребоваться пройтись по каждому элементу

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ:
    O(h) - где h высота дерева. Для хранения стека вызовов рекурсии
"""


# Comment it before submitting
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def remove(root, key):
    if root is None:
        return root

    if key < root.value:
        root.left = remove(root.left, key)
        return root
    elif key > root.value:
        root.right = remove(root.right, key)
        return root
    
    if root.left is None and root.right is None:
        return None
    
    if root.left is None:
        return root.right

    if root.right is None:
        return root.left
    
    parent = root
    current = root.right
    while current.left is not None:
        parent, current = current, current.left
    
    if parent != root:
        parent.left = current.right
    else:
        parent.right = current.right
    
    root.value = current.value
    return root


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    newHead = remove(node7, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8
