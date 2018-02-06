class ListNode:
    #Definition for singly-linked list.
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    def __init__(self):
        self.headL1 = None
        self.headL2 = None
        self.headL3 = None
        self.newheadL1 = None
        self.newheadL2 = None
        self.carry = 0
    def addL1(self,item):
        temp = ListNode(item)
        temp.next = self.headL1
        self.headL1 = temp
        """
        Note:
        ListNode(item)
        ListNode(item).next = self.head
        self.head = ListNode(item)
        ^^^^^
        If the code was written in this way,
        3 objects, instead of 1, were created.
        Hence, A temporary variable is necessary
        """
    def addL2(self,item):
        temp = ListNode(item)
        temp.next = self.headL2
        self.headL2 = temp
    def addL3(self,item):
        temp = ListNode(item)
        temp.next = self.headL3
        self.headL3 = temp
    def printList(self):
        print("List 1: ", end = '')
        nodeL1 = self.headL1
        while(nodeL1):
            print (nodeL1.val, end = '')
            nodeL1 = nodeL1.next
            if(nodeL1):
                print(" -> ", end ='')
        print()
        print("List 2: ", end = '')
        nodeL2 = self.headL2
        while(nodeL2):
            print (nodeL2.val, end ='')
            nodeL2 = nodeL2.next
            if(nodeL2):
                print(" -> ", end ='')
        print()
        print("List 3: ", end = '')
        nodeL3 = self.headL3
        while(nodeL3):
            print (nodeL3.val, end ='')
            nodeL3 = nodeL3.next
            if(nodeL3):
                print(" -> ", end ='')
    def pop(self):
        self.newheadL1 = self.headL1
        self.newheadL2 = self.headL2
        while((self.newheadL1) and (self.newheadL2)):
            tens = self.carry
            currentL1 = self.newheadL1
            currentL2 = self.newheadL2
            total = tens + currentL1.val + currentL2.val
            ones = total%10
            tens = int(total/10)
            self.carry = tens
            self.addL3(ones)
            self.newheadL1 = currentL1.next
            self.newheadL2 = currentL2.next
        if(self.carry ==1):
            self.addL3(1)
    def addTwoNumbers(self, l1, l2):
        for i in range (len(l1)):
            self.addL1(l1[i])
        for j in range (len(l2)):
            self.addL2(l2[j])
        self.pop()
solution = Solution()
solution.addTwoNumbers([3, 8, 9], [6, 7, 4])
solution.printList()
