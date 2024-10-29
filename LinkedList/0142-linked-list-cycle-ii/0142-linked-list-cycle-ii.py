# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head

        nodeSet = set()
        temp =  head

        while temp!=None:
            if temp in nodeSet:
                return temp
            nodeSet.add(temp)
            temp= temp.next        
        
        return None