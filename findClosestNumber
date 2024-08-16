class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = nums[0]

        for i in nums[1:]:
            if abs(i) == abs(ans) and i > ans:
                ans = i
            if abs(i) < abs(ans):
                ans = i
        
        return ans
