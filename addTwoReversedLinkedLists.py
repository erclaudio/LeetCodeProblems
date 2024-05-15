# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        while l1:
            stack1.insert(0,l1.val)
            l1 = l1.next
        stack2 = []
        while l2:
            stack2.insert(0,l2.val)
            l2 = l2.next
        n1 = int("".join(map(str,stack1)))
        n2 = int("".join(map(str,stack2)))
        res = n1+n2
        res=str(res)
        newRes = []
        for i in range(len(res)):
            newRes.append(int(res[i]))
        
        dummy = ListNode()
        current = dummy
        for num in newRes[::-1]:
            current.next = ListNode(num)
            current = current.next
        return dummy.next

       
       

           
        