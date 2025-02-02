#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
     def swapPairs(self, head: ListNode) -> ListNode:
        if not head:return None

        p = head
        p_next = head.next
        pre = None
        ret = None

        while p and p_next:
            if not pre:
                pre = p_next
                ret = pre
            else:
                pre.next = p_next

            p.next = p_next.next
            p_next.next = p
            pre = p
            p = p.next
            if not p:
                break 
            p_next = p.next
                
        if not pre:
            return p

        return ret
# @lc code=end

