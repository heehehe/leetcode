class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high % 2 == 0:
            if low % 2 == 0:
                return (high - low) // 2
            else:
                return (high - low + 1) // 2
        else:
            if low % 2 == 0:
                return (high - low + 1) // 2
            else:
                return (high - low) // 2 + 1
        
        # if high - low + 1 % 2 == 0:
        #     return (high-low) // 2 + 1
        # return (high-low+1) // 2 + 1
        
        # cnt = 0
        # for i in range(low, high+1):
        #     if i % 2 != 0:
        #         cnt += 1
        # return cnt