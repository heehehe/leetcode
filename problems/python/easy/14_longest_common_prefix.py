"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        prefix = None
        for i, s1 in enumerate(strs):
            for s2 in strs[i+1:]:
                prefix_temp = ""
                for _s1 in s1:
                    if s2.startswith(prefix_temp+_s1):
                        prefix_temp += _s1
                        continue
                    break
                
                if prefix == None or len(prefix) > len(prefix_temp):
                    prefix = prefix_temp

        return prefix

"""
Runtime: 749 ms, faster than 5.17% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14.1 MB, less than 11.86% of Python3 online submissions for Longest Common Prefix.
"""

# https://leetcode.com/problems/longest-common-prefix/discuss/6918/Short-Python-Solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

"""
Runtime: 69 ms, faster than 18.83% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14 MB, less than 49.70% of Python3 online submissions for Longest Common Prefix.
"""

"""
## 위 함수에서 if not strs: return "" 부분 제외 시 결과
Runtime: 41 ms, faster than 81.58% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.8 MB, less than 88.15% of Python3 online submissions for Longest Common Prefix.
"""
