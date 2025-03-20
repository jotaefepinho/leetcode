class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1 :
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            if abs(x) > abs(y):
                heapq.heappush(stones, x - y)
            if abs(y) > abs(x):
                heapq.heappush(stones, y - x)
        
        stones = [abs(i) for i in stones]
        return stones[0] if len(stones) == 1 else 0
