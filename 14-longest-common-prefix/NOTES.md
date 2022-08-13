### https://leetcode.com/problems/longest-common-prefix/discuss/6918/Short-Python-Solution

```python
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
```

- Runtime: 69 ms, faster than 18.83% of Python3 online submissions for Longest Common Prefix.
- Memory Usage: 14 MB, less than 49.70% of Python3 online submissions for Longest Common Prefix.

#### 위 함수에서 if not strs: return "" 부분 제외 시 결과
- Runtime: 41 ms, faster than 81.58% of Python3 online submissions for Longest Common Prefix.
- Memory Usage: 13.8 MB, less than 88.15% of Python3 online submissions for Longest Common Prefix.
