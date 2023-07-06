'''
Q: https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.

A: https://leetcode.com/problems/invert-binary-tree/submissions/988129178/

'''


def invertTree(self, root: TreeNode) -> TreeNode:
    if not root:
        return None

    tmp = root.left
    root.left = root.right
    root.right = tmp

    self.invertTree(root.left)
    self.invertTree(root.right)
    return root