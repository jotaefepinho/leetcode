class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0

        while i < len(nums):
            first = nums[i]

            while i < len(nums) - 1 and nums[i + 1] == nums[i] + 1:
                i += 1
            
            if first != nums[i]:
                ans.append(f"{first}->{nums[i]}")
            else: ans.append(f"{first}")

            i += 1
        return ans
