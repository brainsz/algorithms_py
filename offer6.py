#coding=utf-8
'''
题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
'''


class Node:
    def __init__(self,data,left,right):
        self.data=data
        self.left=left
        self.right=right
def construct_tree(pre_order,mid_order):
    #递归出口条件
    if len(pre_order)==0:
        return None
    #前序的第一个节点是根节点
    root_data=pre_order[0]
    for i in range(0,len(mid_order)):
        if mid_order[i]==root_data:
            break
    #递归构造左子树和右子数
    left=construct_tree(pre_order[1:i+1],mid_order[:i])
    right=construct_tree(pre_order[i+1:],mid_order[i+1:])
    return Node(root_data,left,right)

pre=[1,2,4,7,3,5,6,8]
mid=[4,7,2,1,5,3,8,6]
root=construct_tree(pre,mid)
print root.data