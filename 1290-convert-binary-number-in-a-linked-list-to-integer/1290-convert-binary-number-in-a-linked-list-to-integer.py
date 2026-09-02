# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp=head
        decinum=0
        while temp is not  None:
            decinum= decinum*2+temp.val
            temp=temp.next
        return decinum            