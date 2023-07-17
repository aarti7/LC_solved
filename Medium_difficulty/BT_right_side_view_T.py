"""
Q: https://leetcode.com/problems/binary-tree-right-side-view

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.



A: https://leetcode.com/problems/binary-tree-right-side-view/submissions/997057525/


"""


def rightSideView(self, root: TreeNode) -> List[int]:
    res = []
    q = collections.deque([root])

    while q:
        rightSide = None
        qLen = len(q)

        for i in range(qLen):
            node = q.popleft()
            if node:
                rightSide = node
                q.append(node.left)
                q.append(node.right)
        if rightSide:
            res.append(rightSide.val)
    return res
