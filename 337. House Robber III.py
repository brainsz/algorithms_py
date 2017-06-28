#coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #rob[0]存储的是从叶子节点到当前节点的左右孩子层节点抢劫到的最大值
        #rob[1]存储的是从叶子节点到当前节点抢劫的最大值
        def dfs(root):
            if not root:
                return [0,0]
            robLeft=dfs(root.left)
            robRight=dfs(root.right)
            norobCur=robLeft[1]+robRight[1]
            robCur=max()
