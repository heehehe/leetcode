"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if ''.join([_x for _x in list(str(x))[::-1]]) == str(x):
            return True
        return False

"""
Runtime: 107 ms, faster than 39.12% of Python3 online submissions for Palindrome Number.
Memory Usage: 14 MB, less than 16.33% of Python3 online submissions for Palindrome Number.
"""
