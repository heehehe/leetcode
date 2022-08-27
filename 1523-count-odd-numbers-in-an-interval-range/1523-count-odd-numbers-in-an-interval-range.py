class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high % 2 == 0:
            if low % 2 == 0:
                # high even / low even
                return (high - low) // 2
            
            # high even / low odd
            return (high - low + 1) // 2
        
        # high odd / low even
        if low % 2 == 0:
            return (high - low + 1) // 2
        
        # high odd / low odd
        return (high - low) // 2 + 1