class Solution:
    def romanToInt(self, s: str) -> int:
        symbol2val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0

        for i, _s in enumerate(s):
            if (i < len(s) - 1 and symbol2val[_s] < symbol2val[s[i+1]]):
                # 다음 문자보다 값이 작으면 빼주기 (마지막 문자이면 pass)
                total -= symbol2val[_s]
            else: 
                total += symbol2val[_s]
                
        return total