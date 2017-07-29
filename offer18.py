#coding=utf-8

'''
一个二叉树是否是第二个的子树
'''

class TreeNode(object):
    def __init(self,data):
        self.val=data
        self.left=None
        self.right=None

class Solution(object):
    def isSubtree(self,s,t):
        """
        
        :param s:TreeNode 
        :param t: TreeNode
        :return: bool
        """
        if not s:
            return False
        return self.isEqual(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    def isEqual(self,S,T):
        #以s为根节点，判断S和T是否相等
        if not S and not T:
            return True
        if S and T:
            if S.val!=T.val:
                return False
            return self.isEqual(S.left,T.left) and self.isEqual(S.right,T.right)
        else:
            return False