# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, items):
        for node in items:
            temp = ListNode(node)
            temp.next = self.head
            self.head = temp

    def printList(self):
        node = self.head
        while (node):
            print(node.val)
            node = node.next


linkedlist = LinkedList()
linkedlist.append([2, 4, 9])
linkedlist.add([8, 9, 55])
linkedlist.printList()
