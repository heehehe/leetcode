"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # 괄호별 열기 - 닫기 dict 생성
        pmap = {"(": ")", "{": "}", "[": "]"}
        
        _s_check = []
        for _s in s:
            if _s in ("(", "{", "["):
                # 시작 괄호 추가
                _s_check.append(_s)
            elif not _s_check:
                # 처음이 시작 괄호가 아닌 경우
                return False
            else:
                # 괄호가 올바르게 맵핑되었는지 확인
                if pmap[_s_check.pop()] != _s:
                    return False
        if _s_check:
            # for loop 끝나면 _s_check가 비어있어야 하는데 아닌 경우 (닫기 괄호가 없던 경우)
            return False
        return True
    
"""
Runtime: 50 ms, faster than 48.13% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14 MB, less than 25.50% of Python3 online submissions for Valid Parentheses.
"""
