# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0
     

        if head.next is None:
            return head

        while curr!= None:
            count+=1
            curr = curr.next
           
        curr = head
        mid = count//2
        count = 0
        while count!=mid:
            count+=1
            curr= curr.next

        return curr    

           
        