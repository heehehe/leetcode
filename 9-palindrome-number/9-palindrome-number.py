class Solution:
    def isPalindrome(self, x: int) -> bool:
        if ''.join([_x for _x in list(str(x))[::-1]]) == str(x):
            return True
        return False