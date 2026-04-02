#https://www.hackerrank.com/contests/testlinkedlist/challenges/insert-a-node-at-the-tail-of-a-linked-list

# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    node=SinglyLinkedListNode(data)
    if head is None:
        return node
    curr=head
    while curr.next:
        curr=curr.next
    curr.next=node
    return head
