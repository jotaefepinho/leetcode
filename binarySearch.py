class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        m = (r + l)//2
        while r > l:
            if nums[m] < target:
                l = m + 1
            if nums[m] > target:
                r = m - 1
            m = (r+l)//2
        
        if nums[m] == target:
            return r
        return -1
