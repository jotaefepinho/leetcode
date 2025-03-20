class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter
        
        count = Counter(nums)
        heap = []

        for key, val in count.items():
            heapq.heappush(heap, (-val, key))
        
        lista = []

        for i in range(k):
            lista.append(heapq.heappop(heap)[1])

        return lista
