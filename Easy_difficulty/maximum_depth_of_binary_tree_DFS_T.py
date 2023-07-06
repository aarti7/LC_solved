'''
Q: https://leetcode.com/problems/maximum-depth-of-binary-tree/ 

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


A: https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/988131571/

'''



def maxDepth(self, root: TreeNode) -> int:
    stack = [[root, 1]]
    res = 0

    while stack:
        node, depth = stack.pop()

        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    return res