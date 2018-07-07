# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        (2 -> 4 -> 3) + (5 -> 6 -> 4)
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val  # 2 6
                l1 = l1.next     # 4
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)  # 0->2
            cur = cur.next  # 2
            carry //= 10    # 0
        return dummy.next
