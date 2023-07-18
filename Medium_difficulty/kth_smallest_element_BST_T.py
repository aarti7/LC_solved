
'''
Q: https://leetcode.com/problems/kth-smallest-element-in-a-bst

Given the root of a binary search tree, and an integer k, return the kth smallest value 1-indexed) of all the values of the nodes in the tree.

A: https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/997938017/
'''



def kthSmallest(self, root: TreeNode, k: int) -> int:
    stack = []
    curr = root

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        curr = curr.right

