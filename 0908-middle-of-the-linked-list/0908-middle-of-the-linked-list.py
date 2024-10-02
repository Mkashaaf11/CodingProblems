# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        curr2 = head
        count = 1
        count2= 1

        if head.next is None:
            return head

        while curr.next!= None:
            curr = curr.next
            count+=1

        while count2!=count//2:
            curr2 = curr2.next
            count2+=1

        curr2 = curr2.next
        return curr2       
        