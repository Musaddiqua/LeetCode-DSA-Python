# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next
        next_node = curr.next

        first = -1
        last = -1

        min_dist = float('inf')
        position = 1

        while next_node:
            # Check if curr is a critical point
            if ((curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)):

                if first == -1:
                    # First critical point
                    first = position
                else:
                    # Distance from previous critical point
                    min_dist = min(min_dist, position - last)

                # Update last critical point
                last = position

            prev = curr
            curr = next_node
            next_node = next_node.next
            position += 1

        # Fewer than 2 critical points
        if first == last:
            return [-1, -1]

        # Maximum distance = last critical point - first critical point
        max_dist = last - first

        return [min_dist, max_dist]
        