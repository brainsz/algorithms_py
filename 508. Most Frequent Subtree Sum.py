#coding=utf-8

"""
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined 
as the sum of all the node values formed by the subtree rooted at that node (including the node itself). 
So what is the most frequent subtree sum value? If there is a tie, return all the values 
with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
"""
class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None


class Solution(object):
    def findFrequentTreeSum(self,root):
        """
        :type root:TreeNode 
        :rtype:List[int]
        """
        def helper(root,d):
            if not root:
                return 0
            #左子树的值
            left =helper(root.left,d)
            #右子树的值
            right=helper(root.right,d)
            #左子树加上右子树的值，加上根节点的值
            subtreeSum=left+right+root.val
            #计算和的频率
            d[subtreeSum]=d.get(subtreeSum,0)+1
            return subtreeSum

        d={}
        helper(root,d)
        mostFre=0
        ans=[]
        for key in d:
            if d[key]>mostFre:
                # 如果这个数字频率更高
                mostFre=d[key]
                ans=[key]
            elif d[key]==mostFre:
                ans.append(key)
        return ans