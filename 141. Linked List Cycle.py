# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            head1=head
            head2=head.next
            while not head1 is head2:
                head1=head1.next
                head2=head2.next.next
            return True
        except:
            return False