#https://www.hackerrank.com/contests/testlinkedlist/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list

# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def removeDuplicates(llist):
    # Write your code here
    curr = llist
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else: 
            curr = curr.next
    return llist
