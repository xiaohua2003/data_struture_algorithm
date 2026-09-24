# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        cur_node = head
        mid = count // 2
        temp = dummy = ListNode()
        i = 0
        while cur_node:
            if i != mid:
                temp.next = cur_node
                temp = temp.next
            else:
                temp.next = cur_node.next
            cur_node = cur_node.next
            i += 1
        return dummy.next


 
    


  
        





        
            



        