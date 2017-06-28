#coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow,fast=head,head
        while True:
            if fast==None or fast.next==None:
                return None
            slow=slow.next
            fast=fast.next.next
            #当快指针和慢指针相遇时，停止
            if slow==fast:
                break
        #头节点和相遇时候的快节点同时触发，如果相等，则那个节点就是环的起点
        while head!=fast:
            head=head.next
            fast=fast.next
        return head