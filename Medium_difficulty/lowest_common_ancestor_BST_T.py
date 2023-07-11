'''
Q: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 
A: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/992178095/

'''

def lowestCommonAncestor(
    self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
) -> "TreeNode":
    cur = root
    while cur:
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        else:
            return cur
