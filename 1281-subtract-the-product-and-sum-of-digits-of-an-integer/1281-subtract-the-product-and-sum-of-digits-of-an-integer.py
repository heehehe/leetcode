class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/discuss/812200/Python-one-liner-using-eval-function-(28ms-14MB)
        return eval('*'.join(str(n))) - eval('+'.join(str(n)))        

        """ my solution
        ## Runtime: 65 ms, faster than 9.49% / Memory Usage: 13.9 MB, less than 53.81%
        
        product, total = 1, 0
        for nn in str(n):
            product *= int(nn)
            total += int(nn)
        return product - total
        """
 