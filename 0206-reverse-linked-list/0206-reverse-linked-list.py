# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        if head.next is None:
            return head    

        stack  = []

        curr = head

        while curr!=None:
            stack.append(curr.val)
            curr = curr.next   

        curr = head

        while curr!=None:
            curr.val = stack.pop()
            curr = curr.next

        return head         
        