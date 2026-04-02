#https://www.hackerrank.com/contests/testlinkedlist/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail

# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def getNode(llist, positionFromTail):
    # Write your code here
    curr=llist
    length = 0
    while curr:
        length +=1
        curr = curr.next
    target = length -1 -positionFromTail
    curr = llist
    for i in range(target):
        curr = curr.next
    return curr.data
