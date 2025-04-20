class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
      
        merged = [intervals[0]]
      
        for start, end in intervals[1:]:
            # No overlap, interval is added
            if merged[-1][1] < start:
                merged.append([start, end])
            else:
                # Overlap case, the end of the interval is the biggest between the
                # two ends
                merged[-1][1] = max(merged[-1][1], end)
      
        # Return merged
        return merged

