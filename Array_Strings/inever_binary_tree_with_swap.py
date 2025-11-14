from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class InvertBinaryTreeSwap:
    def invert_binary_tree_swap(self, root: Optional[TreeNode]) -> TreeNode:
        if not root:
            return None

        #swap the node
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invert_binary_tree_swap(root.left)
        self.invert_binary_tree_swap(root.right)

        return root