#Task 5
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Helper method to fill the tree
    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return

        curr = self.root
        while True:
            # Smaller values go left, larger or equal go right
            if val < curr.val:
                if not curr.left:
                    curr.left = Node(val)
                    break
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = Node(val)
                    break
                curr = curr.right

    def find_min(self):
        # Check if the tree is empty to prevent crashes
        if not self.root:
            return "Tree is empty"

        curr = self.root
        # Keep going left until we hit the end
        while curr.left:
            curr = curr.left

        return curr.val

    def find_max(self):
        if not self.root:
            return "Tree is empty"

        curr = self.root
        # Keep going right until we hit the end
        while curr.right:
            curr = curr.right

        return curr.val


# --- Testing ---

tree = BST()

print("Test 1 (Empty):")
print("Min:", tree.find_min())
print("Max:", tree.find_max())

# Add some numbers
tree.insert(15)
tree.insert(10)
tree.insert(20)
tree.insert(8)
tree.insert(12)
tree.insert(25)

print("\nTest 2 (Filled):")
print("Min:", tree.find_min())
print("Max:", tree.find_max())