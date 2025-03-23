class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max = 0
        length = len(nums)
        if length == 1:
            return nums[0]
        for i in range(0, length - k):
            if (sum(nums[i : k + i]) > max):
                max = sum(nums[i:k + i])
        
        return max/k
