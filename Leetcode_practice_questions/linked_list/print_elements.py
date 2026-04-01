#https://www.hackerrank.com/contests/testlinkedlist/challenges/print-the-elements-of-a-linked-list

# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    curr=head
    while curr:
        print(curr.data)
        curr=curr.next
