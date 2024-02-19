# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        multiplier = 1
        l1_temp = l1
        l2_temp = l2
        l1_num = l2_num = 0
        while l1_temp != None:
            l1_num += l1_temp.val * multiplier
            multiplier *= 10
            l1_temp = l1_temp.next

        # Reset for the second linked list
        multiplier = 1

        while l2_temp != None:
            l2_num += l2_temp.val * multiplier
            multiplier *= 10
            l2_temp = l2_temp.next

        # Normal integer addition
        result = l1_num + l2_num

        # Save last digit first
        l3 = ListNode(result % 10)
        l3_temp = l3

        while result > 0:
            result //= 10
            if result > 0:
                # Create a node with the value
                l3_temp.next = ListNode(result % 10)
            # Move the pointer
            l3_temp = l3_temp.next

        return l3
