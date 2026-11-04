#Task 3

class Node:
    def __init__(self, grade):
        self.grade = grade
        self.left = None
        self.right = None

def count_leaves(node):
    if not node:
        return 0
    # A leaf has no children
    if not node.left and not node.right:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

def get_height(node):
    if not node:
        return 0
    # 1 for current level + max depth of subtrees
    return 1 + max(get_height(node.left), get_height(node.right))

def count_nodes(node):
    if not node:
        return 0
    # 1 (current) + left nodes + right nodes
    return 1 + count_nodes(node.left) + count_nodes(node.right)


# Build tree manually
root = Node(85)
root.left = Node(75)
root.right = Node(92)

root.left.left = Node(70)
root.left.right = Node(80)

root.right.left = Node(90)
root.right.right = Node(99)

# Print results
print("Root grade:", root.grade)
print("Leaves count:", count_leaves(root))
print("Tree height:", get_height(root))
print("Total nodes:", count_nodes(root))