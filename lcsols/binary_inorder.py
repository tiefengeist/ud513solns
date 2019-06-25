class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inOrder(self, root):
        res, stack = [], [(root, False)]
        while stack:
            root, visited = stack.pop()
            if root is None:
                continue
            if visited:
                res.append(root.val)
            else:
                stack.append((root.right, False))
                stack.append((root, True))
                stack.append(root.left, False)
