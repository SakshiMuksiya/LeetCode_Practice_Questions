#https://www.hackerrank.com/contests/testlinkedlist/challenges/insert-a-node-into-a-sorted-doubly-linked-list

# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(llist, data):
    # Write your code here
    node = DoublyLinkedListNode(data)
    if llist is None or data <= llist.data:
        node.next  = llist
        if llist:
            llist.prev = node
        return node
    
    curr = llist
    while curr.next and data >= curr.next.data:
        curr = curr.next
    node.next = curr.next
    node.prev = curr
    
    if curr.next:
        curr.next.prev = node
    curr.next = node
    return llist
