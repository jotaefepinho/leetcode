class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify(nums)

        k = len(nums) - k

        for i in range(k + 1):
            a = heapq.heappop(nums)
        return a
