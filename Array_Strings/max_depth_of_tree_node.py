from typing import Optional

class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class MaxDepthTreeNode:
    def max_depth_tree_node(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left = self.max_depth_tree_node(root.left)
        right = self.max_depth_tree_node(root.right)

        return 1 + max(left, right)