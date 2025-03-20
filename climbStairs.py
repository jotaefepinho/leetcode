class Solution:
    def climbStairs(self, n: int) -> int:
        memo = (n + 1) * [-1]
        
        memo[0] = 1
        memo[1] = 1

        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        
        return memo[n]
