class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_count = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        for i in text:
            if i.lower() in balloon_count:
                balloon_count[i] += 1
        
        balloon_count['l'] //= 2
        balloon_count['o'] //= 2
        
        return min(balloon_count.values())
