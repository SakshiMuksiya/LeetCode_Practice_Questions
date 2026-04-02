#https://www.hackerrank.com/contests/testlinkedlist/challenges/detect-whether-a-linked-list-contains-a-cycle

# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return 1
    return 0
