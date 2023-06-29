"""
Q: https://leetcode.com/problems/reverse-linked-list/


Given the head of a singly linked list, reverse the list, and return the reversed list.


A: https://leetcode.com/problems/reverse-linked-list/submissions/982643529/

"""


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev  