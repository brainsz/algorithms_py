#coding=utf-8

'''
二叉树中和为某一值得路径
'''

import copy
class Solution:
    def FindPath(self,root,expectNumber):
        if root is None:
            return []
        rest=expectNumber
        pathList=[]
        path=[]
        self.findallpath(root,rest,pathList,path)
        return pathList
    def findallpath(self,root,rest,pathlist,path):
        if root is None:
            return
        path.append(root.val)
        root-=root.val
        if root.left is None and root.right is None:
            if rest==0:
                pathlist.append(copy.deepcopy(path))
        self.findallpath(root.left,rest,pathlist,path)
        self.findallpath(root.right,rest,pathlist,path)
        path.pop()