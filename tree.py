#coding=utf-8

""""""
class Node(object):
    """节点类"""
    def __init__(self,val=-1,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree(object):
    """树类"""
    def __init__(self):
        self.root=Node()
    #添加节点
    def add(self,val):
        node=Node(val)
        if self.root.val==-1:      #如果树为空,则对根节点赋值
            self.root=node
        else:
            myQueue=[]
            treeNode=self.root
            myQueue.append(treeNode)
            while myQueue:          #对已有的节点进行层次遍历
                treeNode=myQueue.pop(0) #数组最左边的节点
                if treeNode.left==None:
                    treeNode.left=node
                    return
                elif treeNode.right==None:
                    treeNode.right=node
                    return
                else:
                    myQueue.append(treeNode.left)
                    myQueue.append(treeNode.right)
    def front_digui(self,root):
        """利用递归先序遍历树"""
        if root==None:
            return
        print root.val
        self.front_digui(root.left)
        self.front_digui(root.right)
    def front_stack(self,root):
        """利用堆栈实现树的先序遍历"""
        if root==None:
            return
        myStack=[]
        node=root
        while root or myStack:
            while node:#从根结点开始，找到左子树
                print node.val
                myStack.append(node)
                node=node.left
            node=myStack.pop()#while结束表示当前节点node为空,即前一个节点没有左子树了
            node =node.right #开始查看它的右子树

    def middle_digui(self,root):
        """利用递归中序遍历树"""
        if root==None:
            return
        self.front_digui(root.left)
        print root.val
        self.front_digui(root.right)

    def middle_stack(self,root):
        """中序遍历"""
        if root==None:
            return
        myStack=[]
        node=root
        while node or myStack:
            while node:#从根结点开始,一直找它的左子树
                myStack.append(node)
                node =node.left
            node =myStack.pop() #前一个节点没有左子树
            print node.val
            node=node.right
    def later_digui(self,root):
        """利用递归实现树的后序遍历,左右根"""
        if root==None:
            return
        self.later_digui(root.left)
        self.later_digui(root.right)
        print root.val
    def later_stack(self,root):
        """利用堆栈实现后序遍历"""
        myStack1=[]
        myStack2=[]
        node=root
        myStack1.append(node)
        while myStack1:#这个while循环找出后序遍历的逆序,存在myStack2里面
            node=myStack1.pop()
            if node.left:  #左子树先进入数组
                myStack1.append(node.left)
            if node.right: #右子树进入数组
                myStack1.append(node.right)
            myStack2.append(node) #根右左的形式进入myStack2中
        while myStack2:#将myStack2中的元素出栈，即为后序遍历次序
            print myStack2.pop().val
    def level_queue(self,root):
        """利用队列实现树的层次遍历"""
        if root==None:
            return
        myQueue=[]
        node=root
        myQueue.append(node)
        while myQueue:
            node=myQueue.pop(0)
            print node.val
            if node.left:
                myQueue.append(node.left)
            if node.right:
                myQueue.append(node.right)

if __name__=='__main__':
    """主函数"""
    vals=range(10)#生成十个数据作为树节点
    print "十个数据",vals
    tree=Tree()#新建一个树对象
    for val in vals:
        tree.add(val) #逐个加入树的节点
    print '队列实现层次遍历'
    tree.level_queue(tree.root)
    print '\n\n递归实现先序遍历:'
    tree.front_digui(tree.root)
