# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur.val)
            cur = cur.next

        res = 0
        n = len(nodes)
        for i in range(n // 2):
            twin = n - 1 -i 
            res = max(res, nodes[i] + nodes[twin])
        return res


            

        