#https://www.hackerrank.com/contests/testlinkedlist/challenges/delete-a-node-from-a-linked-list

# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteNode(llist, position):
    # Write your code here
    if position==0:
        return llist.next
    curr=llist 
    for i in range(position-1):
        curr=curr.next
    curr.next= curr.next.next
    return llist
