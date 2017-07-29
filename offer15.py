#coding=utf-8

'''

'''

class Node(object):
    def __init__(self,val,p=0):
        self.data=val
        self.next=p
class LinkList(object):
    def __init__(self):
        self.head=0
    #初始化链表
    def initLinkList(self,data):
        # 初始化链表
        self.head = Node(0)
        p = self.head
        for i in data:
            node = Node(i)
            p.next = node
            p = p.next
            # 获得链表长度

    def getlength(self):
        p = self.head
        length = 0
        while p != 0:
            length += 1
            p = p.next
        return length
    def find_k_num(self,k):
        if k==0:
            return None
        link_len=self.getlength()
        p1=self.head
        p2=self.head
        count=0
        while count!=k:
            p1=p1.next
            if p1==0:
                return None
            count+=1
        while p1:
            p1=p1.next
            p2=p2.next
        return p2.data
    def reverse(self):
        pRever=None
        pNode=self.head
        pPrev=None
        while pNode:
            pNext=pNode.next
            if pNext==None:
                pRever=pNode
            pNode.next=pPrev
            



arr=[1,2,3,4,5,6]
l=LinkList()
l.initLinkList(arr)
print l.find_k_num(3)
