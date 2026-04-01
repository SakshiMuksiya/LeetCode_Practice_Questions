#https://www.hackerrank.com/contests/testlinkedlist/challenges/find-the-merge-point-of-two-joined-linked-lists

# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    set1 = set()
    curr = head1
    while curr:
        set1.add(curr)
        curr = curr.next
    curr = head2
    while curr:
        if curr in set1:
            return curr.data
        curr = curr.next
