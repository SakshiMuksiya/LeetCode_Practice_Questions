#https://www.hackerrank.com/contests/testlinkedlist/challenges/insert-a-node-at-the-head-of-a-linked-list

#SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    # Write your code here
    node=SinglyLinkedListNode(data)
    node.next=llist
    llist=node
    return llist
