class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p and q:
            return False
        if not q and p:
            return False
    
        val1 = self.isSameTree(p.left,q.left)
        val2 = self.isSameTree(p.right,q.right)

        return (val1 and val2) and p.val == q.val