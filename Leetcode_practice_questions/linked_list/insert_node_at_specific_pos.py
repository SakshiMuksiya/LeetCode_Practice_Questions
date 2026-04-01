#https://www.hackerrank.com/contests/testlinkedlist/challenges/insert-a-node-at-a-specific-position-in-a-linked-list

# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):
    # Write your code here
    node=SinglyLinkedListNode(data)
    curr=llist
    for i in range(position-1):
        curr=curr.next
    node.next=curr.next
    curr.next=node
    return llist
