#coding=utf-8

"""
94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import tree
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        my_stack=[]
        res=[]
        node=root
        while node or my_stack:
            while node:
                my_stack.append(node)
                node=node.left#找到最左边的节点
            node=my_stack.pop() #弹出最后一个节点
            res.append(node.val) #加入到list中
            node=node.right
        return res


elems=range(1,4)#生成十个数据作为树节点
treeNode=tree.Tree()#新建一个树对象
for elem in elems:
    treeNode.add(elem) #逐个加入树的节点

ss=Solution()
print ss.inorderTraversal(treeNode.root)