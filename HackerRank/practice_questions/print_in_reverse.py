#https://www.hackerrank.com/contests/testlinkedlist/challenges/print-the-elements-of-a-linked-list-in-reverse

# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reversePrint(llist):
    # Write your code here
    lst=[]
    curr=llist
    while curr:
        lst.append(curr.data)
        curr=curr.next
    while lst:
        print(lst.pop())
