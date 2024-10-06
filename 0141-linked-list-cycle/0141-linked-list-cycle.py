# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head ==None:
            return False

        Nodeset = set()
        temp = head

        while temp!=None:
            if temp in Nodeset:
                return True
            Nodeset.add(temp)    
            temp = temp.next

        return False        

        