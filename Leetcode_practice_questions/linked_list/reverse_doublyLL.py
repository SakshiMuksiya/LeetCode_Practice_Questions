#https://www.hackerrank.com/contests/testlinkedlist/challenges/reverse-a-doubly-linked-list

# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def reverse(llist):
    # Write your code here
    curr = llist
    new_head = None
    while curr:
        curr.prev = curr.next
        curr.next = new_head
        new_head = curr
        curr = curr.prev
    return new_head
