#https://www.hackerrank.com/contests/testlinkedlist/challenges/reverse-a-linked-list

# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reverse(llist):
    # Write your code here
    prev=None
    curr=llist
    while curr:
        next_node=curr.next
        curr.next=prev
        prev=curr
        curr=next_node
    return prev
