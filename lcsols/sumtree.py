"""
Transforming binary search tree into greater sum tree (where each node has sum of all nodes greater than itself)
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def toGST(self, root):
        def helper(root, prev):
            if not root:
                return root
                helper(root.right, prev)
                root.val += prev[0]
                prev[0] = root.val
                helper(root.left, prev)
                return root
        prev = [0]
        return helper(root, prev)
