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