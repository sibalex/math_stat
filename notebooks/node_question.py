class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#def inorder(node):
#    if node is None:
#        return None
#    inorder(node.left)
#    print(node.val)
#    inorder(node.right)


def inorder_iterativuh(node):
    stack = []
    while (stack or node is not None):
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.val)
            node = node.right


root = Node(12)
root.left = Node(6)
root.right = Node(4)


#inorder(root)
inorder_iterativuh(root)

