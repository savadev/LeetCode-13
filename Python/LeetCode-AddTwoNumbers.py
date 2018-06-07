# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self):
        self.head = None
        self.carry = 0
    def add(self, item):
        temp = ListNode(item)
        temp.next = self.head
        self.head = temp
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self.l1 = l1
        self.l2 = l2
        tmpList = []
        while((self.l1) or (self.l2)):
            tens = self.carry
            currentL1 = self.l1
            currentL2 = self.l2
            if(currentL1 is None):
                total = tens + currentL2.val
                self.l2 = currentL2.next
            elif(currentL2 is None):
                total = tens + currentL1.val
                self.l1 = currentL1.next
            else:
                total = tens + currentL1.val + currentL2.val
                self.l1 = currentL1.next
                self.l2 = currentL2.next
            ones = total%10
            tens = int(total/10)
            self.carry = tens
            tmpList.append(ones)

        if(self.carry == 1):
            tmpList.append(1)
        tmpList.reverse()
        for i in tmpList:
            self.add(i)

        return self.head
