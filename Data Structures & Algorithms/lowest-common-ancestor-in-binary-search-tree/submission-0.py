# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def bst(root):
            if p.val < root.val and q.val < root.val:
                return bst(root.left)
            if p.val > root.val and q.val > root.val:
                return bst(root.right)
            else:
                return root
        return bst(root)