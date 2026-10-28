# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            
            l1 = t1.left
            r1 = t1.right
            l2 = t2.left
            r2 = t2.right

            if t1.val != t2.val:
                return False
            return dfs(l1, l2) and dfs(r1, r2)
        
        return dfs(p, q)