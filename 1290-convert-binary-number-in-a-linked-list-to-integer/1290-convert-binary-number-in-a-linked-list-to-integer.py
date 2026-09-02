# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp = head
        count = 0
        ans = 0

        # Count the number of nodes
        while temp is not None:
            count += 1
            temp = temp.next

        # Calculate decimal value
        temp = head

        while count > 0:
            ans += (2 ** (count - 1)) * temp.val
            count -= 1
            temp = temp.next

        return ans