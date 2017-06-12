#coding=utf-8

import tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        

elems=[1,2,3,4,5]#生成十个数据作为树节点
treeNode=tree.Tree()#新建一个树对象
for elem in elems:
    treeNode.add(elem) #逐个加入树的节点

ss=Solution()
print ss.preorderTraversal(treeNode.root)