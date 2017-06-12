#coding=utf-8

"""
144. Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3]
"""

import tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        my_stack=[]
        res=[]
        node=root
        while node or my_stack:
            while node:#从根结点开始，找到左子树
                res.append(node.val)
                my_stack.append(node)
                node=node.left
            print my_stack
            node=my_stack.pop()#while结束表示当前节点node为空,即前一个节点没有左子树了
            node =node.right #开始查看它的右子树
        return res


elems=[1,4,3,2]#生成十个数据作为树节点
treeNode=tree.Tree()#新建一个树对象
for elem in elems:
    treeNode.add(elem) #逐个加入树的节点

ss=Solution()
print ss.preorderTraversal(treeNode.root)

