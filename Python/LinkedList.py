#Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x # a value
         self.next = None # a memory address
class LinkedList:
    def __init__(self):
        self.head = None # a memory address
    def add(self,item):
        temp = ListNode(item)
        temp.next = self.head
        self.head = temp
    def printList(self):
        node = self.head
        while(node):
            print (node.val)
            node = node.next

linkedlist = LinkedList()
linkedlist.add([2, 4, 9])
linkedlist.add([8, 9, 55])
linkedlist.printList()
