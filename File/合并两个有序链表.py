# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return

        head = pre = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                pre.next, l1 = l1, l1.next
            else:
                pre.next, l2 = l2, l2.next
            pre = pre.next
        if l1:
            pre.next = l1
        if l2:
            pre.next = l2
        return head.next
        


if __name__ == "__main__":
    l1 = ln1 = ListNode(0)
    l2 = ln2 = ListNode(0)
    for i in [1,2,4]:
        ln1.next = ListNode(i)
        ln1 = ln1.next

    for i in [1,3,4]:
        ln2.next = ListNode(i)
        ln2 = ln2.next
    l1