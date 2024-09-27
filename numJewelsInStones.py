class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        set_jewels = set(jewels)
        total = 0

        for stone in stones:
            if stone in set_jewels:
                total += 1
        
        return total
