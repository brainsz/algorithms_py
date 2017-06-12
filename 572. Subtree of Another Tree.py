# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isTheSame(s,t):
            #如果两个数都到达叶子节点,则相等
            if s==None and t==None:
                return True
            #当其中一个已经到达但是另外一个没有到达，返回False
            if (s!=None and t==None) or (s==None and t!=None):
                return False
            #当前val相等,继续对左右子树做同样的事情,如果都为True,返回True
            if (s.val==t.val ) and isTheSame(s.left,t.left) and isTheSame(s.right,t.right):
                return True
            return False

        if s==None:
            return False
        if(s.val==t.val) and isTheSame(s,t):
            return True
        else:
            return isSubtree(s.left,t) or isSubtree(s.right,t)
        return False
