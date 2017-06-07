
#coding=utf-8
"""
Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input: 
         1
       /   \
      2     3
Output: 1
Explanation: 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1

"""
import tree

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0

        def find(root):
            if root is None:
                return 0
            left_sum = find(root.left)
            right_sum = find(root.right)
            self.sum += abs(left_sum - right_sum)
            #返回左子树加上右子树和根结点的值
            return root.elem + left_sum + right_sum
        find(root)
        return self.sum


elems=range(1,4)#生成十个数据作为树节点
treeNode=tree.Tree()#新建一个树对象
for elem in elems:
    treeNode.add(elem) #逐个加入树的节点

ss=Solution()
print ss.findTilt(treeNode.root)
