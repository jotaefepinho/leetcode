# Solution with hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = {}

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in remainder:
                return remainder[rem], i
            else:
                remainder[nums[i]] = i

# Solution with two pointers: Array must be sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while numbers[left] + numbers[right] != target:
            if numbers[right] > target - numbers[left]:
                right -= 1
            else:
                left += 1
        
        return [left + 1, right + 1]
