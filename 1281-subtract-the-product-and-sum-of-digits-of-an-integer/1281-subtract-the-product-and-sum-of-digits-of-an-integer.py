class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product, total = 1, 0
        for nn in str(n):
            product *= int(nn)
            total += int(nn)
        return product - total
            