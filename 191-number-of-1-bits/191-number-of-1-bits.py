class Solution:
    def hammingWeight(self, n: int) -> int:
        return len([1 for nn in bin(n) if nn == '1'])