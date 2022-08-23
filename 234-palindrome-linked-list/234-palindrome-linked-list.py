# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # https://leetcode.com/problems/palindrome-linked-list/discuss/2466070/Daily-LeetCoding-Challenge-August-Day-23
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = ''
        while head:
            values += str(head.val)
            head = head.next
        return values == values[::-1]
        
    # https://leetcode.com/problems/palindrome-linked-list/discuss/64689/Python-easy-to-understand-solution-with-comments-(operate-nodes-directly).
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        
        # compare the first and second half nodes
        while node: # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
