#coding=utf-8

'''
求一个二叉树的镜像
思路：前序遍历树的每一个节点，如果有左右节点，则交换
'''

class TreeNode(object):
    def __init(self,data):
        self.val=data
        self.left=None
        self.right=None

class Solution(object):
    def MirrorRecursively(self,root):
        if root is None:
            return;
        if root.left is None and root.right==None:
            return;
        pTemp=root.left
        root.left=root.right
        root.right=pTemp
        if root.left:
            self.MirrorRecursively(root.left)
        if root.right:
            self.MirrorRecursively(root.right)
